def solution(dots):
    answer = 0
    first_dot = dots[0]
    three_dots = dots[1:]
    
    for i in range(len(three_dots)):
        x_a = first_dot[0] - three_dots[i%3][0] 
        y_a = first_dot[1] - three_dots[i%3][1]
        x_b = three_dots[(i+1)%3][0] - three_dots[(i+2)%3][0]
        y_b = three_dots[(i+1)%3][1] - three_dots[(i+2)%3][1]
        if x_a/y_a == x_b/y_b:
            answer = 1
            break
    return answer