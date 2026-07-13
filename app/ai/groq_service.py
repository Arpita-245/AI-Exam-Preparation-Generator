import os

from groq import Groq
from flask import current_app


class GroqService:

    def __init__(self):
        """
        Initialize Groq client.
        """

        api_key = current_app.config.get("GROQ_API_KEY")

        if not api_key:
            api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY is missing. Please add it to your .env file."
            )

        self.client = Groq(api_key=api_key)

    def ask_ai(self, prompt):
        """
        Send a prompt to the Groq LLM and return the response.
        """

        if not prompt or not prompt.strip():
            return "Prompt cannot be empty."

        try:

            response = self.client.chat.completions.create(

                model=current_app.config.get(
                    "GROQ_MODEL",
                    "llama-3.1-8b-instant"
                ),

                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an intelligent AI tutor that helps "
                            "students learn by generating summaries, quizzes, "
                            "recommendations, and answering academic questions."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                temperature=0.4,
                max_tokens=2048,
                top_p=1,
                stream=False
            )

            if (
                response
                and response.choices
                and response.choices[0].message
                and response.choices[0].message.content
            ):
                return response.choices[0].message.content.strip()

            return "No response received from the AI."

        except Exception as e:
            print("\n========== GROQ ERROR ==========")
            print(e)
            print("================================\n")

            return f"AI service error: {str(e)}"