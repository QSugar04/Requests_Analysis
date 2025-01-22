import datetime
from data import commits,repo
# 获取仓库的所有 Pull Request 记录
pull_requests = repo.get_pulls(state="closed")



# 计算评审时间的平均值和中位数
average_review_time = sum(review_times) / len(review_times)
median_review_time = sorted(review_times)[len(review_times) // 2]

# 输出平均评审时间和中位数评审时间
print("Average Review Time: {:.2f} hours".format(average_review_time))
print("Median Review Time: {:.2f} hours".format(median_review_time))

