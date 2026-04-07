# game.py
class Quiz:
    # 속성 정의
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 퀴즈 출력 메서드
    def show_quiz(self, index):
        print(f"[문제 {index}] {self.question}\n")
        for i in range(len(self.choices)):
            choice = self.choices[i]
            print(f"{i + 1}. {choice}")

    # 정답 확인 메서드
    def is_correct(self, user_answer):
        return self.answer == user_answer
    
class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes
        self.score = 0
    
    def start(self):
        #퀴즈가 없는 경우
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다")
            return
        
        print("\n퀴즈를 시작합니다 (총 5문제)")
        print("\n"+"-"*20)
        self.score = 0

        for i in range(len(self.quizzes)):
            quiz = self.quizzes[i]
            quiz.show_quiz(i+1)
            
            try:
                user_input = int(input("\n정답 입력: "))
                if quiz.is_correct(user_input):
                    print("정답입니다!")
                    self.score += 1
                else:
                    print(f"오답입니다. 정답은 {quiz.answer}번")
            except ValueError:
                print("잘못된 입력입니다. 오답 처리됩니다.")
            
        self.show_result()

    def show_result(self):
        print("="*30)
        print(f"결과: {len(self.quizzes)}문제 중 {self.score}문제 정답! ({self.score/len(self.quizzes)*100}점)")
        print("="*30)

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