import time

beg_time = time.gmtime(0)
print(beg_time)

curr_time = time.localtime()
hour = curr_time.tm_hour
mins = curr_time.tm_min
secs = curr_time.tm_sec
print(curr_time)
print(hour)
print(mins)
print(secs)

if hour >= 4 and hour <= 11:
    print("Good morning")
elif hour >= 12 and hour <= 15:
    print("Good afternoon !!")
elif hour >= 16 and hour <= 19:
    print("Good evening !!")
else:
    print("Good Night !!")
