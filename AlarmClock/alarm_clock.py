# first install "playsound" library using pip in your terminal
# Features - escape sequences or invicible characters was used. its used to manipulate things in the terminal. 
# in our case, it was used for clearing/deleting contents and then return the cursor to the home position.

from playsound import playsound
import time 

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H" #This is going to return the cursor to the home position, so that when we print again, its going to print over
#whatever was there before. 


def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

    
    while True:
        playsound("alarm.mp3") 
        stop = input("Stop: Y/N ?: ").lower()
        if stop == "Y".lower():
            quit()
        else:
            pass
        
        
print("Welcome to the Alarm Clock program. Please set your alarm!")
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)


