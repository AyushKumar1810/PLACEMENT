# QUESTION:
# Given number of pages in n different books and m students. 
# The books are arranged in ascending order of number of pages. 
# Every student is assigned to read some consecutive books. 
# The task is to assign books in such a way that the maximum number of pages 
# assigned to a student is minimum.

# Example :


# Input : pages[] = {12, 34, 67, 90}
#         m = 2
# Output : 113
# Explanation:
# There are 2 number of students. Books can be distributed 
# in following fashion : 
#   1) [12] and [34, 67, 90]
#       Max number of pages is allocated to student 
#       2 with 34 + 67 + 90 = 191 pages
#   2) [12, 34] and [67, 90]
#       Max number of pages is allocated to student
#       2 with 67 + 90 = 157 pages 
#   3) [12, 34, 67] and [90]
#       Max number of pages is allocated to student 
#       1 with 12 + 34 + 67 = 113 pages

# Of the 3 cases, Option 3 has the minimum pages = 113.

#NOTE=#Logic-Another explanation (for logic building): We need to reduce the
#  maximum books allocated so that its minimum among all the permutation.
# The logic for this is: Allocate ~maximum number of books possible to all the 
# students. - Think about it, you are trying to allocate as much books as possible 
# to each students - (which is equivalent to reducing the maximum value).
# *"Related Problems For Practice" :
# * Book Allocation Problem (GFG)
# *Aggressive cow (spoj)
# *Prata and roti (spoj)
# *EKO (spoj)
# *Google kickstart A Q-3 2020
# *Painter Partition Problem
# ""Below Leetcode Problems""=
# 1482 Minimum Number of Days to Make m Bouquets
# 1283 Find the Smallest Divisor Given a Threshold
# 1231 Divide Chocolate
# 1011 Capacity To Ship Packages In N Days
# 875 Koko Eating Bananas Minimize 
# 774 Max Distance to Gas Station
# 410 Split Array Largest Sum


def can_allocate_pages(arr, n, s, max_pages):
    """
    Check if it is possible to allocate 's' students such that each student can read a maximum of 'max_pages'.
    """
    students = 1  # Number of students allocated
    pages_read = 0  # Total pages read by all students

    for i in range(n):
        # If the current book has more pages than the maximum allowed 'max_pages', it is not possible to allocate
        # the pages evenly, so return False.
        if arr[i] > max_pages:
            return False

        # If adding the current book's pages to 'pages_read' exceeds 'max_pages', a new student is required.
        # Increment the student count and reset 'pages_read' to the current book's pages.
        if pages_read + arr[i] > max_pages:
            students += 1
            pages_read = arr[i]
        else:
            pages_read += arr[i]

        # If the number of students allocated exceeds 's', it is not possible to allocate the books, so return False.
        if students > s:
            return False

    # If all iterations are completed without any issues, it is possible to allocate the books, so return True.
    return True


def allocate_minimum_pages(arr, n, s):
    """
    Perform binary search to find the minimum number of pages each student has to read.
    """
    # If the number of books is less than the number of students, it is not possible to allocate each student at least one book.
    if n < s:
        return -1

    total_pages = sum(arr)  # Total number of pages in the book array

    # Set the lower bound 'min_pages' as the maximum value in the book array,
    # and the upper bound 'max_pages' as the total number of pages.
    min_pages = max(arr)
    max_pages = total_pages
    result = -1  # The minimum number of pages each student has to read

    # Binary search loop
    while min_pages <= max_pages:
        mid_pages = (min_pages + max_pages) // 2  # Calculate the middle value

        # Check if it is possible to allocate 's' students with a maximum of 'mid_pages' pages each.
        if can_allocate_pages(arr, n, s, mid_pages):
            # If it is possible, update the result and search for a lower value (lower 'max_pages').
            result = mid_pages
            max_pages = mid_pages - 1
        else:
            # If it is not possible, search for a higher value (higher 'min_pages').
            min_pages = mid_pages + 1

    # Return the result, which represents the minimum number of pages each student has to read.
    return result


# Main program
arr = [10, 20, 30, 40]  # Book array
n = len(arr)  # Number of books
students = 2  # Number of students

# Find the minimum pages each student has to read
minimum_pages = allocate_minimum_pages(arr, n, students)

# Print the result
if minimum_pages != -1:
    print("Minimum pages each student has to read:", minimum_pages)
else:
    print("It is not possible to allocate books to students.")




    
# another approach without giving size of array , n 
def allocate_minimum_pages(arr, s):
    if len(arr) < s:
        return -1

    total_pages = sum(arr)
    max_pages = max(arr)
    min_pages = max_pages
    result = -1

    while min_pages <= total_pages:
        mid_pages = (min_pages + total_pages) // 2

        students = 1
        pages_read = 0

        for pages in arr:
            if pages_read + pages > mid_pages:
                students += 1
                pages_read = 0

            pages_read += pages

        if students > s:
            min_pages = mid_pages + 1
        else:
            result = mid_pages
            total_pages = mid_pages - 1

    return result


# Main program
arr = [10, 20, 30, 40]
students = 2

minimum_pages = allocate_minimum_pages(arr, students)

if minimum_pages != -1:
    print("Minimum pages each student has to read:", minimum_pages)
else:
    print("It is not possible to allocate books to students.")




