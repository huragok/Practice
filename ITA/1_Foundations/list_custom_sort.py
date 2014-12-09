#! /usr/bin/env python3

class list_custom_sort(list):
    def sort_insert(self):
        for i in range(1, len(self)):
            key = self[i]
            j = i - 1
            while j > -1 and self[j] > key:
                self[j + 1] = self[j]
                j = j - 1
            self[j + 1] = key

    def sort_merge(self):
        print(len(self))
        self._sort_merge(0, len(self))

    def _sort_merge(self, p, r):
        if r - p > 1:
            q = int((p + r) / 2)
            self._sort_merge(p, q)
            self._sort_merge(q, r)
            L = self[p : q]
            R = self[q : r]
            iL = 0
            iR = 0
            L = L + [10000]
            R = R + [10000]
            for i in range(p, r):             
                if L[iL] < R[iR]:
                    self[i] = L[iL]
                    iL += 1
                else:
                    self[i] = R[iR]
                    iR += 1


if __name__ == "__main__":
    x = list_custom_sort([2,4,5,7,1,2,3,6])
    x.sort_merge()
    print(x)
 
