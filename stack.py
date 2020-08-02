from typing import Any

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, val: Any) -> None:
        self.stack.append(val)

    def pop(self) -> Any:
        result = self.stack[-1]
        del self.stack[-1]
        return result


# Test-Driven Development
# TDD

def test_push_pop():
    stack = Stack()
    stack.push(3)
    stack.push(2)
    stack.push(1)
    assert stack.pop() == 1
    assert stack.pop() == 2
    assert stack.pop() == 3

    return "Tests passed"

print(test_push_pop())
