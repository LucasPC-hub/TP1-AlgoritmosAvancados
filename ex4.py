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
            min_child_pos = self.left_child(pos)

            if (self.right_child(pos) <= self.size and
                    self.heap[self.right_child(pos)] < self.heap[min_child_pos]):
                min_child_pos = self.right_child(pos)

            if self.heap[pos] > self.heap[min_child_pos]:
                self.swap(pos, min_child_pos)
                self.heapify_down(min_child_pos)

    def insert(self, element):
        self.heap.append(element)
        self.size += 1

        current = self.size
        while current > 1 and self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def pop(self):
        if self.size == 0:
            raise IndexError("Heap vazio")

        min_element = self.heap[1]

        self.heap[1] = self.heap[self.size]

        self.heap.pop()

        self.size -= 1

        if self.size > 0:
            self.heapify_down(1)

        return min_element


if __name__ == "__main__":
    min_heap = MinHeap()

    elements = [10, 5, 15, 7, 20, 3, 25]
    for element in elements:
        min_heap.insert(element)

    print("Heap após inserções:", min_heap)

    print("Elementos removidos em ordem:")
    while min_heap.size > 0:
        print(min_heap.pop(), end=" ")
    print("\n")

    data = [8, 4, 12, 2, 6, 10, 14]
    for item in data:
        min_heap.insert(item)

    print("Segundo heap:", min_heap)
    print("Removendo raiz:", min_heap.pop())
    print("Heap após remoção:", min_heap)