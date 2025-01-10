import datetime
import schedule
import time

def Schedule_minute():
    print("Sceduler Schedules After Minute...")
    print("Current Time Is:",datetime.datetime.now())

    
def main():
      
    print("Automation Using Python") 
    
    schedule.every(1).minutes.do(Schedule_minute)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__=="__main__":
    main()    