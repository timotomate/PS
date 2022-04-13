array = [7,5,9,0,3,1]


def selectionsort(array):
    for i in range(len(array)):
        min_index = i
        # 아직 비정렬상태인 array[j:] 전체 순회 필요
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        
    return array


def insertionsort(array):
    for i in range(len(array)):
        start = array[i]
        # 선택정렬과 다르게 비징렬상태인 array[j:] 전체 순회 필요 없음
        # 비정렬상태 array의 첫번째 값 array[j]만 이용. array[j]랑 이미 정렬된 array[:j]를 순회하며 비교
        for j in range(i,0,-1):
            if start > array[j]:
                start, array[j] = array[j], start
            # 이미 정렬된 상태인 array의 최댓값이 array[j]보다 작으면 순회 필요 없음 끝.
            # 이 부분 때문에 array가 대부분 정렬되어 있는 상태라면 selectionsort보다 유리
            else:
                break
    
    return array



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
    

print(selectionsort(array))
print(insertionsort(array))
quick_sort(array, 0, len(array)-1)
print(array)