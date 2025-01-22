from collections import Counter
import matplotlib.pyplot as plt
from data import commits

# 设置 x 轴范围，从 0 到 2000，为了限制直方图的显示范围，避免过长的提交信息影响图表的可读性
plt.xlim(0, 2000)

# 获取每个提交信息的长度
commit_message_lengths = [len(commit.commit.message) for commit in commits]

# 绘制提交信息长度的直方图，使用对数刻度
plt.hist(commit_message_lengths, bins=30, edgecolor='black', log=True)
plt.xlabel('Commit Message Length')  
plt.ylabel('Frequency (log scale)')  
plt.title('Distribution of Commit Message Lengths')  

# 保存图像为当前目录的文件
plt.savefig("length of Commit Messages.png")

# 关闭图像，释放资源
plt.close()
print("图表已保存为 length of Commit Messages.png")

# 分析提交的时间分布，了解仓库的活跃程度。
commit_times = [commit.commit.author.date for commit in commits]

# 统计每年的提交数量
commit_year_counts = Counter(date.year for date in commit_times)

# 绘制折线图
years, counts = zip(*commit_year_counts.items())
plt.plot(years, counts, marker='o')  
plt.xlabel('Year')  
plt.ylabel('Number of Commits') 
plt.title('Requests Repository Commit Evolution Over Years')  

# 保存图像为当前目录的文件
plt.savefig("Requests Repository Commit Evolution Over Years.png")

# 关闭图像，释放资源
plt.close()

print("图表已保存为 Requests Repository Commit Evolution Over Years.png")
