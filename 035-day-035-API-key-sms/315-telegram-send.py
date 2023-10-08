import requests
import os

# https://stackoverflow.com/questions/75116947/how-to-send-messages-to-telegram-using-python

TOKEN = os.environ.get("TELEGRAM_TOKEN")
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
# print(requests.get(url).json()) # to get chat_id

chat_id = os.environ.get("TELEGRAM_CHAT_ID")
message = "Siri er søt"
url = (
    f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
)
print(requests.get(url).json())  # this sends the message


# yo = {
#     "ok": True,
#     "result": [
#         {
#             "update_id": 35888427,
#             "message": {
#                 "message_id": 4,
#                 "from": {
#                     "id": 5339068918,
#                     "is_bot": False,
#                     "first_name": "Kristian",
#                     "last_name": "Skreosen",
#                     "username": "Skraevern",
#                     "language_code": "nb",
#                 },
#                 "chat": {
#                     "id": 5339068918,
#                     "first_name": "Kristian",
#                     "last_name": "Skreosen",
#                     "username": "Skraevern",
#                     "type": "private",
#                 },
#                 "date": 1696792117,
#                 "text": "04980",
#                 "entities": [{"offset": 0, "length": 5, "type": "code"}],
#             },
#         }
#     ],
# }
