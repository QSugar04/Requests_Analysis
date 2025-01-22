from collections import Counter
import matplotlib.pyplot as plt
from data import repo,commits



# 关闭图像，释放资源
plt.close()

print("图表已保存为 Label Distribution.png")

# 分析主题分布，提取每个 issue 的标题作为主题
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
