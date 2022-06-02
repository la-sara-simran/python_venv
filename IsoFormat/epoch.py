# import time
#  from datetime import datetime
import datetime
# from pytz import timezone
# epoch_time=402471.238201


def epoch_to_iso(epoch_time):


    time = datetime.datetime.fromtimestamp(epoch_time)
    datetime_str = time.strftime("%Y-%m-%d  %H:%M:%S.%f")
    print(datetime_str)


epoch_to_iso(402471.238201)
# helloWorld - camel case
# hello_world -  snake case
# HelloWorld - sentence case
# hello-world - kebab case
