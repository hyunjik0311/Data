import time
import serial

port = "COM5"
baud = 9600
ser = serial.Serial(
    port=port,
    baudrate=baud,
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=8
)
if ser.isOpen():
    print("드론 연결 성공", ser.name)

command01 = str.encode('gyrorest' + '\r')
ser.write(command01)
time.sleep(0.1)

if ser.readable():
    response = ser.readline()
    print(response[:len(response) - 1].decode())
    time.sleep(1)
print("드론 이륙 명령 수행 중...")
command01 = str.encode('takeoff' + '\r')
ser.write(command01)
time.sleep(0.5)
if ser.readable():
    response = ser.readline().decode()
    print("드론 응답:", response)
    time.sleep(1)
print("이륙 완료!")

command01 = str.encode('cw 150 3000' + '\r')
ser.write(command01)
time.sleep(3)
if ser.readable():
    response = ser.readline()
    print(response[:len(response) - 1].decode())
    time.sleep(1)
print("드론 자동 착륙 실행 중...")
command01 = str.encode('land' + '\r')
ser.write(command01)
time.sleep(0.1)

if ser.readable():
    response = ser.readline().decode()
    print("드론 응답:", response)
    time.sleep(1)

print("착륙 완료!")
