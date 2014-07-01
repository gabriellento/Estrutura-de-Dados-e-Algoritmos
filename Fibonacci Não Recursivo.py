def fibonacci(n,a1 = 1,a2 = 1):
    if n <= 2:
        return 1
    else:
        for i in range(n-2):
            fibfim = a1 + a2
            a1=a2
            a2=fibfim
        return fibfim

fibonacci(20)
