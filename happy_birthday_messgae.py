import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import date

# Slack Bot token'ınızı "SLACK_BOT_TOKEN" yerine girin.

client = WebClient(token="token")

# Doğum günü mesajının gönderileceği kanalın ID'sini "CHANNEL_ID" yerine girin.
channel_id = "C03A2N40ZDE"

user_id = "U04QHF3563A"
# Doğum günü mesajı için kullanılacak metni belirleyin.
message = "Bugün {}'in doğum günü! 🎉🎂🎁".format("ASLIHAN ŞENER ")

# Doğum günü hangi kullanıcı için gönderilecekse, o kullanıcının ID'sini "USER_ID" yerine girin.


# Doğum günü bugün mü kontrol edin.
today = date.today()
birthday = date(2022, 3, 13) # Kullanıcının doğum gününe ait tarih bilgisini girin.
if today.month == birthday.month and today.day == birthday.day:
    try:
        response = client.chat_postMessage(
            channel=channel_id,
            text=message
        )
        print("Doğum günü mesajı başarıyla gönderildi: {}".format(response["ts"]))
    except SlackApiError as e:
        print("Hata: {}".format(e))