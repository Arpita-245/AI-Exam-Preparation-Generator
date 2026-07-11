import re


class QuizParser:

    @staticmethod
    def parse(quiz_text):

        questions = []

        pattern = r'(\d+\..*?)(?=\n\d+\.|\Z)'

        blocks = re.findall(
            pattern,
            quiz_text,
            re.S
        )

        for block in blocks:

            lines = [
                line.strip()
                for line in block.split("\n")
                if line.strip()
            ]

            if len(lines) < 6:
                continue

            question = lines[0]

            options = lines[1:5]

            answer = ""

            for line in lines:

                if line.lower().startswith("correct answer"):

                    full_answer = line.split(":", 1)[1].strip()

                    # Store only A/B/C/D
                    answer = full_answer[0].upper()

            questions.append({

                "question": question,

                "options": options,

                "answer": answer

            })

        return questions