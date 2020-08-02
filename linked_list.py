from typing import Any

class _Node:

    def __init__(self, val=None, next=None):
        self._val = val
        self._next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val: Any) -> None:
        """
        adds a value to the end of the linked list
        duplicate values are allowed.
        :param val: the value to store
        :return: None
        """
        new_node = _Node(val=val)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail._next = new_node
            self.tail = new_node

    def delete(self, val: Any) -> None:
        """
        deletes the node with the val that is given
        deletes the first node for the duplicated values
        :param val: the value to delete
        :return: None
        """
        if self.head == None:
            raise Exception("The linked list is empty")

        node = self.head
        con = False

        if self.head._val == val and self.tail._val == val:
            con = True
            self.head = None
            self.tail = None
            return None

        if self.head._val == val:
            con = True
            self.head = self.head._next

        while node._next._next != None:
            if node._next._val == val:
                con = True
                node._next = node._next._next
                break
            node = node._next

        if node._next == self.tail and con == False:
            con = True
            node._next = None
            self.tail = node

        if con == False:
            raise Exception("No nodes with the given value")

    def contains(self, val: Any) -> bool:
        """
        returns true if a node with the given value exists in the linked list
        :param val: val
        :return: True/False
        """
        node = self.head

        while node != None:
            if node._val == val:
                return True

            node = node._next

        return False

    def is_empty(self) -> bool:
        """
        returns true if the linked list is empty
        :param val: val
        :return: True/False
        """
        if self.head == None:
            return True

        return False


# Test-Driven Development
# TDD

def test_empty():
    l = LinkedList()
    assert l.is_empty()

    return "Tests passed"

def test_add_two_items():
    l = LinkedList()
    l.add(12)
    l.add(13)
    assert l.contains(12)
    assert l.contains(13)

    return "Tests passed"

def test_delete_four_items():
    l = LinkedList()
    l.add(12)
    l.add(13)
    l.add(14)
    l.add(15)
    l.add(16)
    l.delete(12)
    l.delete(15)
    l.delete(16)
    l.delete(14)
    l.delete(13)
    assert l.is_empty()

    return "Tests passed"

print(test_empty())
print(test_add_two_items())
print(test_delete_four_items())
