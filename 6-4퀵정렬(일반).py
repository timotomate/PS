array = [7,5,9,0,3,1]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우엔 그냥 종료
        return
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 값 찾을 때 까지 전진. 작은 값 찾으면 그 인덱스가 left
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 값 찾을 때 까지 후진. 큰 값 찾으면 그 인덱스가 right
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        
        # 교차하면 pivot값 교체
        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        # 교차하지 않은 일반적인 경우엔 그냥 left,right값 swap
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array,0, len(array)-1)
print(array)