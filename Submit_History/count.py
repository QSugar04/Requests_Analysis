from collections import Counter
import matplotlib.pyplot as plt
from data import commits

# 统计每个月的提交数量
commit_dates = [commit.commit.author.date for commit in commits]
commit_month_count = Counter(date.strftime('%Y-%m') for date in commit_dates)

# 绘制提交数量随着时间的变化图表并保存
months, counts = zip(*sorted(commit_month_count.items()))  # 确保按时间排序
plt.figure(figsize=(10, 6))  
plt.plot(months, counts, marker='o') 
plt.xlabel('Month')
plt.ylabel('Number of Commits')
plt.title('Requests Repository Commit Evolution')
plt.xticks(rotation=45)  
plt.tight_layout()  

# 保存图像为当前目录的文件
plt.savefig("commit_evolution.png")

# 关闭图像，释放资源
plt.close()

print("图表已保存为 commit_evolution.png")
