from data import repo
from collections import defaultdict
import matplotlib.pyplot as plt
from data import commits

# 统计每周提交次数的分布
commit_weekly_counts = defaultdict(int)
for commit in commits:
    week_number = commit.commit.author.date.isocalendar()[1]
    commit_weekly_counts[week_number] += 1

weeks, counts = zip(*commit_weekly_counts.items())
plt.plot(weeks, counts)
plt.xlabel('Week')
plt.ylabel('Number of Commits')
plt.title('Weekly Commit Pattern')
plt.savefig('Weekly Commit Pattern')
