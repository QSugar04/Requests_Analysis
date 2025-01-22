import requests
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 替换为你的 GitHub 用户名和访问令牌
USERNAME = "QSugar"
TOKEN = "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"

# API URL，使用 GitHub API 获取仓库的提交记录。
url = "https://api.github.com/repos/psf/requests/commits?per_page=100"
response = requests.get(url, auth=(USERNAME, TOKEN))

# 检查响应状态码，如果响应状态码不是 200（表示成功），打印错误信息并退出程序。
if response.status_code != 200:
    print(f"Error: Unable to fetch commits, status code {response.status_code}")
    print(response.text)  # 输出错误信息
    exit()

# 解析响应数据，将响应内容解析为 JSON 格式。
commits = response.json()

# 检查数据格式，确保返回的数据是列表格式
if not isinstance(commits, list):
    print("Unexpected API response format.")
    print(commits)
    exit()

# 统计和绘图代码保持不变...
commit_types = {}
total_commits = len(commits)

# 遍历每个提交记录，提取提交类型并统计数量。
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
# font_path = "path/to/your/chinese/font.ttf"
# plt.rcParams['font.family'] = 'Arial Unicode MS'

plt.savefig("Commit Types Distribution.png")

# 关闭图像，释放资源
plt.close()

print("图表已保存为 Commit Types Distribution.png")
