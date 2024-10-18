from JLAB import *

# 모터 초기화
motorL = MotorSimGIF(-80, 0)
motorR = MotorSimGIF(80, 0)


# LED 선언부 

# 왼쪽 LED 2개
ledL1 = Led(-80, 120, "yellow")  # 왼쪽 첫 번째 LED
ledL2 = Led(-40, 120, "yellow")     # 왼쪽 두 번째 LED

# 중앙 LED 1개
ledC = Led(0, 120, "yellow")      # 중앙 LED

# 오른쪽 LED 2개
ledR1 = Led(40, 120, "yellow")   # 오른쪽 첫 번째 LED
ledR2 = Led(80, 120, "yellow")      # 오른쪽 두 번째 LED

ledB1 = Led(80,-120,"red")
ledB2 = Led(-80,-120,"red")

#스위치 선언부 

# 좌우 스위치
left_switch = Switch(-80, 90)  # 왼쪽 스위치
right_switch = Switch(80, 90)  # 오른쪽 스위치

# 전진/후진 스위치
forward_switch = Switch(0, 100)   # 전진 스위치
backward_switch = Switch(0, -100)  # 후진 스위치

# 정지 스위치
stop_switch = Switch(0, 0)  # 정지 스위치



# 모든 LED 켜기
ledL1.write(1)  # 왼쪽 첫 번째 LED 켜기
ledL2.write(1)  # 왼쪽 두 번째 LED 켜기
ledC.write(1)   # 중앙 LED 켜기
ledR1.write(1)  # 오른쪽 첫 번째 LED 켜기
ledR2.write(1)  # 오른쪽 두 번째 LED 켜기

# 모든 LED 끄기
ledL1.write(0)  # 왼쪽 첫 번째 LED 끄기
ledL2.write(0)  # 왼쪽 두 번째 LED 끄기
ledC.write(0)   # 중앙 LED 끄기
ledR1.write(0)  # 오른쪽 첫 번째 LED 끄기
ledR2.write(0)  # 오른쪽 두 번째 LED 끄기

ledB1.write(1)
ledB2.write(1)

ledB1.write(0)
ledB2.write(0)
i=1
while True:
    ledL1.write(0)  # 왼쪽 첫 번째 LED 끄기
    ledL2.write(0)  # 왼쪽 두 번째 LED 끄기
    ledC.write(0)   # 중앙 LED 끄기
    ledR1.write(0)  # 오른쪽 첫 번째 LED 끄기
    ledR2.write(0)  # 오른쪽 두 번째 LED 끄기   

    if left_switch.read() == 1:
        ledB1.write(0)
        ledB2.write(0)

        # 왼쪽으로 회전

        motorL.write(0, 0)
        motorR.write(1, 0)

        if i==1:
            ledC.write(1)  # 중앙 LED 켜기
            time.sleep(0.1)
            i=i+1

        elif i==2:
            ledL2.write(1)  # 왼쪽 두 번째 LED 켜기
            time.sleep(0.1)
            i=i+1

        elif i==3:
            ledL1.write(1)  # 왼쪽 첫 번째 LED 켜기 
            time.sleep(0.1)
            i=1



    elif right_switch.read() == 1:
        ledB1.write(0)
        ledB2.write(0)


        # 오른쪽으로 회전

        motorL.write(0, 1)  # 왼쪽 모터 켜고, 오른쪽 모터 정지
        motorR.write(0, 0)

        if i==1:
            ledC.write(1)  # 중앙 LED 켜기
            time.sleep(0.1)
            i=i+1

        elif i==2:
            ledR1.write(1)  # 오른쪽 두 번째 LED 켜기
            time.sleep(0.1)
            i=i+1

        elif i==3:
            ledR2.write(1)  # 오른쪽 첫 번째 LED 켜기 
            time.sleep(0.1)
            i=1


    elif forward_switch.read() == 1:
        ledB1.write(0)
        ledB2.write(0)

        # 전진
        motorL.write(0, 1)
        motorR.write(1, 0)


    elif backward_switch.read() == 1:
        ledB1.write(0)
        ledB2.write(0)

        # 후진
        motorL.write(1, 0)
        motorR.write(0, 1)


    elif stop_switch.read() == 1:
        # 정지
        motorL.write(0, 0)
        motorR.write(0, 0)

        ledB1.write(1)
        ledB2.write(1)


    else:
        # 기본적으로 정지 상태
        motorL.write(0, 0)
        motorR.write(0, 0)
