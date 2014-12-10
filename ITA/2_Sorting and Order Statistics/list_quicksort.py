#! /usr/bin/env python3

class list_quicksort(list):
    def sort_quick(self):
        self._sort_quick(0, len(self))

    def _sort_quick(self, p, r):
        if r - p < 2:
            return
        q = self._partition(p, r)
        self._sort_quick(p, q)
        self._sort_quick(q, r)

    def _partition(self, p, r):
        i = p - 1
        for j in range(p, r - 1):
            if self[j] < self[r - 1]:
                i += 1
                [self[i], self[j]] = [self[j], self[i]]

        [self[r - 1], self[i + 1]] = [self[i + 1], self[r - 1]]
        return i + 1

if __name__ == "__main__":
    x = list_quicksort([2,8,7,1,3,5,6,4])
    print(x)
    x.sort_quick()
    print(x)
