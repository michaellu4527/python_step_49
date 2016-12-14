def bubbleSort(list1):
    for num in range(0, len(list1)-1):  # Loop through length of list
        for i in range(0, len(list1)-1-num):  # If something has been sorted, we don't need                                              to iterate through that anymore, so                                                      subtract that number of elements (i)
            if list1[i]>list1[i+1]:      # Comparing 2 adjacent values
                temp = list1[i]         # Saving the value so it doesn't get overwrittten
                list1[i] = list1[i+1]   # Start swap
                list1[i+1] = temp       # Finish swap

    return list1