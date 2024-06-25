import logging
import zipfile
import os
from datetime import datetime

# 配置日誌
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def log_message(message, level='info'):
    levels = {
        'debug': logging.debug,
        'info': logging.info,
        'warning': logging.warning,
        'error': logging.error,
        'critical': logging.critical
    }
    log_func = levels.get(level, logging.info)
    log_func(message)

def compress_logs():
    with zipfile.ZipFile('logs.zip', 'w') as zipf:
        zipf.write('app.log')
    print("日誌已壓縮")

def extract_logs():
    with zipfile.ZipFile('logs.zip', 'r') as zipf:
        zipf.extractall('extracted_logs')
    print("日誌已解壓")

def display_logs():
    if os.path.exists('app.log'):
        with open('app.log', 'r') as logfile:
            for line in logfile:
                print(line.strip())
    else:
        print("日誌文件不存在")

# 記錄日誌
log_message("這是一條信息消息")
log_message("這是一條錯誤消息", level='error')

# 顯示日誌
print("當前日誌內容：")
display_logs()

# 壓縮日誌
compress_logs()

# 解壓日誌
extract_logs()
