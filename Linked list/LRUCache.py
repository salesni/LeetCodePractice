"""
146. LRU Cache
Solved
Medium

Topics
Companies
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 
"""


class DoubleLinkNode:
    def __init__(self,value:int = 0, key:int = 0,
                    next:Optional = None,
                    prev:Optional = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = next
class LRUCache:

    def __init__(self, capacity: int):
        self.hash_node:Dict[int,DoubleLinkNode] = {}
        self.head_prev = DoubleLinkNode()
        self.tail_after = DoubleLinkNode()
        self.capacity = capacity

        self.head_prev.next = self.tail_after
        self.tail_after.prev = self.head_prev
    
    def _remove(self,node:DoubleLinkNode):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _put_in_front(self,node:DoubleLinkNode):
        # RECENTLY USED ITEM
        head = self.head_prev.next
        node.next = head
        head.prev = node
        self.head_prev.next = node
        node.prev = self.head_prev

    
    def get(self, key: int) -> int:
        if key not in self.hash_node:
            return -1
        else:
            node = self.hash_node[key]
            self._remove(node)
            self._put_in_front(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hash_node:
            node = self.hash_node[key]
            node.value = value
            self._remove(node)
            self._put_in_front(self.hash_node[key])
        else:
            if self.capacity == len(self.hash_node):
                tail = self.tail_after.prev
                tail.prev.next = self.tail_after
                self.tail_after.prev = tail.prev
                self.hash_node.pop(tail.key)
                del tail
            
            new_node = DoubleLinkNode(value,key)
            self.hash_node[key] = new_node
            self._put_in_front(new_node)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
