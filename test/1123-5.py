# 앞뒤 이동

import time
import serial
port = "COM5"
baud = 9600
ser = serial.Serial(port=port,
baudrate=baud, parity='N', stopbits=1, bytesize=8,
timeout=8)
ser.isOpen() #시리얼포트가열려있으면True를리턴하는함수
print("드론연결성공:", ser.name)
command01 = str.encode('gyrorest'+'\r')
ser.write(command01)
time.sleep(0.1)
if ser.readable():
    response = ser.readline()
    print(response[:len(response) - 1].decode())
    time.sleep(1)
print("드론이륙명령수행중...")
command01 = str.encode('takeoff'+'\r') #encode()는 문자열을바이트코드로변환
ser.write(command01) #실제드론에게명령을전송하는부분
time.sleep(0.5)
if ser.readable():
    response = ser.readline().decode()
    print("드론응답:", response)
    time.sleep(1)
print("이륙완료!")
time.sleep(5) #호버링
command01 = str.encode('forward 150 2000'+'\r')
ser.write(command01)
time.sleep(2)
if ser.readable():
    response = ser.readline()
    print(response[:len(response) - 1].decode())
    time.sleep(1)
command01 = str.encode('back 150 2000'+'\r')
ser.write(command01)
time.sleep(2)
if ser.readable():
    response = ser.readline()
    print(response[:len(response) - 1].decode())
    time.sleep(1)
print("드론 자동착륙실행중...")
command01 = str.encode('land'+'\r')
ser.write(command01)
time.sleep(0.1)
if ser.readable():
    response = ser.readline().decode()
    print("드론 응답:", response)
    time.sleep(1)
print("착륙 완료!")