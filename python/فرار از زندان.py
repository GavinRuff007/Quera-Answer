import heapq
from collections import deque

def dij(s,e,p):
    n = len(p)
    dis2 = [[1e9 for _ in range(n)] for _ in range(n)]
    dis2[s[0]][s[1]] = 0
    heap = [[0,s]]
    while heap:
        [d, node] = heapq.heappop(heap)
        if node == e:
            return d
        if d > dis2[node[0]][node[1]]:
            continue
        i,j = node
        dis = d
        while i>0 and p[i-1][j] == 0:
            dis += 1
            i -= 1
        if dis < dis2[i][j]:
            dis2[i][j] = dis
            heapq.heappush(heap, [dis, [i, j]])
        i,j = node
        dis = d
        while i< n-1 and p[i+1][j] == 0:
            dis += 1
            i += 1
        if dis < dis2[i][j]:
            dis2[i][j] = dis
            heapq.heappush(heap, [dis, [i,j]])
        i,j = node
        dis = d
        while j>0 and p[i][j-1] == 0:
            dis += 1
            j -= 1
        if dis < dis2[i][j]:
            dis2[i][j] = dis
            heapq.heappush(heap,[dis,[i,j]])
        i,j = node
        dis = d
        while j< n-1 and p[i][j+1] == 0:
            dis += 1
            j += 1
        if dis < dis2[i][j]:
            dis2[i][j] = dis
            heapq.heappush(heap,[dis,[i,j]])
    return -1   



def shortest_distance(start, end, prison):
    rows = len(prison)
    cols = len(prison[0])

    queue = deque()
    queue.append(start)

    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0

    while queue:
        current = queue.popleft()
        row, col = current

        # بررسی وجود مقصد
        if current == end:
            # بررسی قابلیت بایستدن در مقصد
            if prison[row][col] == 0:
                return distances[row][col]
            else:
                return -1

        # حرکت به سمت بالا
        if row > 0 and prison[row-1][col] == 0 and distances[row-1][col] == float('inf'):
            queue.append((row-1, col))
            distances[row-1][col] = distances[row][col] + 1

        # حرکت به سمت پایین
        if row < rows - 1 and prison[row+1][col] == 0 and distances[row+1][col] == float('inf'):
            queue.append((row+1, col))
            distances[row+1][col] = distances[row][col] + 1

        # حرکت به سمت چپ
        if col > 0 and prison[row][col-1] == 0 and distances[row][col-1] == float('inf'):
            queue.append((row, col-1))
            distances[row][col-1] = distances[row][col] + 1

        # حرکت به سمت راست
        if col < cols - 1 and prison[row][col+1] == 0 and distances[row][col+1] == float('inf'):
            queue.append((row, col+1))
            distances[row][col+1] = distances[row][col] + 1

    # اگر به مقصد نرسیده باشیم
    return -1   



def find_shortest_path(start, end, prison):
    rows = len(prison)
    cols = len(prison[0])
    
    # تابع کمکی برای بررسی اعتبار حرکت در محدوده زندان
    def is_valid_move(x, y):
        return x >= 0 and x < rows and y >= 0 and y < cols and prison[x][y] == 0

    # تابع کمکی برای پیدا کردن مسیر کوتاهترین مسافت با استفاده از الگوریتم عمق اول
    def dfs(x, y, distance):
        # بررسی اینکه زندانی به مقصد رسیده است یا خیر
        if [x, y] == end:
            return distance

        # تنظیم خانه فعلی به عنوان دیوار تا دوباره به آن بازنگری نکنیم
        prison[x][y] = 1

        # حرکت در جهار های ممکن (بالا، پایین، چپ، راست)
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        min_distance = float('inf')

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y):
                # حساب کردن مسافت جدید برای حرکت در جهت جدید
                new_distance = dfs(new_x, new_y, distance + 1)
                # آپدیت کردن مسافت کوتاهتر
                if new_distance != -1:
                    min_distance = min(min_distance, new_distance)

        # بازگشت -1 اگر مسیری پیدا نشده است
        if min_distance == float('inf'):
            return -1

        return min_distance

    # فراخوانی تابع مبتنی بر عمق
    result = dfs(start[0], start[1], 0)

    return result      
s = eval(input())
e = eval(input())
p = eval(input())

try:
    print(dij(s,e,p))
        
except:          
    if find_shortest_path(s, e, p)   != -1:
          print(find_shortest_path(s, e, p))
    elif find_shortest_path(s, e, p)   == -1 :
            
          print("-1")  
            
            
            
            