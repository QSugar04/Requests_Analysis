from collections import Counter
import matplotlib.pyplot as plt
from data import commits

# 获取提交信息中的关键词
commit_keywords = []
for commit in commits:
    commit_keywords.extend(commit.commit.message.lower().split())

# 过滤掉常见的停用词（可以根据实际需求扩展停用词列表）
stop_words = set(['and', 'the', 'in', 'of', 'to', 'for', 'with', 'on', 'at'])
filtered_keywords = [word for word in commit_keywords if word not in stop_words]

# 统计关键词的使用频率
keyword_counts = Counter(filtered_keywords)

# 取前N个关键词绘制柱状图
top_n_keywords = 10
top_keywords = dict(keyword_counts.most_common(top_n_keywords))

# 绘制柱状图
plt.bar(top_keywords.keys(), top_keywords.values())
plt.xlabel('Keyword')
plt.ylabel('Frequency')
plt.title('Top Keywords in Commit Messages')
# 保存图像为当前目录的文件
plt.savefig("Top Keywords in Commit Messages.png")

# 关闭图像，释放资源
plt.close()

print("图表已保存为 Top Keywords in Commit Messages.png")
