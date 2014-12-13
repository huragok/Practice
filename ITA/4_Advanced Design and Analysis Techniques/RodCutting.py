#! /usr/bin/env python3

def cut_rod_dp(n, p): # Dynamic programming
    r = [-1] * (n + 1) # Initialize the revenue
    s = [None] * (n + 1) # Initialize the first cuts
    
    r[0] = 0
    s[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            if r[i] < r[j] + p[i - j]:
                r[i] = r[j] + p[i - j]
                s[i] = i - j
    return (r, s)

def cut_rod_mrc(n, p, r, s): # Memorized recursive
    if n == 0:
        r[0] = 0
        s[0] = 0
    else:
        r[n] = -1
        for j in range(0, n):
            if r[j] < 0:
                cut_rod_mrc(j, p, r, s)
            if r[n] < r[j] + p[n - j]:
                r[n] = r[j] + p[n - j]
                s[n] = n - j

def print_rod(r, s):
    n = len(r) - 1
    count = 0
    while n > 0:
        count += 1
        print("Cut {0}: {1}".format(count, s[n]))
        n -= s[n]

if __name__ == "__main__":
    p = (0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30)
    n = 9

    (r, s) = cut_rod_dp(n, p)
    print_rod(r, s)

    r = [-1] * (n + 1)
    s = [None] * (n + 1)
    cut_rod_mrc(n, p, r, s)
    print_rod(r, s)
