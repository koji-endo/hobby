#!/usr/bin/env python
#-*- coding: utf-8 -*-
#この2行はシバンと言ってないとうまく動かないことがあります。
#この最初の2行以外のコメントアウトは特に意味がありません。
#ﾌﾟﾛｸﾞﾗﾑ内でアンダースコアを使っているのは僕の癖で特にpythonとしては意味はありません。

#np_grad_potent.py
#ライブラリをインポートしています。
import numpy as np
import sys
from datetime import datetime
#クラスは便利なんですが、ちょっととっつきにくい概念です。
# 関数主体でプログラムを書きたくて、引数に大量の変数を代入したくなかったのでクラスを使いました。
# グローバル変数みたいなものを使うために使っています。
		
class grad_potent():
	# プログラム全体で使いたい変数をここで定義します。
	# 一部の変数は___init___内で定義しています。
	x=np.array([],dtype="int32")
	y=np.array([],dtype="int32")
	v=np.array([],dtype="int32")
	voltage=5000
	x_distance=0
	d_list=[]
	a_list=[]
	deltaV_list=[]
	step_list=[]
	# この関数はE=grad_pitent()としたときに自動実行されます。
	# コンストラクタと言ってクラスの初期化時に実行されるものです。

	def __init__(self): 

	
		# csv読み込みモードかコマンドライン入力モードかの判定
		# python np_grad_potent.pyでコンパイルした時は
		# sys.argv=["np_grad_potent.py"]
		# python np_grad_potent.py read_data1.csvでコンパイルした時は
		# sys.argv=["np_grad_potent.py","read_data1.csv"]
		# となります。配列の長さの違いでどちらのモードか見分けています。
		# len()が配列の長さを知るための関数です。
		if(len(sys.argv)>1):
			file_name=sys.argv[1]
			print("-------------------------")
			print("csv mode: we use {} file".format(file_name))
			print("-------------------------")
			index=0
			#ファイルの中身を読む処理です、1行ずつ読んでいきます。
			for line in open(file_name,'r'):
				li=line
				# "#"が文頭にある行は飛ばすように処理します。
				if li[0]!="#": #!=はnot equalです。
					#改行記号を取って、スペースで区切って配列に入れます。
					li=li.rstrip("\n")
					li=li.split(" ")
					if index==0 : #1行目だった場合(コメントアウト除く)
						self.wall=float(li[0])
						self.phia=float(li[1])
						self.phib=float(li[3])
						self.la=float(li[2])
						self.lb=float(li[4])
					else:
						if len(li)==4:
							self.d_list.append(float(li[0]))
							self.a_list.append(float(li[1]))
							self.deltaV_list.append(float(li[2]))
							self.step_list.append(int(li[3]))
						elif len(li)==2:
							self.lc=(float(li[0]))
							self.phic=(float(li[1]))
					index+=1
			#csv読み込みモードかどうかのフラグです。
			self.csv=1
		else:
			print("-------------------------")
			print("command line input mode")
			print("-------------------------")
			#input関数によってゲットできたデータ(文字列型)をfloat関数で実数型に変換します。
			self.wall=float(input("input wall-length of electrode [mm]: "))
			self.phia=float(input("input phia [mm]: "))
			self.phib=float(input("input phib [mm]: "))
			self.la=float(input("input la [mm]: "))
			self.lb=float(input("input lb [mm]: "))
			self.csv=0
		
		print("wall={}, phia={}, la={}, phib={}, lb={}".format(
			self.wall, 
			self.phia, 
			self.la, 
			self.phib, 
			self.lb
			))

	def make_sample_holder(self):
		self.voltage_stable_part(
			0,
			self.la,
			self.phia,
			self.phib+self.wall,
			self.voltage
		)
		self.voltage_stable_part(
			self.la+0.1,
			self.lb,
			self.phib,
			self.phib+self.wall,
			self.voltage
		)
		self.x_distance=self.lb

	def voltage_stable_part(self,x_begin,x_end,y_begin,y_end,voltage):
		cal_x_begin=int(x_begin*10)
		cal_x_end=int(x_end*10)
		cal_y_begin=int(y_begin*10)
		cal_y_end=int(y_end*10)
		dot_num=int((cal_x_end-cal_x_begin+1)*(cal_y_end-cal_y_begin+1))
		#np.onesは指定した長さの全ての要素が1の配列を作る関数です。
		#for文はpythonでは遅いため、あまり使いたくなく、代わりにこういうものを使います。
		tmp_v=np.ones(dot_num,dtype="int32")*int(voltage)*100
		#np.arangeは等差数列を作る関数です。
		#np.tileは配列を指定回数繰り返した配列を作る関数です。たとえば、np.tile([1,2,3],2)は
		#[1,2,3,1,2,3]を返します。「配列 繰り返す numpy」で検索したら出てきたので使いました。
		#こういう関数は大体そろっているのがpythonの魅力です。
		tmp_x=np.tile(np.arange(cal_x_begin,cal_x_end+1,dtype="int32"),(cal_y_end-cal_y_begin+1))
		tmp_tmp_y=np.arange(cal_y_begin,cal_y_end+1,dtype="int32")
		#outerはベクトルaとbから行列C[i,j]=a[i]*b[j]なる行列を作る関数です。
		#今回は[1,1,1,2,2,2,3,3,3,4,4,4...]のような配列を作るのが目的のため以下のようなステップを踏みました。
		#ベクトル[1,1,1]と[1,2,3,4,...]をかけて[[1,1,1],[2,2,2],[3,3,3],[4,4,4]...]なる二次元配列(行列)を作る。
		#その行列をreshape関数で1次元に変換する。
		tmp_y=np.outer(tmp_tmp_y,np.ones(cal_x_end-cal_x_begin+1,dtype="int32"))
		tmp_y=tmp_y.reshape(-1,)
		# self.x配列の末尾にtmp_x配列を突っ込みます。
		self.x=np.hstack((self.x,tmp_x))
		self.y=np.hstack((self.y,tmp_y))
		self.v=np.hstack((self.v,tmp_v))
		self.voltage=voltage

	def parameter_listener(self):
		if(self.csv):
			return
		else:
			self.deltaVa=float(input("input 1st step delta Va [V] : "))
			self.da=float(input("input d [mm] (space between electrodes) : "))
			self.aa=float(input("input a [mm] (thickness of electrode) : "))
			self.stepa=int(input("input number of step : "))

	def report(self,index=0):
		if index>0:
			print("now:{} step".format(index))
		print("now nx={} (grid_size:0.1^3), now voltage={}[V]".format(self.x_distance,self.voltage))

	def voltage_descending_part(self,index):
		if(self.csv):
			self.deltaVa=self.deltaV_list[index]
			self.da=self.d_list[index]
			self.aa=self.a_list[index]
			self.stepa=self.step_list[index]
		voltage=self.voltage
		for i in range(self.stepa):
			# voltage=voltage-self.deltaVaと同じ意味です。
			voltage-=self.deltaVa
			self.voltage_stable_part(
				self.x_distance+self.da,
				self.x_distance+self.aa+self.da,
				self.phib,
				self.phib+self.wall,
				voltage
			)
			self.x_distance+=self.da+self.aa
		self.x_distance+=self.da

	def make_tail_part(self):
		#-0.1は界面のための処理
		self.voltage_stable_part(
			self.x_distance,
			self.x_distance+self.lc-0.1,
			self.phib,
			self.phib+self.wall,
			0
		)
		self.x_distance+=self.lc
		self.voltage_stable_part(
			self.x_distance,
			self.x_distance+10,
			self.phic,
			self.phib+self.wall,
			0
		)
	def file_output(self):

		header="""# ASCII text representation of a SIMION PA file.
begin_potential_array
begin_header
	mode -1
	symmetry cylindrical
	max_voltage 500000
	nz 1
	mirror_x 0
	mirror_y 1
	mirror_z 0
	field_type electrostatic
	ng 100
	dx_mm 0.1
	dy_mm 0.1
	fast_adjustable 0
	data_format x y z is_electrode potential
end_header
begin_points"""
		footer="end_points\nend_potential_array"
		xlen=len(self.x)
		n1=np.zeros(xlen,dtype="int32")
		n2=np.ones(xlen,dtype="int32")
		print(self.x.dtype,self.y.dtype,n1.shape,self.v.dtype)
		result=np.vstack((self.x,self.y,n1,n2,self.v))
		print(self.x)
		print (result)
		time=datetime.now().strftime("%Y%m%d_%H%M%S")
		np.savetxt("result"+time+".patxt",result.T,fmt="%.0f",header=header,comments="",footer=footer)

	def main(self):
		self.make_sample_holder()
		self.report()
		if self.csv:
			for i in range(len(self.d_list)):
				self.voltage_descending_part(i)
				self.report(index=i)
		else:
			i=0
			while True:
				input_answer="X"
				while input_answer!="y" and input_answer!="n":
					input_answer=input("\nDo you wish to continue? (yes:y no:n): ")
				if input_answer=="y":
					self.parameter_listener()
					self.voltage_descending_part(i)
					i+=1
					self.report(index=i)
				else:
					self.lc=float(input("input tail_length lc [mm] : "))
					self.phic=float(input("input aperture size phic [mm] : "))
					break #whileから抜け出します。
		self.make_tail_part()
		self.report()
		self.file_output()

E=grad_potent()
E.main()








