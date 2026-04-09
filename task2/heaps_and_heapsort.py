from abc import ABC, abstractmethod
import tree_printer as tprint

# Heaps & HeapSort
class Heap:
    def __init__(self, data_array):
        self.data = data_array
        self.build_heap()

    def build_heap(self):
        n = (len(self.data) // 2) - 1
        for i in range(n, -1, -1):
            self.heapify(i, len(self.data) - 1)
     

    @abstractmethod
    def heapify(self, i, n):
        """Sift Down"""
        pass

    @abstractmethod
    def sift_up(self, i):
        """Sift Up"""
        pass 

    def get_root(self):
        if not self.data:
            raise IndexError("Heap is empty.")
        return self.data[0]

    def left_child(self, i):
            return i * 2 + 1

    def right_child(self, i):
            return (i * 2) + 2
    def parent(self, i):
        return (i - 1) // 2
   
    def insert(self, item):
        self.data.append(item)
        self.sift_up(len(self.data) - 1)

    def pop(self, i=-1):
        if not self.data:
            raise IndexError ("Cannot pop element: heap is empty.")
        if i < 0:
            i +=len(self.data)


        popped_item = self.data[i]
        if i == len(self.data) -1:
            self.data.pop()
            return popped_item
        else:
            self.data[i] = self.data.pop()
            self.sift_up(i)
            self.heapify(i, len(self.data) - 1 )
        return popped_item

    def extract_root(self):
        return self.pop(0)
    def sort(self):
        """
        Warning: In-place sorting destroys the heap property.
        After calling this, self.data will be a sorted array, not a valid heap.
        """
        
        for n in range(len(self.data) - 1, 0, -1):
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
   
    def sift_up(self,i):
        while i >0:
            p = self.parent(i)
            if self.data[i] > self.data[p]:
                self.data[i], self.data[p] = self.data[p], self.data[i]
                i = p
            else:
                break

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
    def sift_up(self,i):
        while i >0:
            p = self.parent(i)
            if self.data[i] < self.data[p]:
                self.data[i], self.data[p] = self.data[p], self.data[i]
                i = p
            else:
                break

if __name__ == "__main__":
    data_array = [1, 4, 3, 7, 8, 3, 6, 2, 7, 10]
    print("original data:")
    print(data_array)
    print("-" * 60)

    print("max heap:")
    maxheap = Max_Heap(data_array.copy())
    print(maxheap.data)
    tprint.print_heap(maxheap)
    print("-" * 60)

    print("min heap:")
    minheap = Min_Heap(data_array.copy())
    print(minheap.data)
    tprint.print_heap(minheap)
    print("-" * 60)
   
    print("pop last item:")
    maxheap.pop()
    print(maxheap.data)
    tprint.print_heap(maxheap)
    print("-" * 60)

    print("heap sort:")
    maxheap.sort()
    print(maxheap.data)
    tprint.print_heap(maxheap)

    #Empty Heao Optimization Test
    print("\n" + "-" * 60)
    print("Test Optimization: Empty Heap Operation")
    try:
        empty_minheap = Min_Heap([])
        empty_minheap.extract_root()
    except IndexError as e:
        print("Caught exception:", e)
   
    try:
        empty_minheap = Min_Heap([])
        empty_minheap.pop()
    except IndexError as e:
        print("Caught exception:", e)
    
    print("\n" + "-" * 60)
