n = int(input())

def weird_algorithm(n):
    print(int(n), end = " ")
    while(n != 1):
        if n % 2 == 0:
            n /= 2
        else:
            n = (n * 3) + 1
        print(int(n), end = " ")

weird_algorithm(n)