from collections import Counter
import matplotlib.pyplot as plt
from datetime import datetime, timezone
from data import commits

# 筛选出2022年及以后的提交记录
commits_since_2022 = [commit for commit in commits if commit.commit.author.date >= datetime(2022, 1, 1, tzinfo=timezone.utc)]

# 提取这些提交的日期，并按年份和月份统计提交数量
commit_dates_since_2022 = [commit.commit.author.date for commit in commits_since_2022]
commit_month_count_since_2022 = Counter(date.strftime('%Y-%m') for date in commit_dates_since_2022)

# 绘制2022年至今的提交数量随时间的变化图表
# 使用zip(*)将Counter对象解包为两个元组：月份和对应的提交数量
months_since_2022, counts_since_2022 = zip(*commit_month_count_since_2022.items())

