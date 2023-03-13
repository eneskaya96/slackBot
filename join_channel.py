from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token="token")

channel_id = "C03A2N40ZDE"

try:
    response = client.conversations_join(channel=channel_id)
    print("Bot, kanala başarıyla katıldı: {}".format(response["channel"]["name"]))
except SlackApiError as e:
    print("Hata: {}".format(e))