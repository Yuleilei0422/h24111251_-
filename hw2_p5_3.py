n = int(input("Please input a number:"))
a, b = 0, 1
for i in range(n):
    a, b = b, a + b

def longest_palindrome(s):
    n2 = len(s)
    dp = [[False] * n2 for _ in range(n2)]
    ans = ""
    for l in range(n2):
        for i in range(n2):
            j = i + l
            if j >= n2:
                break
            if l == 0:
                dp[i][j] = True
            elif l == 1:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
            if dp[i][j] and l + 1 > len(ans):
                ans = s[i:j+1]
    return ans
# 凱撒密碼函數
def caesar_cipher(text, key):
    result = ""  # 初始化結果為空字串
    for char in text:  # 遍歷輸入的每一個字元
        ascii_code = ord(char)  # 獲取字元的 ASCII 碼
        encrypted_code = ascii_code + key  # 將 ASCII 碼加上密鑰
        encrypted_code = ((encrypted_code - 65) % 26) + 65  # 將結果限制在大寫字母的範圍內
        result += chr(encrypted_code)  # 將加密後的 ASCII 碼轉換回字元，並添加到結果中
    return result  # 返回結果

# 仿射密碼函數
def affine_cipher(text, key1, key2):
    result = ""  # 初始化結果為空字串
    for char in text:  # 遍歷輸入的每一個字元
        ascii_code = ord(char)  # 獲取字元的 ASCII 碼
        encrypted_code = key1 * ascii_code + key2  # 將 ASCII 碼乘以密鑰1，然後加上密鑰2
        encrypted_code = ((encrypted_code - 65) % 26) + 65  # 將結果限制在大寫字母的範圍內
        result += chr(encrypted_code)  # 將加密後的 ASCII 碼轉換回字元，並添加到結果中
    return result  # 返回結果

# 讀取用於檢測回文的兩個字串和需要加密的明文
s1 = input("The first string for Palindromic detection (s1)=")
s2 = input("The second string for Palindromic detection (s2)=")
plaintext=input("The plaintext to be encrypted:")

print("-----extract key for encypt method-----")
print("The %d-th Fibonacci sequence number is %d" % (n, a))  # 輸出費波那契數列的第 n 項
print("The longest palindrome substring is", longest_palindrome(s1))  # 輸出 s1 的最長回文子字串
print("The longest palindrome substring is", longest_palindrome(s2))  # 輸出 s2 的最長回文子字串
print("Length is:%d" %len(longest_palindrome(s1)))  # 輸出 s1 的最長回文子字串的長度
print("Length is:%d" %len(longest_palindrome(s2)))  # 輸出 s2 的最長回文子字串的長度

print("-----encryption completed-----")
key_caesar = int(a)
key_affine1 = len(longest_palindrome(s1))
key_affine2 = len(longest_palindrome(s2))

encrypted_text = caesar_cipher(plaintext, key_caesar)
encrypted_text = affine_cipher(encrypted_text, key_affine1, key_affine2)

print("The encrypted text is:", encrypted_text)




