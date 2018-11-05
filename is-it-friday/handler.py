from datetime import datetime

FRIDAY_INDEX = 4

def handle(req):
    now = datetime.now()
    weekday = now.weekday()
    if weekday == FRIDAY_INDEX:
        return "yes"
    return "no"

