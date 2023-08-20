from line_notify import LineNotify
import csv
from datetime import date, timedelta
import os

ACCESS_TOKEN = os.environ["LINE_TOKEN"]
notify = LineNotify(ACCESS_TOKEN)

dates = []
today = date.today()
while not (today.weekday() == 3 and 15 <= today.day <= 21):
    dates.append(today.strftime("%Y-%m-%d"))
    today += timedelta(days=1)

message = "[Dividend Infomation in Vietnam]\n"
cum_dividend = 0
with open("/home/lawrence910426/Trading-Notifications/vietnam/VN30.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        if row[0] in dates:
            message += f"date: {row[0]}, dividend: {row[1]}\n"
            cum_dividend += float(row[1])
message = f"Total Dividend: {cum_dividend}\n" + message

print(message)
notify.send(message)
