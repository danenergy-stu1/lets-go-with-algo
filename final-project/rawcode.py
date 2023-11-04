class SearchAndSort(object):
    def __init__(self, data):
        self.data = list(set(data))  # Remove duplicates
        self.quick_sort(self.data, 0, len(self.data) - 1)  # Sort the data

    def partition(self, arr, low, high):
        i = (low - 1)
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    def quick_sort(self, arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def binary_search(self, target):
        low = 0
        high = len(self.data) - 1

        while low <= high:
            mid = (high + low) // 2

            if self.data[mid] < target:
                low = mid + 1
            elif self.data[mid] > target:
                high = mid - 1
            else:
                return ( f'the number you are looking for is found at {mid+1}th place')  # Element found
        return -1  # Element not found
    

mission1= SearchAndSort([3,4,7,8,1,2,0,5])
print(mission1.binary_search(5))
print()

