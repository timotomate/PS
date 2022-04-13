array = [7,5,9,0,3,1]

for i in range(1, len(array)): # 2 번째 원소부터
    for j in range(i, 0, -1):# 1i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else: # 자기보다 작은 데이터 만나면 그 위치에서 멈춤
            break
    print(array)

print("The result is = ", array)