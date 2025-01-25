import datetime
from data import repo,commits

# 获取仓库的所有 issue 记录
issues = repo.get_issues(state="all")

# 初始化两个列表，分别用于存储每个 issue 的回复时间和评论数量
reply_times = []
comment_counts = []


# 计算平均回复时间并打印
average_reply_time = sum(reply_times) / len(reply_times)
print("Average Reply Time: {:.2f} hours".format(average_reply_time))

# 计算平均评论数量并打印
average_comment_count = sum(comment_counts) / len(comment_counts)
print("Average Comment Count: {:.2f}".format(average_comment_count))
