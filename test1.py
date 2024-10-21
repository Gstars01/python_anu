from JLAB_2024 import *

motorFL = MotorSimGIF(80,80)
motorFR = MotorSimGIF(-80,80)
motorBL = MotorSimGIF(80,-80)
motorBR = MotorSimGIF(-80,-80)

MF = Switch(0,20)
MB = Switch(0,-20)
ML = Switch(20,0)
MR = Switch(-20,0)
wd = Switch(0,0)

while True:
    if MF.read()==1 and wd.read()==0:  # 전진
        motorFL.write(0, 1)
        motorFR.write(1, 0)

    elif MB.read()==1 and wd.read()==0:
        # 후진
        motorFL.write(1, 0)
        motorFR.write(0, 1)

    elif MR.read()==1 and wd.read()==0:
        #우회전 
        motorFL.write(0, 0)
        motorFR.write(1, 0)
        
    elif ML.read()==1 and wd.read()==0:
        #좌회전
        motorFL.write(0, 1)  # 왼쪽 모터 켜고, 오른쪽 모터 정지
        motorFR.write(0, 0)

    elif MF.read()==1 and wd.read()==1:
        # 전진
        motorFL.write(0, 1)
        motorFR.write(1, 0)
        motorBL.write(0, 1)
        motorBR.write(1, 0)

    elif MB.read()==1 and wd.read()==1:
        # 후진
        motorFL.write(1, 0)
        motorFR.write(0, 1)
        motorBL.write(1, 0)
        motorBR.write(0, 1)

    elif MR.read()==1 and wd.read()==1:
        #우회전 
        motorFL.write(0, 0)
        motorFR.write(1, 0)
        motorBL.write(0, 1)
        motorBR.write(1, 0)
        
    elif ML.read()==1 and wd.read()==1:
        #좌회전
        motorFL.write(0, 1)  # 왼쪽 모터 켜고, 오른쪽 모터 정지
        motorFR.write(0, 0)
        motorBL.write(0, 1)
        motorBR.write(1, 0)

    else: 
            FLmotor.write(0,0)
            FRmotor.write(0,0)
            BLmotor.write(0,0)
            BRmotor.write(0,0)

