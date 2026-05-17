class ListNode:
    def __init__(self, key, value, nxt, prv):
        self.key = key
        self.value = value
        self.next = nxt
        self.prev= prv

class LRUCache:

    def __init__(self, capacity: int):
        self.list_head=None
        self.list_tail=None
        self.cache = {}
        self.capacity = capacity

    # prev - node - next

    # prev - node


    def move_node(self, node):
        if self.list_head is node:
            return 
        if self.list_tail is node:
            self.list_tail.prev.next=None
            self.list_tail = self.list_tail.prev
            node.prev=None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev=None
        node.next = self.list_head
        self.list_head.prev=node
        self.list_head= node
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_node(node)
        return node.value



    def put(self, key: int, value: int) -> None:
        current_size = len(self.cache)
        if current_size == 0:
            node=ListNode(key, value, None, None)
            self.cache[key]= node
            self.list_head=node
            self.list_tail=node
        elif key in self.cache:
            existing_node = self.cache[key]
            existing_node.value=value
            self.move_node(existing_node)
        else:
            node = ListNode(key, value, self.list_head, None)
            self.list_head.prev=node
            self.list_head = node
            self.cache[key]=node
        if len(self.cache) > self.capacity:
            self.cache.pop(self.list_tail.key)
            self.list_tail.prev.next = None
            self.list_tail = self.list_tail.prev