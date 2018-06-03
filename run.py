from main.config.conf import *
from main.monitoring.base import *
import schedule


monitoring = Monitoring(urls)
monitor = monitoring.job

schedule.every(every_min).minutes.do(monitor)

if __name__ == "__main__":
    monitor()
    print("=====MONITORING STARTED=====")
    while True:
        schedule.run_pending()
        time.sleep(every_min)