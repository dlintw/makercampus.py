import os
from datetime import datetime

LOG_FILE = 'log.txt'

def write_log(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a') as logfile:
        logfile.write(f"{timestamp} - {message}\n")

def read_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as logfile:
            logs = logfile.readlines()
            for log in logs:
                print(log.strip())
    else:
        print("No log file found.")

def clear_logs():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        print("Logs cleared.")
    else:
        print("No log file to clear.")

# 記錄日誌
write_log("This is the first log message.")
write_log("This is the second log message.")

# 讀取並顯示日誌
print("Current Logs:")
read_logs()

# 清除日誌
clear_logs()