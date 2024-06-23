heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(heights)
left = 0            # 左邊的初始位置
right = n - 1       # 右邊的初始位置
left_max = 0        # 左邊最大高度
right_max = 0       # 右邊最大高度
ans = 0             # 結果
while left < right: # 只要左邊還沒超過右邊
    if heights[left] < heights[right]:   # 如果左邊的高度小於右邊的高度
        if heights[left] > left_max:     # 如果目前位置的高度大於左邊最大高度
            left_max = heights[left]     # 更新左邊最大高度
        else:                             # 目前位置可以容納的水的高度為左邊最大高度減目前高度
            ans += left_max - heights[left] 
        left += 1                        # 左邊向右移
    else:                                 # 如果右邊的高度小於等於左邊的高度
        if heights[right] > right_max:   # 如果目前位置的高度大於右邊最大高度
            right_max = heights[right]   # 更新右邊最大高度
        else:                             # 否則目前位置可以容納的水的高度為右邊最大高度減去目前高度
            ans += right_max - heights[right]
        right -= 1                       # 右邊向左移動
print(ans)
