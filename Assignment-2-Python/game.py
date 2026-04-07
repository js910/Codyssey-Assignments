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
    
# 기본 퀴즈 목록
default_quizzes = [
    Quiz(
        "객체를 단 하나만 생성하여 어디서든 참조하게 하는 생성 패턴은?",
        ["프로토타입(Prototype)", "싱글톤(Singleton)", "브리지(Bridge)", "복합체(Composite)"],
        2
    ),
    Quiz(
        "자료 흐름도(DFD)의 자료를 정의하고 상세히 설명하는 도구는?",
        ["자료 사전(Data Dictionary)", "소단위 명세서(Minispec)", "상태 전이도(STD)", "CASE"],
        1
    ),
    Quiz(
        "하나의 메시지에 대해 여러 형태의 응답을 할 수 있는 객체지향 원리는?",
        ["캡슐화(Encapsulation)", "상속(Inheritance)", "다형성(Polymorphism)", "추상화(Abstraction)"],
        3
    ),
    Quiz(
        "모듈이 다른 모듈의 내부 기능을 직접 참조하는 가장 강한 결합도는?",
        ["내용 결합도(Content)", "공통 결합도(Common)", "외부 결합도(External)", "제어 결합도(Control)"],
        1
    ),
    Quiz(
        "비즈니스 로직과 UI를 분리하는 모델/뷰/컨트롤러 패턴의 명칭은?",
        ["클라이언트-서버", "계층화 패턴", "파이프-필터", "MVC 패턴"],
        4
    )
]