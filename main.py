import requests
import logging
from bs4 import BeautifulSoup

# ログのフォーマットを設定
log_format = '%(levelname)s : %(asctime)s : %(message)s'
logging.basicConfig(filename='path/log.log', level=logging.INFO, format=log_format)
logging.info('START')  # ログの開始を記録

