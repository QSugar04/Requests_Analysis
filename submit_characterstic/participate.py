import datetime
from data import repo,commits

# 获取仓库的所有 issue 记录
issues = repo.get_issues(state="all")

# 统计回复时间和评论数量
reply_times = []
comment_counts = []

for issue in issues:
    comments = issue.get_comments()
    if comments.totalCount > 0:
        first_comment = comments[0]
        last_comment = comments.reversed[0]
        first_comment_time = first_comment.created_at
        last_comment_time = last_comment.created_at
        time_difference = last_comment_time - first_comment_time
        reply_times.append(time_difference.total_seconds() / 3600)  # 将回复时间转换为小时
        comment_counts.append(comments.totalCount)

# 计算平均回复时间
average_reply_time = sum(reply_times) / len(reply_times)
print("Average Reply Time: {:.2f} hours".format(average_reply_time))

# 计算平均评论数量
average_comment_count = sum(comment_counts) / len(comment_counts)
print("Average Comment Count: {:.2f}".format(average_comment_count))
