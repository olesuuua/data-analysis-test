"""nums = [4, 2, 9, 0, 4, 7] → удалите первое вхождение 4, отсортируйте список по
возрастанию."""
nums = [4, 2, 9, 0, 4, 7]
nums.remove(4)
nums_sort = sorted(nums)
print(nums_sort)