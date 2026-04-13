# quiz.py
class Quiz:
    # 속성 정의
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 객체를 딕셔너리로
    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    # 퀴즈 출력 메서드
    def show_quiz(self, index):
        print(f"[문제 {index}] {self.question}\n")
        for i in range(len(self.choices)):
            choice = self.choices[i]
            print(f"{i + 1}. {choice}")

    # 정답 확인 메서드
    def is_correct(self, user_answer):
        return self.answer == user_answer