import sys

time = input().strip()
hour = time.split(":")[0]
if "PM" in time:
    hour = int(hour)
    if hour != 12: hour += 12
    time = time.replace("PM","")
    time = str(hour)+":"+":".join(time.split(":")[1:])
elif "AM" in time:
    hour = int(hour)
    if hour == 12:
        hour = "00"
        time = str(hour)+":"+":".join(time.split(":")[1:])
    time = time.replace("AM","")
print(time)
