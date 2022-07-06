


def _aux_binary_search(s,arr,min,max):
    if max < min:
        return None
    else:
        mid = (min + max) // 2
        if arr[mid] > s:
            return _aux_binary_search(s,arr,min,mid-1)
        elif arr[mid] < s:
            return _aux_binary_search(s,arr,mid+1,max)
        else:
            return mid

def binary_search_rec(s,arr):
    if len(arr) > 1:
        return _aux_binary_search(s,arr,0,len(arr)) 
    return None

def binary_search_ite(s,arr):
    min = 0
    max = len(arr)
    while min <= max:
        mid = (min + max) // 2
        if arr[mid] > s:
            max = mid - 1
        elif arr[mid] < s:
            min = mid + 1
        else:
            return mid
    return None