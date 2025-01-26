from data import repo
import matplotlib.pyplot as plt
from collections import Counter


# 获取仓库的所有Issue
issues = repo.get_issues(state='all')

# 统计Issue状态分布
issue_states = Counter(issue.state for issue in issues)
# 提取状态标签和对应的数量
labels = list(issue_states.keys())
sizes = list(issue_states.values())

# 绘制 Issue 状态分布的饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

# 设置饼图的x轴和y轴相等，以确保饼图是圆形的
plt.axis('equal')

# 设置饼图的标题
plt.title('Distribution of Issue States')

# 保存饼图为图片文件，文件名是"Distribution of Issue States"
plt.savefig("Distribution of Issue States")

# 统计平均解决时间
closed_issues = [issue for issue in issues if issue.state == 'closed']
average_resolution_time = sum((issue.closed_at - issue.created_at).days for issue in closed_issues) / len(closed_issues)
print(f'Average Resolution Time for Issues: {average_resolution_time} days')
