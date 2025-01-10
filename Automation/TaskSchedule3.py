#it is taskschedular program

import datetime
import schedule
import time

def Schedule_minute():
    print("Sceduler Schedules After Minute...")
    print("Current Time Is:",datetime.datetime.now())
    
def Schedule_Hour():
    print("Sceduler Schedules After Hour...")
    print("Current Time Is:",datetime.datetime.now())   
    
def Schedule_Sunday():
    print("Sceduler Schedules After Hour...")
    print("Current Time Is:",datetime.datetime.now())     

def main():
      
    print("Automation Using Python") 
    
    schedule.every(1).minutes.do(Schedule_minute)
    schedule.every().hour.do(Schedule_Hour)
    schedule.every().sunday.do(Schedule_Sunday)
    
    while True:
        schedule.run_pending()
        time.sleep(1)  #it takes parameters in seconds
    
if __name__=="__main__":
    main()    