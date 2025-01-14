from collections import Counter
import matplotlib.pyplot as plt
from data import commits

# 获取每个作者的提交数量
author_commits = Counter(commit.commit.author.name for commit in commits)

# 选择贡献最多的前N位作者
top_n = 15
top_authors = dict(author_commits.most_common(top_n))

# 将其余的作者合并为一个“其他”类别
other_authors = dict(author_commits - Counter(top_authors))

# 绘制贡献比例的饼图
labels = list(top_authors.keys()) + ['Other']
sizes = list(top_authors.values()) + [sum(other_authors.values())]

# 绘制饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # 使饼图保持圆形
plt.title(f'Top {top_n} Contributors and Others')
plt.tight_layout()  # 自动调整子图参数使之适应图像区域

# 保存图像为当前目录的文件
plt.savefig("Top 15 Contributors and Others.png")

# 关闭图像，释放资源
plt.close()

print("图表已保存为 Top 15 Contributors and Others.png")
