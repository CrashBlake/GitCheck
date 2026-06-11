### This module contains the core logic for fetching and processing user events from the GitHub API. It defines functions to retrieve user events and process them to display relevant information about the user's recent activity on GitHub. The module also handles configuration loading from a JSON file to ensure that the API endpoint can be easily updated if needed.

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

## Function to process and print user events
def event_process(username):
    data = get_user_events(username)
    if data is not None:
        for event in data:
            event_type = event['type']
            repository = event['repo']['name']
            payload = event['payload']['action'] if 'action' in event['payload'] else 'No Description'
            print(f"{event_type} in repository: {repository} - {payload}")