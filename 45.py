def print_pairs(arr, N):
   # hash set
   hash_set = set()
    
   for i in range(0, len(arr)):
       val = N-arr[i]
       if (val in hash_set):
           print("Пара: " + str(arr[i]) + ", " + str(val))
       hash_set.add(arr[i])

arr = [1, 2, 40, 3, 9, 4]
N = 11
print_pairs(arr, N)