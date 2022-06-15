array = [7,5,9,0,3,1]

for i in range(len(array)):
    min_index = i #가장 작은 값의 인덱스 번호(위치)
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# N번만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 함
# 빅오 표기법은 O(N^2)
