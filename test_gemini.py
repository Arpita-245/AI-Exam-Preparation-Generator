from app import create_app
from app.ai.gemini_service import GeminiService

app = create_app()

with app.app_context():

    gemini = GeminiService()

    response = gemini.ask_ai(
        "Explain Artificial Intelligence in 50 words."
    )

    print(response)