import logging
import os
from datetime import datetime

# 設定 LOG 檔案名稱
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, "app.log")

# 設定 Logger
logging.basicConfig(
    level=logging.INFO,  # 設定最低 LOG 等級
    format="%(asctime)s [%(levelname)s] %(message)s",  # 記錄格式
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),  # 輸出到檔案
        logging.StreamHandler()  # 輸出到終端機
    ]
)

# 簡單的 LOG 寫入函式
def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

def log_error(message):
    logging.error(message)

if __name__ == "__main__":
    log_info("這是一條 INFO 訊息")
    log_warning("這是一條 WARNING 訊息")
    log_error("這是一條 ERROR 訊息")
    print("Log 記錄完成，請查看 logs/app.log")
