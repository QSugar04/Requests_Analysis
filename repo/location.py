from data import repo
import matplotlib.pyplot as plt
from collections import Counter

# 获取仓库贡献者分布
contributors = repo.get_contributors()
# 统计每个贡献者的地理位置分布
contributor_counts = Counter(contributor.location for contributor in contributors if contributor.location)

# 获取前15个地区
top_contributor_locations = dict(contributor_counts.most_common(15))

# 绘制贡献者地理分布饼图
labels = list(top_contributor_locations.keys())
sizes = list(top_contributor_locations.values())

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Top 15 Contributor Locations')
plt.savefig('Top 15 Contributor Locations')
