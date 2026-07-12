from app.ai.groq_service import GroqService


class SummaryService:

    @staticmethod
    def generate_summary(text):

        prompt = f"""
You are an AI Tutor.

Read the following study material carefully.

Generate a clear, well-structured summary in simple language.

The summary should:
- Cover all important concepts.
- Use bullet points wherever possible.
- Be easy for students to revise.
- Avoid unnecessary details.

Study Material:

{text}
"""

        groq = GroqService()

        return groq.ask_ai(prompt)