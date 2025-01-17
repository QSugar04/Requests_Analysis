import requests
import matplotlib.pyplot as plt

# 通过GitHub API获取仓库的提交信息
url = "https://api.github.com/repos/psf/requests/commits"
response = requests.get(url)
commits = response.json()
print(commits)
exit()
# 统计不同类型的提交数量
commit_types = {}
total_commits = len(commits)
for commit in commits:
    commit_type = commit["commit"]["message"].split(":")[0]
    commit_types[commit_type] = commit_types.get(commit_type, 0) + 1

# 计算每个类型的提交占比
commit_percentages = {commit_type: count / total_commits * 100 for commit_type, count in commit_types.items()}

# 绘制饼图
plt.figure(figsize=(8, 6))
plt.pie(list(commit_percentages.values()), labels=list(commit_percentages.keys()), autopct='%1.1f%%')
plt.title("Commit Types Distribution")
plt.axis('equal')

# 解决字体缺失问题
font_path = "path/to/your/chinese/font.ttf"
plt.rcParams['font.family'] = 'Arial Unicode MS'

plt.savefig("Commit Types Distribution.png")

# 关闭图像，释放资源
plt.close()

print("图表已保存为 Commit Types Distribution.png")
