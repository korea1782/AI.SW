---
by. korea1782

```python
# Merge sort
# divide = O(logn)
# merge = O(n)
# O(logn) * O(n) = O(nlogn)
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0; j=0; k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
    return alist

# Quick sort 
# best case less than O(nlogn)
# worst case n^2
def quickSort(alist):
    if len(alist) <= 1:
        return alist
    pivot = alist[len(alist)//2]
    leftlist, midlist, rightlist = list(),list(), list()
    for i in alist:
        if i < pivot:
            leftlist.append(i)
        elif i == pivot:
            midlist.append(i)
        elif i > pivot:
            rightlist.append(i)
    return quickSort(leftlist) + midlist + quickSort(rightlist)
```
