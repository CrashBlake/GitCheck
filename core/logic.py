import requests
import json

with open('config.json') as config_file:
    config = json.load(config_file)
    base_url = config['url']
    github_token = config['github_token']


def get_user_events(username):
    url = f"{base_url}{username}/events/public"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching events for user {username}: {response.status_code}")
        return None

def count_events(event_data, event_type):
    count = 0
    for event in event_data:
        if event['type'] == event_type:
            count += 1
    return count

def event_print(event_type, repository):
    if event_type == "PushEvent":
        print(f"PushEvent in repository: {repository}")
    elif event_type == "PullRequestEvent":
        print(f" PullRequestEvent in repository: {repository}")
    elif event_type == "IssuesEvent":
        print(f"IssuesEvent in repository: {repository}")
    elif event_type == "CreateEvent":
        print(f"CreateEvent in repository: {repository}")
    elif event_type == "DeleteEvent":
        print(f"DeleteEvent in repository: {repository}")
    elif event_type == "ForkEvent":
        print(f"ForkEvent in repository: {repository}")
    elif event_type == "WatchEvent":
        print(f"WatchEvent in repository: {repository}")
    elif event_type == "IssueCommentEvent":
        print(f"IssueCommentEvent in repository: {repository}")

def event_process(username):
    data = get_user_events(username)
    if data is not None:
        for event in data:
            event_type = event['type']
            repository = event['repo']['name']
            payload = event['payload']['action'] if 'action' in event['payload'] else 'No Description'
            event_print(event_type, repository, payload)