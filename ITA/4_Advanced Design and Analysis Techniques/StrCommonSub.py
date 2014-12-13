#! /usr/bin/env python3

def find_common_sub(str_1, str_2):
    M = len(str_1)
    N = len(str_2)

    s = [[None] * (N + 1) for m in range(M + 1)] # Length of the max common subseq
    for m in range(M + 1):
        s[m][0] = 0
    for n in range(N + 1):
        s[0][n] = 0
    
    for m in range(1, M + 1):
        for n in range(1, N + 1):
            if str_1[m - 1] == str_2[n - 1]:
                print("m = {0}, n = {1}".format(m, n))
                s[m][n] = s[m - 1][n - 1] + 1
            else:
                s[m][n] = max((s[m][n - 1], s[m - 1][n]))
    return s

def get_common_sub(str_1, str_2, s): 
    M = len(str_1)
    N = len(str_2)

    m = M
    n = N
    common_seq = ''
    while m > 0 and n > 0:
        if s[m][n] == s[m - 1][n]:
            m -= 1
        elif s[m][n] == s[m][n - 1]:
            n -= 1
        else:            
            common_seq = str_1[m - 1] + common_seq
            m -= 1
            n -= 1
    return common_seq

if __name__ == "__main__":
    str_1 = '10010101'
    str_2 = '010110110'
    
    s = find_common_sub(str_1, str_2)
    print(get_common_sub(str_1, str_2, s))
    for m in range(8):
        print(s[m]) 
