from datetime import datetime
import pytz

pubdate = "3 Oct 2016 17:00:10"
temp_time = datetime.strptime(pubdate, "%d %b %Y %H:%M:%S")
temp_time.replace(tzinfo=pytz.timezone("EST"))
ancient_time = datetime(1987, 10, 15)
ancient_time = ancient_time.replace(tzinfo=pytz.timezone("EST"))

def evaluate(pubdate,ancient_time):
    pubdate = pubdate.replace(tzinfo = None)
    ancient_time = ancient_time.replace(tzinfo = None)
    diffrence = ancient_time - pubdate
    days = diffrence.days
    if(days < 0):
        return False
    else if(days != 0):
        return True
    else:
        return bool(diffrence.seconds)
            





print(evaluate(temp_time,ancient_time))