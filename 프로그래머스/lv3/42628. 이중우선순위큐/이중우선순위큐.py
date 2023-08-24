# def solution(operations):
#     answer = []

#     for i in operations:
#         if i[0] == 'I':
#             answer.append(int(i[2:]))
#         elif i[0] == 'D':
#             if i[2:] == '1':
#                 try:
#                     answer.remove(max(answer))
#                 except:
#                     pass
#             elif i[2:] == '-1':
#                 try:
#                     answer.remove(min(answer))
#                 except:
#                     pass

#     if len(answer) == 0:
#         answer = [0, 0]
#     else:
#         answer = [max(answer), min(answer)]

#     return answer

def solution(operations):
    answer = []

    for op in operations:
        command, value = op.split()
        value = int(value)

        if command == 'I':
            answer.append(value)
        elif command == 'D' and value == 1 and answer:
            answer.remove(max(answer))
        elif command == 'D' and value == -1 and answer:
            answer.remove(min(answer))

    return [max(answer), min(answer)] if answer else [0, 0]
