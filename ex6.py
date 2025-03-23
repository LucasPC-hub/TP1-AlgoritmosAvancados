class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self, i):
        parent_idx = self.parent(i)
        if i == 0 or self.heap[parent_idx][0] <= self.heap[i][0]:
            return
        self.swap(i, parent_idx)
        self.heapify_up(parent_idx)

    def heapify_down(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < self.size and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left

        if right < self.size and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        if smallest != i:
            self.swap(i, smallest)
            self.heapify_down(smallest)

    def insert(self, priority, task):
        self.heap.append((priority, task))
        self.size += 1
        self.heapify_up(self.size - 1)

    def get_min(self):
        if self.size == 0:
            return None
        return self.heap[0]

    def extract_min(self):
        if self.size == 0:
            return None

        min_task = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heap.pop()

        if self.size > 0:
            self.heapify_down(0)

        return min_task

    def is_empty(self):
        return self.size == 0


class TaskScheduler:
    def __init__(self):
        self.priority_queue = MinHeap()
        self.task_count = 0

    def add_task(self, description, priority):
        self.task_count += 1
        task = {
            'id': self.task_count,
            'description': description,
            'priority': priority
        }
        self.priority_queue.insert(priority, task)
        return task['id']

    def get_next_task(self):
        if self.priority_queue.is_empty():
            return None
        priority, task = self.priority_queue.get_min()
        return task

    def execute_next_task(self):
        if self.priority_queue.is_empty():
            return None
        priority, task = self.priority_queue.extract_min()
        return task

    def has_tasks(self):
        return not self.priority_queue.is_empty()


if __name__ == "__main__":
    scheduler = TaskScheduler()

    scheduler.add_task("Completar relatório urgente", 1)
    scheduler.add_task("Responder e-mails", 3)
    scheduler.add_task("Preparar apresentação", 2)
    scheduler.add_task("Atualizar site", 4)
    scheduler.add_task("Reunião com cliente", 1)

    print("Executando tarefas em ordem de prioridade:")

    while scheduler.has_tasks():
        task = scheduler.execute_next_task()
        print(f"Executando: {task['description']} (Prioridade: {task['priority']})")