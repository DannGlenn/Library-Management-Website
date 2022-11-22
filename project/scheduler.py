import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import tzlocal
from project.models import Book, Log
from project import db, app

# a method which runs both on startup and at 12am, ensures the overdue logs are updated as such
def check_if_overdue():
    with app.app_context():
        arr = db.session.query(Log, Book).join(Book).filter(Log.overdue == False, Log.return_date == None)
        today = datetime.datetime.today()
        for log, book in arr:
            borrow_time = today - log.borrow_date
            # book type dictates borrow days allowed before overdue: [1, 2, 3] : [10, 5, 2] respectively
            if (borrow_time.days > 10 and book.type == 1) or (borrow_time.days > 5 and book.type == 2) or (borrow_time.days > 2 and book.type == 3):
                log.overdue = True
        db.session.commit()

#scheduling the job to run at 12am
scheduler = BackgroundScheduler(timezone=str(tzlocal.get_localzone()))
scheduler.add_job(func=check_if_overdue, trigger='cron', hour=0, minute=0)
scheduler.start()

