import datetime
import matplotlib.pyplot as plt
from data import commits, repo

# 获取项目的贡献者列表
contributors = repo.get_contributors()

# 统计贡献者的年龄
# 获取当前年份，用于计算年龄
now = datetime.datetime.now().year
ages = []
# 遍历每个贡献者，计算其年龄并存储到 ages 列表中
for contributor in contributors:
    if contributor.name:  
        # 获取贡献者的创建时间（假设为出生日期）
        birth_date = contributor.created_at.strftime("%Y")  
        # 计算贡献者的年龄
        age = now - int(birth_date)
        ages.append(age)  

# 绘制贡献者的年龄分布直方图
plt.hist(ages, bins=20, edgecolor='black')
plt.xlabel("Age")
plt.ylabel("Number of Contributors")
plt.title("Age Distribution of Contributors")

# 保存图像为当前目录的文件
plt.savefig("Age Distribution of Contributors.png")

# 关闭图像，释放资源
plt.close()

# 输出提示信息，告知用户图表已保存
print("图表已保存为 Age Distribution of Contributors.png")
