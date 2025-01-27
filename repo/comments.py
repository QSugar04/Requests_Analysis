from data import repo
import matplotlib.pyplot as plt
from collections import Counter

# 获取仓库的所有评论
comments = repo.get_comments()

# 统计评论的作者
comment_authors = Counter(comment.user.login for comment in comments)

# 绘制评论数量最多的前N位作者
top_n = 15  # 选择你希望的前N位作者数量
top_comment_authors = dict(comment_authors.most_common(top_n))
other_comment_authors = dict(comment_authors - Counter(top_comment_authors))

comment_labels = list(top_comment_authors.keys()) + ['Other']
comment_sizes = list(top_comment_authors.values()) + [sum(other_comment_authors.values())]

# 使用matplotlib的pie函数绘制饼图
plt.pie(comment_sizes, labels=comment_labels, autopct='%1.1f%%', startangle=140)

# 设置饼图为正圆形
plt.axis('equal')

# 设置饼图的标题
plt.title(f'Top {top_n} Comment Authors and Others')

# 保存饼图为图片文件，文件名中包含了前N位作者的数量信息
plt.savefig(f'Top {top_n} Comment Authors and Others')
