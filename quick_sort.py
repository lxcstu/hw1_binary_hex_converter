# -*- coding: utf-8 -*-
"""Quick Sort

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14bAb8sF_92uKM81yLt1DVZNKY16IoN-4
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])

    return sorted_list

# 測試範例
arr = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
sorted_arr = merge_sort(arr)
print("排序後的數列:", sorted_arr)