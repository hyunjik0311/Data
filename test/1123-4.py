# 저장용

for i in range(1, 10):
    command= str.encode('funled'+ '\r')
    ser.write(command)
if ser.readable():
    response = ser.readline()
    print(f"[{i}/9]FunLED 전 송 성 공 . 응답: {response[:len(response)].decode()}")
else:
    print(f"[{i}/9]FunLED전송완료.(응답 대기중...)")
time.sleep(1.0)
print('\n[LED 9단계자동변경시퀀스완료]')
time.sleep(2)