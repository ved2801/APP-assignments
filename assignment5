def find_lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    # Step 1: Initialize DP table with zeros
    # Size: (m + 1) x (n + 1)
    lcs_table = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Step 2: Build the DP table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])
                
    # Step 3: Backtrack from lcs_table[m][n] to reconstruct the LCS string
    lcs_length = lcs_table[m][n]
    lcs_chars = [''] * lcs_length
    
    i, j = m, n
    index = lcs_length - 1
    
    while i > 0 and j > 0:
        # If current characters match, they are part of the LCS
        if X[i - 1] == Y[j - 1]:
            lcs_chars[index] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        # Move in the direction of the larger value
        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i -= 1
        else:
            j -= 1
            
    lcs_string = "".join(lcs_chars)
    return lcs_length, lcs_string


# --- Test Cases ---
if __name__ == "__main__":
    # Example from lab manual
    str1 = "AGGTAB"
    str2 = "GXTXAYB"
    
    length, subsequence = find_lcs(str1, str2)
    
    print(f"Sequence 1 : {str1}")
    print(f"Sequence 2 : {str2}")
    print(f"Length of LCS : {length}")
    print(f"LCS String   : {subsequence}")
