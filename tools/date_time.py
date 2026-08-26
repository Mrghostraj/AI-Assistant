from datetime import datetime
from zoneinfo import ZoneInfo


# ============================================================
# TIMEZONE
# ============================================================

INDIA_TZ = ZoneInfo("Asia/Kolkata")


# ============================================================
# CURRENT TIME
# ============================================================

def get_current_time():

    now = datetime.now(INDIA_TZ)

    return now.strftime(
        "It is %I:%M %p."
    )


# ============================================================
# CURRENT DATE
# ============================================================

def get_current_date():

    now = datetime.now(INDIA_TZ)

    return now.strftime(
        "Today is %d %B %Y."
    )


# ============================================================
# CURRENT DAY
# ============================================================

def get_current_day():

    now = datetime.now(INDIA_TZ)

    return now.strftime(
        "Today is %A."
    )


# ============================================================
# DATE + DAY
# ============================================================

def get_date_and_day():

    now = datetime.now(INDIA_TZ)

    return now.strftime(
        "Today is %A, %d %B %Y."
    )


# ============================================================
# DATE + DAY + TIME
# ============================================================

def get_date_time():

    now = datetime.now(INDIA_TZ)

    return now.strftime(
        "Today is %A, %d %B %Y, and the time is %I:%M %p."
    )


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    print(get_current_time())
    print(get_current_date())
    print(get_current_day())
    print(get_date_and_day())
    print(get_date_time())