from abc import ABC, abstractmethod
import tree_printer as tprint
import math

# Heaps & HeapSort
class Heap:
    def __init__(self, data_array):
        self.data = data_array
        self.last_index = len(self.data) - 1
        self.build_heap()

    def build_heap(self):
        n = math.ceil(self.last_index / 2) - 1
        for i in range(n, -1, -1):
            self.heapify(i, self.last_index)
        return

    @abstractmethod
    def heapify(self, i, n):
        pass

    def get_root(self):
        return self.data[0]

    def left_child(self, i):
        if i == 0:
            return 1
        else:
            return i * 2 + 1

    def right_child(self, i):
        if i == 0:
            return 2
        else:
            return (i * 2) + 2

    def insert(self, item):
        self.data.append(item)
        self.last_index += 1
        self.build_heap()
        return

    def pop(self, i=-1):
        popped_item = self.data[i]
        if i == -1:
            self.data.pop()
            self.last_index -= 1
        else:
            self.data[i] = self.data.pop()
            self.last_index -= 1
            self.heapify(i, self.last_index)
        return popped_item

    def extract_root(self):
        root = self.data[0]
        self.data[0] = self.data[self.last_index]
        self.data.pop()
        self.last_index -= 1
        self.heapify(0, self.last_index)
        return root

    def sort(self):
        for n in range(self.last_index, -1, -1):
            self.data[n], self.data[0] = self.data[0], self.data[n]
            self.heapify(0, n-1)
        return

class Max_Heap(Heap):
    def __init__(self, data_array):
        super().__init__(data_array)

    def heapify(self, i, n):
        l = self.left_child(i)
        r = self.right_child(i)
        largest = i
        if l <= n and self.data[l] > self.data[i]:
            largest = l
        if r <= n and self.data[r] > self.data[largest]:
            largest = r
        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.heapify(largest, n)
        return

class Min_Heap(Heap):
    def __init__(self, data_array):
        super().__init__(data_array)

    def heapify(self, i, n):
        l = self.left_child(i)
        r = self.right_child(i)
        smallest = i
        if l <= n and self.data[l] < self.data[i]:
            smallest = l
        if r <= n and self.data[r] < self.data[smallest]:
            smallest = r
        if smallest != i:
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            self.heapify(smallest, n)
        return

if __name__ == "__main__":
    data_array = [1, 4, 3, 7, 8, 3, 6, 2, 7, 10]
    print("original data:")
    print(data_array)
    print("-" * 50)

    print("max heap:")
    maxheap = Max_Heap(data_array)
    print(maxheap.data)
    tprint.print_heap(maxheap)
    print("-" * 50)

    print("min heap:")
    maxheap = Min_Heap(data_array)
    print(minheap.data)
    tprint.print_heap(minheap)
    print("-" * 50)

    print("pop last item:")
    maxheap.pop()
    print(maxheap.data)
    tprint.print_heap(maxheap)
    print("-" * 50)

    print("heap sort:")
    maxheap.sort()
    print(maxheap.data)
    tprint.print_heap(maxheap)
