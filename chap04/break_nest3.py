flag = False  # breakされたか

for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        if result > 50:
            # breakのフラグをTrueに
            flag = True
            break
        print(result, end=" ")
    print()
    # フラグがTrueであれば外側のループも脱出
    if flag:
        break
