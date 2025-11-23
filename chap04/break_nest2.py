for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        if result > 50:
            break
        print(result, end=" ")
    # 内側のループを正常終了したら次の周回へ
    else:
        print()
        continue
    # 内側のループをbreakしたら、外側もbreak
    break
