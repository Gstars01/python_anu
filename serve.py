from JLAB import *

# 모터 초기화
motorL = MotorSimGIF(-80, 0)
motorR = MotorSimGIF(80, 0)

#스위치 선언부 

# 정지 스위치
choose_switch1 = Switch(30, 100)  # 경로 선택 스위치
choose_switch2 = Switch(-30, 100)  # 경로 선택 스위치

# 전진 함수
def forward(steps):
    print(f"전진 {steps}번 실행 중...")
    for _ in range(steps):
        motorL.write(0, 1)
        motorR.write(1, 0)

# 우회전 함수
def turn_right(steps):
    print(f"우회전 {steps}번 실행 중...")
    for _ in range(steps):
        motorL.write(0, 1)
        motorR.write(0, 0)

# 좌회전 함수
def turn_left(steps):
    print(f"좌회전 {steps}번 실행 중...")
    for _ in range(steps):
        motorL.write(0, 0)
        motorR.write(1, 0)



# 모든 LED 켜기

while True:
    if choose_switch1.read()== 1:
        # 순방향 동작
        print("====================순방향 동작 시작==================")
        forward(24)     # 전진 24번
        turn_right(8)   # 우회전 8번
        forward(16)     # 전진 16번
        turn_left(8)    # 좌회전 8번
        forward(32)     # 전진 32번

        #180도 회전
        time.sleep(5)
        print("======================180도 회전=======================")
        turn_left(16)
        

        # 역방향 동작
        print("======================역방향 동작 시작==================")
        forward(32)     # 전진 32번 (반대 방향)
        turn_right(8)   # 우회전 8번 (반대 방향에서 좌회전 효과)
        forward(16)     # 전진 16번
        turn_left(8)    # 좌회전 8번 (반대 방향에서 우회전 효과)
        forward(24)     # 전진 24번
        print("모든 동작 완료")

        

    elif choose_switch2.read()== 1:
        # 순방향 동작
        print("====================순방향 동작 시작==================")
        forward(24)     # 전진 24번
        turn_left(8)    # 좌회전 8번
        forward(16)     # 전진 16번
        turn_right(8)   # 우회전 8번
        forward(24)     # 전진 24번

        #180도 회전
        time.sleep(5)
        print("======================180도 회전=======================")
        turn_left(16)


        # 역방향 동작
        print("======================역방향 동작 시작==================")
        forward(24)     # 전진 24번 (반대 방향)
        turn_left(8)    # 좌회전 8번 (반대 방향에서 우회전 효과)
        forward(16)     # 전진 16번
        turn_right(8)   # 우회전 8번 (반대 방향에서 좌회전 효과)
        forward(24)     # 전진 24번
        print("모든 동작 완료")


    else:
        motorL.write(0, 0)
        motorR.write(0, 0)

        

