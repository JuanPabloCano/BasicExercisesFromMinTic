import time

def countdown(time_sec):
    
"""     for i in range(time_sec, -1, -1):
        time.sleep(1)
        print(f"{i} seconds to go")
"""        
"""     while time_sec:
        mins, secs= divmod(time_sec, 60)
        timeFormat= "{:02d}:{:02d}".format(mins, secs)
        print(timeFormat, end= "\r")
        time.sleep(1)
        time_sec -= 1
    print("Stop")
"""

countdown(int(input("Ingrese el tiempo del temporizador: ")))

