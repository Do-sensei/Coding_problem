from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    
    def bfs(x, y, blob_id):
        queue = deque([(x, y)])
        land[x][y] = blob_id
        size = 1
        
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1:
                    land[nx][ny] = blob_id
                    queue.append((nx, ny))
                    size += 1
                    
        return size
    
    blob_id = 2
    blob_sizes = {}
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                blob_size = bfs(i, j, blob_id)
                blob_sizes[blob_id] = blob_size
                blob_id += 1
                
    max_oil = 0
    for col in range(m):
        unique_blobs = set()
        for row in range(n):
            if land[row][col] > 1:
                unique_blobs.add(land[row][col])
                
        total_oil = sum(blob_sizes[blob] for blob in unique_blobs)
        max_oil = max(max_oil, total_oil)
        
    return max_oil