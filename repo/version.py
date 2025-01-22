from data import repo
import matplotlib.pyplot as plt
from collections import Counter

# 获取仓库版本发布信息
releases = repo.get_releases()
# 提取每个版本的发布时间
release_dates = [release.published_at for release in releases]
# 按月份统计版本发布的数量
release_month_count = Counter(date.strftime('%Y-%m') for date in release_dates)

# 检查是否有版本发布数据
if release_month_count:
    release_months, release_counts = zip(*release_month_count.items())
    # 绘制版本发布数量随时间的变化趋势图
    plt.plot(release_months, release_counts)
    plt.xlabel('Month')
    plt.ylabel('Number of Releases')
    plt.title('Repository Releases Evolution')
    # 保存图表为文件
    plt.savefig('Repository Releases Evolution')
else:
    print("No releases found.")
