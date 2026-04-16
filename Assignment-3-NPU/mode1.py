# mode1.py
import time

# 공통: mac 연산
def calculate_mac(matrix_a, matrix_b):
    total_sum = 0.0
    size = len(matrix_a)
    for i in range(size):
        for j in range(size):
            total_sum += matrix_a[i][j] * matrix_b[i][j]
    return total_sum

# 모드1: 사용자 입력 (n*n)
def get_input_matrix(size=3):
    matrix = []
    while len(matrix) < size:
        try:
            line = input(f"{len(matrix)+1}행: ").strip()
            row = [float(x) for x in line.split()]
            if len(row) != size:
                print(f"오류: {size}개를 입력해야 합니다.")
                continue
            if any(val < 0.0 or val > 1.0 for val in row):
                print("오류: 0에서 1까지의 숫자만 입력 가능합니다.")
                continue
            matrix.append(row)

        except ValueError:
            print(f"오류: 숫자만 입력하세요.")
        except (KeyboardInterrupt, EOFError):
            raise
    return matrix

# 모드1: 실행
def run_mode1():
    print("\n--- [1] 필터 입력 ---")
    print("필터 A (3줄 입력, 공백 구분)")
    f_a = get_input_matrix(3)
    print("\n필터 B (3줄 입력, 공백 구분)")
    f_b = get_input_matrix(3)
    print("\n--- [2] 패턴 입력 ---")
    print("패턴 (3줄 입력, 공백 구분)")
    p = get_input_matrix(3)

    start = time.perf_counter()
    for _ in range(10): # 10회 평균 측정
        score_a = calculate_mac(p, f_a)
        score_b = calculate_mac(p, f_b)
    end = time.perf_counter()
    avg_ms = ((end - start) / 10) * 1000

    print("\n--- [3] MAC 결과 ---")
    
    # 판정 (Epsilon 적용)
    if abs(score_a - score_b) < 1e-9:
        print(f"A 점수: {score_a:.8f}\nB 점수: {score_b:.8f}")
        print("판정: 판정 불가")
    else:
        print(f"A 점수: {score_a:.1f}\nB 점수: {score_b:.1f}")
        print(f"연산 시간(평균/10회): {avg_ms:.3f}ms")
        print(f"판정: {'A' if score_a > score_b else 'B'}")