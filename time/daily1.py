import datetime
import matplotlib.pyplot as plt
from data import commits

# 统计每天的提交数量
daily_commits = {}
for commit in commits:
    # 提取提交的日期，并将其格式化为 YYYY-MM-DD 的字符串
    date = commit.commit.author.date.strftime("%Y-%m-%d")
    if date in daily_commits:
        daily_commits[date] += 1
    else:
        daily_commits[date] = 1

# 对提交数量按日期排序
sorted_daily_commits = sorted(daily_commits.items(), key=lambda x: datetime.datetime.strptime(x[0], "%Y-%m-%d"))

# 提取日期和提交数量
dates = [x[0] for x in sorted_daily_commits]
num_commits = [x[1] for x in sorted_daily_commits]

# 绘制提交数量随时间变化的折线图，dates 为 X 轴，num_commits 为 Y 轴
plt.plot(dates, num_commits)
plt.xlabel("Date")
plt.ylabel("Number of Commits")
plt.title("Commits per Day")
plt.xticks(rotation=90)

# 保存图像为当前目录的文件
plt.savefig("Commits per Day.png")

# 关闭图像，释放资源
plt.close()

# 输出提示信息，告知用户图表已保存
print("图表已保存为 Commits per Day.png")