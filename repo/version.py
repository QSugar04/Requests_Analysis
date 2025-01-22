from data import repo
import matplotlib.pyplot as plt
from collections import Counter

# 获取仓库版本发布信息
releases = repo.get_releases()
release_dates = [release.published_at for release in releases]
release_month_count = Counter(date.strftime('%Y-%m') for date in release_dates)

if release_month_count:
    release_months, release_counts = zip(*release_month_count.items())
    plt.plot(release_months, release_counts)
    plt.xlabel('Month')
    plt.ylabel('Number of Releases')
    plt.title('Repository Releases Evolution')
    plt.savefig('Repository Releases Evolution')
else:
    print("No releases found.")
