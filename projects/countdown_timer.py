import time
n = 100620
for x in range(n, 0, -1):
    sec = x % 60
    minutes = int(x/60) %60
    hours = int(x/3600) %24
    days = int(x/86400) 
    print(f"{days:02}:{hours:02}:{minutes:02}:{sec:02}");
    time.sleep(1)

print("Time's up")
