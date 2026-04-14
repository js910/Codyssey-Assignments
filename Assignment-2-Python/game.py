# game.py
import json
import os
import random
from quiz import Quiz

class QuizGame:
    def __init__(self, default_quizzes):
        self.file_path = "state.json"
        self.default_quizzes = default_quizzes
        self.quizzes = []
        self.q_min = 1
        self.q_max = 4
        self.high_score = 0
        self.has_played = False
        self.load_state()


    # --- 데이터 관리 ---
    # state.json 불러오기
    def load_state(self):
        if not os.path.exists(self.file_path):
            self.quizzes = []
            return
        
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.quizzes = self.validate_data(data)
                self.high_score = data.get("best_score", 0)
                self.has_played = data.get("has_played", False)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"데이터 로드 실패: {e}\n새로 시작합니다.")
            self.quizzes = []

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

    # JSON 검증
    def validate_data(self, data):
        if not isinstance(data, dict):
            raise ValueError("데이터 형식이 사전(dict) 타입이 아닙니다.")
        
        # 필수 키 체크
        required_keys = ["quizzes", "best_score", "has_played"]
        for key in required_keys:
            if key not in data:
                raise ValueError(f"필수 데이터 항목('{key}')이 누락되었습니다.")

        # 리스트 상세 검증
        validated_quizzes = []
        quizzes_data = data.get("quizzes", [])
        
        for i in range(len(quizzes_data)):
            q = quizzes_data[i]
            question = q.get("question", "").strip()
            choices = q.get("choices", [])
            answer = q.get("answer")

            if not question or not isinstance(choices, list) or len(choices) != self.q_max or answer is None:
                raise ValueError(f"{i+1}번째 퀴즈에 누락된 항목이 있습니다.")

            if not all(c.strip() for c in choices):
                raise ValueError(f"{i+1}번째 퀴즈의 선택지 중 비어있는 항목이 있습니다.")

            if len(choices) != self.q_max:
                raise ValueError(f"{i+1}번째 퀴즈의 선택지 개수 오류")

            if not isinstance(answer, int) or not (self.q_min <= answer <= self.q_max):
                raise ValueError(f"{i+1}번째 퀴즈의 정답 범위를 확인하세요.")

            validated_quizzes.append(Quiz(question, choices, answer))
        if not validated_quizzes:
            raise ValueError("유효한 퀴즈 없음")
        return validated_quizzes
    

    # -- 실행 로직 --
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
   
    # 메뉴 표시
    def show_menu(self):
        quiz_count = len(self.quizzes)
        print("\n" + "="*30)
        print(f"  퀴즈 게임")
        print("1. "+("기본 "if quiz_count==0 else "")+"퀴즈 풀기")
        print("2. "+("나만의 퀴즈 만들기"if quiz_count==0 else "퀴즈 추가"))
        print("3. "+("기본 "if quiz_count==0 else "")+"퀴즈 목록")
        print("4. 점수 확인\n0. 종료")
        print("="*30)
        return self.safe_answer("선택: ",0,4)


    # -- 메뉴별 기눙 --
    # 퀴즈 풀기
    def start_quiz(self):
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            while True:
                choice = input("기본 퀴즈로 진행하시겠습니까? (y/n): ").lower().strip()
                if choice == 'y':
                    self.quizzes = self.default_quizzes
                    print(f"\n기본 퀴즈를 불러왔습니다 ({len(self.quizzes)}문제). 퀴즈를 시작합니다\n"+"-"*20)
                    break
                elif choice == 'n':
                    print("퀴즈를 먼저 추가해 주세요.")
                    return
                else:
                    print("잘못된 입력입니다. 'y' 또는 'n'를 입력해주세요.")      
        else:
            print(f"\n퀴즈를 시작합니다 (총 {len(self.quizzes)}문제)\n"+"-"*20)

        # 랜덤 셔플
        random_quiz = random.sample(self.quizzes, len(self.quizzes))
        score = 0

        for i in range(len(random_quiz)):
            quiz = random_quiz[i]
            quiz.show_quiz(i+1) 
            user_input = self.safe_answer("\n정답 입력: ", self.q_min, self.q_max)
            if quiz.is_correct(user_input):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번")
        self.show_result(score)

    # 퀴즈 추가
    def add_quiz(self):
        print("\n새로운 퀴즈 추가\n")
        while True:
            question = input("문제 내용: ").strip()
            if question:
                break
            print("오류: 문제 내용을 입력해야 합니다.")

        # 선택지 입력
        choices = []
        for i in range(self.q_max):
            while True:
                choice = input(f"선택지 {i + 1}: ").strip()
                if choice:
                    choices.append(choice)
                    break
                print(f"오류: 선택지 {i + 1}의 내용을 입력해주세요.")

        answer = self.safe_answer(f"정답 번호 ({self.q_min}-{self.q_max}): ", self.q_min, self.q_max)
        self.quizzes.append(Quiz(question, choices, answer))
        print("퀴즈가 성공적으로 추가되었습니다.")
        self.save_state()

    # 퀴즈 목록
    def show_list(self):
        target = self.quizzes if self.quizzes else self.default_quizzes

        print(f"\n퀴즈 목록 (총 {len(target)}개)\n"+"-"*20)
        for i in range(len(target)):
            print(f"[{i+1}] {target[i].question}")
        print("-"*20)

    # 최고점수 출력
    def show_highscore(self):
        if not self.has_played:
            print("\n아직 게임 플레이 기록이 없습니다.")
        else:
            print(f"\n최고 점수: {self.high_score}점")


    # --- 내부 함수 ---
    # 점수 표시
    def show_result(self, score):
        quiz_count = len(self.quizzes)
        current_score = int(score/quiz_count*100) if quiz_count > 0 else 0
        print(f"\n{'='*30}\n결과: {quiz_count}문제 중 {score}문제 정답! ({current_score}점)\n{'='*30}")
        
        # 최고점수 기록
        self.has_played = True
        if current_score > self.high_score:
            self.high_score = current_score
            print(f"(축하) 새로운 최고 점수입니다!")
        self.save_state()
                
    # 선택지 예외처리
    def safe_answer(self, prompt, min_val, max_val):
        while True:
            try:
                val = input(prompt).strip()
                if not val: continue
                num = int(val)
                if min_val<=num<=max_val:
                    return num
                print(f"{min_val}-{max_val} 사이의 숫자를 입력하세요")
            except ValueError:
                print("숫자 형식으로 입력하세요")
            except (KeyboardInterrupt, EOFError):
                print("\n입력이 중단되었습니다.")
                raise