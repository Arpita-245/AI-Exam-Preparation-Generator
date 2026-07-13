from app.ai.groq_service import GroqService
import re


class QuizService:

    @staticmethod
    def generate_quiz(text):
        """
        Generate 10 MCQs using Groq AI and return
        a structured list of dictionaries.
        """

        if not text:
            return None

        # Limit text size
        text = text[:6000]

        prompt = f"""
You are an expert teacher.

Read the study material and generate EXACTLY 10 multiple-choice questions.

Rules:
1. Each question must have exactly four options.
2. Only one option is correct.
3. Keep questions clear and simple.
4. Do NOT add explanations.
5. Return ONLY this format.

Example:

Q1. What is Artificial Intelligence?

A) Option A
B) Option B
C) Option C
D) Option D

Answer: A

Repeat until Question 10.

Study Material:

{text}
"""

        try:

            groq = GroqService()

            response = groq.ask_ai(prompt)

            if not response:
                return None

            return QuizService.parse_quiz(response)

        except Exception as e:

            print("Quiz Generation Error:", e)

            return None

    # =====================================================
    # Parse AI Response
    # =====================================================
    @staticmethod
    def parse_quiz(text):

        if not text:
            return None

        questions = []

        # Split by Q1., Q2., ...
        blocks = re.split(r"Q\d+\.", text)

        for block in blocks:

            block = block.strip()

            if not block:
                continue

            try:

                lines = [
                    line.strip()
                    for line in block.split("\n")
                    if line.strip()
                ]

                question = lines[0]

                options = []

                answer_letter = None

                for line in lines[1:]:

                    if re.match(r"^[A-D]\)", line):

                        option = line[2:].strip()

                        options.append(option)

                    elif line.lower().startswith("answer"):

                        answer_letter = (
                            line.split(":")[1]
                            .strip()
                            .upper()
                        )

                if len(options) != 4:
                    continue

                # Convert A/B/C/D into option text
                answer = ""

                mapping = {
                    "A": 0,
                    "B": 1,
                    "C": 2,
                    "D": 3
                }

                if answer_letter in mapping:
                    answer = options[mapping[answer_letter]]

                questions.append(
                    {
                        "question": question,
                        "options": options,
                        "answer": answer
                    }
                )

            except Exception as e:

                print("Quiz Parsing Error:", e)

                continue

        if len(questions) == 0:
            return None

        return questions[:10]