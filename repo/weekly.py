from data import repo
from collections import defaultdict
import matplotlib.pyplot as plt
from data import commits


# 统计每周提交次数的分布
commit_weekly_counts = defaultdict(int)
# 遍历所有提交记录
for commit in commits:
    week_number = commit.commit.author.date.isocalendar()[1]
    commit_weekly_counts[week_number] += 1

# 提取周数和对应的提交次数
weeks, counts = zip(*commit_weekly_counts.items())
# 绘制每周提交次数的折线图
plt.plot(weeks, counts)
plt.xlabel('Week')
plt.ylabel('Number of Commits')
plt.title('Weekly Commit Pattern')
# 保存图表为文件
plt.savefig('Weekly Commit Pattern')
