class RandomizedSet(object):
    def __init__(self):
        self.vals = []

    # do initialize if necessary


    # @param {int} val Inserts a value to the set
    # Returns {bool} true if the set did not already contain the specified element or false
    def insert(self, val):
        bLen = len(self.vals)
        self.vals = set(self.vals.append(val))
        aLen = len(self.vals)
        return bLen != aLen

    # Write your code here


    # @param {int} val Removes a value from the set
    # Return {bool} true if the set contained the specified element or false
    def remove(self, val):
        pass

    # Write your code here


    # return {int} a random number from the set
    def getRandom(self):
        pass

# Write your code here
