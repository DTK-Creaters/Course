'''
課題8
初めに2つの自然数を入力させ、入力された数字が10より大きければ掛算、小さければ足し算をさせる
関数(返り値あり)を
(一つ目)引数ナシ
(二つ目)引数アリ
バージョンで作って、プログラムを作ってください。
'''

#-----------------------------------------------------
def calculator1():
    a=int(input("1つ目の自然数を入力してください: "))
    b=int(input("2つ目の自然数を入力してください: "))

    if a>10 or b>10:
        return a*b
    else:
        return a+b

print(calculator1())

#------------------------------------------------------
def calculator1(a, b):
    if a>10 or b>10:
        return a*b
    else:
        return a+b

a=int(input("1つ目の自然数を入力してください: "))
b=int(input("2つ目の自然数を入力してください: "))
print(calculator1(a, b))