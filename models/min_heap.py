# models/min_heap.py
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        self.heap.append(element)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index][0] < self.heap[parent_index][0]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def extract_min(self):
        if not self.heap:
            return None
        min_element = self.heap[0]
        last_element = self.heap.pop()
        if self.heap:
            self.heap[0] = last_element
            self._sift_down(0)
        return min_element

    def _sift_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                
    def print_heap(self):
            print("\nCurrent Heap:")
            for item in self.heap:
                print(f"Selisih: {item[0]} menit, ID: {item[1]['id']}, Nama: {item[1]['nama_tugas']}")
