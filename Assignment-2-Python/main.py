# main.py
from game import QuizGame, default_quizzes

def main():
    game = QuizGame(default_quizzes)

    while True:
        print("="*30)
        print("\n     퀴즈 게임")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("0. 종료")
        print("="*30)
        
        choice = input("선택: ").strip()
        
        if choice == "1":
            game.start()
        elif choice == "2":
            print("\n새로운 퀴즈를 추가합니다")
        elif choice == "3":
            print("\n등록된 퀴즈 목록")
        elif choice == "4":
            print("\n최고 점수: n점 (n문제 중 n문제 정답)")
        elif choice == "0":
            print("\n프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요")

if __name__ == "__main__":
    main()