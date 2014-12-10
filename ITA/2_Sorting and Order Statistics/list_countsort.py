#! /usr/bin/env python3

class list_countsort(list):

    def sort_count(self, n):
        pdf = [0] * n
        for i in self:
            pdf[i] += 1
        
        s = - 1
        for i in range(n):
            if pdf[i] > 0:
                self[s + 1: s + pdf[i] + 1] = [i] * pdf[i]
                s += pdf[i]

if __name__ == "__main__":
    x = list_countsort([2, 5, 3, 0, 2, 3, 0, 3])
    print(x)
    x.sort_count(6)
    print(x)
