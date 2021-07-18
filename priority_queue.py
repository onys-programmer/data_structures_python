# 과제1번 코드란

class PriorityQueue:
    def __init__(self):
        self.heap_array = list()
        pass

    def swap(self, idx_1, idx_2):
        self.heap_array[idx_1], self.heap_array[idx_2] = self.heap_array[idx_2], self.heap_array[idx_1]
        pass

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
          return False

        parent_idx = inserted_idx // 2

        while self.heap_array[inserted_idx] < self.heap_array[parent_idx]:
            self.swap(inserted_idx, parent_idx)
            inserted_idx = parent_idx
        pass  

    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1

        # case1: 왼쪽 자식 노드도 없을 때
        if left_child_popped_idx >= len(self.heap_array):
            return
        # case2: 오른쪽 자식 노드만 없을 때
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx][0] > self.heap_array[left_child_popped_idx][0]:
                self.swap(popped_idx, left_child_popped_idx)
                self.move_down(left_child_popped_idx)
            else:
                return
        # case3: 왼쪽, 오늘 쪽 자식 노드 모두 있을 때
        else:
            if self.heap_array[left_child_popped_idx][0] < self.heap_array[right_child_popped_idx][0]:
                if self.heap_array[popped_idx][0] > self.heap_array[left_child_popped_idx][0]:
                    self.swap(popped_idx, left_child_popped_idx)
                    self.move_down(left_child_popped_idx)
                else: 
                    return
            else:
                if self.heap_array[popped_idx][0] > self.heap_array[right_child_popped_idx][0]:
                    self.swap(popped_idx, right_child_popped_idx)
                    self.move_down(right_child_popped_idx)
                else: 
                    return
        pass

    def is_empty(self):
        return True if len(self.heap_array) == 0 else False
        pass
 
    def put(self, data):
        if len(self.heap_array) == 0:
          self.heap_array.append(None)
          self.heap_array.append(data)
          return True
        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1
        self.move_up(inserted_idx)
        pass
 
    def peek(self):
        if len(self.heap_array) <= 1:
          return None
        else:
          return self.heap_array[0]
        pass

    def get(self):
        if len(self.heap_array) <= 1:
            return None
        else: 
            temp = self.heap_array[1]
            self.heap_array[1] = self.heap_array[-1]
            del self.heap_array[-1]
            self.move_down(1)
            return temp

# Test code
 
pq = PriorityQueue()
pq.put((0, 'a'))
pq.put((5, 'b'))
pq.put((2, 'c'))
pq.put((1, 'd'))
pq.put((3, 'e'))
pq.put((4, 'f'))
 
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
