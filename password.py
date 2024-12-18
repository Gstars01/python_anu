from JLAB import *
import time

from JLAB_2024 import *

s0 = Sensor(0, 0)
s1 = Sensor(0, 80)
s2 = Sensor(0, 160)
s3 = Sensor(80, 0)
s4 = Sensor(80, 80)
s5 = Sensor(80, 160)
s6 = Sensor(160, 0)
s7 = Sensor(160, 80)
s8 = Sensor(160, 160)

reset_sw = DipSW(0, -50)

motor = MotorSimGIF(-100, 0)

state = 0
# pass word 2, 4, 8, 0
pw = [0, 0, 0, 0, 0 ]
ans = [1,4,8,0,2]

def move_motor(count):
    for j in range(count):
        motor.write(1,0)

while True:
    if s0.read()==1:
        
        pw[state]=0
        state+=1

    else:
        motor.write(0,0)

    if s1.read()==1:

        pw[state]=1
        state+=1

    else:
        motor.write(0,0)
    
    if s2.read()==1:
        
        pw[state]=2
        state+=1

    else:
        motor.write(0,0)
        
    if s3.read()==1:
        pw[state]=3
        state+=1

    else:
        motor.write(0,0)
        
    if s4.read()==1:
        pw[state]=4
        state+=1

    else:
        motor.write(0,0)
        
    if s5.read()==1:
        pw[state]=5
        state+=1

    else:
        motor.write(0,0)
        
    if s6.read()==1:
        pw[state]=6
        state+=1

    else:
        motor.write(0,0)
        
    if s7.read()==1:
        pw[state]=7
        state+=1

    else:
        motor.write(0,0)
        
    if s8.read()==1:
        pw[state]=8
        state+=1
    
    else:
        motor.write(0,0)
    
    if reset_sw.read()==1:
        count = 1
        for i in pw:
            if pw[0] == ans[0]:
                count = count + 1
                if count == 4:
                    print("correct password")
                    move_motor(10)
                    for i in range(4):
                        pw[i] = 0
                    state = 0
                    count = 0
            else:
                print("wrong password")
                for i in range(1):
                    pw[i] = 0
                state = 0
                motor.write(0,0)
                count = 0
                break

    else:
        motor.write(0,0)
        print(state)
        time.sleep(0.5)

            
