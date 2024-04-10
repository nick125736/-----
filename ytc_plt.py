import csv
import matplotlib.pyplot as plt
import numpy as np

csv_file = './csv/vk_xq1P7vIU.csv'

def read_csv(file):
    polarities = []
    subjectivities = []
    with open(file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            polarities.append(float(row['polarities']))
            subjectivities.append(float(row['subjectivities']))
    return polarities, subjectivities

polarities, subjectivities = read_csv(csv_file)

def cal(data):
    median = np.median(data)
    mean = np.mean(data)
    return median, mean

median_polarity, mean_polarity = cal(polarities)
median_subjectivity, mean_subjectivity = cal(subjectivities)

plt.figure(figsize=(10, 5))
plt.scatter(polarities, subjectivities, color='b', alpha=0.5)
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')

plt.axvline(x=median_polarity, color='red', linestyle='--', label=f'Median Polarity: {median_polarity:.2f}')
plt.axvline(x=mean_polarity, color='green', linestyle='--', label=f'Mean Polarity: {mean_polarity:.2f}')
plt.axhline(y=median_subjectivity, color='red', linestyle='--', label=f'Median Subjectivity: {median_subjectivity:.2f}')
plt.axhline(y=mean_subjectivity, color='green', linestyle='--', label=f'Mean Subjectivity: {mean_subjectivity:.2f}')

plt.legend()
plt.grid()
plt.show()

# 当涉及到统计数据时，除了平均数之外，中位数和众数也是非常有用的统计量。下面是一些常见的统计量以及它们的用途：

# 平均数（Mean）：所有数值的总和除以数值的数量。它可以用来表示数据的集中趋势。

# 中位数（Median）：将数据排序后位于中间位置的数值。它可以用来表示数据的中心值，不受极端值的影响。

# 众数（Mode）：数据集中出现最频繁的数值。它可以用来表示数据的典型值。

# 标准差（Standard Deviation）：衡量数据的离散程度。较大的标准差表示数据点更分散。

# 方差（Variance）：标准差的平方。它描述了数据点与均值之间的差异程度。

# 四分位数（Quartiles）：将数据排序后分成四等份的数值。第一四分位数(Q1)表示数据中25%的值低于它，第三四分位数(Q3)表示数据中75%的值低于它。