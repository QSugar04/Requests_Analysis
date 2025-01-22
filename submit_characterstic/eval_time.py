import datetime
from data import commits,repo
# 获取仓库的所有 Pull Request 记录
pull_requests = repo.get_pulls(state="closed")

# 统计每个 Pull Request 的评审时间
review_times = []
# 遍历每个 Pull Request，计算其评审时间
for pull_request in pull_requests:
    # 检查 Pull Request 是否已合并
    if pull_request.merged:
        created_at = pull_request.created_at
        merged_at = pull_request.merged_at
        review_time = merged_at - created_at
        review_times.append(review_time.total_seconds() / 3600)  # 将评审时间从秒转换为小时，并添加到列表中

# 计算评审时间的平均值和中位数
average_review_time = sum(review_times) / len(review_times)
median_review_time = sorted(review_times)[len(review_times) // 2]

# 输出平均评审时间和中位数评审时间
print("Average Review Time: {:.2f} hours".format(average_review_time))
print("Median Review Time: {:.2f} hours".format(median_review_time))

