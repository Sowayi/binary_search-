class BinarySearch(list):
    def __init__(self, length, difference):
        self.length = length
        self.difference = difference
        for elements in range(1, length + 1):
            self.append(elements * difference)

        self.length = len(self)

    """ Instead of searching through a list sequentially, the binary search starts
    by examining the middle item. if the item is the one being searched for, search terminates.
    if not,if item is greater than middle item, lower half of list is eliminated. the same
    process occurs for the upper half og the list."""
    
    def search(self, key):
        #left side of array goes form middle to zero, and right side from middle to length of the array - 1
        left = 0
        right = self.length - 1
        #index and count are initialized to 0
        index = -1
        count = 0
        while True:
             #divides array into 2 halves
            middle = ((left + right) // 2)
            if left > middle or middle > right:
                # terminate the loop, key not found
                break
             
            if self[middle] == key:
                # assigns index to the value at the middle
                index = middle
                break

            elif self[right] == key:
                # if the index variable is found to the right after splitiing,assigns index key to index variable 
                index = right
                break

            elif self[left] == key:
                # assigns index key value to index variable if found in left index after partition
                index = left
                break
            #incase the left and right portions are the same length
            elif middle == left or middle == right:
                break

            elif self[middle] < key:
                left = middle + 1

            elif self[middle] > key:
                right = middle - 1
            count += 1

        return {'count': count, 'index':index}
