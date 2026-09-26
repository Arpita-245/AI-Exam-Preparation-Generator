# AI Exam Prep — AI-Based Exam Preparation & Question Generator

Upload study notes (PDF/DOCX/TXT) and automatically generate MCQs, True/False,
Fill-in-the-Blank, Short Answer, and Long Answer questions. Take timed
quizzes with save/resume, get instant scoring, AI-detected weak topics and
recommendations, and full admin oversight (users, subjects, questions,
reports) — in a glassmorphism, dark/light-mode, fully responsive UI.

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.12, Flask, SQLAlchemy (Flask-SQLAlchemy) |
| Frontend | HTML5, CSS3 (custom glassmorphism design system), Bootstrap 5, vanilla JS, Chart.js, AOS |
| Database | SQLite (default) / MySQL (`DATABASE_URL`) |
| AI / NLP | Rule-based NLP generator (always available, offline) + optional spaCy / Hugging Face FLAN-T5 |
| File Processing | PyPDF2, pdfplumber, python-docx, Pillow (avatars) |
| Auth | Flask-Login + Werkzeug password hashing, CSRF via Flask-WTF |
| PDF Reports | fpdf2 |
| Deployment | Render (gunicorn) |

## Architecture

```
ai_exam_prep/
├── app/
│   ├── __init__.py          # application factory
│   ├── config.py            # environment-based configuration
│   ├── extensions.py        # db, login_manager, csrf
│   ├── forms.py             # all WTForms definitions
│   ├── models/                # User, Subject, Document, Question, Quiz,
│   │                           # QuizQuestion, QuizAttempt, AttemptAnswer, Recommendation
│   ├── routes/                 # auth, main, upload, quiz, student, admin blueprints
│   ├── services/                # quiz grading, recommendation persistence, dummy mail
│   ├── ai/                       # text extraction, NLP preprocessing, question generation
│   ├── utils/                     # validators, decorators, avatar handling, PDF report
│   ├── static/                     # css/ (tokens + components), js/, uploads/
│   └── templates/                   # base, auth, student, admin, quiz, shared, errors
├── requirements.txt
├── run.py
├── render.yaml
└── .env.example
```

## Why the AI works with zero setup

The question generator is a fully deterministic, offline NLP pipeline
(regex + frequency heuristics for sentence/topic/difficulty detection,
plausibility-ranked MCQ distractors, fact-swap True/False, definition-
pattern Short Answer). No model download is required. spaCy and a FLAN-T5
transformer pass are optional, detected at runtime, and used only to
improve quality when present — the app is fully functional without them.

## Local Setup

```bash
cd ai_exam_prep
python -m venv venv

# Windows (PowerShell):
venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt

copy .env.example .env      # Windows
# cp .env.example .env      # macOS/Linux

# Windows (PowerShell):
$env:FLASK_APP = "run.py"
# macOS/Linux:
export FLASK_APP=run.py

flask init-db
python run.py
# -> http://localhost:5000
```

**Default admin login** (created by `flask init-db`):
- Username: `admin`
- Password: `Admin@1234`

Change this immediately in any real deployment.

## Using MySQL instead of SQLite

Set `DATABASE_URL` in `.env`:
```
DATABASE_URL=mysql+pymysql://username:password@host:3306/exam_prep_db
```
Then re-run `flask init-db`. No code changes needed.

## Feature Checklist

- **Auth**: Register, Login, Logout, Remember Me, Forgot Password, Reset
  Password (tokenized links, 30-min expiry), dummy Email Verification
  (link is logged + flashed on-screen since no real SMTP is configured),
  Change Password.
- **Student Dashboard**: welcome banner, animated-counter stats, recent
  activity, AI recommendations.
- **Upload Notes**: drag-and-drop, PDF/DOCX/TXT, file validation, optional
  subject tagging.
- **AI Processing**: text extraction/cleaning, sentence tokenization,
  keyword/topic extraction, difficulty detection.
- **Question Generator**: MCQ (plausible distractors), True/False
  (fact-swap negation), Fill-in-the-Blank, Short Answer, Long Answer;
  Easy/Medium/Hard/Mixed difficulty.
- **Quiz Module**: live timer, progress bar, previous/next nav, per-question
  nav dots, debounced save-progress (resume after closing the tab),
  auto-submit on timeout, dedicated Review Answers page.
- **Results**: score, percentage, time taken, correct/wrong breakdown,
  downloadable PDF report.
- **Analytics**: Chart.js score trend, topic-wise accuracy, difficulty-wise
  accuracy.
- **Recommendation Engine**: persisted `Recommendation` rows generated
  after every attempt — weak topics, difficulty struggles, question-type
  struggles, strength callouts.
- **History**: full quiz attempt log with links to result/review.
- **Profile**: edit name/bio, upload avatar (auto-resized), change password.
- **Admin Panel**: dashboard (platform stats), manage users
  (activate/deactivate/delete), manage subjects (CRUD), manage documents
  (oversight/delete), manage questions (edit/delete individually), manage
  quizzes (oversight), Reports (platform-wide weak topics, question-type
  accuracy, per-student average score ranking).
- **Security**: SQLAlchemy ORM (no raw SQL / no injection surface), CSRF
  tokens on every state-changing request, secure UUID-based filenames,
  file type/size allow-listing, password strength rules, role-based route
  decorators, generic "if an account exists" messaging on forgot-password
  (no account enumeration).

## Deploying to Render

1. Push to GitHub.
2. Render → **New + → Blueprint**, point at the repo (reads `render.yaml`).
3. Set `DATABASE_URL` if using managed MySQL/Postgres (optional).
4. After first deploy, open the Render shell and run `flask init-db` once.

> Render's free-tier filesystem is ephemeral — for production use, set
> `DATABASE_URL` to a managed database and consider object storage for
> uploaded documents/avatars if you need durability across deploys.
