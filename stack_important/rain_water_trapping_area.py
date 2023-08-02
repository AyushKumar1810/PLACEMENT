def rain_water_tapping(arr):
    maxL = [0] * len(arr)
    maxL[0] = arr[0]
    for i in range(1, len(arr)):
        maxL[i] = max(maxL[i-1], arr[i])
    
    maxR = [0] * len(arr)
    maxR[len(arr)-1] = arr[len(arr)-1]
    for i in range(len(arr)-2, -1, -1):
        maxR[i] = max(maxR[i+1], arr[i])
    
    total_water = 0
    for i in range(len(arr)):
        total_water += min(maxL[i], maxR[i]) - arr[i]
    
    return total_water


# Example usage
input_arr = [3, 0, 1, 2, 0, 4]
output = rain_water_tapping(input_arr)
print("Trapped rainwater:", output)
