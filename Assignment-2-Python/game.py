# game.py
import json
import os
from data import Quiz
class QuizGame:
    def __init__(self, default_quizzes):
        self.file_path = "state.json"
        self.default_quizzes = default_quizzes
        self.quizzes = []
        self.load_state()

    # state.json 불러오기
    def load_state(self):
        try:
            #예외처리
            if not os.path.exists(self.file_path):
                self.quizzes = self.default_quizzes
                self.high_score = 0
                return            
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                new_list = []
                for q in data.get("quizzes", []):
                    obj = Quiz(q["question"], q["choices"], q["answer"])
                    new_list.append(obj)
                self.quizzes = new_list
                self.high_score = data.get("best_score",0)
                self.has_played = data.get("has_played",False)       
        except:
            print(f"\n파일 로드 실패. 기본 데이터를 사용합니다")
            self.quizzes = self.default_quizzes
            self.high_score = 0
            self.has_played = False

    # state.json 저장하기
    def save_state(self):
        try:
            data = {
                "quizzes": [q.to_dict() for q in self.quizzes],
                "best_score": self.high_score,
                "has_played": self.has_played
            }
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"파일 저장 실패: {e}")
    
    # 메뉴 표시
    def show_menu(self):
        print("="*30)
        print("\n     퀴즈 게임")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("0. 종료")
        print("="*30)
        return self.safe_answer("선택: ",0,4)
        
    # 실행
    def run(self):
        while True:
            choice = self.show_menu()
            match choice:
                case 1: self.start_quiz()
                case 2: self.add_quiz()
                case 3: self.show_list()
                case 4: self.show_highscore()
                case 0:
                    print("\n프로그램을 종료합니다.")
                    self.save_state()
                    break

    # 퀴즈 풀기
    def start_quiz(self):
        #퀴즈가 없는 경우
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다")
            return
        
        print(f"\n퀴즈를 시작합니다 (총 {len(self.quizzes)}문제)")
        print("\n"+"-"*20)
        self.score = 0

        for i in range(len(self.quizzes)):
            quiz = self.quizzes[i]
            quiz.show_quiz(i+1) 
            user_input = self.safe_answer("\n정답 입력: ",1,4)
            if quiz.is_correct(user_input):
                print("정답입니다!")
                self.score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번")
        self.show_result()
        self.update_score()

    # 점수 표시
    def show_result(self):
        print("="*30)
        print(f"결과: {len(self.quizzes)}문제 중 {self.score}문제 정답! ({self.score/len(self.quizzes)*100}점)")
        print("="*30)

    # 퀴즈 추가
    def add_quiz(self):
        print("\n새로운 퀴즈 추가\n")
        question = input("문제 내용: ").strip()
        choices = [input(f"선택지 {i+1}: ") for i in range(4)]
        answer = self.safe_answer("정답 번호 (1-4): ",1,4)
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_state()

    # 퀴즈 목록
    def show_list(self):
        print(f"\n등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        
        # 퀴즈가 없는 경우
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요")
            return
        
        print("\n"+"-"*20)
        for i in range(len(self.quizzes)):
            print(f"[{i}] {self.quizzes[i].question}")
        print("-"*20)

    # 최고점수 기록
    def update_score(self):
        if len(self.quizzes) == 0: return
        self.has_played = True
        this_score = (int)(self.score/len(self.quizzes)*100)
        if this_score > self.high_score:
            self.high_score = this_score
            print(f"(축하) 새로운 최고 점수입니다!")
        self.save_state()

    # 최고점수 출력
    def show_highscore(self):
        if not self.has_played:
            print("\n아직 게임 플레이 기록이 없습니다.")
        else:
            print(f"\n최고 점수: {self.high_score}점")

    # 예외처리
    def safe_answer(self, prompt, min, max):
        while True:
            try:
                val = input(prompt).strip()
                if not val:
                    print("다시 입력해주세요")
                    continue
                num = int(val)
                if min<=num<=max:
                    return num
                else:
                    print(f"{min}-{max} 사이의 숫자를 입력하세요")
            except ValueError:
                print("숫자 형식으로 입력하세요")