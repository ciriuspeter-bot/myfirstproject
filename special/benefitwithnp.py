import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
# 예시 데이터: 학생들의 시험 점수 (0~100점)
np.random.seed(42)  # 재현성을 위한 시드 설정
scores = np.random.normal(70, 15, 100)  # 평균 70, 표준편차 15, 100개 데이터
scores = np.clip(scores, 0, 100)  # 0~100 범위로 제한

# 다른 데이터셋: 제품 가격 (만원 단위)
prices = np.random.exponential(50, 50)  # 지수분포
prices = np.round(prices, 1)

# 범주형 데이터
categories = np.random.choice(['A', 'B', 'C', 'D'], 100, p=[0.3, 0.4, 0.2, 0.1])

def print_basic_stats(data, data_name="데이터"):
    """기본 통계량을 출력하는 함수"""
    print(f"\n=== {data_name} 통계 분석 ===")
    print(f"데이터 개수 (count): {len(data)}")
    print(f"평균 (mean): {np.mean(data):.2f}")
    print(f"중앙값 (median): {np.median(data):.2f}")
    print(f"최소값 (min): {np.min(data):.2f}")
    print(f"최대값 (max): {np.max(data):.2f}")
    print(f"범위 (range): {np.max(data) - np.min(data):.2f}")
    print(f"분산 (variance): {np.var(data):.2f}")
    print(f"표준편차 (std): {np.std(data):.2f}")
    print(f"왜도 (skewness): {stats.skew(data):.3f}")
    print(f"첨도 (kurtosis): {stats.kurtosis(data):.3f}")

# 실행
print_basic_stats(scores, "시험 점수")
print_basic_stats(prices, "제품 가격")