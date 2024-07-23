Dynamic programming (DP) is a powerful algorithmic technique used to solve problems by breaking them down into simpler subproblems and storing the results of these subproblems to avoid redundant calculations. This approach is particularly useful for optimization problems, where the goal is to find the best solution among many possible ones.

### Key Concepts in Dynamic Programming

1. **Optimal Substructure**: A problem exhibits optimal substructure if an optimal solution to the problem can be constructed from optimal solutions of its subproblems. This property is essential for applying dynamic programming.

2. **Overlapping Subproblems**: A problem has overlapping subproblems if the same subproblems are solved multiple times. Dynamic programming solves each subproblem once and stores the results in a table (often an array or a matrix) to avoid redundant work.

### Steps to Solve a Problem Using Dynamic Programming

1. **Characterize the Structure of an Optimal Solution**: Identify how the solution to the problem can be constructed from solutions to smaller subproblems.

2. **Define the Recursive Solution**: Write the problem in a recursive form, breaking it down into subproblems.

3. **Compute the Value of the Optimal Solution Bottom-Up**: Solve the subproblems in a bottom-up manner, starting with the smallest subproblems and combining their solutions to solve larger subproblems.

4. **Construct the Optimal Solution (if needed)**: If the actual solution needs to be constructed, keep track of the decisions made to build the solution.

### Common Examples of Dynamic Programming Problems

1. **Fibonacci Sequence**: The Fibonacci sequence is a classic example of a problem that can be solved efficiently using dynamic programming by storing the results of previously computed Fibonacci numbers.

2. **Knapsack Problem**: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

3. **Longest Common Subsequence (LCS)**: Given two sequences, find the length of their longest common subsequence.

4. **Edit Distance**: Given two strings, find the minimum number of operations required to convert one string into the other.

### Example: Fibonacci Sequence

Here’s a simple example using dynamic programming to compute the nth Fibonacci number.

#### Recursive Solution
```python
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)
```

#### Dynamic Programming Solution
```python
def fib_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

The dynamic programming solution is much more efficient than the naive recursive solution because it avoids redundant calculations by storing intermediate results.

Dynamic programming can be applied in various fields such as computer science, operations research, economics, and bioinformatics, making it a versatile and essential tool for solving complex problems.

Dynamic programming can be implemented in two main ways: **bottom-up** and **top-down**. Both approaches have their own advantages and are used based on the specific problem and its constraints.

### Bottom-Up Approach

The bottom-up approach, also known as the iterative approach, involves solving smaller subproblems first and using their solutions to build up to the solution of the larger problem. This approach typically uses tabulation to store the results of subproblems in a table (often an array or matrix), which is then used to solve the larger problem.

#### Example: Fibonacci Sequence (Bottom-Up)
```python
def fib_bottom_up(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

In this example, we start by solving the smallest subproblems (`fib(0)` and `fib(1)`) and use their solutions to solve larger subproblems up to `fib(n)`.

### Top-Down Approach

The top-down approach, also known as the memoization approach, involves solving the problem by breaking it down into subproblems recursively. The results of subproblems are stored in a cache (often a dictionary or array) to avoid redundant calculations. This approach uses recursion with memoization to store and reuse the results of previously solved subproblems.

#### Example: Fibonacci Sequence (Top-Down)
```python
def fib_top_down(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_top_down(n - 1, memo) + fib_top_down(n - 2, memo)
    return memo[n]
```

In this example, we start by trying to solve the original problem (`fib(n)`) and break it down into smaller subproblems (`fib(n-1)` and `fib(n-2)`). We store the results of these subproblems in a memoization table to avoid redundant calculations.

### Comparison

- **Memory Usage**: The bottom-up approach usually requires more memory to store the table of subproblems, while the top-down approach with memoization can use less memory since it only stores the results of the subproblems that are actually needed.
- **Initialization**: The bottom-up approach requires initializing the entire table before solving the problem, whereas the top-down approach initializes the memoization table on-the-fly.
- **Recursion vs. Iteration**: The top-down approach uses recursion, which can lead to a deep call stack and possible stack overflow for very large problems. The bottom-up approach uses iteration, which avoids this issue.
- **Ease of Implementation**: The top-down approach can be easier to implement initially, especially for problems that naturally fit a recursive structure. The bottom-up approach can be more intuitive for understanding the progression of subproblems from the smallest to the largest.

### When to Use Each Approach

- **Top-Down**: Use this approach when the problem has a natural recursive structure and the number of subproblems is not too large, so that memoization can effectively reduce redundant calculations.
- **Bottom-Up**: Use this approach when the problem involves many overlapping subproblems and you want to avoid the overhead of recursion, especially if the recursion depth could be large.

By understanding both approaches, you can choose the one that best fits the problem at hand and the constraints you are working with.

Converting a recursive solution to a dynamic programming solution involves transforming the recursive calls into an iterative process that uses a table to store intermediate results. This conversion can be approached in two main ways: top-down with memoization and bottom-up with tabulation.

Here is a step-by-step guide to converting a recursive solution into a dynamic programming solution:

### Steps to Convert Recursive Code to Dynamic Programming

1. **Identify the Subproblems**:
   Determine what subproblems are being solved recursively and how they overlap.

2. **Define the Recurrence Relation**:
   Express the solution to the problem in terms of solutions to smaller subproblems.

3. **Choose the DP Approach**:
   Decide whether to use a top-down (memoization) or bottom-up (tabulation) approach.

4. **Create a Storage Structure**:
   Allocate a table (array or matrix) to store the results of subproblems.

5. **Iterate and Fill the Table**:
   Fill the table iteratively in the bottom-up approach or recursively in the top-down approach with memoization.

6. **Extract the Final Solution**:
   Retrieve the solution to the original problem from the table.

### Example: Converting Recursive Fibonacci to DP

#### Recursive Solution
```python
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)
```

#### Top-Down with Memoization
1. **Identify Subproblems**: `fib(n)` depends on `fib(n-1)` and `fib(n-2)`.
2. **Recurrence Relation**: `fib(n) = fib(n-1) + fib(n-2)`.

```python
def fib_top_down(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_top_down(n - 1, memo) + fib_top_down(n - 2, memo)
    return memo[n]
```

#### Bottom-Up with Tabulation
1. **Identify Subproblems**: Same as above.
2. **Recurrence Relation**: Same as above.
3. **Create Storage Structure**: Allocate an array to store Fibonacci numbers up to `n`.

```python
def fib_bottom_up(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```
## Climbing Stairs Problem with Dynamic Programming

In this article, we'll discuss how to solve the "Climbing Stairs" problem using dynamic programming. This problem is a classic example of how dynamic programming can be used to count the number of ways to achieve a goal, specifically when the number of ways to reach a particular state depends on previously computed states.

### Problem Statement

Given a number of stairs `n`, starting from the 0th stair, we need to climb to the `N`th stair. At any time, we can climb either one or two steps. We need to return the total number of distinct ways to reach the `N`th stair.

### Identifying a Dynamic Programming Problem

We can identify this as a dynamic programming problem because:

1. **Count the total number of ways**: The problem asks us to count the number of distinct ways to reach the Nth stair.
2. **Overlapping subproblems**: To reach a stair, we can come from either the previous stair or the one before it, which involves recalculating some results multiple times.

### Steps to Solve the Problem

1. **Represent the problem in terms of indexes**: Consider `n` stairs as indexes from 0 to N.
2. **Possible choices at each index**: At each stair, you can either take one step or two steps.
3. **Return the sum of all choices**: Since the problem asks to count all the ways, we'll sum up the possible ways to reach each stair.

### Recursive Solution

We'll start with a recursive solution that will later help us understand the transition to a dynamic programming solution.

#### Recursive Function

```python
def count_ways_recursive(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return count_ways_recursive(n - 1) + count_ways_recursive(n - 2)
```

### Top-Down Approach with Memoization

In the top-down approach, we use memoization to store the results of subproblems to avoid redundant calculations.

```python
def count_ways_top_down(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    if n == 1:
        return 1
    memo[n] = count_ways_top_down(n - 1, memo) + count_ways_top_down(n - 2, memo)
    return memo[n]

# Example usage:
n = 3
print(count_ways_top_down(n))  # Output: 3
```

### Bottom-Up Approach with Tabulation

In the bottom-up approach, we use a table (array) to store the results of subproblems iteratively.

```python
def count_ways_bottom_up(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Example usage:
n = 3
print(count_ways_bottom_up(n))  # Output: 3
```

### Space Optimization

We observe that to compute `dp[i]`, we only need the last two values `dp[i-1]` and `dp[i-2]`. Therefore, we can optimize space by using two variables instead of an array.

```python
def count_ways_optimized(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    prev2 = 1
    prev = 1
    for i in range(2, n + 1):
        current = prev + prev2
        prev2 = prev
        prev = current
    return current

# Example usage:
n = 3
print(count_ways_optimized(n))  # Output: 3
```

### Time and Space Complexity

- **Time Complexity**: O(N) for all approaches, as we are iterating through the stairs once.
- **Space Complexity**:
  - Top-Down with Memoization: O(N) for the memoization table.
  - Bottom-Up with Tabulation: O(N) for the dp array.
  - Space Optimized: O(1), using constant space.

By understanding these approaches, you can efficiently solve the climbing stairs problem using dynamic programming techniques.
 
Certainly! The "Frog Jump" problem is a classic dynamic programming problem where a frog can jump from the \(i\)th stone to the \((i+1)\)th stone or \((i+2)\)th stone, and we need to find the minimum cost to reach the last stone. The problem can be defined as follows:

### Problem Definition:
Given an array `height` of length \(n\) where `height[i]` represents the height of the \(i\)th stone, the frog can jump from stone \(i\) to stone \(i+1\) or stone \(i+2\). The cost of a jump is the absolute difference in heights between the stones. Find the minimum cost to reach the last stone starting from the first stone.

### Approach:
We can solve this problem using dynamic programming. We define `dp[i]` as the minimum cost to reach the \(i\)th stone. The recurrence relation will be:

- If the frog jumps from \(i\) to \(i+1\): `dp[i+1] = dp[i] + abs(height[i+1] - height[i])`
- If the frog jumps from \(i\) to \(i+2\): `dp[i+2] = dp[i] + abs(height[i+2] - height[i])`

We need to initialize `dp[0] = 0` because there is no cost to start at the first stone.

### Implementation in Python:

```python
class Solution:
    def frogJump(self, height):
        n = len(height)
        if n == 0:
            return 0
        if n == 1:
            return 0

        dp = [0] * n
        dp[0] = 0
        dp[1] = abs(height[1] - height[0])

        for i in range(2, n):
            jump_one = dp[i-1] + abs(height[i] - height[i-1])
            jump_two = dp[i-2] + abs(height[i] - height[i-2])
            dp[i] = min(jump_one, jump_two)

        return dp[-1]

# Example usage:
height = [10, 30, 40, 20]
solution = Solution()
print(solution.frogJump(height))  # Expected output: 30
```

### Explanation of the Code:

1. **Initialization**:
   - `dp[0] = 0`: No cost to stand on the first stone.
   - `dp[1] = abs(height[1] - height[0])`: Cost to jump from the first stone to the second stone.

2. **Iterate through the array starting from the third stone**:
   - For each stone \(i\), calculate the cost to jump from the \((i-1)\)th stone and from the \((i-2)\)th stone.
   - The minimum of these two values will be the cost to reach the \(i\)th stone.

3. **Return the value at the last stone**:
   - `dp[-1]` gives the minimum cost to reach the last stone.

This dynamic programming approach ensures that we efficiently calculate the minimum cost in \(O(n)\) time with \(O(n)\) space complexity.

Sure, let's consider a more general version of the Frog Jump problem where the frog can jump up to \(K\) stones ahead.

### Problem Definition:
Given an array `height` of length \(n\) where `height[i]` represents the height of the \(i\)th stone, and an integer \(K\) representing the maximum distance the frog can jump, find the minimum cost to reach the last stone starting from the first stone. The cost of a jump is the absolute difference in heights between the stones.

### Approach:
We can use dynamic programming to solve this problem. We define `dp[i]` as the minimum cost to reach the \(i\)th stone. The recurrence relation will be:

\[ \text{dp}[i] = \min(\text{dp}[j] + \left| \text{height}[i] - \text{height}[j] \right|) \]
for all \(j\) where \( \max(0, i-K) \leq j < i \).

### Implementation in Python:

```python
class Solution:
    def frogJump(self, height, K):
        n = len(height)
        if n == 0:
            return 0
        if n == 1:
            return 0
        
        dp = [float('inf')] * n
        dp[0] = 0
        
        for i in range(1, n):
            for j in range(1, K+1):
                if i - j >= 0:
                    dp[i] = min(dp[i], dp[i-j] + abs(height[i] - height[i-j]))
        
        return dp[-1]

# Example usage:
height = [10, 30, 40, 20]
K = 2
solution = Solution()
print(solution.frogJump(height, K))  # Expected output: 30
```

### Explanation of the Code:

1. **Initialization**:
   - `dp` array is initialized to `float('inf')` except for `dp[0]`, which is `0` because there is no cost to stand on the first stone.

2. **Iterate through each stone**:
   - For each stone \(i\) (starting from the second stone), check all possible jumps \(j\) (from 1 to \(K\)) that lead to stone \(i\).
   - Update `dp[i]` with the minimum cost found by considering jumps from any valid stone \(i-j\).

3. **Return the value at the last stone**:
   - `dp[-1]` gives the minimum cost to reach the last stone.

This approach ensures that we efficiently calculate the minimum cost to reach the last stone while considering up to \(K\) possible jumps for each stone. The time complexity is \(O(nK)\) and the space complexity is \(O(n)\).

Sure, let's break down the for loop in the dynamic programming solution for the frog jump problem with \(K\) distance in detail.

### For Loop Explanation:

Here is the relevant part of the code:

```python
for i in range(1, n):
    for j in range(1, K+1):
        if i - j >= 0:
            dp[i] = min(dp[i], dp[i-j] + abs(height[i] - height[i-j]))
```

### Outer Loop: `for i in range(1, n)`

This loop iterates over each stone starting from the second stone (index 1) to the last stone (index \(n-1\)).

- **Purpose**: To compute the minimum cost to reach each stone \(i\) from the starting stone.
- **Range**: `i` goes from 1 to \(n-1\).

### Inner Loop: `for j in range(1, K+1)`

This loop iterates over the possible jumps the frog can make to reach the current stone \(i\).

- **Purpose**: To consider each possible jump distance \(j\) from stone \(i-j\) to stone \(i\), and update the minimum cost to reach stone \(i\).
- **Range**: `j` goes from 1 to \(K\).

### Condition: `if i - j >= 0`

This condition checks if the jump \(j\) from the current stone \(i\) is valid (i.e., it doesn't jump to a negative index).

- **Purpose**: To ensure that the frog does not jump to an invalid (negative) index.
- **Check**: `i - j` must be greater than or equal to 0.

### Update Statement: `dp[i] = min(dp[i], dp[i-j] + abs(height[i] - height[i-j]))`

This line updates the minimum cost to reach stone \(i\).

- **`dp[i]`**: The current minimum cost to reach stone \(i\).
- **`dp[i-j]`**: The minimum cost to reach the stone \(i-j\).
- **`abs(height[i] - height[i-j])`**: The cost to jump from stone \(i-j\) to stone \(i\) (absolute difference in their heights).
- **`min(dp[i], dp[i-j] + abs(height[i] - height[i-j]))`**: We update `dp[i]` to the minimum value between the current `dp[i]` and the cost to jump from `i-j` to `i`.

### Step-by-Step Execution with Example:

Let's go through an example with `height = [10, 30, 40, 20]` and \(K = 2\).

1. **Initialization**:
   ```python
   dp = [0, inf, inf, inf]
   ```

2. **First Iteration (i = 1)**:
   - **Inner Loop (j = 1)**:
     - Check if `1 - 1 >= 0` (true).
     - Update `dp[1] = min(dp[1], dp[0] + abs(30 - 10)) = min(inf, 0 + 20) = 20`.
   - **Inner Loop (j = 2)**: (skipped, as `1 - 2 < 0`)
   - Result after first iteration:
     ```python
     dp = [0, 20, inf, inf]
     ```

3. **Second Iteration (i = 2)**:
   - **Inner Loop (j = 1)**:
     - Check if `2 - 1 >= 0` (true).
     - Update `dp[2] = min(dp[2], dp[1] + abs(40 - 30)) = min(inf, 20 + 10) = 30`.
   - **Inner Loop (j = 2)**:
     - Check if `2 - 2 >= 0` (true).
     - Update `dp[2] = min(dp[2], dp[0] + abs(40 - 10)) = min(30, 0 + 30) = 30`.
   - Result after second iteration:
     ```python
     dp = [0, 20, 30, inf]
     ```

4. **Third Iteration (i = 3)**:
   - **Inner Loop (j = 1)**:
     - Check if `3 - 1 >= 0` (true).
     - Update `dp[3] = min(dp[3], dp[2] + abs(20 - 40)) = min(inf, 30 + 20) = 50`.
   - **Inner Loop (j = 2)**:
     - Check if `3 - 2 >= 0` (true).
     - Update `dp[3] = min(dp[3], dp[1] + abs(20 - 30)) = min(50, 20 + 10) = 30`.
   - Result after third iteration:
     ```python
     dp = [0, 20, 30, 30]
     ```

### Final Result:

The value at `dp[n-1]` (i.e., `dp[3]`) gives the minimum cost to reach the last stone, which is `30`.

Let's use the Frog Jump problem approach with the given array `height = [10, 20, 30, 10, 60, 70]` and assume \( K = 2 \), which means the frog can jump up to 2 stones ahead. We will use dynamic programming to determine the minimum cost to reach the last stone.

### Approach:
1. **Initialization**:
   - `dp[i]` will store the minimum cost to reach stone \(i\).

2. **Recurrence Relation**:
   - For each stone \(i\), the frog can jump from any of the last \(K\) stones: \(i-1\), \(i-2\), etc.
   - Update `dp[i]` as follows:
     \[
     dp[i] = \min(dp[i-j] + \left| \text{height}[i] - \text{height}[i-j] \right|) \text{ for } j = 1 \text{ to } K \text{ if } i-j \geq 0
     \]

3. **Base Case**:
   - `dp[0] = 0` (no cost to stand on the first stone).

### Step-by-Step Execution:

1. **Initialize the `dp` Array**:
   ```python
   height = [10, 20, 30, 10, 60, 70]
   K = 2
   n = len(height)
   dp = [float('inf')] * n
   dp[0] = 0
   ```

2. **Iterate through Each Stone**:
   - **For i = 1**:
     - **Inner Loop (j = 1)**:
       - Update `dp[1] = min(dp[1], dp[0] + abs(20 - 10)) = min(inf, 0 + 10) = 10`
     - Result after processing stone 1:
       ```python
       dp = [0, 10, inf, inf, inf, inf]
       ```

   - **For i = 2**:
     - **Inner Loop (j = 1)**:
       - Update `dp[2] = min(dp[2], dp[1] + abs(30 - 20)) = min(inf, 10 + 10) = 20`
     - **Inner Loop (j = 2)**:
       - Update `dp[2] = min(dp[2], dp[0] + abs(30 - 10)) = min(20, 0 + 20) = 20`
     - Result after processing stone 2:
       ```python
       dp = [0, 10, 20, inf, inf, inf]
       ```

   - **For i = 3**:
     - **Inner Loop (j = 1)**:
       - Update `dp[3] = min(dp[3], dp[2] + abs(10 - 30)) = min(inf, 20 + 20) = 40`
     - **Inner Loop (j = 2)**:
       - Update `dp[3] = min(dp[3], dp[1] + abs(10 - 20)) = min(40, 10 + 10) = 20`
     - Result after processing stone 3:
       ```python
       dp = [0, 10, 20, 20, inf, inf]
       ```

   - **For i = 4**:
     - **Inner Loop (j = 1)**:
       - Update `dp[4] = min(dp[4], dp[3] + abs(60 - 10)) = min(inf, 20 + 50) = 70`
     - **Inner Loop (j = 2)**:
       - Update `dp[4] = min(dp[4], dp[2] + abs(60 - 30)) = min(70, 20 + 30) = 50`
     - Result after processing stone 4:
       ```python
       dp = [0, 10, 20, 20, 50, inf]
       ```

   - **For i = 5**:
     - **Inner Loop (j = 1)**:
       - Update `dp[5] = min(dp[5], dp[4] + abs(70 - 60)) = min(inf, 50 + 10) = 60`
     - **Inner Loop (j = 2)**:
       - Update `dp[5] = min(dp[5], dp[3] + abs(70 - 10)) = min(60, 20 + 60) = 60`
     - Result after processing stone 5:
       ```python
       dp = [0, 10, 20, 20, 50, 60]
       ```

### Final Result:

The minimum cost to reach the last stone (stone 5) is stored in `dp[5]`, which is `60`.

### Final Python Code:

Here's the complete code implementing this approach:

```python
class Solution:
    def frogJump(self, height, K):
        n = len(height)
        if n == 0:
            return 0
        if n == 1:
            return 0
        
        dp = [float('inf')] * n
        dp[0] = 0
        
        for i in range(1, n):
            for j in range(1, K+1):
                if i - j >= 0:
                    dp[i] = min(dp[i], dp[i-j] + abs(height[i] - height[i-j]))
        
        return dp[-1]

# Example usage:
height = [10, 20, 30, 10, 60, 70]
K = 2
solution = Solution()
print(solution.frogJump(height, K))  # Expected output: 60
```

### Explanation:
- The `dp` array is updated iteratively based on the costs of jumps from valid previous stones.
- The final result in `dp[n-1]` gives the minimum cost to reach the last stone, which, in this example, is `60`.

Sure, let's delve into the problem of finding the maximum sum of non-adjacent elements in an array step by step.

### Problem Statement:
Given an array of integers, find the maximum sum of its elements such that no two elements considered for the sum are adjacent in the array.

### Example:
Consider the array `arr = [3, 2, 7, 10]`.

- If you choose 3, you cannot choose 2.
- If you choose 2, you can choose 7 and 10 (but not 3).
- If you choose 7, you cannot choose 2 and 10.
- If you choose 10, you cannot choose 7.

The goal is to maximize the sum under these constraints.

### Approach:
We can use dynamic programming to solve this problem efficiently.

### Dynamic Programming Solution:
1. **Define the State:**
   - Let `dp[i]` be the maximum sum we can achieve considering the first \(i\) elements of the array without selecting two adjacent elements.

2. **Base Cases:**
   - `dp[0]` = `arr[0]` (If there is only one element, the maximum sum is the element itself).
   - `dp[1]` = `max(arr[0], arr[1])` (For the first two elements, the maximum sum is the maximum of the two elements since we can't pick both).

3. **Recurrence Relation:**
   - For each element \(i\) from 2 to \(n-1\):
     - We have two options: either include `arr[i]` in our sum or exclude it.
     - If we include `arr[i]`, then the previous element `arr[i-1]` cannot be included, so we add `arr[i]` to `dp[i-2]`.
     - If we exclude `arr[i]`, then the sum is just `dp[i-1]`.
     - Thus, the relation is: `dp[i] = max(dp[i-1], arr[i] + dp[i-2])`.

4. **Final Result:**
   - The value `dp[n-1]` will give the maximum sum of non-adjacent elements.

### Implementation in Python:
Here’s how we can implement this approach:

```python
def max_sum_non_adjacent(arr):
    n = len(arr)
    
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    
    # Initialize dp array
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    
    # Fill dp array using the recurrence relation
    for i in range(2, n):
        dp[i] = max(dp[i-1], arr[i] + dp[i-2])
    
    # The last element of dp array contains the result
    return dp[-1]

# Example usage
arr = [3, 2, 7, 10]
print(max_sum_non_adjacent(arr))  # Output: 13 (3 + 10)
```

### Explanation:
1. **Initialization:**
   - `dp[0] = arr[0]` because the maximum sum considering only the first element is the element itself.
   - `dp[1] = max(arr[0], arr[1])` because with two elements, the maximum sum is the greater of the two (since we cannot pick both).

2. **Filling the DP Table:**
   - For each element from index 2 to \(n-1\), we decide whether to include the current element in the sum.
   - If we include `arr[i]`, we add its value to the maximum sum up to `arr[i-2]` (because we skip `arr[i-1]`).
   - If we exclude `arr[i]`, the maximum sum up to `arr[i]` is the same as the maximum sum up to `arr[i-1]`.

3. **Result:**
   - The result is found in `dp[n-1]`, which represents the maximum sum of non-adjacent elements in the array.

This dynamic programming approach ensures we find the optimal solution in \(O(n)\) time with \(O(n)\) space complexity.

Sure! Here is the problem statement for the House Robber problem:

### House Robber Problem Statement:

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. The only constraint stopping you from robbing each of them is that adjacent houses have security systems connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

### Example:

**Example 1:**
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```

**Example 2:**
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
```

### Constraints:
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

### Approach:

To solve this problem, we can use dynamic programming. The idea is to keep track of the maximum amount of money that can be robbed up to each house, without robbing two adjacent houses. Here's the plan:

1. **Define State:**
   - Let `dp[i]` be the maximum amount of money that can be robbed from the first \(i+1\) houses.

2. **Recurrence Relation:**
   - For each house \(i\), you have two options:
     - Do not rob the current house \(i\), then `dp[i] = dp[i-1]`.
     - Rob the current house \(i\), then add the value of the current house to the maximum amount that can be robbed up to the house \(i-2\), i.e., `dp[i] = nums[i] + dp[i-2]`.
   - Combine these two options: `dp[i] = max(dp[i-1], nums[i] + dp[i-2])`.

3. **Base Cases:**
   - `dp[0] = nums[0]`: If there's only one house, rob it.
   - `dp[1] = max(nums[0], nums[1])`: For the first two houses, rob the one with the most money.

4. **Final Result:**
   - The value `dp[n-1]` will give the maximum amount of money that can be robbed from all the houses.

The solution can be implemented in Python as follows:

```python
def rob(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    
    # Initialize dp array
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    # Fill dp array using the recurrence relation
    for i in range(2, n):
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])
    
    # The last element of dp array contains the result
    return dp[-1]

# Example usage
nums1 = [1, 2, 3, 1]
print(rob(nums1))  # Output: 4

nums2 = [2, 7, 9, 3, 1]
print(rob(nums2))  # Output: 12
```

This dynamic programming approach ensures that the optimal solution is found in \(O(n)\) time complexity with \(O(n)\) space complexity.

To solve the problem of counting the number of unique paths in a grid from the top-left corner to the bottom-right corner, where you can only move either down or right at any point in time, we can use dynamic programming.

### Problem Recap
You are given a grid with `m` rows and `n` columns. You start at the top-left corner (cell `(0, 0)`) and you want to reach the bottom-right corner (cell `(m-1, n-1)`). You can only move down or right at any point in time. Your task is to find out how many unique paths there are from the start to the destination.

### Solution Explanation
We will use a 2D array `dp` where `dp[i][j]` represents the number of unique paths to reach cell `(i, j)` from the starting cell `(0, 0)`.

### Steps:

1. **Initialization:**
   - `dp[0][0] = 1` because there is exactly one way to be at the start cell (doing nothing).
   - For the first row, `dp[0][j] = 1` for all `j` because the only way to move in the first row is by moving right.
   - For the first column, `dp[i][0] = 1` for all `i` because the only way to move in the first column is by moving down.

2. **Filling the DP Table:**
   - For each cell `(i, j)`, the number of ways to get there is the sum of the number of ways to get to the cell directly above it `(i-1, j)` and the number of ways to get to the cell directly to the left of it `(i, j-1)`.
   - Therefore, `dp[i][j] = dp[i-1][j] + dp[i][j-1]`.

3. **Result:**
   - The value at `dp[m-1][n-1]` will be our answer, i.e., the number of unique paths to reach the bottom-right corner.

Here's the Python implementation:

```python
def unique_paths(m, n):
    # Create a 2D DP array initialized to 0
    dp = [[0] * n for _ in range(m)]

    # Initialize the first row and first column
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    # Fill the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]

# Example usage:
m, n = 3, 7
print(unique_paths(m, n))  # Output: 28
```

### Example

Let's go through a small example:

#### Input
- `m = 3`
- `n = 3`

#### Initialization
```
1 1 1
1 0 0
1 0 0
```

#### Filling the DP Table
- For cell `(1, 1)`: `dp[1][1] = dp[0][1] + dp[1][0] = 1 + 1 = 2`
- For cell `(1, 2)`: `dp[1][2] = dp[0][2] + dp[1][1] = 1 + 2 = 3`
- For cell `(2, 1)`: `dp[2][1] = dp[1][1] + dp[2][0] = 2 + 1 = 3`
- For cell `(2, 2)`: `dp[2][2] = dp[1][2] + dp[2][1] = 3 + 3 = 6`

#### Resulting DP Table
```
1 1 1
1 2 3
1 3 6
```

The number of unique paths from `(0, 0)` to `(2, 2)` is `6`.

### Conclusion
This dynamic programming approach ensures that we compute the number of unique paths efficiently in \(O(m \times n)\) time complexity, with \(O(m \times n)\) space complexity for the DP table.

Based on the problem statement and the example provided in the image, let's walk through the solution to find the number of unique paths in an N x M grid with obstacles.

### Problem Explanation

You are given an `N x M` grid where:
- `0` represents a non-blocked cell.
- `-1` represents a blocked cell (no path possible through this cell).

You need to count the total number of unique paths from the top-left corner of the maze to the bottom-right corner. At every cell, you can move either down or to the right.

### Example

Given the following grid:

```
0  0  0
0 -1  0
0  0  0
```

The goal is to find the number of unique paths from the top-left corner `(0, 0)` to the bottom-right corner `(2, 2)`.

### Steps to Solve

1. **Initialization**:
   - If the start or end cell is blocked, return `0`.
   - Initialize a DP table with the same dimensions as the grid.

2. **Base Case**:
   - Set the starting cell `dp[0][0]` to `1` if it's not blocked, otherwise `0`.

3. **Fill the DP Table**:
   - For the first row, if a cell is not blocked, it inherits the path count from its left neighbor.
   - For the first column, if a cell is not blocked, it inherits the path count from the cell above.
   - For other cells, if a cell is not blocked, its path count is the sum of the path counts from the cell above and the cell to the left.

4. **Result**:
   - The value at `dp[N-1][M-1]` is the number of unique paths to reach the bottom-right corner.

### Python Implementation

Here's the Python code to solve the problem:

```python
def unique_paths_with_obstacles(obstacleGrid):
    # Get dimensions
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    
    # If the starting or ending point is blocked, return 0
    if obstacleGrid[0][0] == -1 or obstacleGrid[m-1][n-1] == -1:
        return 0
    
    # Initialize the DP table
    dp = [[0] * n for _ in range(m)]
    
    # Start from the top-left corner
    dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
    
    # Fill the first row
    for j in range(1, n):
        if obstacleGrid[0][j] == 0:
            dp[0][j] = dp[0][j-1]
    
    # Fill the first column
    for i in range(1, m):
        if obstacleGrid[i][0] == 0:
            dp[i][0] = dp[i-1][0]
    
    # Fill the rest of the dp table
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # The number of unique paths to the bottom-right corner
    return dp[m-1][n-1]

# Example usage
obstacleGrid = [
    [0, 0, 0],
    [0, -1, 0],
    [0, 0, 0]
]

print(unique_paths_with_obstacles(obstacleGrid))  # Output: 2
```

### Explanation of the Code

1. **Initialization**:
   - The `dp` array is initialized with zeros. The starting cell `dp[0][0]` is set to `1` if it's not blocked.

2. **First Row and Column**:
   - For the first row, if a cell is not blocked (`obstacleGrid[0][j] == 0`), it inherits the value from its left neighbor.
   - For the first column, if a cell is not blocked (`obstacleGrid[i][0] == 0`), it inherits the value from the cell above it.

3. **Filling the DP Table**:
   - For each cell `(i, j)`, if the cell is not blocked, its value is the sum of the values from the cell above (`dp[i-1][j]`) and the cell to the left (`dp[i][j-1]`).

4. **Result**:
   - The value in `dp[m-1][n-1]` represents the number of unique paths to reach the bottom-right corner.

This approach ensures that we correctly account for obstacles and only consider valid paths through the grid.

Certainly! Let's go through the example provided step-by-step to understand how the solution works.

### Example Grid
We are given the following grid:
```
0  0  0
0 -1  0
0  0  0
```
Here, `0` represents a non-blocked cell, and `-1` represents a blocked cell. We need to find the number of unique paths from the top-left corner `(0, 0)` to the bottom-right corner `(2, 2)`.

### Step-by-Step Explanation

1. **Initialization**:
   - Determine the dimensions of the grid: `m = 3` (rows) and `n = 3` (columns).
   - If the starting point `grid[0][0]` or the ending point `grid[m-1][n-1]` is blocked, return `0`. In this case, both are not blocked.

2. **Create the DP Table**:
   - Create a 2D list `dp` initialized to zeros with the same dimensions as the grid:
     ```python
     dp = [
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]
     ]
     ```

3. **Initialize the Starting Cell**:
   - Set `dp[0][0]` to `1` because there is exactly one way to start at the beginning if it's not blocked:
     ```python
     dp[0][0] = 1
     ```

4. **Fill the First Row**:
   - For each cell in the first row, if the cell is not blocked, it inherits the value from its left neighbor:
     ```python
     for j in range(1, n):
         if obstacleGrid[0][j] == 0:
             dp[0][j] = dp[0][j-1]
     ```
     After this step, the `dp` table looks like:
     ```python
     dp = [
         [1, 1, 1],
         [0, 0, 0],
         [0, 0, 0]
     ]
     ```

5. **Fill the First Column**:
   - For each cell in the first column, if the cell is not blocked, it inherits the value from the cell above:
     ```python
     for i in range(1, m):
         if obstacleGrid[i][0] == 0:
             dp[i][0] = dp[i-1][0]
     ```
     After this step, the `dp` table looks like:
     ```python
     dp = [
         [1, 1, 1],
         [1, 0, 0],
         [1, 0, 0]
     ]
     ```

6. **Fill the Rest of the DP Table**:
   - For each cell `(i, j)` not in the first row or column, if the cell is not blocked, its value is the sum of the values from the cell above (`dp[i-1][j]`) and the cell to the left (`dp[i][j-1]`):
     ```python
     for i in range(1, m):
         for j in range(1, n):
             if obstacleGrid[i][j] == 0:
                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
     ```
     Let's go through this step-by-step for our example:

     - For cell `(1, 1)`, it is blocked (`-1`), so `dp[1][1] = 0`.
     - For cell `(1, 2)`, it inherits from the left (`dp[1][1]` which is `0`) and from above (`dp[0][2]` which is `1`), so `dp[1][2] = 1`.
     - For cell `(2, 1)`, it inherits from the left (`dp[2][0]` which is `1`) and from above (`dp[1][1]` which is `0`), so `dp[2][1] = 1`.
     - For cell `(2, 2)`, it inherits from the left (`dp[2][1]` which is `1`) and from above (`dp[1][2]` which is `1`), so `dp[2][2] = 2`.

     The final `dp` table looks like:
     ```python
     dp = [
         [1, 1, 1],
         [1, 0, 1],
         [1, 1, 2]
     ]
     ```

7. **Result**:
   - The value at `dp[m-1][n-1]` is the number of unique paths to reach the bottom-right corner:
     ```python
     return dp[m-1][n-1]  # This is dp[2][2] which is 2
     ```

### Python Code

Here's the complete Python code:

```python
def unique_paths_with_obstacles(obstacleGrid):
    # Get dimensions
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    
    # If the starting or ending point is blocked, return 0
    if obstacleGrid[0][0] == -1 or obstacleGrid[m-1][n-1] == -1:
        return 0
    
    # Initialize the DP table
    dp = [[0] * n for _ in range(m)]
    
    # Start from the top-left corner
    dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
    
    # Fill the first row
    for j in range(1, n):
        if obstacleGrid[0][j] == 0:
            dp[0][j] = dp[0][j-1]
    
    # Fill the first column
    for i in range(1, m):
        if obstacleGrid[i][0] == 0:
            dp[i][0] = dp[i-1][0]
    
    # Fill the rest of the dp table
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # The number of unique paths to the bottom-right corner
    return dp[m-1][n-1]

# Example usage
obstacleGrid = [
    [0, 0, 0],
    [0, -1, 0],
    [0, 0, 0]
]

print(unique_paths_with_obstacles(obstacleGrid))  # Output: 2
```

This code correctly calculates the number of unique paths from the top-left corner to the bottom-right corner, considering the obstacles in the grid.

This line of code initializes the starting point of a dynamic programming (DP) table used to compute the number of unique paths in a grid, considering obstacles. Here’s a breakdown of what it does:

```python
dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
```

### Explanation:

- **`dp[0][0]`**: This represents the number of ways to reach the cell at the top-left corner of the grid, which is the starting point.

- **`obstacleGrid[0][0]`**: This checks the value of the cell at the top-left corner of the original grid (`obstacleGrid`). If this value is `0`, it means there is no obstacle in this cell. If it's `1`, it means there is an obstacle.

- **`1 if obstacleGrid[0][0] == 0 else 0`**:
  - **`1`**: If the starting cell (`obstacleGrid[0][0]`) is free of obstacles (`0`), then there is exactly one way to be in this cell (by starting there).
  - **`0`**: If the starting cell contains an obstacle (`1`), then there is no way to start or proceed from this cell.

### In Summary:
The line initializes the number of unique paths to the starting cell (`dp[0][0]`). If the starting cell is not obstructed, it is initialized to `1`, indicating one possible way to be in that cell (starting there). If the starting cell is obstructed, it is set to `0`, meaning you cannot start there, so there are no valid paths from this point.

The approach used in the code is **bottom-up**. Here's why:

### Bottom-Up Approach

1. **Initialization**:
   - The DP table `dp` is initialized to keep track of the number of unique paths to each cell in the grid.
   - The starting cell `dp[0][0]` is initialized first, and its value depends directly on the initial state of the grid cell `obstacleGrid[0][0]`.

2. **Filling the Table**:
   - The table is filled in a row-major order, starting from the top-left corner and moving towards the bottom-right corner.
   - Each cell in the DP table `dp[i][j]` is filled based on the values of the cells directly above it (`dp[i-1][j]`) and to the left of it (`dp[i][j-1]`).

3. **Final Result**:
   - The final value, `dp[m-1][n-1]`, represents the number of unique paths to the bottom-right corner of the grid.

### Top-Down Approach

In a **top-down approach**, you would typically use recursion with memoization:

1. **Recursion**:
   - Start from the bottom-right corner and recursively calculate the number of unique paths to reach that cell from the starting cell.

2. **Memoization**:
   - Store the results of subproblems in a memoization table to avoid redundant calculations.

### Example of Top-Down Approach (not implemented in the original code):

```python
def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    memo = {}

    def dp(i, j):
        if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
            return 0
        if i == 0 and j == 0:
            return 1
        if (i, j) in memo:
            return memo[(i, j)]

        memo[(i, j)] = dp(i - 1, j) + dp(i, j - 1)
        return memo[(i, j)]

    return dp(m - 1, n - 1)
```

In summary, the code you provided follows the **bottom-up dynamic programming approach**, where you build the solution from the base cases up to the final solution.

Certainly! Let's break down the code in detail with an example to understand how the dynamic programming (DP) solution works for the "Ninja and his friends" problem.

### Dynamic Programming Table Structure
- We use a 3D DP table `dp` where `dp[r][c1][c2]` represents the maximum chocolates collected by Alice and Bob starting at row `r` with Alice in column `c1` and Bob in column `c2`.

### Step-by-Step Explanation with Example

#### Example Matrix:
```python
matrix = [
    [3, 6, 8, 2],
    [5, 2, 4, 3],
    [1, 1, 20, 10],
    [1, 1, 20, 10]
]
```

#### Initialization:
1. **Base Case**:
   For the last row (n-1), if Alice and Bob are in the same column, count the chocolates once. Otherwise, sum the chocolates from both cells.
   ```python
   for j1 in range(m):
       for j2 in range(m):
           if j1 == j2:
               dp[n-1][j1][j2] = matrix[n-1][j1]
           else:
               dp[n-1][j1][j2] = matrix[n-1][j1] + matrix[n-1][j2]
   ```
   After this step, `dp[3][j1][j2]` will be:
   ```
   [
    [1, 2, 21, 11],
    [2, 1, 21, 11],
    [21, 21, 20, 30],
    [11, 11, 30, 10]
   ]
   ```

2. **Filling the DP Table**:
   We fill the table starting from the second last row up to the first row.

#### Transition:
1. **Iterate from the second last row to the first row**:
   ```python
   for i in range(n-2, -1, -1):
       for j1 in range(m):
           for j2 in range(m):
   ```

2. **Calculate Maximum Chocolates for Each Cell**:
   For each cell `(i, j1, j2)`, consider all possible moves for Alice and Bob:
   ```python
   max_choco = float('-inf')
   for dj1 in [-1, 0, 1]:
       for dj2 in [-1, 0, 1]:
           if 0 <= j1 + dj1 < m and 0 <= j2 + dj2 < m:
   ```

3. **Update the DP Table**:
   Calculate the chocolates collected if Alice and Bob move to new positions `(j1 + dj1, j2 + dj2)`:
   ```python
   if j1 == j2:
       ans = matrix[i][j1] + dp[i+1][j1+dj1][j2+dj2]
   else:
       ans = matrix[i][j1] + matrix[i][j2] + dp[i+1][j1+dj1][j2+dj2]
   ```
   If the new positions are out of bounds, we use a very small value (`-1e9`) to ensure it's not chosen:
   ```python
   else:
       ans = -1e9
   max_choco = max(max_choco, ans)
   ```

4. **Store the Maximum Chocolates Collected**:
   Update `dp[i][j1][j2]`:
   ```python
   dp[i][j1][j2] = max_choco
   ```

5. **Return the Result**:
   The result is stored in `dp[0][0][m-1]`:
   ```python
   return dp[0][0][m-1]
   ```

#### Detailed Step-by-Step Example:

##### Last Row Initialization:
```python
matrix = [
    [3, 6, 8, 2],
    [5, 2, 4, 3],
    [1, 1, 20, 10],
    [1, 1, 20, 10]
]
```
For `n-1` (row 3):
```
dp[3][j1][j2]:
[
    [1, 2, 21, 11],
    [2, 1, 21, 11],
    [21, 21, 20, 30],
    [11, 11, 30, 10]
]
```

##### Second Last Row:
For row 2:
- `(2, 0, 0)`: Alice and Bob in the same column.
  ```python
  dp[2][0][0] = matrix[2][0] + dp[3][1][1] = 1 + 1 = 2
  ```

- `(2, 0, 1)`: Alice in column 0, Bob in column 1.
  ```python
  dp[2][0][1] = matrix[2][0] + matrix[2][1] + dp[3][0][0] = 1 + 1 + 2 = 4
  ```

Repeat this process for all combinations of `(j1, j2)` for row 2.

##### First Row:
Repeat the same process for row 1 and row 0.

Finally, return `dp[0][0][m-1]` which contains the maximum chocolates collected.

### Final Code:
```python
class Solution:
    def solve(self, n, m, grid):
        if not grid or not grid[0]:
            return 0
        
        # Initialize the DP table
        dp = [[[0 for _ in range(m)] for _ in range(m)] for _ in range(n)]
        
        # Base case: Fill the last row
        for j1 in range(m):
            for j2 in range(m):
                if j1 == j2:
                    dp[n-1][j1][j2] = grid[n-1][j1]
                else:
                    dp[n-1][j1][j2] = grid[n-1][j1] + grid[n-1][j2]
        
        # Fill the DP table
        for i in range(n-2, -1, -1):
            for j1 in range(m):
                for j2 in range(m):
                    max_choco = float('-inf')
                    
                    for dj1 in [-1, 0, 1]:
                        for dj2 in [-1, 0, 1]:
                            if 0 <= j1 + dj1 < m and 0 <= j2 + dj2 < m:
                                if j1 == j2:
                                    ans = grid[i][j1] + dp[i+1][j1+dj1][j2+dj2]
                                else:
                                    ans = grid[i][j1] + grid[i][j2] + dp[i+1][j1+dj1][j2+dj2]
                            else:
                                ans = -1e9
                            max_choco = max(max_choco, ans)
                    
                    dp[i][j1][j2] = max_choco
        
        return dp[0][0][m-1]

# Example usage
matrix = [
    [3, 6, 8, 2],
    [5, 2, 4, 3],
    [1, 1, 20, 10],
    [1, 1, 20, 10]
]
solution = Solution()
print(solution.solve(4, 4, matrix))  # Expected output: maximum chocolates collected by Alice and Bob
```

This code ensures the expected time complexity \( O(n \times m \times m) \) and space complexity \( O(n \times m \times m) \).