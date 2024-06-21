input = [[4, 3, 2, 1],
         [0, 0, 0, 0],
         [0, 0, 9, 0],
         [1, 2, 3, 4]]
N = 4

forest = []


from collections import deque

def problem3(input):
    bear_size = 2
    honeycomb_count = 0
    total_time = 0
    bear_x, bear_y = 0, 0

    forest = [row[:] for row in input]
    
    # 곰의 초기 위치 찾기
    for i in range(N):
        for j in range(N):
            if forest[i][j] == 9:
                bear_x, bear_y = i, j
                forest[i][j] = 0  # 초기 위치를 0으로 지정   
    print("곰의 초기 위치 x : {0}, y : {1}".format(bear_x, bear_y))
    
    # 곰이 이동하는 방향벡터. (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 좌표가 맞는지 확인
    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < N

    while True:
        # BFS를 위한 큐 초기화
        queue = deque([(bear_x, bear_y, 0)])  
        visited = [[False] * N for _ in range(N)] # 방문한 위치 기록
        visited[bear_x][bear_y] = True

        found_honey = False 
        possible_honey = [] # 찾은 벌집의 위치, 시간 저장
        
        while queue:
            x, y, time = queue.popleft() # 현재 위치, 시간 가져옴
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy # 현재 위치에서 새로운 위치로 게산
                
                if is_valid(nx, ny) and not visited[nx][ny]: # 위치가 유효한 지, 방문하지 않았는 지
                    cell_value = forest[nx][ny]
                    
                    if cell_value == 0 or cell_value <= bear_size: # 방문 가능 한 지
                        visited[nx][ny] = True
                        queue.append((nx, ny, time + 1)) # 해당 경우 모두 만족 시 위치 및 시간을 리스트에 추가 
                        
                        if 1 <= cell_value < bear_size:
                            possible_honey.append((nx, ny, time + 1))
                            found_honey = True
        
        if found_honey:
            possible_honey.sort(key=lambda x: (x[2], x[0], x[1]))  # 시간, 행, 열 순으로 정렬
            bear_x, bear_y, time = possible_honey[0]
            forest[bear_x][bear_y] = 0
            honeycomb_count += 1
            total_time += time
            
            if honeycomb_count == bear_size:
                bear_size += 1
                honeycomb_count = 0
        else:
            break
    
    result = total_time
    return result

result = problem3(input)

assert result == 14
print("정답입니다.")