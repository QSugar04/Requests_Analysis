import matplotlib.pyplot as plt
from data import repo,commits

# 获取仓库的所有贡献者
contributors = repo.get_contributors()

# 提取贡献者用户名和提交数量
contributor_data = [(contributor.login, contributor.contributions) for contributor in contributors]

# 按照提交数量排序
contributor_data.sort(key=lambda x: x[1], reverse=True)

# 取前 N 名贡献者
# 这里取前 10 名贡献者，可以根据需要调整数量
top_contributors = contributor_data[:10]  
# 提取用户名和提交数量
top_usernames, top_contributions = zip(*top_contributors)

# 绘制柱状图
plt.figure(figsize=(10, 5))
plt.bar(top_usernames, top_contributions, color='blue')
plt.xlabel('Contributor')
plt.ylabel('Number of Contributions')
plt.title('Top Contributors by Contributions')
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()

# 显示图表
plt.savefig('Top Contributors by Contributions')
