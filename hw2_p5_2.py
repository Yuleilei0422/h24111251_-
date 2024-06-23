def longest_palindrome(s):
    n2 = len(s)  # 獲取輸入字串的長度
    dp = [[False] * n2 for _ in range(n2)]  # 創建一個二維布爾值列表，用於動態規劃
    ans = ""  # 初始化最長回文子字串為空字串
    for l in range(n2):  # 遍歷每一個可能的子字串長度
        for i in range(n2):  # 遍歷每一個可能的子字串起始位置
            j = i + l  # 計算子字串的結束位置
            if j >= n2:  # 如果結束位置超出了字串的範圍，則跳出內部循環
                break
            if l == 0:  # 如果子字串長度為 1，則它一定是回文的
                dp[i][j] = True
            elif l == 1:  # 如果子字串長度為 2，則它是回文的當且僅當它的兩個字元相同
                dp[i][j] = (s[i] == s[j])
            else:  # 如果子字串長度大於 2，則它是回文的當且僅當它的首尾字元相同，並且去掉首尾字元後仍然是回文的
                dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
            if dp[i][j] and l + 1 > len(ans):  # 如果當前子字串是回文的，並且比已知的最長回文子字串還要長，則更新最長回文子字串
                ans = s[i:j+1]
    return ans  # 返回最長回文子字串

print("The longest palindrome substring is", longest_palindrome(s))  # 輸出最長回文子字串
print("Length is:%d" %len(longest_palindrome(s)))  # 輸出最長回文子字串的長度