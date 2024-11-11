from JLAB import *

motorL = MotorSimGIF(-80,0)
motorR = MotorSimGIF(80,0)

s0 = Switch(-80,90)
s1 = Switch(0,90)
s2 = Switch(80,90)

def sw_read(s):
    if s.read()==1:
        return 1
    else:
        return 0


def motorW(a,b,c,d):
    motorL.write(a,b)
    motorR.write(c,d)
    time.sleep(0.1)


while True:
    if sw_read(s0)==0 and sw_read(s1)==1 and sw_read(s2)==0:
        motorW(0,1,0,1)
    elif sw_read(s0)==1 and sw_read(s1)==0 and sw_read(s2)==0:
        motorW(0,0,0,1)
    elif sw_read(s0)==0 and sw_read(s1)==0 and sw_read(s2)==1:
        motorW(0,1,0,0)
    else:
        motorW(0,0,0,0)
