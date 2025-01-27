from github import Github
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# GitHub 访问令牌
GITHUB_TOKEN = "your_github_token"
REPO_NAME = "psf/requests"

# 初始化 GitHub 客户端
g = Github(GITHUB_TOKEN)


# 分析提交历史
def fetch_commit_history(repo_name):
    repo = g.get_repo(repo_name)
    commits = repo.get_commits()
    commit_data = []

    for commit in commits:
        commit_data.append({
            "sha": commit.sha,
            "author": commit.author.login if commit.author else "Unknown",
            "date": commit.commit.author.date,
            "message": commit.commit.message,
        })

    return pd.DataFrame(commit_data)


# 分析提交特性
def analyze_submit_characteristics(df):
    df["date"] = pd.to_datetime(df["date"])
    df["day_of_week"] = df["date"].dt.day_name()
    df["hour"] = df["date"].dt.hour
    return df


# 仓库演化数据
def fetch_repo_evolution(repo_name):
    repo = g.get_repo(repo_name)
    return {
        "stars": repo.stargazers_count,
        "forks": repo.forks_count,
        "issues": repo.open_issues_count,
        "created_at": repo.created_at,
        "updated_at": repo.updated_at,
    }


# 可视化提交历史
def visualize_submit_history(df):
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)
    df.resample("M").size().plot(kind="line", figsize=(10, 6), title="Submit History (Commits per Month)")
    plt.xlabel("Date")
    plt.ylabel("Number of Commits")
    plt.show()


# 可视化提交特性
def visualize_submit_characteristics(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x="day_of_week",
                  order=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    plt.title("Commits by Day of the Week")
    plt.xlabel("Day of Week")
    plt.ylabel("Number of Commits")
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.histplot(df["hour"], bins=24, kde=True)
    plt.title("Commits by Hour of Day")
    plt.xlabel("Hour")
    plt.ylabel("Frequency")
    plt.show()


# 可视化仓库演化
def visualize_repo_evolution(evolution_data):
    labels = ["Stars", "Forks", "Issues"]
    values = [evolution_data["stars"], evolution_data["forks"], evolution_data["issues"]]

    plt.figure(figsize=(8, 6))
    sns.barplot(x=labels, y=values)
    plt.title("Repository Evolution")
    plt.xlabel("Metrics")
    plt.ylabel("Count")
    plt.show()


# 主函数
def main():
    # 提交历史
    print("Fetching commit history...")
    commit_df = fetch_commit_history(REPO_NAME)

    # 提交特性分析
    print("Analyzing submit characteristics...")
    commit_df = analyze_submit_characteristics(commit_df)

    # 仓库演化数据
    print("Fetching repository evolution data...")
    repo_evolution = fetch_repo_evolution(REPO_NAME)

    # 可视化
    print("Visualizing submit history...")
    visualize_submit_history(commit_df)

    print("Visualizing submit characteristics...")
    visualize_submit_characteristics(commit_df)

    print("Visualizing repository evolution...")
    visualize_repo_evolution(repo_evolution)


if __name__ == "__main__":
    main()