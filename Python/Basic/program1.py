'''
ここでは変数を使った、計算を扱います。
コメントにそれがどのような計算をしているのかが書かれているので、それを参照しながらやってください。
もしわからないことがあれば、私にslackで聞いてください。
'''

a=2       #(今定義した変数である)aに2を代入
print(a)  #aの値を表示
b=5       #(今定義した変数である)bに5を代入
print(b)  #bの値を表示

c=a+b               #cにaとbを足した時の値をcに代入
print(c)            #cの値だけ表示
print("c="+str(c))  #c=(cの値を表示)

d=a-b               #dにaからbを引いた時の値をdに代入
print("c="+str(d))

e=a*b               #eにaとbを掛けた時の値をeに代入
print("e="+str(e))

f=b/a               #fにbをaで割った時の値をfに代入
print("f="+str(f))

g=b%a               #gにbをaで割ったものの「余り」をgに代入
print("g="+str(g))

h=c*e+a              #計算されて代入された変数と最初に数値を代入した変数を使い、計算、それをhに代入
print("h="+str(h))

i=f/e                 #計算されて代入された変数同士を、計算、それをiに代入
print("i="+str(i))


#ちなみに以下のような応用的な代入の仕方もあります(下の結果はコンソールで表示されません、各自自分でやってみてください)
#c, d, e, f, g, h, i= a+b, a-b, a*b, b/a, b%a, c*e+a, f/e
#print(a, b, c, d, e, f, g, h, i)

'''
課題work1
a=25, b=12として、aを2乗したものにbを5回かけた値を出力するプログラムを作成しよう。
'''