# - Creat a virtual env:
# python3 -m venv __virtual_name__

# - Activate
# source /path/to/bin/activate

# - Deactivate
# deactivate

# !pip install __package_name__

# To see all the packages installed in the virtual env:
# pip freeze

# To install requirements from a file:
# pip install -r __file_name__

import datetime
from pytz import timezone
# epoch_time=402471.238201
def epoch_to_iso(epoch_time):
    time = datetime.datetime.fromtimestamp(epoch_time)
    datetime_str = time.strftime("%Y-%m-%d  %H:%M:%S.%f")
    print(datetime_str)
    return time

# epoch_to_iso(402471.238201)

def timezones():
    india = epoch_to_iso(402471.238201)
    new_york= india.astimezone(timezone('America/New_York'))
    print(new_york)
    london= india.astimezone(timezone('Europe/London'))
    print(london)
    tokyo= india.astimezone(timezone('Asia/Tokyo'))
    print(tokyo)

timezones()