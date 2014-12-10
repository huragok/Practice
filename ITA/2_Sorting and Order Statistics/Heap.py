#! /usr/bin/env python3

class Heap(list):
    def __init__(self, *args, **kargs):
        list.__init__(self, *args, **kargs)
        self.heapsize = 0

    def max_heapify(self, i):
        flag_left = True if 2 * i + 1 < self.heapsize else False
        flag_right = True if 2 * i + 2 < self.heapsize else False
        
        i_max = i
        if flag_left:
            if self[2 * i + 1] > self[i_max]:
                i_max = 2 * i + 1
        
        if flag_right:
            if self[2 * i + 2] > self[i_max]:
                i_max = 2 * i + 2

        [self[i], self[i_max]] = [self[i_max], self[i]]

        if flag_left:
            self.max_heapify(2 * i + 1)
        if flag_right:
            self.max_heapify(2 * i + 2)

    def build_heap(self):
        self.heapsize = len(self)
        for i in range(int(len(self) / 2) - 1, -1, -1):
            self.max_heapify(i)

    def sort_heap(self):
        self.build_heap()
        for i in range(len(self) - 1, 0, -1):
            [self[i], self[0]] = [self[0], self[i]]
            self.heapsize -= 1
            self.max_heapify(0)

if __name__ == "__main__":
    x = Heap([4,1,3,2,16,9,10,14,8,7])
    print(x)
    x.build_heap()
    print(x)
    x.sort_heap()
    print(x)
