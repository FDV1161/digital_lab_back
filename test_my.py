from app.models import JournalReadings
import random
from app import app
from database import session, db
import datetime

with app.app_context():
    
    # for i in range(250):        
    #     time +=  datetime.timedelta(0,60*10)
    #     print(time)
    time = datetime.datetime.fromisoformat("2022-03-30 00:00:00")
    for i in range(250):
        # 2022-03-30 23:21:19.254230
        time +=  datetime.timedelta(0,60*10)
        
        jr = JournalReadings(
            created_at=time,
            value=random.uniform(-2, 15),
            device_func_id=3
        )
        session.add(jr)
    session.commit()

