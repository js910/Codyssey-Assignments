# mode2.py
import json
import time
from mode1 import calculate_mac

# 라벨 정규화
def normalize_label(label):
    l = str(label).lower().strip()
    if l in ['+', 'cross']: return "Cross"
    if l in ['x']: return "X"
    return "UNDECIDED"

# 모드2: 실행
def run_mode2():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("오류: data.json 파일이 없습니다.")
        return

    filters = data.get("filters", {})
    patterns = data.get("patterns", {})
    
    print("\n--- [1] 필터 로드 ---")
    loaded_sizes = sorted([int(k.split('_')[1]) for k in filters.keys()])
    for size in loaded_sizes:
        print(f"✓ size_{size}  필터 로드 완료 (Cross, X)")

    stats = {"total": 0, "pass": 0, "fail": 0, "failures": []}
    perf_data = {} # 평균 시간 저장용

    print("\n--- [2] 패턴 분석 ---")
    for p_key, p_val in patterns.items():
        # 키에서 크기 추출
        size_n = int(p_key.split('_')[1])
        input_data = p_val["input"]
        expected = normalize_label(p_val["expected"])
        
        # 해당 크기의 필터 로드
        f_set = filters.get(f"size_{size_n}", {})
        f_cross = f_set.get("cross")
        f_x = f_set.get("x")

        # 행렬 크기 및 필터 존재 여부 검증
        if f_cross is None or f_x is None or len(input_data) != size_n:
            stats["total"] += 1
            stats["fail"] += 1
            stats["failures"].append(f"{p_key}: 스키마 또는 크기 불일치")
            continue

        # 10회 반복 측정
        iterations = 10
        total_ms = 0.0
        
        for _ in range(iterations):
            t_start = time.perf_counter()
            sc_cross = calculate_mac(input_data, f_cross)
            sc_x = calculate_mac(input_data, f_x)
            t_end = time.perf_counter()
            total_ms += (t_end - t_start) * 1000
        
        avg_ms = total_ms / iterations
        perf_data[size_n] = avg_ms # 해당 크기의 평균 시간 갱신

        # 판정 (Epsilon)
        if abs(sc_cross - sc_x) < 1e-9: result = "UNDECIDED"
        else: result = "Cross" if sc_cross > sc_x else "X"
        status = "PASS" if result == expected else "FAIL"

        # 출력
        print(f"- {p_key}")
        if result == "UNDECIDED":
            print(f"Cross 점수: {sc_cross:.16f}")
            print(f"X 점수: {sc_x:.16f}")
            print(f"판정: {result} | expected: {expected} | {status} (동점 규칙)")
        else:
            print(f"Cross 점수: {sc_cross:.10g}")
            print(f"X 점수: {sc_x:.10g}")
            print(f"판정: {result} | expected: {expected} | {status}")
        
        # 통계 업데이트
        stats["total"] += 1
        if status == "PASS":
            stats["pass"] += 1
        else:
            stats["fail"] += 1
            fail_reason = "동점(UNDECIDED) 처리 규칙" if result == "UNDECIDED" else f"판정 불일치({result})"
            stats["failures"].append(f"{p_key}: {fail_reason}에 따라 FAIL")

    # 성능 분석 표 출력
    print("\n--- [3] 성능 분석 (평균/10회) ---")
    print("크기 | 평균 시간(ms) | 연산 횟수")
    for sz in sorted(perf_data.keys()):
        print(f"{sz}x{sz} | {perf_data[sz]:.4f} | {sz*sz}")

    # 결과 요약
    print("\n--- [4] 결과 요약 ---")
    print(f"총 테스트 {stats['total']}개\n통과 {stats['pass']}개\n실패 {stats['fail']}개")
    if stats["failures"]:
        print("\n실패 케이스:")
        for f in stats["failures"]:
            print(f"- {f}")