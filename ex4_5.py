from JLAB import *

sw0 = DipSW(0,-120)
led_day = Led(90,0,'red')
led_night = Led(-90,0,'blue')
day = MotorSimGIF(0,0)
lim_high =  Switch(-40,80)
lim_low = Switch(-40,200)
while True:
    if sw0.read()==1:
        print("day\n\n\n")
        led_night.write(0)
        led_day.write(1)
        if lim_high.read() == 0:
            day.write(0,1)
            print("door going up\n\n\n")
        elif lim_high.read() == 1:
            day.write(0,0)
            print("lim_reach\n\n\n")

    else:
        led_day.write(0)
        led_night.write(1)
        print("night\n\n\n")
        if lim_low.read() == 0:
            day.write(1,0)
            print("door going down\n\n\n")
        elif lim_low.read()==1:
            day.write(0,0)
            print("lim_reach\n\n\n")

    
