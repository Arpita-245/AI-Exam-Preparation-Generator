import os

from groq import Groq

from flask import current_app


class GroqService:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def ask_ai(self, prompt):

        try:

            response = self.client.chat.completions.create(

                model=current_app.config["GROQ_MODEL"],

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                temperature=0.5,

                max_tokens=2048

            )

            return response.choices[0].message.content

        except Exception as e:

            print("Groq Error:", e)

            return (
                "AI service is temporarily unavailable."
            )