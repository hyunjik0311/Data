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


<파이썬드론코딩>
1. 상승하기
command01 =str.encode('up 150 2000'+'\r’)
2. 하강하기
command01 =str.encode('down 150 2000'+'\r’)
3. 앞으로360도회전하기
command01 =str.encode('flip f'+'\r’)
4. 뒤로360도회전하기
command01 =str.encode('flip b'+'\r’)
5. 우측으로360도회전하기
command01 = str.encode('flip r'+'\r’)
6. 좌측으로360도회전하기
Command01 = str.encode('flip l'+'\r')