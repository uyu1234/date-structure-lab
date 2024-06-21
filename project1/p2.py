# 프로젝트 문제 2번
input = ")))()"

def problem2(input):
    left = 0
    right = 0

    for char in input:
        #char에 input 저장
        if char == '(':
            #(의 경우 )가 필요하기에 오른쪽에 1 추가
            right += 1
        if char == ')':
            if right>0:
                right -= 1
            #)의 경우 오른쪽에 있는 값이 0보다 클 경우 1 감소시킴
            else:
                left += 1
            #오른쪽에 변화 없으면 1 추가
        

    result = right+left
    return result

result = problem2(input)

assert result == 3
print("정답입니다.")
