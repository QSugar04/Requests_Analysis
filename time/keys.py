from collections import Counter
import matplotlib.pyplot as plt
from data import repo,commits

# 获取提交信息中的关键词
commit_keywords = []
for commit in commits:
    commit_keywords.extend(commit.commit.message.lower().split())

# 过滤掉常见的停用词（可以根据实际需求扩展停用词列表）
stop_words = set(['and', 'the', 'in', 'of', 'to', 'for', 'with', 'on', 'at'])
# 使用列表推导式过滤掉停用词，仅保留有意义的关键词
filtered_keywords = [word for word in commit_keywords if word not in stop_words]

# 统计关键词的使用频率
keyword_counts = Counter(filtered_keywords)

# 取前N个关键词绘制柱状图
top_n_keywords = 10
top_keywords = dict(keyword_counts.most_common(top_n_keywords))

# 将其余的关键词合并为一个“其他”类别
other_keywords = dict(keyword_counts - Counter(top_keywords))

# 绘制贡献比例的饼图
labels = list(top_keywords.keys()) + ['Other']
sizes = list(top_keywords.values()) + [sum(other_keywords.values())]


# 绘制饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # 使饼图保持圆形
plt.title(f'Top {top_n_keywords} Contributors and Others')
plt.savefig(f'Top {top_n_keywords} Contributors and Others')
