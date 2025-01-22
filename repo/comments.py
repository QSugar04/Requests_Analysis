from data import repo
import matplotlib.pyplot as plt
from collections import Counter

# 获取仓库的所有评论
comments = repo.get_comments()

# 统计评论的作者
comment_authors = Counter(comment.user.login for comment in comments)


