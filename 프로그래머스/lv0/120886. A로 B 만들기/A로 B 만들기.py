def solution(before, after):
    after = sorted(after)
    before = sorted(before)
    if after == before:
        return 1
    else:
        return 0