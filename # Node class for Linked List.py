# Node class for Linked List
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

# Stack implementation using Linked List
class Stack:
    def _init_(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        if self.is_empty():
            return "Stack is Empty"
        current = self.top
        stack_elements = []
        while current:
            stack_elements.append(current.data)
            current = current.next
        return stack_elements


# Queue implementation using Linked List
class Queue:
    def _init_(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue Underflow"
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_data

    def is_empty(self):
        return self.front is None

    def display(self):
        if self.is_empty():
            return "Queue is Empty"
        current = self.front
        queue_elements = []
        while current:
            queue_elements.append(current.data)
            current = current.next
        return queue_elements


# Driver Code to Test
if __name__ == "_main_":
    # Stack Test
    print("Stack Implementation:")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack after pushes:", stack.display())
    print("Popped Element:", stack.pop())
    print("Stack after pop:", stack.display())
    print("Top Element:", stack.peek())

    # Queue Test
    print("\nQueue Implementation:")
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue after enqueues:", queue.display())
    print("Dequeued Element:", queue.dequeue())
    print("Queue after dequeue:", queue.display())
    input("Press Enter to Exit.......")