
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for s in string:
        hash = ((hash << 5) + hash) + ord(s)

    return hash % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    i = hash(key, hash_table.capacity)
    pair = Pair(key, value)
    node = Node(pair, None)
    run = True
    current = hash_table.storage[i]
    if current != None:
        while run:
            if current.value.key == key:
                current.value.value = value
                run = False
            elif current.next_node == None:
                current.next_node = pair
                run = False
            else:
                current = current.next_node
    else:
        hash_table.storage[i] = pair

    #     #bucket not empty
    #     current = hash_table.storage[i]
    #     while current.value.key != key:
    #     # if hash_table.storage[i].value.key != key:

    #         #print wanring
    #         print(f"Yo, dawg. There's already something written at address: {hash_table.storage[i]} It's  {value}")
    # else:
    #     #add the pair to hash_table
    #     hash_table.storage[i] = pair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)

    if hash_table.storage[index] is None:
        print('warning')
    else:
        hash_table.storage[index] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)

    if hash_table.storage[index] is None:
        return None
    if hash_table.storage[index] is not None and hash_table.storage[index].key != key:
        return None
    else:
        return hash_table.storage[index].value



def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
