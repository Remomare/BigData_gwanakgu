import matplotlib.pyplot as plt
import numpy as np

x = np.arange(6)
reasons = ["위급상황 대처", "식사 해결", "문화생활","경제적 어려움 ","안전 불안","주거관리"]
values = [35.9, 30.8, 11.9, 10.2, 6.7, 4.5]

plt.bar(x, values)

plt.ylabel("비율")
plt.title("1인 가구 고충")
plt.xticks(x, reasons)

plt.rc('font', family="Malgun Gothic") #그래프 내부의 한글 깨짐 처리

plt.show()