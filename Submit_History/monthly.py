from collections import Counter
import matplotlib.pyplot as plt
from datetime import datetime, timezone
from data import commits

# 获取2022年以后的提交信息
commits_since_2022 = [commit for commit in commits if commit.commit.author.date >= datetime(2022, 1, 1, tzinfo=timezone.utc)]

# 统计每个月的提交数量
commit_dates_since_2022 = [commit.commit.author.date for commit in commits_since_2022]
commit_month_count_since_2022 = Counter(date.strftime('%Y-%m') for date in commit_dates_since_2022)

# 绘制2022至今的提交数量随时间的变化图表
months_since_2022, counts_since_2022 = zip(*commit_month_count_since_2022.items())
plt.plot(months_since_2022, counts_since_2022)
plt.xlabel('Month')
plt.ylabel('Number of Commits')
plt.title('Requests Repository Commit Evolution (2022 - Present)')
plt.xticks(rotation=45)  # 调整x轴刻度旋转角度，避免重叠
plt.tight_layout()  # 自动调整子图参数使之适应图像区域

# 保存图像为当前目录的文件
plt.savefig("commit_evolution_since2022.png")

# 关闭图像，释放资源
plt.close()

print("图表已保存为 commit_evolution_since2022.png")
