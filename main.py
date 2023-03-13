from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token="token")

try:
    response = client.conversations_list()
    channels = response['channels']
    print(f"Found {len(channels)} channels:")
    for channel in channels:
        print(channel['name'])
except SlackApiError as e:
    print("Error : {}".format(e))
