import random

realans = [random.randint(1, 9) for _ in range(4)]
ans = realans.copy()  # 使用.copy()来复制列表，避免直接赋值导致的引用问题
flag = 0
print(ans)

while True:
    a = 0
    b = 0
    user_input = input("请输入一个以逗号分隔的数字列表(例如:1,2,3,4): ")
    guess = [int(x) for x in user_input.split(",")]
    for i in range(len(guess)):
        if ans[i] == guess[i]:
            a += 1
            ans[i] = "a"
            guess[i] = "g"

    for i in range(len(guess)):
        for j in range(len(ans)):
            if ans[i] == guess[j] and ans[i] != "a":  # 排除已经标记的数字
                b += 1

    print("a", a, "b", b)
    if a == 4:
        print("you win")
        break
    ans = realans.copy()  # 重新初始化答案列表
