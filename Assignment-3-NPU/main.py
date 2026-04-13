import json
import time

# ==========================================
# [공통 함수] 핵심 연산 및 도구
# ==========================================

def calculate_mac(matrix_a, matrix_b):
    """두 행렬의 MAC 연산 (곱하고 더하기)"""
    total_sum = 0.0
    size = len(matrix_a)
    for i in range(size):
        for j in range(size):
            total_sum += matrix_a[i][j] * matrix_b[i][j]
    return total_sum

def normalize_label(label):
    """라벨 정규화: 형식이 다른 정답을 표준 단어로 통일"""
    l = str(label).lower().strip()
    if l in ['+', 'cross']: return "Cross"
    if l in ['x']: return "X"
    return "UNDECIDED"

# ==========================================
# [모드 1] 사용자 직접 입력 (3x3)
# ==========================================

def get_input_matrix(size=3):
    """콘솔로부터 n x n 행렬 입력받기"""
    matrix = []
    while len(matrix) < size:
        try:
            line = input(f"{len(matrix)+1}행: ").split()
            row = [float(x) for x in line]
            if len(row) != size: raise ValueError
            matrix.append(row)
        except:
            print(f"오류: {size}개의 숫자를 공백으로 구분해 입력하세요.")
    return matrix

def run_mode_1():
    print("\n--- [모드 1] 필터 A(십자가) 입력 ---")
    f_a = get_input_matrix(3)
    print("\n--- [모드 1] 필터 B(X) 입력 ---")
    f_b = get_input_matrix(3)
    print("\n--- [모드 1] 패턴 입력 ---")
    p = get_input_matrix(3)

    start = time.perf_counter()
    for _ in range(10): # 평균 측정을 위한 반복
        score_a = calculate_mac(p, f_a)
        score_b = calculate_mac(p, f_b)
    end = time.perf_counter()

    avg_ms = ((end - start) / 10) * 1000
    print(f"\nA 점수: {score_a} | B 점수: {score_b}")
    print(f"연산 시간(avg): {avg_ms:.4f} ms")
    
    # 판정 (Epsilon 적용)
    if abs(score_a - score_b) < 1e-9: print("판정: 판정 불가")
    else: print(f"판정: {'A' if score_a > score_b else 'B'}")

# ==========================================
# [모드 2] data.json 분석 (일괄 처리)
# ==========================================

def run_mode_2():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("오류: data.json 파일이 없습니다.")
        return

    filters = data.get("filters", {})
    patterns = data.get("patterns", {})
    
    stats = {"total": 0, "pass": 0, "fail": 0, "failures": []}
    performance = {} # 시간 복잡도 분석용

    print("\n# [2] 패턴 분석 시작")
    for p_key, p_val in patterns.items():
        # 키(size_5_1)에서 크기(5) 추출
        size_n = int(p_key.split('_')[1])
        input_data = p_val["input"]
        expected = normalize_label(p_val["expected"])
        
        # 해당 크기의 필터 로드
        f_set = filters.get(f"size_{size_n}", {})
        f_cross = f_set.get("cross")
        f_x = f_set.get("x")

        # 시간 측정 및 연산
        t_start = time.perf_counter()
        sc_cross = calculate_mac(input_data, f_cross)
        sc_x = calculate_mac(input_data, f_x)
        t_end = time.perf_counter()
        
        elapsed_ms = (t_end - t_start) * 1000
        performance[size_n] = elapsed_ms # 마지막 측정값 저장 (혹은 평균값)

        # 판정
        if abs(sc_cross - sc_x) < 1e-9: result = "UNDECIDED"
        else: result = "Cross" if sc_cross > sc_x else "X"

        # 통계
        status = "PASS" if result == expected else "FAIL"
        stats["total"] += 1
        if status == "PASS": stats["pass"] += 1
        else:
            stats["fail"] += 1
            stats["failures"].append(f"{p_key}: {result} vs {expected}")

        print(f"- {p_key} | {result} | expected: {expected} | {status}")

    # 성능 분석 표 출력
    print("\n# [3] 성능 분석")
    print("크기 | 평균 시간(ms) | 연산 횟수(N²)")
    for sz in sorted(performance.keys()):
        print(f"{sz}x{sz} | {performance[sz]:.4f} | {sz*sz}")

    # 결과 요약
    print(f"\n# [4] 요약: 총 {stats['total']}, 통과 {stats['pass']}, 실패 {stats['fail']}")
    for f in stats["failures"]: print(f"  * 실패: {f}")

# ==========================================
# [메인] 프로그램 시작점
# ==========================================

def main():
    while True:
        print("\n=== Mini NPU Simulator ===")
        print("1. 사용자 입력 (3x3)")
        print("2. data.json 분석")
        print("3. 종료")
        choice = input("선택: ")
        if choice == '1': run_mode_1()
        elif choice == '2': run_mode_2()
        elif choice == '3': break

if __name__ == "__main__":
    main()