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
hours = sorted(hourly_counts.keys())
counts = [hourly_counts[hour] for hour in hours]
plt.figure(figsize=(12, 6))
plt.plot(hours, counts, marker='o')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Commits')
plt.title('Commit Activity Over the Day')
plt.grid(True)
plt.savefig('Commit Activity Over the Day')
