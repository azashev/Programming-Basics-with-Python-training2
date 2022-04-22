def palindrome(nums):
    for i in nums:
        if i == i[::-1]:
            print(True)
        else:
            print(False)


list_numbers = input().split(', ')

palindrome(list_numbers)
