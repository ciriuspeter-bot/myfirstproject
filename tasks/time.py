import time

while True:
    nowt = time.localtime()
    hour = nowt.tm_hour
    minutes = nowt.tm_min
    second = nowt.tm_sec
    print(f"{hour}:{minutes}:{second}")
    time.sleep(1)