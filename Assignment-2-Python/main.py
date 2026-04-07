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
            game.add_quiz()
        elif choice == "3":
            game.show_list()
        elif choice == "4":
            game.show_highscore()
        elif choice == "0":
            print("\n프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 0-4 사이의 숫자를 입력하세요")

if __name__ == "__main__":
    main()