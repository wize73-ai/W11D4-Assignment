# W11D4-Assignment

Solving the Activity Selection Problem

 

Objective:

Reinforce your understanding of greedy algorithms by solving the Activity Selection problem and documenting your solution approach.

 

Problem Statement:

https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problemLinks to an external site.

https://www.hackerrank.com/challenges/marcs-cakewalk/problemLinks to an external site.

 

Steps to Complete the Exercise:

Understand the Problem:
   - Carefully read the problem statement.

The absolute difference is the positive difference between two values a and b, is written |(a-b)| or |(b-a)| and they are equal. If a=3 and b=2,result is 1 |3-2| = |2-3|. Given an array of integers, find the minimum absolute difference between any two elements in the array.

Example. arr=[-2,2,4]


There are 3 pairs of numbers: (-2,2)=4,(-2,4)=6 and (2,4)=2. The minimum absolute difference is 2.

Function Description

Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that represents the minimum absolute difference between any pair of elements.

minimumAbsoluteDifference has the following parameter(s):

int arr[n]: an array of integers
Returns

int: the minimum absolute difference found
Input Format

The first line contains a single integer n, the size of arr.
The second line contains  space-separated integers, .

   - Identify the inputs and expected output.

   10
-59 -36 -13 1 -53 -92 -2 -96 -54 75
returns 1

5
1 -3 71 68 17
returns 3


Constraints

2<=n<=10**5
-10**9<=arr[i]<=10**9

   - Note any constraints or assumptions.

Plan Your Approach:

   - Consider how a greedy algorithm can be applied to solve the problem.

greedy algorithms naturally brute force every permutation of a problem, making it a natural approach to solving this type of problem.

   - Determine the greedy choice property for selecting activities.

itertools reduce : It operates in-place, without the need for additional data structures, which can be memory-efficient, It can be quite efficient for small arrays.

was unable to use the max pernutation approach to solve all cases, switched to a more linear logic, sort, then compare elements, no permutations are necessary, as the sorted list allows us to inspect the delta between elements, since it is sorted the minimum distance will occure between adhjacent elements, negating the need for a permutation table apllroach.

this method returns a O(n log n) for the sort activity, the rest is negligible, n, or 1

   - Outline your solution before coding.

Write the Code:
   - Use your preferred programming language.

   - Implement your greedy algorithm solution.

   - Use meaningful variable names and comments to explain your code.

Test Your Solution:
   - Create test cases with various activity sets.

   - Ensure your solution produces the correct output for each test case.

   - Consider edge cases and handle them appropriately.

Document Your Solution:
   - Create a documentation file in PDF or Markdown format.

   - Explain your code design choices and the greedy approach used.

How Many Permutations Can Be Generated?
The number of permutations that can be generated from a set of elements depends on the size of the set/array. In combinatorics, the formula for calculating the number of permutations of a set of “n” distinct elements taken “r” at a time is given by:

P(n, r) = \frac{n!}{(n - r)!}  

Where:

P(n,r) represents the number of permutations.
n is the total number of distinct elements.
r is the number of elements taken at a time.
n! (read as “n factorial”) represents the product of all positive integers from 1 to n.

The iterative algorithm for generating permutations efficiently arranges array elements in a systematic order, avoiding the complexities of backtracking. It consistently creates the next lexicographically greater permutation and ensures complete coverage without needing to backtrack, making it a straightforward and efficient approach to generating all possible permutations.

define reduce function (function, iterable)
set up answers array
define function absolute difference(a,b)

set up a loop with iteration to decay length of array
in loop:
pass array to reduce with logic to compare subtraction of two elements in the array, storing the respones as a list of repsonses (answers)
remove the first element of array and return to top

answers = []

def reduce(function, iterable):
    it = iter(iterable)
    for element in it:
        value = function(value, element)
    answers += value

def abs_diff(x, y):
    result = abs(x-y)
    return result

for i in range(n-1):
    reduce(abs_diff(arr[0],arr[i]), arr, float(inf)):
    print(f'popping arr[0] {arr[0]}')
    arr.pop(arr[0])


return min(answers)



Algorithm:
To generate all the permutations of an array from index l to r, fix an element at index l and recur for the index l+1 to r.
Backtrack and fix another element at index l and recur for index l+1 to r.
Repeat the above steps to generate all the permutations.

   - Describe how you identified the greedy choice property.

   - Analyze the time and space complexity of your solution.

Submit Your Solution:
   - Ensure your solution passes the HackerRank submission.

   - Submit your documentation and HackerRank solution via HackerRank.


______________________________Brute Force Attempt 1 _______________________________________________

input = sys.stdin.read
arr = input().split()
n = int(data[0])
answers = []

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            value = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

def abs_diff(x, y):
    return abs(x - y)

def find_min_abs_diff(arr):
    answers = []
    n = len(arr)
    
def minimumAbsoluteDifference(arr):
    comparitor = arr[0]
    # print("first step comparitor = ", comparitor)
    x = 0
    first_length = n -1
    for x in range(first_length):
        z = len(arr)-1
        for i in range(z):
            # print("we are here ", i, "looking at: ", arr[0], " compare to ", arr[i+1], "answer ", abs(arr[0]-arr[i+1]))
            # print("i ", arr[x], "comp:", (arr[x+i]))
            answers.append(abs(arr[0] - arr[i+1]))
            # arr = arr[1:]
            comparitor = arr[0]
            x +=1
        arr = arr[1:]
    return (min(answers))      
    
Caused too many sytex and compile errors, started using print statements to debug logic and flow, isolated process below, 



    for i in range(n-1):
        min_diff = reduce(abs_diff, arr)
        answers.append(min_diff)
        print(f'popping arr[0] {arr[0]}')
        arr.pop(0)

    return min(answers) if answers else float('inf')

would not iterate properly   scrapped

for i in range(n-1):
    comparitor = arr[0]
    for x in range(len(arr[1:]-1)):
        answers.append(abs(comparitor - x))
    arr = arr[1:]
    print answers

    played with this logic .... sintered to 


def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])
        if diff < min_diff:
            min_diff = diff
    return min_diff


    My original approach, that did not satisfy all test cases was brute force using nested loops resulting in a partial answer fater an impact of O(n**2), by sorting the array you only need to use a sliding window to check the difference between the sorted elements, and returning the smallest delta.



   sources :

   https://www.geeksforgeeks.org/different-ways-to-generate-permutations-of-an-array/

def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])
        if diff < min_diff:
            min_diff = diff
    return min_diff