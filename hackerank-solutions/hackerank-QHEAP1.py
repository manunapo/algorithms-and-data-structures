# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


class MinBinaryHeap():

    def __init__(self):
        self.heap = []

    def _swap(self, posa, posb):
        tmp = self.heap[posa]
        self.heap[posa] = self.heap[posb]
        self.heap[posb] = tmp

    def _up_heapify(self, child):
        parent = (child-1)//2
        if (self.heap[parent] > self.heap[child]):
            self._swap(parent, child)
            if parent > 0:
                self._up_heapify(parent)

    def _down_heapify(self, parent):
        left = 2*parent + 1
        right = 2*parent + 2
        smallest = parent
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != parent:
            self._swap(parent, smallest)
            self._down_heapify(smallest)

    def insert(self, key):
        self.heap.append(key)
        self._up_heapify(len(self.heap)-1)

    def delete(self, key):
        for i in range(len(self.heap)):
            if self.heap[i] == key:
                self.heap[i] = self.heap[-1]
                del self.heap[-1]
                self._down_heapify(0)
                break

    def get_min(self):
        if (len(self.heap)) > 0:
            return self.heap[0]
        else:
            return None


mbh = MinBinaryHeap()


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        inp = input().rstrip().split()

        if inp[0] == "1":
            mbh.insert(int(inp[1]))
        elif inp[0] == "2":
            mbh.delete(int(inp[1]))
        elif inp[0] == "3":
            print(f"{mbh.get_min()}")
