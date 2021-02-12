class HashTable(object):
    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def put(self, keys, data):
        index = self.hash_function(keys)

        while self.keys[index] is not None:
            if self.keys[index] == keys:
                self.values[index] = data  # insert
                return
            # rehash and try to find another slot
            index = (index + 1) % self.size

        # insert
        self.keys[index] = keys
        self.values[index] = data

    def get(self, keys):
        index = self.hash_function(keys)

        while self.keys[index] is not None:
            if self.keys[index] == keys:
                return self.values[index]
        # which means the key is not present in the associative array
        return None

    def hash_function(self, key):
        sum = 0
        for pos in range(len(key)):
            sum = sum + ord(key[pos])
        return sum % self.size


if __name__ == "__main":
    table = HashTable()
    table.put("apple", 10)
    table.put("orange", 20)
    table.put("car", 30)
    table.put("table", 40)

    print(table.get("car"))
