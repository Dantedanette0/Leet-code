import random

class RandomizedSet:

    def __init__(self):
        self.random_set = []
        

    def insert(self, val: int) -> bool:
        if val not in self.random_set:  
            self.random_set.append(val)  
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.random_set:
            self.random_set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.random_set[random.randint(0, len(self.random_set) - 1)] 

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
