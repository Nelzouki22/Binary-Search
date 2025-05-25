def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2  # إيجاد العنصر الأوسط
        if lst[mid] == target:
            return mid  # إرجاع الفهرس عند العثور على العنصر
        elif lst[mid] < target:
            left = mid + 1  # البحث في النصف الأعلى
        else:
            right = mid - 1  # البحث في النصف الأسفل
    return -1  # إذا لم يتم العثور عليه

# تجربة البحث
sorted_numbers = [10, 23, 45, 67, 89]
target = 45
result = binary_search(sorted_numbers, target)
print(f"العنصر {target} موجود عند الفهرس {result}" if result != -1 else "العنصر غير موجود")
