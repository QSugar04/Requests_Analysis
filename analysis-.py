from github import Github
import requests

GITHUB_TOKEN = "your_github_token"
REPO_NAME = "psf/requests"

g = Github(GITHUB_TOKEN)


def analyze_repo(repo_name):
    try:
        repo = g.get_repo(repo_name)

        repo_info = {
            "Name": repo.name,
            "Description": repo.description,
            "Stars": repo.stargazers_count,
            "Forks": repo.forks_count,
            "Open Issues": repo.open_issues_count,
            "Watchers": repo.subscribers_count,
            "Created At": repo.created_at,
            "Last Pushed At": repo.pushed_at,
            "License": repo.license.name if repo.license else "No license",
        }

        print("Repository Analysis:")
        for key, value in repo_info.items():
            print(f"{key}: {value}")

        print("\nRecent Issues (last 10):")
        issues = repo.get_issues(state="open")[:10]
        for issue in issues:
            print(f"- #{issue.number} {issue.title} (Created at: {issue.created_at})")

    except Exception as e:
        print(f"Error analyzing repository: {e}")


analyze_repo(REPO_NAME)