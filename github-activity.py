import requests
import argparse

parser = argparse.ArgumentParser(description="Program to view github events")
parser.add_argument("--username", type=str, required=True, help="Github username.")
args = parser.parse_args()
url = f"https://api.github.com/users/{args.username}/events"

response = requests.get(url)
events = response.json()

if response.status_code == 200:
    for event in events[:3]:
        if event["type"] == "CommitCommentEvent":
            pass
        elif event["type"] == "CreateEvent":
            pass
        elif event["type"] == "DeleteEvent":
            pass
        elif event["type"] == "ForkEvent":
            pass
        elif event["type"] == "GollumEvent":
            pass
        elif event["type"] == "IssueCommentEvent":
            pass
        elif event["type"] == "IssuesEvent":
            pass
        elif event["type"] == "MemberEvent":
            pass
        elif event["type"] == "PublicEvent":
            pass
        elif event["type"] == "PullRequestEvent":
            pass
        elif event["type"] == "PullRequestReviewEvent":
            pass
        elif event["type"] == "PullRequestReviewCommentEvent":
            pass
        elif event["type"] == "PullRequestReviewThreadEvent":
            pass
        elif event["type"] == "PushEvent":
            pass
        elif event["type"] == "ReleaseEvent":
            pass
        elif event["type"] == "SponsershipEvent":
            pass
        elif event["type"] == "WatchEvent":
            pass
