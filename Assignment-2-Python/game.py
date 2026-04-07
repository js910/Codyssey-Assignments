# game.py

class Quiz:
    # 속성 정의
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 퀴즈 출력 메서드
    def show_quiz(self, index):
        print(f"\n[문제 {index}] {self.question}")
        for i in range(len(self.choices)):
            choice = self.choices[i]
            print(f"{i + 1}. {choice}")

    # 정답 확인 메서드
    def is_correct(self, user_answer):
        return self.answer == user_answer