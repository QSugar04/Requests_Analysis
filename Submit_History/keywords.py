from collections import Counter
import matplotlib.pyplot as plt
from data import commits

# 提取提交信息中的关键词
commit_keywords = []
for commit in commits:
    # 将提交信息转换为小写并分割为单词
    commit_keywords.extend(commit.commit.message.lower().split())

# 定义停用词列表（可根据实际需求扩展）
stop_words = set(['and', 'the', 'in', 'of', 'to', 'for', 'with', 'on', 'at'])

# 过滤掉停用词
filtered_keywords = [word for word in commit_keywords if word not in stop_words]

# 统计关键词的使用频率
keyword_counts = Counter(filtered_keywords)

# 获取出现频率最高的前N个关键词
top_n_keywords = 10
top_keywords = dict(keyword_counts.most_common(top_n_keywords))

# 绘制柱状图
plt.figure(figsize=(10, 6))  # 设置图像大小
plt.bar(top_keywords.keys(), top_keywords.values(), color='skyblue')  # 添加柱状图颜色
plt.xlabel('Keyword', fontsize=12)  # 设置X轴标签
plt.ylabel('Frequency', fontsize=12)  # 设置Y轴标签
plt.title('Top Keywords in Commit Messages', fontsize=14)  # 设置标题

# 保存图像到当前目录
plt.savefig("Top Keywords in Commit Messages.png", dpi=300)  # 设置保存图像的分辨率

# 关闭图像，释放资源
plt.close()

print("图表已成功保存为 'Top Keywords in Commit Messages.png'")