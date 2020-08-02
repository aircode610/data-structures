from typing import Any

class Queue:

    def __init__(self):
        self._queque = []

    def enqueue(self, val: Any) -> None:
        self._queque.append(val)

    def dequeue(self) -> Any:
        result = self._queque[0]
        del self._queque[0]
        return result

    def is_empty(self) -> bool:
        if len(self._queque) > 0:
            return False
        return True

# Test-Driven Development
# TDD

def test_enqueue_dequeue_is_empty():
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.is_empty() == False
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.is_empty() == True

    return "Tests passed"

print(test_enqueue_dequeue_is_empty())