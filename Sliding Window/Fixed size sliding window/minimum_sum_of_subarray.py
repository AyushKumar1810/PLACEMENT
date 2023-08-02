def slidingWindowMin():
    arr = [2, 3, 4, 6, 5, 1, 4, 2, 3]
    window_size = 3
    custom_sum = 0
    for i in range(window_size):
        custom_sum += arr[i]
    min_sum = float('inf')

    for i in range(window_size, len(arr)):
        new_sum = custom_sum - arr[i - window_size] + arr[i]
        if min_sum > new_sum:
            min_sum = new_sum
        custom_sum = new_sum

    print("Min sum:", min_sum)

slidingWindowMin()
