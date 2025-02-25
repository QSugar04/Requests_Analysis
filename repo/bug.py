from github import Github
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime
import re

# 初始化 Github 客户端
TOKEN = "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"  # 替换为你的 GitHub 令牌
g = Github(TOKEN)

# 替换为目标仓库名
repo_name = "psf/requests"
repo = g.get_repo(repo_name)

# 获取所有标签
labels = repo.get_labels()
selected_label = "bug"

# 获取目标标签对象
selected_label_obj = None
for label in labels:
    if label.name == selected_label:# 查找目标标签
        selected_label_obj = label
        break

if not selected_label_obj:
    print(f"Label '{selected_label}' not found.")
    exit()

# 获取具有特定标签的问题
bug_issues = repo.get_issues(labels=[selected_label_obj])

# 分析Bug修复的提交数量随时间的变化
bug_commit_dates = []
commit_hash_pattern = re.compile(r"(?:[Ff]ixed|[Cc]losed) in commit ([a-f0-9]{7,40})")

for issue in bug_issues:
    # 获取与 Issue 相关的评论
    comments = issue.get_comments()
    for comment in comments:
        match = commit_hash_pattern.search(comment.body)
        if match:
            commit_hash = match.group(1)
            try:
                commit = repo.get_commit(commit_hash)
                bug_commit_dates.append(commit.commit.author.date)
            except Exception as e:
                print(f"Error fetching commit {commit_hash}: {e}")

if bug_commit_dates:
    # 按月份统计提交次数
    bug_commit_month_count = Counter(date.strftime('%Y-%m') for date in bug_commit_dates)
    bug_months, bug_counts = zip(*sorted(bug_commit_month_count.items()))
    plt.plot(bug_months, bug_counts)
    plt.xlabel("Month")
    plt.ylabel("Number of Bug Fixes")
    plt.title("Bug Fix Commit Evolution")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Bug Fix Commit Evolution.png")
    print("图表已保存为 Bug Fix Commit Evolution.png")
else:
    print("No Bug Fix Commits found.")
