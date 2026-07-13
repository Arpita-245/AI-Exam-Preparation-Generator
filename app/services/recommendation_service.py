from app.ai.groq_service import GroqService


class RecommendationService:

    @staticmethod
    def generate_recommendation(summary, quiz_score):
        """
        Generate personalized study recommendations based on
        the AI-generated summary and the student's quiz score.
        """

        if not summary:
            return "Summary is not available."

        if not quiz_score:
            quiz_score = "Not Available"

        # Limit very large summaries
        summary = summary[:4000]

        prompt = f"""
You are an experienced AI Study Mentor.

A student has completed studying a topic and attempted a quiz.

Study Summary:
{summary}

Quiz Score:
{quiz_score}

Generate a personalized study recommendation.

Instructions:
1. Briefly evaluate the student's performance.
2. Mention the student's strengths.
3. Mention possible weak areas.
4. Suggest which concepts should be revised.
5. Recommend what to study next.
6. Give practical revision tips.
7. Suggest an effective study strategy.
8. Motivate the student with a short encouraging message.
9. Keep the response simple and easy to understand.
10. Use headings and bullet points.

Return only the recommendation.
"""

        try:
            groq = GroqService()

            response = groq.ask_ai(prompt)

            if response:
                return response.strip()

            return "Unable to generate recommendation."

        except Exception as e:
            print("Recommendation Generation Error:", e)
            return f"Error generating recommendation: {str(e)}"