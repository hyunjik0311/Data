# LEED 색 9번 변경

import time
import serial
port = "COM5"
baud = 9600
ser = serial.Serial(port=port,
baudrate=baud, parity='N', stopbits=1, bytesize=8,
timeout=8)
ser.isOpen() #시리얼포트가열려있으면True를리턴하는함수
print("드론연결성공:", ser.name)
command01 = str.encode('gyroreset'+'\r')
ser.write(command01)
time.sleep(0.1)


for i in range(1, 10):
    command = str.encode('funled' + '\r')
    ser.write(command)

    if ser.readable():
        response = ser.readline()
        print(f"[{i}/9]FunLED 전송 성공. 응답: {response.decode()}")
    else:
        print(f"[{i}/9]FunLED 전송 완료. (응답 대기중...)")

    time.sleep(1.0)

print('\n[LED 9단계 자동 변경 시퀀스 완료]')

time.sleep(2)