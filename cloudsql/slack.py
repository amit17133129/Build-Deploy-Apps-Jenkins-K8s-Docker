channel = "cp-cloudsql-automation"
token = "xoxb-463549817440-2565143445894-7z5bkfc8HNfs4iT92D3Ltap9"
message_text = "Test1"
# from slack import WebClient
from slack_sdk import WebClient
# from slack.errors import SlackApiError
from slack_sdk.errors import SlackApiError
client = WebClient(token=token)
try:
    response = client.chat_postMessage(
        channel=channel,
        text=message_text
    )
    print(response)
    print("success")
except SlackApiError as e:
    assert e.response["error"]
    print("error")