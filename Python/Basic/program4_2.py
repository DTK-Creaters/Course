#これはprogram4の前編です。
'''
無限ループをする度にctrl+Cをして、中断していては、プログラムとしてあまりよくないので、
無限ループである条件に達した時にそのループから脱出する、
break
を紹介します。
'''

i=0
while True:   #ループの中で何かしらのエラーやbreakが起きない限り、無限にループを続けたいときに書く
    i+=1
    print(i)
    if i==10:
        break   #i=10でループから脱出

n=0
for n in range(20):
    if n%2==0:
        continue    #iが偶数の時for n in range(20):(ループの最初)に戻り、また同じ処理をしていきます。
    print(n)

'''
課題work4
以上のことを用いて
10から続く自然数の中で9の倍数の数字を10個ターミナルに表示させるプログラムを作ってください。
'''