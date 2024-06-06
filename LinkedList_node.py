class Node:
    def __init__(self, _id, value, next_node=None):
        self.id = _id
        self.value = value
        self.next = next_node

    def __str__(self):
        return f"Node {self.id}: value {self.value}"

class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter

    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        if self._current:
            node = self._current
            self._current = self._current.next
            return node
        else:
            raise StopIteration

    def add_node(self, value):
        _id = len(self) + 1
        if not self.head:
            self.head = Node(_id, value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(_id, value)

    def find_node_by_id(self, _id):
        current = self.head
        while current:
            if current.id == _id:
                return current
            current = current.next
        return None  

    def delete_last_node(self):
        if not self.head:  
            return None

        if not self.head.next:  
            removed_node = self.head
            self.head = None
            return removed_node

        current = self.head
        while current.next and current.next.next:
            current = current.next
        
        removed_node = current.next
        current.next = None
        return removed_node

    def print_nodes(self):
        current = self.head
        while current:
            print(current)
            current = current.next

class OrderedLinkedList(LinkedList):
    def add_node(self, value):
        _id = len(self) + 1
        if not self.head or self.head.value > value:
            self.head = Node(_id, value, self.head)
        else:
            current = self.head
            while current.next:
                if current.next.value > value:
                    break
                current = current.next
            current.next = Node(_id, value, current.next)

if __name__ == "__main__":
    container = LinkedList()
    container.add_node(10)
    container.add_node(20)
    container.add_node(30)
    print(len(container))
    container.print_nodes()

    node = container.find_node_by_id(2)
    if node:
        print(f"Found: {node}")
    else:
        print("Node not found")

    removed_node = container.delete_last_node()
    if removed_node:
        print(f"Removed: {removed_node}")
    else:
        print("No node to remove")

    container.print_nodes()

    ordered_container = OrderedLinkedList()
    ordered_container.add_node(40)
    ordered_container.add_node(20)
    ordered_container.add_node(60)
    ordered_container.add_node(50)
    ordered_container.add_node(30)
    ordered_container.print_nodes()
