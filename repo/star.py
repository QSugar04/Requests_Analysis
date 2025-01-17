import requests
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter

# 替换为你的 GitHub 访问令牌
TOKEN = "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"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

# GraphQL 查询模板
QUERY = """
query($owner: String!, $name: String!, $after: String) {
    repository(owner: $owner, name: $name) {
        stargazers(first: 100, after: $after) {
            edges {
                starredAt
            }
            pageInfo {
                endCursor
                hasNextPage
            }
        }
    }
}
"""

def fetch_stars(owner, repo_name):
    """
    获取指定 GitHub 仓库的 stargazers 数据。
    """
    url = "https://api.github.com/graphql"
    variables = {"owner": owner, "name": repo_name, "after": None}
    stars = []

    while True:
        response = requests.post(url, json={"query": QUERY, "variables": variables}, headers=HEADERS)
        data = response.json()

        if "errors" in data:
            raise Exception(f"GraphQL Error: {data['errors']}")

        stargazers = data["data"]["repository"]["stargazers"]
        stars.extend([edge["starredAt"] for edge in stargazers["edges"]])
        
        if not stargazers["pageInfo"]["hasNextPage"]:
            break

        variables["after"] = stargazers["pageInfo"]["endCursor"]

    return stars

def process_trend(stars):
    """
    处理 Star 时间数据，生成按日期的趋势。
    """
    # 转换为日期格式
    dates = [datetime.strptime(star, "%Y-%m-%dT%H:%M:%SZ").date() for star in stars]
    
    # 按日期统计
    date_counts = Counter(dates)
    sorted_dates = sorted(date_counts.items())  # 按日期排序
    dates, counts = zip(*sorted_dates)
    
    return dates, counts

def plot_trend(dates, counts, owner, repo_name):
    """
    绘制 Star 趋势图。
    """
    plt.figure(figsize=(12, 6))
    plt.plot(dates, counts, marker="o", linestyle="-", color="b")
    plt.title(f"Star Trend for {owner}/{repo_name}", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Number of Stars", fontsize=12)
    plt.grid(True)
    plt.tight_layout()

    # 保存图像为文件
    filename = f"Star_Trend_{owner}_{repo_name}.png"
    plt.savefig(filename, format="png", dpi=300)
    print(f"Saved trend plot to {filename}")

if __name__ == "__main__":
    # 替换为目标仓库的所有者和名称
    owner = "psf"
    repo_name = "requests"

    # 获取 Star 数据
    print("Fetching star data...")
    stars = fetch_stars(owner, repo_name)

    # 处理 Star 趋势
    print("Processing trend data...")
    dates, counts = process_trend(stars)

    # 绘制趋势图
    print("Plotting trend...")
    plot_trend(dates, counts, owner, repo_name)
