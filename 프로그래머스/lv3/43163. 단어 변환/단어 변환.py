from collections import deque

def is_convertible(word1, word2):

    diff_count = sum([1 for a, b in zip(word1, word2) if a != b])
    return diff_count == 1

def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [False] * len(words)
    queue = deque([(begin, 0)])
    # print(queue)
    while queue:
        print(queue)
        current_word, depth = queue.popleft()
        print(current_word, depth)

        if current_word == target:
            return depth

        for i, word in enumerate(words):
            if not visited[i] and is_convertible(current_word, word):
                visited[i] = True
                queue.append((word, depth + 1))

    return 0