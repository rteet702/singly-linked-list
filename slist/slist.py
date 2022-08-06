class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        #Add a new value at the front of the list by changing the head.
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def add_to_back(self, val):
        #Add a new value at the back of the list.
        if self.head == None:
            self.add_to_front(val)
            return self

        #run through SList to find last spot in list.
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node

        return self

    def remove_from_front(self):
        stored_head = self.head
        self.head = self.head.next
        del stored_head

    def remove_from_back(self):
        if self.head == None:
            return self
        
        #run through SList to find last spot in list.
        runner = self.head
        stored = None
        while (runner.next != None):
            stored = runner
            runner = runner.next
        stored.next = None

        return self

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None