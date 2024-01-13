import schedule
import time
from main import check_for_updates
import logging  

LINE_NOTIFY_TOKEN = 'lhJWSltbTmeL0vHJX2vJQq9ZZzAzaEMcRzHLi4yOeKC'

# ロギングの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def job():
    check_for_updates(LINE_NOTIFY_TOKEN)

def main():
    job()  # 初回のチェック
    schedule.every(5).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

