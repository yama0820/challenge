#http://tinyurl.com/zx7o2v9

x=12
y=5

if x<10:
    print("xは10未満です。")
else:
    print("xは10以上です。")

if y<=10:
    print("yは10以下です。")
elif y>10 and y<=25:
    print("yは10より大きく25以下です。")
elif y>25:
    print("yは25未満です。")

print("x/yの商は",x%y,"です。")

print("x/yの余は",x//y,"です。")

age=33

if age>=20 and age<30:
    print("あなたは20代")
elif age>=30 and age<40:
    print("あなたは30代")
