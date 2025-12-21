class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Map key -> Node
        
        # Dummy head and tail nodes to simplify edge cases.
        # Head is "Most Recently Used" end.
        # Tail is "Least Recently Used" end.
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove a node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: Node):
        """Add a node right after the dummy head (MRU position)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move to head (mark as recently used)
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing node
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            # Create new node
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_head(node)
            
            # Check capacity
            if len(self.cache) > self.capacity:
                # Remove LRU node (from tail)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]

    def print_list(self):
        """Prints the list from head to tail."""
        elements = []
        current = self.head.next
        while current and current != self.tail:
            elements.append(f"({current.key}, {current.value})")
            current = current.next
        
        print("head->" + "->".join(elements) + "->tail")

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    try:
        # 1. Initialize Cache
        cap_input = input("Enter cache capacity: ").strip()
        if not cap_input:
            cap = 2 # Default
            print("Using default capacity: 2")
        else:
            cap = int(cap_input)
        
        lRUCache = LRUCache(cap)
        print(f"LRU Cache initialized with capacity {cap}.")
        print(f"LRU Cache initialized with capacity {cap}.")
        print("Commands: 'get', 'put', 'list', 'exit'")

        while True:
            # 2. Get Command
            command = input("\nCommand (get/put/list/exit): ").strip().lower()
            
            if command == 'exit':
                break
                
            elif command == 'get':
                try:
                    key = int(input("Enter key: "))
                    result = lRUCache.get(key)
                    print(f"Result: {result}")
                except ValueError:
                    print("Invalid key. Please enter an integer.")

            elif command == 'put':
                try:
                    # Accepts input like "1, 1" or "(1, 1)"
                    user_val = input("Enter key, value (e.g. 4, 3): ").strip()
                    # Remove parens if present
                    clean_val = user_val.replace('(', '').replace(')', '')
                    parts = clean_val.split(',')
                    
                    if len(parts) != 2:
                        print("Invalid format. Please use 'key, value'.")
                        continue
                        
                    key = int(parts[0].strip())
                    value = int(parts[1].strip())
                    
                    lRUCache.put(key, value)
                    print(f"Inserted: key={key}, value={value}")
                    
                except ValueError:
                    print("Invalid numbers. Please enter integers.")

            elif command == 'list':
                lRUCache.print_list()

            else:
                print("Unknown command.")
                
    except ValueError:
        print("Invalid capacity. Program exiting.")
    except KeyboardInterrupt:
        print("\nExiting...")
