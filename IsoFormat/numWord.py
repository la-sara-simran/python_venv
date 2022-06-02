from datetime import datetime


def numtoword(input):
    print(datetime.strptime(input, "%d-%m-%Y").strftime("%Y %B, %d"))


numtoword("20-05-2022")
