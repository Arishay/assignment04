import time 

def countdown_timer(time_in_second):
    while time_in_second > 0:
        mins,secs = divmod(time_in_second , 60)
        time_format = ' {:02d}:{:02d}'.format(mins,secs)
        print(time_format , end = '\r')
        time.sleep(1)
        time_in_second -= 1
    print('00:00 \n Time\'s Up!')


time_second = int(input("Enter time in seconds: "))
countdown_timer(time_second)