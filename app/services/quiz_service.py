from app.ai.groq_service import GroqService


class QuizService:

    @staticmethod
    def generate_quiz(text):

        prompt = f"""
You are an expert teacher.

Read the following study material carefully.

Generate exactly 10 multiple-choice questions.

Rules:
- Generate exactly 10 questions.
- Each question must have 4 options (A, B, C, D).
- Mention the correct answer after each question.
- Questions should cover the entire study material.
- Keep the difficulty moderate.
- Return only plain text.
- Do not include explanations.

Study Material:

{text}
"""

        groq = GroqService()

        return groq.ask_ai(prompt)