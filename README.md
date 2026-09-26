# SentinelReview — AI Code Review & Bug Detection Platform

An AI-powered code review platform: paste, upload, or connect a GitHub PR,
and it runs real static analysis tools plus an AI-powered semantic review
(Groq, Gemini, or Claude — pick whichever provider you have a key for),
returning bugs, security findings, and quality issues with plain-English
explanations, suggested fixes, and one-click AI-generated fix diffs.

## Honest scope note

The original brief for this project described a platform on the scale of
CodeRabbit, Snyk Code, and SonarQube Cloud combined. That's genuinely
months-to-years of work for a funded engineering team. What's in this
repository is a **large, working vertical slice** of that vision, built so
every piece you run actually does what it claims. A few things need your
own credentials to activate (GitHub OAuth App), and are clearly marked below.

## What's actually implemented

**Real static analysis, not just heuristics**
- Python: **Bandit** (security) + **Pylint** (bugs/quality) run as real
  subprocesses when installed (they are, in the Docker image)
- JavaScript/TypeScript: real **ESLint** (bundled standalone flat config,
  no project setup needed), layered with heuristic checks ESLint's minimal
  ruleset doesn't cover (innerHTML/XSS, document.write, nested loops)
- Both gracefully **fall back to built-in heuristic analyzers** if the
  tools aren't installed — the app works with zero extra setup either way
- **13 languages** total: Python, JavaScript, TypeScript, Java, C, C++, C#,
  PHP, HTML, CSS, Go, Ruby, SQL — each with real, language-specific checks
  (see `app/static_analysis.py` for the full list per language)
- HTML analysis **delegates embedded `<script>`/`<style>` blocks** to the
  JS/CSS analyzers automatically

**Language mismatch detection (a real bug fix)**
- Every review cross-checks content against signature patterns for all 13
  languages. Upload HTML but declare "python", and the review flags it as
  a critical issue, re-analyzes as the *actual* detected language, and
  hard-caps the score (≤15 health, ≥70 risk) — this closes a real bug where
  mismatched uploads were scoring as healthy code.

**AI features**
- AI-generated review summary, code-health score, risk score, and
  additional semantic issues beyond what static analysis catches
- **AI-generated fix diffs**: click "Generate fix" on any issue for a real
  unified diff, not just advice text
- **AI Diagram Generator**: architecture, class, sequence, ER, and
  function call-graph diagrams — generated as real Mermaid syntax from the
  file you're reviewing and rendered inline (`components/DiagramViewer.tsx`)
- **AI Documentation Generator**: README section, API docs, or a changelog
  entry generated from the file, downloadable
- **AI Test Generator**: real unit test code for the file, in the standard
  test framework for that language (pytest/Jest/JUnit/etc.)
- **AI Pair Programmer chat**: ask questions about the specific file
  you're reviewing ("explain this function", "where might bugs hide?"),
  grounded in that file's actual content
- **Learning Mode**: every issue can be re-explained at a beginner or
  expert level, or as a root-cause analysis, on demand
- Deterministic mock fallback for all of the above when
  `ANTHROPIC_API_KEY` isn't set, so the whole app is demoable without a key

**Gamification**
- Real stats computed from your actual review history — total reviews,
  issues found, critical/high issues caught, languages used, current daily
  streak — and 8 badges that unlock based on those numbers (not fake
  placeholders): First Steps, Regular Reviewer, Review Machine, Bug
  Hunter, Security Sentinel, Polyglot, On a Roll, Consistency Champion
  (`GET /api/users/me/stats`, shown on the dashboard)

**Auto-fix → PR (the safe version of an autonomous agent)**
- Rather than an agent that silently commits changes across a repo, this
  generates a full corrected file via AI and opens an ordinary GitHub
  pull request with it — a human always reviews and merges, nothing lands
  unreviewed. Available per-file after running a GitHub PR review.
  Verified end-to-end with mocked GitHub API calls (branch creation,
  commit, PR creation).

**Background processing (Celery + Redis)**
- The review pipeline runs as a real Celery task (`app/tasks.py`). In eager
  mode (the default) it runs synchronously in-process — zero extra
  infrastructure for local dev/tests. With Redis + a worker (as wired in
  `docker-compose.yml`), it's genuinely asynchronous: the API returns
  `queued` immediately and a separate worker process does the analysis.
  This was tested end-to-end with a live Redis broker and worker process.

**GitHub integration**
- "Sign in with GitHub" OAuth login (creates/links an account)
- List your repos, list a repo's open PRs, run the full analysis pipeline
  against every changed file in a PR, and optionally post the summary as a
  PR comment
- ⚠️ **Requires your own GitHub OAuth App** (client ID + secret) to
  activate — see setup below. Without it configured, these endpoints
  return a clear 501 instead of failing confusingly. The underlying GitHub
  API client code was verified against the real GitHub API; the OAuth
  login round-trip itself needs your credentials to test end-to-end.

**Other features**
- Rate limiting on the review endpoint (20/minute, per-user)
- Score trend analytics (Recharts chart) per project
- Inline code viewer with line-level issue annotations (click a line to
  expand), alongside a traditional list view — toggle between them
- Drag-and-drop file upload with language auto-detected from the extension
- Markdown export of a full review report
- CI pipeline (`.github/workflows/ci.yml`) running backend tests + frontend
  build on every push

**Workflow features**
- **Issue triage**: dismiss or mark "won't fix" on any finding so it stops
  resurfacing as new on every re-review — reopen anytime
- **Delta/regression view**: re-run a review on an updated version of the
  same file and see exactly what's new, resolved, or still present since
  the last review of that filename in the project (a "Changes" tab on the
  review page)
- **Batch zip upload**: upload a `.zip` of multiple files and get one
  review per supported file plus an aggregate summary, instead of
  uploading one file at a time
- **Shareable read-only links**: generate a public URL for any review — no
  login required to view it — and revoke it anytime
- **PDF and CSV export**: alongside the existing Markdown export, download
  a formatted PDF report or a CSV of findings for spreadsheet tracking
- **In-app notifications**: a bell icon with unread count, populated when
  an async review completes or fails — no more staring at a polling page
- **Light mode**: a theme toggle in the navbar, persisted across sessions

**Reliability & scale**
- **Response caching**: diagram/docs/test generations are cached (Redis,
  with an in-memory fallback) by content hash, so re-clicking the same
  button on the same file doesn't burn free-tier AI quota twice
- **Usage dashboard**: `/dashboard/settings` shows how many AI calls
  you've made today and which provider is actually active — no more
  guessing whether you're about to hit a free-tier rate limit
- **API keys**: generate a key under Settings and call this app's API
  programmatically (e.g. from your own CI) via an `X-API-Key` header,
  alongside the existing JWT login flow

**GitHub automation**
- **Repo linking + webhook**: link a project to a GitHub repo, add a
  webhook pointing at `/api/github/webhook`, and every push/PR gets
  reviewed automatically with a posted comment — instead of manually
  clicking "Review this PR" each time. Signature verification (HMAC-SHA256)
  is fully unit-tested with locally-constructed signed payloads; the
  webhook delivery itself needs a publicly reachable backend URL (e.g. via
  ngrok or a real deployment) since GitHub can't reach `localhost`.

**Testing**
- 66 passing backend tests covering auth (JWT + API key), the full review
  pipeline, language-mismatch detection, one test per language analyzer,
  real-tool integration with graceful-fallback verification, rate
  limiting, fix generation, analytics, diagrams, docs/test generation,
  chat, explain modes, gamification stats, the mocked auto-fix-to-PR flow,
  multi-provider AI selection/fallback, issue triage, delta view, share
  links, PDF/CSV export, batch upload, usage tracking, API key
  create/use/revoke, notifications, GitHub webhook signature verification
  (valid signature, bad signature, missing signature, and correctly
  ignoring unlinked repos/non-PR events), and the schema migration itself
  (upgrading a simulated old database without data loss, and confirming
  it's a safe no-op on an already-current schema)
- Frontend type-checks clean and builds to a production bundle with zero
  errors across all 10 routes

## Architecture

```
┌─────────────┐  JWT / OAuth   ┌──────────────┐        ┌───────────────┐
│   Next.js    │ ──────────────▶│   FastAPI     │◀──────▶│  PostgreSQL / │
│  (frontend)  │◀────────────── │   (backend)   │        │    SQLite     │
└─────────────┘   JSON/REST    └──────┬───────┘        └───────────────┘
                                       │
                    ┌──────────────────┼──────────────────┐
                    ▼                  ▼                  ▼
            ┌──────────────┐  ┌────────────────┐  ┌───────────────┐
            │ real_tools.py │  │  celery task    │  │ github_client │
            │ (bandit/      │  │ (Redis-backed,  │  │ .py (OAuth +  │
            │  pylint/      │  │  async in prod) │  │  PR review)   │
            │  eslint) +    │  └────────────────┘  └───────────────┘
            │ static_analysis│
            │ .py heuristics │
            └──────────────┘
```

## Running it

**If you're upgrading an existing installation** (i.e. you already had this
running before and are pulling a newer version): no manual steps needed.
On startup, the backend automatically adds any columns that newer code
expects but an existing database is missing — this fixed a real bug where
a persistent Postgres volume from an older version threw `column ... does
not exist` errors until restarted. `docker compose down && docker compose
up --build` (or just restarting the containers) is all that's required.

### Option A — Docker Compose (recommended)

```bash
cp backend/.env.example backend/.env       # optional: add ANTHROPIC_API_KEY, GitHub creds
docker compose up --build
```

- Frontend: http://localhost:3000
- Backend docs (Swagger UI): http://localhost:8000/docs

This starts Postgres, Redis, the API, a **Celery worker**, and the
frontend — the full async pipeline, not just the dev-mode eager fallback.

### Option B — run locally (no Docker)

Backend:
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Runs on SQLite with `CELERY_ALWAYS_EAGER=true` by default — no Postgres or
Redis required to try it out.

For real static tools locally (optional — falls back to heuristics otherwise):
```bash
pip install bandit pylint
npm install -g eslint@9
```

Frontend:
```bash
cd frontend
npm install
npm run dev
```

### Running the backend tests
```bash
cd backend
pip install -r requirements.txt
pytest tests/ -v
```

### Enabling GitHub integration

1. Go to https://github.com/settings/developers → **New OAuth App**
2. Authorization callback URL: `http://localhost:8000/api/auth/github/callback`
3. Copy the Client ID and generate a Client Secret
4. Set `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET` in `backend/.env` (or as
   env vars for the `backend`/`worker` services in `docker-compose.yml`)
5. "Continue with GitHub" on the login page and the PR review page under
   the dashboard will now work

### Enabling live AI review — free options available

Every AI feature (review summaries, diagrams, docs, tests, chat, fix
generation) works with a mock response out of the box, so nothing requires
payment to try. To get real AI output, set **one** of these:

**Groq (recommended — fastest, most generous free tier)**
1. Sign up at https://console.groq.com
2. Create an API key
3. `GROQ_API_KEY=gsk_...`

**Google Gemini (also free, no credit card)**
1. Get a key at https://aistudio.google.com/apikey
2. `GEMINI_API_KEY=...`

**Anthropic (paid, Claude models)**
- `ANTHROPIC_API_KEY=sk-ant-...`

`AI_PROVIDER=auto` (the default) tries Groq → Gemini → Anthropic, using
whichever has a key set — you don't need to change anything else if you
set exactly one. Set `AI_PROVIDER` explicitly (`groq`, `gemini`, or
`anthropic`) to force a specific one if you've set more than one key.

**⚠️ Critical: where to put the `.env` file depends on how you run this.**
- **Docker Compose**: create `.env` in the **project root** (next to
  `docker-compose.yml`), not `backend/.env`. Compose reads its
  `${GROQ_API_KEY}`-style substitutions from a root-level `.env` file —
  `backend/.env` has no effect on a Docker run. After creating/editing it,
  run `docker compose down && docker compose up --build` (a plain
  `up --build` on already-running containers won't always pick up new env
  values).
- **Running locally** (`uvicorn` directly): `backend/.env` is correct —
  pydantic-settings loads it from the backend working directory.

**Verifying it actually picked up your key**: visit
`http://localhost:8000/api/ai/status` — it reports which provider (if any)
is active and which keys it sees as configured, so you don't have to guess
from mock text alone.

## Roadmap — what's still not built (and why)

**Deliberately not built as "fake" versions of large infra projects:**
- **Fully autonomous multi-file agent** that commits/refactors across a
  repo without review — implemented instead as **Auto-fix → PR** (see
  above), which is the same underlying capability but always routed
  through a human-reviewed pull request rather than silent commits.
- **Live code execution playground** — running arbitrary user-submitted
  code server-side needs real sandboxing (isolated containers, resource/
  network limits) to be safe; a half-built version would be a genuine
  security liability, not a shortcut worth taking.
- **Voice AI assistant** and **AI code review video recording** — outside
  this app's scope; would need speech-to-text/video-generation
  infrastructure unrelated to code review itself.
- **Plugin/rules marketplace** and **multi-repository workspace** — each
  is a substantial product surface on its own (billing, submission review,
  cross-repo indexing) beyond a single build pass.
- **Full repository-wide semantic search / RAG chat** — the per-file AI
  chat that *is* built covers the single-file case well; scaling that to
  "search this entire codebase" needs an embeddings pipeline + vector DB
  (Qdrant, as in the original brief) which is a separate infra project.

**Collaboration & org features**
- Organizations, teams, roles/permissions, invitations, comment threads
  on individual issues
- Email/Slack/Discord delivery for notifications (in-app notifications
  are implemented; external delivery channels are not)

**Auth hardening**
- Refresh tokens (currently a single long-lived access token)
- Google OAuth (GitHub OAuth is implemented)

**Further language coverage**
- Tree-sitter-based parsing for Rust, Swift, Kotlin, and richer JSX/Vue/
  Angular template awareness beyond plain JS/TS

**Known items to address before production use**
- The frontend's dependency chain has npm-audit-flagged advisories
  inherited from transitive dependencies; re-run `npm audit` before
  deploying publicly.
- The GitHub OAuth `state` parameter and the webhook's repo→project
  lookup are both fine for a single-process deployment; a multi-worker
  production deployment should move OAuth state to Redis (already used
  elsewhere in the app) instead of an in-memory set.
- `JWT_SECRET` in `.env.example` is a placeholder — generate a real random
  secret per environment.
- The GitHub webhook's signature verification and event routing are fully
  unit-tested, but actual delivery from GitHub has not been exercised
  end-to-end since that requires a publicly reachable backend URL.
- `app/migrations.py` is a deliberately minimal "add missing columns"
  migration, not a real migration framework — it handles exactly the
  additive-column case that bit this project once already. Anything
  beyond that (renaming/dropping columns, changing a column's type,
  splitting a table) should go through a real tool like Alembic
  (already listed in `requirements.txt` but not yet wired up) instead of
  extending this file further.
