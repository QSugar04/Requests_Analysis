from collections import Counter
import matplotlib.pyplot as plt
from data import commits

# 遍历所有提交记录，提取提交信息中的关键词
# 将提交信息转换为小写并按空格分割为单词，然后将所有单词收集到一个列表中
commit_keywords = []
for commit in commits:
    commit_keywords.extend(commit.commit.message.lower().split())

# 定义一个停用词集合，用于过滤掉常见的无意义单词
stop_words = set(['and', 'the', 'in', 'of', 'to', 'for', 'with', 'on', 'at'])

# 过滤掉停用词，仅保留有意义的关键词
filtered_keywords = [word for word in commit_keywords if word not in stop_words]

# 使用Counter统计每个关键词的出现频率
keyword_counts = Counter(filtered_keywords)

# 选择出现频率最高的前N个关键词用于绘制柱状图
# top_n_keywords定义了需要展示的关键词数量
top_n_keywords = 10
top_keywords = dict(keyword_counts.most_common(top_n_keywords))

# 绘制柱状图
plt.bar(top_keywords.keys(), top_keywords.values())
plt.xlabel('Keyword')
plt.ylabel('Frequency')
plt.title('Top Keywords in Commit Messages')

# 文件将保存在当前工作目录中
plt.savefig("Top Keywords in Commit Messages.png")

# 关闭图像窗口，释放绘图资源
plt.close()

# 输出提示信息并告知用户图表已成功保存
print("图表已保存为 Top Keywords in Commit Messages.png")