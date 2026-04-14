# main.py
from mode1 import run_mode1
from mode2 import run_mode2

def main():
    try:
        while True:
            print("\n=== Mini NPU Simulator ===")
            print("1. 사용자 입력 (3x3)")
            print("2. data.json 분석")
            print("3. 종료")
            choice = input("선택: ")
            if choice == '1': run_mode1()
            elif choice == '2': run_mode2()
            elif choice == '3': break
    except (KeyboardInterrupt, EOFError):
        print("\n시스템이 강제 종료되었습니다.")

if __name__ == "__main__":
    main()