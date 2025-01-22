from github import Github
token='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'
g = Github(token)

# 获取仓库
repo = g.get_repo("psf/requests")

# 获取仓库的提交历史
commits = repo.get_commits()
