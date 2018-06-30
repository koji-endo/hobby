#!/usr/bin/env python
#-*- coding: utf-8 -*-
#この2行はシバンと言ってないとうまく動かないことがあります。
#この最初の2行以外のコメントアウトは特に意味がありません。
#ﾌﾟﾛｸﾞﾗﾑ内でアンダースコアを使っているのは僕の癖で特にpythonとしては意味はありません。

#grad_potent.py

#how to compile
#python grad_potent.py data.csv

# class values():

p=0
x=[]
y=[]
v=[]
def initial_setup():
	#csv読み込みモードかコマンドライン入力モードか
	
	if(len(sys.argv)>1):
		file_name=sys.argv[1]
		print("csv mode: we use {} file".format(file_name))
		for line in open(file_name,'r'):
			li=line
			print(li)
		li=li.split(", ")
		wall=int(li[0])
		phia=int(li[1])
		la=int(li[2])
		phib=int(li[3])
		lb=int(li[4])
	else:
		print("command line input mode")
		wall=int(input("input wall-length of electrode [mm]"))
		phia=int(input("input phia [mm]"))
		la=int(input("input la [mm]"))
		phib=int(input("input phib [mm]"))
		lb=int(input("input lb [mm]"))
	
	print("wall={}, phia={}, la={}, phib={}, lb={}".format(wall, phia, la, phib, lb))
	voltage=5000*100 #読みやすいようにfortranコードと統一しましたがこれも実際の値ではないのでcal_表記を付けたほうが保守上は便利だと思います。
	cal_wall=wall*10
	cal_phib_in=phib*10/2
	cal_phib_out=cal_phib_in+cal_wall-1
	cal_la=la*10+100
	cal_lb=lb*10

def make_sample_holder():
	for x_i in range(cal_phia_in,cal_phib_out+1):
		for y_i in range(1,cal_la+1):
			p=p+1
			#.appendは配列に追加するための関数です。
			x.append(distance+y_i-1)
			y.append(p)
			v.append(voltage)

	distance=cal_la
	print("la={4.1f}[mm], now nx={05d} (grid_size:0.1^3), now voltage={7.2f}[V]".format(la,distance,voltage/100))

	for y_i in range(cal_phib_in,cal_phib_out+1):
		for x_i in range(1,cal_la+1):
			p=p+1
			#.appendは配列に追加するための関数です。
			x.append(distance+x_i-1)
			y.append(p)
			v.append(voltage)

	distance=cal_la+cal_lb #保守上修正しました。
	print("lb={4.1f}[mm], now nx={05d} (grid_size:0.1^3), now voltage={7.2f}[V]".format(la,distance,voltage/100))

def second_setup():
	deltaVa=int(input("input 1st step delta Va [V]"))
	da==int(input("input d [mm] (space between electrodes)"))
	aa=int(input("input a [mm] (thickness of electrode)"))
	stepa=int(input("input number of first step"))

	cal_deltaVa=deltaVa*100
	cal_da=da*10
	cal_aa=aa*10
	distance=distance+cal_aa
	for x_i1 in range(1,stepa+1): #for x_i in range(stepa)と書くのが普通です。そうすると1からでなく0から始まりますが
		distance+=cal_da #distance=distance+cal_daと同じ意味です。通常こう書きます。
		for y_i in range(cal_phib_in,cal_phib_out):
			for x_i2 in range(cal_aa):
				#.appendは配列に追加するための関数です。
				x.append(distance+x_i2-1)
				y.append(y_i)
				v.append(voltage)
			distance+=cal_aa

	input_answer="z" #最初はwhile分にエラーしてほしいのでy,nとは異なる文字を入れておく。
	while input_answer!="y"||"n":
		input_answer=input("input d [mm] (space between electrodes)")
	if input_answer="y":
		second_setup()
	else:
		return

def tail_make():
	#同じ感じで出来ます。









import sys
initial_setup()