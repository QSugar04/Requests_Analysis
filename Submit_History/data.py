from github import Github

# 使用个人的GitHub Token进行身份验证
token = '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'

g = Github(token)

# 获取PEP仓库
repo = g.get_repo("psf/requests")

# 获取仓库的提交历史    
commits = repo.get_commits()

# 打印提交信息示例
# for commit in commits:
#   print(commit.commit.author.date, commit.commit.author.name, commit.commit.message)
