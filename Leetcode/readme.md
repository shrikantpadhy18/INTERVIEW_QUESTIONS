MaxGap:Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.
<a href="https://leetcode.com/problems/maximum-gap/">PROBLEM LINK</a>
<hr>
<br>
First missing positive :Given an unsorted integer array, find the smallest missing positive integer.
<a href="https://leetcode.com/problems/first-missing-positive/">Problem Link</a>
<hr>
<br>
Longest palindromic Substring: Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

<a href="https://leetcode.com/problems/longest-palindromic-substring/">PROBLEM LINK</a>
<hr>
<br>

 Longest Substring Without Repeating Characters: Given a string, find the length of the longest substring without repeating characters.
 <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/">PROBLEM LINK</a>
<hr>
<br>

Longest Valid Parentheses :Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
<a href="https://leetcode.com/problems/longest-valid-parentheses/">PROBLEM LINK</a>

<hr>
<br>
3SUM CLOSEST : Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
<a href="https://leetcode.com/problems/3sum-closest/">problem link</a>
<hr>
<br>
Minimum Path Sum:Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
<a href="https://leetcode.com/problems/minimum-path-sum/">Problem Link</a>
<hr>
<br>
Spiral Matrix: Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
<br>
Example 1:
<br>
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
<br>
Example 2:
<br>
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
<br>
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
<a href="https://leetcode.com/problems/spiral-matrix/">PROBLEM LINK</a>
<hr>
<br>
Unique Paths :A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
<br>
How many possible unique paths are there?
Above is a 7 x 3 grid. How many possible unique paths are there?
<br>
Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
 
Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
<a href="https://leetcode.com/problems/unique-paths/">Problem Link</a>
<hr>
<br>
Unique Path2 :A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
<a href="https://leetcode.com/problems/unique-paths-ii/">Problem Link</a>
<hr>
<br>
Rotate List: Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
<br>
<a href="https://leetcode.com/problems/rotate-list/">Problem Link</a>
<hr>
<br>
Frog Jump:A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

[0,1,2,3,4,8,9,11]
Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.
<a href="https://leetcode.com/problems/frog-jump/">Problem Link</a>
<br>
<hr>

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
<a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/">PROBLEM_LINK</a>

<br>
<hr>

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
<a href="https://leetcode.com/problems/group-anagrams/"> PROBLEM_LINK/a>

<hr>
<br>
Problem:Island Perimeter


You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

<a href="https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3383/">PROBLEM_LINK</a>

<hr>
<br>
Problem:Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

<a href="https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/810/">PROBLEM_LINK</a>