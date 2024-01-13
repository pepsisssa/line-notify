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

def check_for_updates(line_notify_token):
    global LAST_HREF
    try:
        res = requests.get(URL)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        elems = soup.find_all('a', attrs={'class': 'entry-card-wrap'})
        
        if elems:
            elem = elems[0]
            title = elem.get('title', '')
            href = elem.get('href', '')

            if LAST_HREF != href:
                send_line_notify(title + " " + URL + href, line_notify_token)
                logger.info(f"Notification sent: {title} {URL}{href}")
            LAST_HREF = href

    except requests.exceptions.RequestException as e:
        logger.error(f"Web scraping error: {e}")