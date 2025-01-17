import datetime
import matplotlib.pyplot as plt
from data import commits,repo

# 获取贡献者列表
contributors = repo.get_contributors()

# 统计贡献者的年龄
now = datetime.datetime.now().year
ages = []
for contributor in contributors:
    if contributor.name:
        # 获取贡献者的出生日期
        birth_date = contributor.created_at.strftime("%Y")
        # 计算贡献者的年龄
        age = now - int(birth_date)
        ages.append(age)

# 绘制贡献者的年龄分布直方图
plt.hist(ages, bins=20, edgecolor='black')
plt.xlabel("Age")
plt.ylabel("Number of Contributors")
plt.title("Age Distribution of Contributors")
plt.savefig("Age Distribution of Contributors.png")

# 关闭图像，释放资源
plt.close()

print("图表已保存为 Age Distribution of Contributors.png")
