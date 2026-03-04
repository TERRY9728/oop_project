#  from PrettyPrint import PrettyPrintTree

# Heaps & HeapSort
class Heap:
    def __init__(self, data_array):
        self.data = data_array
        self.size = len(self.data)
        self.build_heap()

    def build_heap(self):
        for i in range((self.size // 2), 0, -1):
            self.heapify(i)
        return

    def heapify(self, i):
        pass

    def get_root(self):
        return self.data[0]

    def get_lchild_index(self, i):
        return i * 2

    def get_rchild_index(self, i):
        return (i * 2) + 1

    def insert(self):
        pass

    def pop(self):
        pass

    def extract_root(self):
        pass

    def heap_sort(self):
        pass

class Max_Heap(Heap):
    def __init__(self, data_array):
        super().__init__(data_array)

    def heapify(self, i):
        l = self.get_lchild_index(i)
        r = self.get_rchild_index(i)
        largest = i
        if l <= self.size and self.data[l-1] > self.data[i-1]:
            largest = l
        else:
            largest = i
        if r <= self.size and self.data[r-1] > self.data[largest-1]:
            largest = r
        if largest != i:
            self.data[i-1], self.data[largest-1] = self.data[largest-1], self.data[i-1]
            self.heapify(largest)
        return

class Min_Heap(Heap):
    pass

if __name__ == "__main__":
    data_array = [1, 4, 3, 7, 8, 3, 6, 2, 7, 10]
    maxheap = Max_Heap(data_array)
    print(maxheap.data)

