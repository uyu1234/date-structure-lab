# 프로젝트 문제 1번
input = [10, 40, 30, 60, 30]

def problem1(input):
    
    # 평균값
    mean = sum(input)/len(input) 
    #sum()함수로 리스트 내의 모든 값을 더한 후 해당 값을 리스트의 길이로 나누었다.
    
    #중앙값
    median_list=sorted(input) 
    #sorted()함수를 사용하여 input리스트의 값을 크기순으로 정렬함
    middle_index=len(median_list)//2
    median = median_list[middle_index]


    result = [mean,median]
    
    return result

result = problem1(input)

assert result == [34, 30]
print("정답입니다.")
