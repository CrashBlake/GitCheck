import requests
import json

with open('config.json') as config_file:
    config = json.load(config_file)
    base_url = config['url']
    github_token = config['github_token']


def get_user_events(username):
    url = f"{base_url}{username}/events"
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
        print(f"Number of commits in the last 24 hours: {count_events(get_user_events(repository), 'PushEvent')}")
    elif event_type == "PullRequestEvent":
        print(f"Number of pull requests in the last 24 hours: {count_events(get_user_events(repository), 'PullRequestEvent')}")
    elif event_type == "IssuesEvent":
        print(f"Number of issues in the last 24 hours: {count_events(get_user_events(repository), 'IssuesEvent')}")

def event_print(username):
    data = get_user_events(username)
    if data is not None:
        for event in data:
            event_type = event['type']
            repository = event['repo']['name']
            event_print(event_type, repository)