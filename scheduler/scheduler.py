from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import delete_old_chats

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(delete_old_chats, 'interval', days=1)
    scheduler.start()
