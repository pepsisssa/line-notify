import requests
import logging
from bs4 import BeautifulSoup

# ログのフォーマットを設定
log_format = '%(levelname)s : %(asctime)s : %(message)s'

# ロギング設定を行う関数を作成
def configure_logging(log_file_path, log_level=logging.INFO):
    # ルートロガーを取得
    logger = logging.getLogger()

    # ログのフォーマットを設定
    formatter = logging.Formatter(log_format)

    # コンソールハンドラを作成して設定
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # ファイルハンドラを作成して設定
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # ログレベルを設定
    logger.setLevel(log_level)

# ロギングの設定を行う関数を呼び出し
configure_logging('path/log.log')
logging.info('START')