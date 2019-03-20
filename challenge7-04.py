lists = "048"

while True:
    a = input("数字を入力するか、qで終了します:")
    if a in lists:
        print("正解")
        break
    print("不正解")
