# Hello

name = input('Enter your name : ')
print(f'Hi {name}~')

# Print

import time

start = time.time()
for i in range(1, 6):
    print(i)
end = time.time()
print(end - start)

# BigO

n = int(input("정수 입력 : "))
total = n * (n + 1) // 2
print(f"1부터 {n}까지 누산 합계는 {total}입니다.")
# f(n) = 1 + 2
# O(1) 상수시간

# Counts

n = int(input("정수 입력 : "))
count = 0
for i in range(1, n+1):
    print(i)
    count += i  # count = count + i
    # print(count)
print(f"1부터 {n}까지 누산 합계는 {count}입니다.")

# List_DS

# artists = []
artists = list()
print(artists)
artists.append("리센느")
print(artists)
artists.append("핑클")
artists.append("데이식스")
print(artists)
print(artists.pop(1))
print(artists)

# Space

x = 1
n = int(input("Input factorial number : "))
a_list = list()
for i in range(1,n+1):
    a_list.append(x)
    x = x * i
print(f"{n}! = {x}")
print(a_list)
# O(n) Space complexity

# List_Array

import array

a = array.array('f',(1.0, 1.5, 2.0, 2.5))
print(a)
print(a[1])
# a[1] = "1"  # TypeError: must be real number, not str
a[1] = -9.12
print(a)  # array('f', [1.0, -9.119999885559082, 2.0, 2.5]), IEEE754 부동소수점

# List_DS

# scores = [[99, 100, 98],[100, 91, 100],[89, 92, 87]]
scores = [
    [99, 100, 98],
    [100, 91, 100],
    [89, 92, 87]
]
print(scores)
print(scores[1][2])

# Linked_List

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        """
        연결 리스트 초기화 함수
        """
        self.head = None


    def append(self, data):
        """
        노드 추가 함수
        :param data: 노드 데이터 값
        :return: None
        """
        if not self.head:  # 최초 노드 연결용. 단 1회 실행
            self.head = Node(data)
            return
        current = self.head  # 첫 번째 노드의 위치를 받은 지역변수 current
        while current.next:  # 가르키는 다음 노드가 존재하면 반복.
            current = current.next  # current를 다음 노드로 이동
        current.next = Node(data)  # while문 종료(마지막 노드를 찾음) 후 새 노드 생성. 그리고 새 노드를 마지막 노드에 연결.


    def __str__(self):  # 매직메서드로 print 함수등에 출력할 내용을 정리
        n = self.head
        while n is not None:
            print(n.data)
            n = n.next  # 다음 노드로 이동
        return '[끝]'


pokemons = LinkedList()
pokemons.append('꼬부기')  # head
pokemons.append('피카츄')
pokemons.append('파이리')
pokemons.append('뮤')
print(pokemons)  # <__main__.LinkedList object at 0x000002BDD72C7230>