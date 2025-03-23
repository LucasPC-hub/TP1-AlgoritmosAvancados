class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def __str__(self):
        return str(self.heap[1:])

    def parent(self, pos):
        return pos // 2

    def left_child(self, pos):
        return 2 * pos

    def right_child(self, pos):
        return 2 * pos + 1

    def is_leaf(self, pos):
        return pos * 2 > self.size

    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def heapify_down(self, pos):
        if not self.is_leaf(pos):
            if (self.right_child(pos) <= self.size and
                    (self.heap[pos] > self.heap[self.left_child(pos)] or
                     self.heap[pos] > self.heap[self.right_child(pos)])):

                if (self.right_child(pos) > self.size or
                        self.heap[self.left_child(pos)] < self.heap[self.right_child(pos)]):
                    self.swap(pos, self.left_child(pos))
                    self.heapify_down(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.heapify_down(self.right_child(pos))

    def heapify_up(self, pos):
        current = pos
        while current > 1 and self.heap[self.parent(current)] > self.heap[current]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def insert(self, element):
        self.heap.append(element)
        self.size += 1
        self.heapify_up(self.size)

    def extract_min(self):
        if self.size == 0:
            raise IndexError("Heap vazio")

        min_element = self.heap[1]

        self.heap[1] = self.heap[self.size]

        self.heap.pop()
        self.size -= 1

        if self.size > 0:
            self.heapify_down(1)

        return min_element

    def get_min(self):
        if self.size == 0:
            raise IndexError("Heap vazio")
        return self.heap[1]

    def build_heap(self, array):
        self.heap = [0]
        self.heap.extend(array)
        self.size = len(array)

        for i in range(self.size // 2, 0, -1):
            self.heapify_down(i)


if __name__ == "__main__":
    min_heap = MinHeap()

    elements = [10, 5, 15, 7, 20, 3, 25]
    for element in elements:
        min_heap.insert(element)

    print("Heap após inserções:", min_heap)

    print("Elementos extraídos em ordem:")
    while min_heap.size > 0:
        print(min_heap.extract_min(), end=" ")
    print()

    min_heap.build_heap([12, 8, 17, 5, 9, 3, 21, 6])
    print("Heap construído a partir do array:", min_heap)

    print("Elementos extraídos em ordem:")
    while min_heap.size > 0:
        print(min_heap.extract_min(), end=" ")