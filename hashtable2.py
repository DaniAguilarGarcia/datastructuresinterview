#universal hashing
#hashtables are use where: constant time lookup and insertion required
#crytographic applications, indexing data is required
#hash table data structure stores elements in key-value pairs where: 
#key- unique integer that is used for indexing values, value - data that are associated with keys

hashTable = [[],] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0
    for i in range(2, n//2):
        if n % i == 0:
            return 0
    return 1

def getPrime(n):
    if n % 2 == 0:
        n = n + 1
    while not checkPrime(n):
        n += 2
    return n

def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity

def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = 0
