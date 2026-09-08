# ==========================================
# 1. TOP-DOWN APPROACH (Memoization)
# ==========================================
def knapsack_top_down(values, weights, W):
    n = len(values)
    # Initialize memoization table with -1
    # Dimensions: (n + 1) x (W + 1)
    memo = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

    def solve(i, w):
        # Base case: no items left or remaining weight capacity is 0
        if i == 0 or w == 0:
            return 0
        
        # Return already computed state
        if memo[i][w] != -1:
            return memo[i][w]

        # Case 1: Item's weight exceeds remaining capacity -> Exclude item
        if weights[i - 1] > w:
            memo[i][w] = solve(i - 1, w)
        else:
            # Case 2: Max value between excluding and including the item
            exclude = solve(i - 1, w)
            include = values[i - 1] + solve(i - 1, w - weights[i - 1])
            memo[i][w] = max(exclude, include)

        return memo[i][w]

    return solve(n, W)


# ==========================================
# 2. BOTTOM-UP APPROACH (Tabulation)
# ==========================================
def knapsack_bottom_up(values, weights, W):
    n = len(values)
    # Initialize DP table with 0s
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build DP table iteratively
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                # Max of (exclude item, include item)
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Exclude item
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# ==========================================
# MAIN / DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Data
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50

    print("--- 0/1 Knapsack Execution ---")
    print(f"Item Values  : {values}")
    print(f"Item Weights : {weights}")
    print(f"Capacity (W) : {W}")
    print("-" * 30)

    # Solve via Top-Down
    max_val_td = knapsack_top_down(values, weights, W)
    print(f"Maximum Value (Top-Down / Memoization) : {max_val_td}")

    # Solve via Bottom-Up
    max_val_bu = knapsack_bottom_up(values, weights, W)
    print(f"Maximum Value (Bottom-Up / Tabulation) : {max_val_bu}")
