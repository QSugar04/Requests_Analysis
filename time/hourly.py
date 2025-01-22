import matplotlib.pyplot as plt
from datetime import datetime
from collections import Counter
from data import repo,commits
# 获取仓库的所有提交
commits = list(repo.get_commits())

# 提取提交时间信息
commit_times = [commit.commit.author.date for commit in commits]

# 统计每小时的提交数量
hourly_counts = Counter(time.hour for time in commit_times)


