from app.ai.groq_service import GroqService


class RecommendationService:

    @staticmethod
    def generate_recommendation(summary, quiz_score):

        prompt = f"""
You are an AI Study Mentor.

Student Summary:
{summary}

Quiz Score:
{quiz_score}

Based on the score, provide personalized study recommendations.

Rules:
- Keep the response concise.
- Mention strengths.
- Mention weak areas.
- Suggest what to study next.
- Suggest revision strategy.
"""

        groq = GroqService()

        return groq.ask_ai(prompt)