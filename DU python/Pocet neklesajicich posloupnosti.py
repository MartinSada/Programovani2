k = int(input())

def neklesPosl(k):
    chart = [[0]*7 for i in range(k+1)]

    for i in range (1,7):
        chart[1][i] = 1

    for i in range(2,k+1):
        for j in range(1,7):
            for p in range(1,j+1):
                chart[i][j] += chart[i-1][p]

    print(sum(chart[k]))

neklesPosl(k)