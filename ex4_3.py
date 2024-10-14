from JLAB import * 

motor = MotorSimGIF(0,0)
sw3 = DipSW(60,-120)
sw2 = DipSW(-60,-120)
sw4 = DipSW(120,-120)
sw1 = DipSW(-120,-120)


while True:
    if sw1.read()==1:
        motor.write(0,0)        
    elif sw2.read()==1:
        motor.write(0,1)
        time.sleep(0.01)
    elif sw3.read()==1:
        motor.write(0,1)
        time.sleep(0.1)
    elif sw4.read()==1:
        motor.write(0,1)
        time.sleep(0.3)
    else:
        motor.write(0,0)
    time.sleep(0.1)
