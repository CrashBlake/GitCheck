import requests
import json

## Load configuration from config.json

with open('config.json') as config_file:
    config = json.load(config_file)
    base_url = config['url']

## Function to fetch user events from GitHub API

def get_user_events(username):
    url = f"{base_url}{username}/events/public"
    response = requests.get(url)
    ##status_code = response.status_code
    ##print("Status Code:", status_code)
    if response.status_code == 200:
        if response.json() == []:          
            print(f"No recent events found for user {username}")
            return None
        return response.json()
    elif response.status_code == 404:
        print(f"Error fetching events for user {username}: User not found")
        return None


# def event_print(event_type, repository):
#     if event_type == "PushEvent":
#         print(f"PushEvent in repository: {repository}")
#     elif event_type == "PullRequestEvent":
#         print(f" PullRequestEvent in repository: {repository}")
#     elif event_type == "IssuesEvent":
#         print(f"IssuesEvent in repository: {repository}")
#     elif event_type == "CreateEvent":
#         print(f"CreateEvent in repository: {repository}")
#     elif event_type == "DeleteEvent":
#         print(f"DeleteEvent in repository: {repository}")
#     elif event_type == "ForkEvent":
#         print(f"ForkEvent in repository: {repository}")
#     elif event_type == "WatchEvent":
#         print(f"WatchEvent in repository: {repository}")
#     elif event_type == "IssueCommentEvent":
#         print(f"IssueCommentEvent in repository: {repository}")
#     elif event_type == "MemberEvent":
#         print(f"MemberEvent in repository: {repository}")


def event_process(username):
    data = get_user_events(username)
    if data is not None:
        for event in data:
            event_type = event['type']
            repository = event['repo']['name']
            payload = event['payload']['action'] if 'action' in event['payload'] else 'No Description'
            print(f"{event_type} in repository: {repository} - {payload}")
            # event_print(event_type, repository)