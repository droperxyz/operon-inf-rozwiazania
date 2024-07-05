def IsPrime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def SuperPrime(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10

    return IsPrime(sum)


def BSuperPrime(number):
    binary = ""
    sum_of_bin = 0

    while number > 0:
        binary += str(number % 2)
        number //= 2

    binary = int(binary[::-1])

    while binary > 0:
        sum_of_bin += binary % 10
        binary //= 10

    return IsPrime(sum_of_bin)


def Partitioning(nums, left, right):
    limit = left
    pivot = nums[right]

    for i in range(left, right):
        if nums[i] < pivot:
            nums[i], nums[limit] = nums[limit], nums[i]
            limit += 1

    nums[limit], nums[right] = nums[right], nums[limit]

    return limit


def QuickSort(nums, left, right):
    if left < right:
        sorted = Partitioning(nums, left, right)
        QuickSort(nums, left, sorted - 1)
        QuickSort(nums, sorted + 1, right)


file = open('liczby15.txt', 'r')
counter = 0
nums = []

for line in file:
    line = int(line.strip())

    if IsPrime(line) and SuperPrime(line) and BSuperPrime(line):
        nums.append(line)

QuickSort(nums, 0, len(nums) - 1)
print(*nums)

file.close()
