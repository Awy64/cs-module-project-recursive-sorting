# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    merged_arr = []

    if len(arrA) == 0:
      return arrB
    if len(arrB) == 0:
      return arrA
    index_left = index_right = 0
    while index_left < len(arrA) and index_right < len(arrB):
      if arrA[index_left] <= arrB[index_right]:
        merged_arr.append(arrA[index_left])
        index_left = index_left + 1
      else:
        merged_arr.append(arrB[index_right])
        index_right = index_right + 1
    merged_arr.extend(arrA[index_left:])
    merged_arr.extend(arrB[index_right:])


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:  
      m = len(arr) // 2
      l = arr[:m]
      r = arr[m:]
      left = merge_sort(l)
      right = merge_sort(r)

      arr = merge(left, right)


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

