import matplotlib.pyplot as plt
from datetime import datetime
from collections import Counter
from data import repo,commits

# 获取仓库的所有提交
commits = list(repo.get_commits())

# 提取提交时间信息
commit_times = [commit.commit.author.date for commit in commits]

# 统计每小时的提交数量
hourly_counts = Counter(time.hour for time in commit_times)

# 绘制提交高峰图
# 对hourly_counts的键（小时）进行排序，得到一天中的小时列表
hours = sorted(hourly_counts.keys())

# 根据排序后的小时列表，从hourly_counts字典中获取对应的提交次数，生成一个列表
counts = [hourly_counts[hour] for hour in hours]

# 创建一个新的图形，指定大小为12x6英寸
plt.figure(figsize=(12, 6))

# 绘制小时和提交次数的折线图，使用'o'标记每个数据点
plt.plot(hours, counts, marker='o')

# 设置x轴的标签为“Hour of Day”（一天中的小时）
plt.xlabel('Hour of Day')

# 设置y轴的标签为“Number of Commits”（提交次数）
plt.ylabel('Number of Commits')

# 设置图表的标题为“Commit Activity Over the Day”（一天中的提交活动）
plt.title('Commit Activity Over the Day')

# 显示网格线，使图表更易于阅读
plt.grid(True)

# 将图表保存为文件，文件名为'Commit Activity Over the Day'，不带扩展名
plt.savefig('Commit Activity Over the Day')
