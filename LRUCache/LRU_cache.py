class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hash = {}
        self.capacity = capacity
        self.dll = DoubleLinkedList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash:
            return -1
        else:
            self.dll.moveToFront(self.hash[key])
        return self.hash[key].value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.hash:
            self.dll.updateNode(self.hash[key], value)
            self.hash[key].value = value
        else:
            node = Node(key, value)
            if self.capacity == len(self.hash):
                k = self.dll.removeRear()
                del self.hash[k]
            self.dll.addToFront(node)
            self.addToHash(key, node)

    def addToHash(self, key, node):
        self.hash[key] = node


class Node(object):
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.nextt = None

    def updateValue(self, v):
        self.value = v


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def addToFront(self, node):
        if self.head is not None:
            self.head.prev = node
            node.nextt = self.head
        else:
            self.tail = node
        self.head = node

    def removeRear(self):
        key = self.tail.key
        if self.tail.prev is None:
            self.head, self.tail = None, None
        else:
            self.tail = self.tail.prev
            self.tail.nextt = None
        return key

    def removeMidNode(self, node):
        p, n = node.prev, node.nextt
        if p is None:  # node is head
            if n is None:  # node is the only node
                self.head, self.tail = None, None
            else:
                self.head = n
                n.prev = None
        else:
            if n is None:
                self.tail = p
                p.nextt = None
            else:
                p.nextt = n
                n.prev = p
        node.prev, node.nextt = None, None
        return node

    def updateNode(self, node, v):
        node = self.removeMidNode(node)
        node.updateValue(v)
        self.addToFront(node)

    def moveToFront(self, node):
        node = self.removeMidNode(node)
        self.addToFront(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

obj = LRUCache(2)
for x in [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]:
    if len(x) == 1:
        print obj.get(x[0])
    else:
        obj.put(x[0],x[1])



# obj = LRUCache(10)
# for x in [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]:
#     if len(x) == 1:
#         print obj.get(x[0])
#     if len(x) == 2:
#         obj.put(x[0],x[1])

