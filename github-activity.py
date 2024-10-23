import requests
import argparse

parser = argparse.ArgumentParser(description="Program to view github events")
parser.add_argument("--username", type=str, required=True, help="Github username.")
args = parser.parse_args()
url = f"https://api.github.com/users/{args.username}/events"

response = requests.get(url)
events = response.json()

if response.status_code == 200:
    for event in events:
        event_type = event["type"]
        payload = event["payload"]

        if event_type == "CommitCommentEvent":
            print(f"{payload["action"].title()} comment: {payload["comment"]}")
        elif event_type == "CreateEvent":
            if payload["ref_type"] == "repository":
                create_event_message = (
                    f"Created repository called {event["repo"]["name"]}"
                )
            elif payload["ref_type"] == "branch":
                create_event_message = (
                    f"Created branch called {payload["master_branch"]}"
                )
            else:
                create_event_message = f"Created tag in {event["repo"]["name"]}"
            print(create_event_message)
        elif event_type == "DeleteEvent":
            print(f"Deleted {payload["ref_type"]} from {event["repo"]["name"]}")
        elif event_type == "ForkEvent":
            print(f"Forked: {payload["forkee"]["full_name"]}")
        elif event_type == "GollumEvent":
            print(f"{payload["pages"]} updated")
        elif event_type == "IssueCommentEvent":
            if payload["action"] == "created":
                print(f"Created comment at: {payload["comment"]["url"]}")
            elif payload["action"] == "edited":
                print(f"Edited comment at: {payload["comment"]["url"]}")
            else:
                print(f"Deleted comment at: {payload["comment"]["url"]}")
        elif event_type == "IssuesEvent":
            if payload["action"] == "opened":
                print("Opened issue")
            if payload["action"] == "edited":
                print("Edited issue")
            if payload["action"] == "closed":
                print("Closed issue")
            if payload["action"] == "reopened":
                print("Reopened issue")
            if payload["action"] == "assigned":
                print("Assigned issue")
            if payload["action"] == "unassigned":
                print("Unassigned issue")
            if payload["action"] == "labeled":
                print("Labeled issue")
            if payload["action"] == "unlabeled":
                print("Unlabeled issue")
        elif event_type == "MemberEvent":
            if payload["action"] == "added":
                print(
                    f"{payload["action"].title()} {payload["member"]} to {event["repo"]["name"]}"
                )
            else:
                print(f"Edited collaborator permissions")
        elif event_type == "PublicEvent":
            print(f"Made {event["repo"]["name"]} public")
        elif event_type == "PullRequestEvent":
            if payload["action"] == "opened":
                print("Opened a pull request")
            if payload["action"] == "edited":
                print("Edited a pull request")
            if payload["action"] == "closed":
                print("Closed a pull request")
            if payload["action"] == "reopened":
                print("Reopened a pull request")
            if payload["action"] == "assigned":
                print("Assigned a pull request")
            if payload["action"] == "unassigned":
                print("Unassigned a pull request")
            if payload["action"] == "review_requested":
                print("Requested a review for a pull request")
            if payload["action"] == "review_request_removed":
                print("Removed a review request from a pull request")
            if payload["action"] == "labeled":
                print("Labeled a pull request")
            if payload["action"] == "unlabeled":
                print("Unlabeled a pull request")
            if payload["action"] == "synchronize":
                print("Synchronized a pull request")
        elif event_type == "PullRequestReviewEvent":
            print(f"Created a pull request review at {event["pull_request_url"]}")
        elif event_type == "PullRequestReviewCommentEvent":
            print("Commented on a pull request review")
        elif event_type == "PullRequestReviewThreadEvent":
            if payload["action"] == "resolved":
                print("Resolved a comment thread on a pull request")
            else:
                print(
                    "Marked a resolved comment thread on a pull request as unresolved"
                )
        elif event_type == "PushEvent":
            print(f'"{payload["commits"][0]["message"]}" in {event["repo"]["name"]}')
        elif event_type == "ReleaseEvent":
            if payload["action"] == "published":
                print(f"Published new release at: {payload["release"]["url"]}")
            else:
                print(f"Edited release at: {payload["release"]["url"]}")
        elif event_type == "SponsershipEvent":
            if payload["action"] == "created":
                print("Created sponsership listing")
            else:
                print("Edited sponsership listing")
        elif event_type == "WatchEvent":
            print(f"starred a repository")
        else:
            print("They don't have any activity!")
else:
    print(
        "Either that isn't a valid username or Github is acting up. Please try again!"
    )
