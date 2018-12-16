# Hashing: The basics

## Hash Tables: Operations and Applications
- an array provides random access to any position in O(1) (constant time)
- a hash table exploits this property by hashing every key (i.e. create a number from it)
- a hash table is therefore a dictionary, i.e. it does NOT MAINTAIN ANY ORDER
- Application: Deduplication
- Application: the 2-SUM problem (from an unsorted array of n integers check if it contains two numbers x,y that sum to t)
    - a naive solution could be to just go from left to right and search y for each x --> O(n²)
    - a better solution is to sort the array first, start from the left and then perform a binary search for each x --> O(n*log n)
    - the best solution is however to use a hash table. 
        - Because the bulk of operations in the better solution is looking up y for any x, this can be done in constant time when using a hash table.

## Hash Tables: Implementation Details I
- a naîve hash table could be implemented with an array, using a lot of space and providing O(1) operations
- an alternative naîve implementation would use a linked list, using only the required space and providing O(n) operations
- to get the best of both worlds, a set of n buckets is created
- a hash function maps from a key to a position in the array
- the problem is that even for small sizes of n this hash function will produce collisions (birthday paradox)
    - solution 1 (chaining): each bucket contains a linked list of elements
        --> easy to make deletions in O(n), insertions in O(1), little space overhead
    - solution 2 (open addressing): only one object is stored in each bucket. In case of a collision the first empty bucket is searched (linear probing) or a second hash function is used to determine the offset to the next bucket to try (double hashing)
        --> hard to make deletions, no space overhead
        
## Hash Tables: Implementation Details II
- the choice of the hash function drives the performance of Hash Tables because every operation uses it
- a good hash function should therefore be fast and spread the hashes uniformly
- it's easy to design bad hash functions
- quick and dirty hash functions map objects to a number (hash code) and then this number to the bucket index (compression)
- to choose n (the number of buckets) you should follow the following ruls of thumb
    - choose a prime (especially when using modulo as compression function)
    - n should not be too close to a power to 2 or 10

# Universal Hashing

## Pathological Data Sets and Universal Hashing Motivation
- the load factor of a hash table is the average number of objects per bucket (#objects/#buckets) --> with probing the load factor does not become >1
- the load factor should not become too big. This means if the load factor hits a certain threshold, the Hash Table doubles its size.
- the problem with hash function is that for every hash function there is a pathological data set that prevents this function from spreading the values evenly
- a perfect hash function that spreads data evenly independent of the data DOES NOT EXIST
- this is a problem because it means that pathological datasets can be constructed to bring down a system
    - one solution for this is to use cryptographic hash function, for which it is very difficult to find pathological datasets
    - another solution is to use a family of hash function and choose one at random (randomization)

## Universal Hashing: Definition and Example
not viewed

## Universal Hashing: ANalysis of Chaining
not viewed

## Hash Table Performance with Open Addressing
not viewed

# Bloom Filters

## Bloom FIlters: The Basics
- Bloom Filters are a more space efficient variant of Hash Tables
    - Pro: requires much less space than Hash Tables
    - Con: 
        - can't store an associated object (Hash Set) 
        - can't delete an object
        - can make mistakes (small false positives, i.e. the Bloom Filter might say an object has been inserted when it has not)
- Application: Spell Checker (Bloom Filter contains a dictionary of valid words)
- Application: List of forbidden passwords
- Application: network routers
- A Bloom Filter uses 2 ingredients:
    - array of n bits where each entry stores n/|S| bits (S being the objects to store)
    - k hash functions, h_1, ..., h_k (k being a small constant)
- INSERT: each of the hash functions is used to hash an object x and the corresponding bit in an array A is set to 1
- LOOKUP: the object to lookup is hashed as for the insert and the corresponding bit mask is looked up in A
    --> there are no false positives, i.e. the Bloom Filter will always return True if the object was added
    --> because of collisions however it is possible that a Bloom Filter returns True even if the object was not inserted
    
## Bloom Filters: Heuristic Analysis
- the probability that a given bit in A is set to one after inserting all elements is 1 - (1 - 1/n)^k*|S|
    --> initially all bits are 0
    --> (1-1/n) is the probability that the bit remains 0 for a single element for a single hash function
    --> (1-1/n)^k is the same probability for a single element after all hash functions have been applied
    --> (1-1/n)^k*|S| is the same probability after all elements are inserted
    --> 1 - (1-1/n)^k*|S| is therefore the probability that the bit is set to 1
- the probability for a false positive is very small because a bit mask for an object that was not inserted has to match the one of an inserted object
    --> for b bits per object the error rate is <= [1-(-k/b)]^k
- for a given b k can be set to approximately (ln 2) * b
- the Error Rate is then approximately (1/2)^((ln 2)*b)