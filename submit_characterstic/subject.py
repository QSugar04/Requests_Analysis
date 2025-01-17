from collections import Counter
import matplotlib.pyplot as plt
from data import repo,commits

issues = repo.get_issues(state="closed")

# 统计标签分布
labels_counter = Counter()
for issue in issues:
    labels = issue.labels
    for label in labels:
        labels_counter[label.name] += 1

# 绘制标签分布柱状图
labels = list(labels_counter.keys())
counts = list(labels_counter.values())

plt.bar(labels, counts)
plt.xlabel("Labels")
plt.ylabel("Count")
plt.title("Label Distribution")
plt.xticks(rotation=90)
plt.savefig("Label Distribution.png")

# 关闭图像，释放资源
plt.close()

print("图表已保存为 Label Distribution.png")

# 分析主题分布
topics = []
for issue in issues:
    title = issue.title
    topics.append(title)

# 统计主题分布
topics_counter = Counter(topics)

# 打印贡献较多的主题
top_contributed_topics = topics_counter.most_common(5)
print("Top Contributed Topics:")
for topic, count in top_contributed_topics:
    print(topic, "-", count, "contributions")
