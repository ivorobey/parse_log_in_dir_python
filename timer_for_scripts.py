
import subprocess
import time
import schedule

import parser_acceslog_in_dir
import parser_log_in_dir


def task1():
    subprocess.call("parser_acceslog_in_dir.py", shell=True)

def task2():
    subprocess.call("parser_log_in_dir.py", shell=True)


scheduler1 = schedule.Scheduler()
scheduler1.every(15).minutes.do(task1())


scheduler2 = schedule.Scheduler()
scheduler2.every().day.at("12:00").do(task2())



while True:
    # run_pending needs to be called on every scheduler
    scheduler1.run_pending()
    scheduler2.run_pending()
    time.sleep(1)

