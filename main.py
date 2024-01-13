import requests
from bs4 import BeautifulSoup
import logging  

URL = "https://scraping-for-beginner.herokuapp.com/"
LAST_HREF = ''

# ロギングの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_line_notify(notification_message, line_notify_token):
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'{notification_message}'}
    requests.post(line_notify_api, headers=headers, data=data)