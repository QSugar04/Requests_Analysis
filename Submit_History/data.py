from github import Github

# 使用个人的GitHub Token进行身份验证
# 注意：在实际代码中，建议将Token存储在环境变量或配置文件中，避免直接写在代码里
token = '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'

# 初始化GitHub客户端
g = Github(token)

# 获取仓库
repo = g.get_repo("psf/requests")

# 获取仓库的提交历史    
commits = repo.get_commits()

# 打印提交信息示例
# for commit in commits:
#   print(commit.commit.author.date, commit.commit.author.name, commit.commit.message)
