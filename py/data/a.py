while True:
    N = int(input())
    if N == 0:
        break
    A,B,C,D = map(int,input().split())
    M = [list(map(int,input().split())) for _ in range(N+1)]


    now_x ,now_y = M[0][0], M[0][1]
    dx = 0
    dy = 0
    dame = 0

    for  i in range(N):
        if (now_x < A and C < M[i][0]) or (M[i][0] < A and  C < now_x):
            dx += abs(M[i][0] - now_x) - (C - A)
        elif A < now_x < C < M[i][0]:
            dx += (M[i][0] - now_x) - (C - now_x)
        elif A < M[i][0] < C < now_x:
            dx += (now_x - M[i][0]) - (C - M[i][0])
        elif C < now_x < M[i][0] or C < M[i][0] < now_x or now_x< M[i][0] < A or M[i][0] < now_x < A:
            dx += abs(M[i][0] - now_x)
        
        if (now_y < B and  D < M[i][1]) or (M[i][1] < A and  D < now_y):
            dy += abs(M[i][0] - now_y) - (D - B)
        elif B < now_y < D < M[i][1]:
            dy += (M[i][1]-  now_y) - (D - now_y)
        elif B < M[i][1] < D < now_y:
            dy += (now_y - M[i][1]) - (D - M[i][1])
        elif D < now_y < M[i][1] or D < M[i][1] < now_y or  now_y < M[i][1] < B or M[i][1] < now_y < B:
            dy += abs(M[i][1] - now_y)

    dame = dx + dy 
    print("dame"+str(dame))