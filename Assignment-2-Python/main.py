# main.py
from game import QuizGame, default_quizzes

def main():
    game = QuizGame(default_quizzes)
    game.run()
    
if __name__ == "__main__":
    main()