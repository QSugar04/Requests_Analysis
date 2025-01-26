from github import Github

# 使用个人的GitHub Token进行身份验证
token='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'

# 初始化GitHub客户端
g = Github(token)

# 获取仓库
repo = g.get_repo("psf/requests")

# 获取仓库的提交历史
commits = repo.get_commits()
