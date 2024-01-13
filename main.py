import requests
from bs4 import BeautifulSoup
import logging  

URL = "https://scraping-for-beginner.herokuapp.com/"
LAST_HREF = ''

# ロギングの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
