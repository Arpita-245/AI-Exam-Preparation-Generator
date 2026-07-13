from app.ai.groq_service import GroqService


class SummaryService:

    @staticmethod
    def generate_summary(text):
        """
        Generate an AI summary from extracted text.
        """

        if not text:
            return "No text available."

        text = text[:6000]

        prompt = f"""
You are an expert AI tutor.

Generate a concise study summary.

Instructions:
- Use headings.
- Use bullet points.
- Cover important concepts.
- Keep it easy to revise.

Study Material:

{text}
"""

        try:
            groq = GroqService()
            response = groq.ask_ai(prompt)

            if response:
                return response.strip()

            return "Unable to generate summary."

        except Exception as e:
            print("Summary Error:", e)
            return None