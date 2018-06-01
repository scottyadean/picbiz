import time
from datetime import datetime, timedelta

def fix_date(strdate, split_on="/"):
  try:
    dt = str(strdate.strip())
    if dt == '':
      return False
    d = dt.split(split_on)
    if len(d) <= 2:
      return False

    #2017:08:28 11:14:16
    if len(d[0]) == 4:
      year  = d[0].strip()
      month = "{0:0>2}".format(d[1].strip())
      day   = "{0:0>2}".format(d[2].split(" ")[0])

    #04-28-18
    else:
      year  = d[2].strip()
      month = "{0:0>2}".format(d[0].strip())
      day   = "{0:0>2}".format(d[1].split(" ")[0])

    return "{}-{}-{}".format(year, month, day)

  except Exception as e:
    return False


def format_date(dt, f='%Y-%m-%d'):
  if dt.strip() == '':
    return None

  if "/" in dt:
    dt = fix_date( dt, "/" )

  if ":" in dt:
    dt = fix_date( dt, ":" )

  if dt == False:
    return None

  return datetime.strptime(dt, f).date() if dt else None



def get_date_from_ts(ts, f='%Y-%m-%d'):
  return datetime.fromtimestamp(int(ts)).strftime(f)
