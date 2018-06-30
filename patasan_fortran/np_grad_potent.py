#!/usr/bin/env python
#-*- coding: utf-8 -*-
#この2行はシバンと言ってないとうまく動かないことがあります。
#この最初の2行以外のコメントアウトは特に意味がありません。
#ﾌﾟﾛｸﾞﾗﾑ内でアンダースコアを使っているのは僕の癖で特にpythonとしては意味はありません。

#grad_potent.py
import numpy as np
import sys
class grad_potent():
	x=np.array([],dtype="int32")
	y=np.array([],dtype="int32")
	v=np.array([],dtype="int32")
	voltage=5000
	x_distance=0
	d_list=[]
	a_list=[]
	deltaV_list=[]
	step_list=[]
	def __init__(self): 
		#csv読み込みモードかコマンドライン入力モードか
		if(len(sys.argv)>1):
			file_name=sys.argv[1]
			print("csv mode: we use {} file".format(file_name))
			index=0
			for line in open(file_name,'r'):
				li=line
				if li[0]!="#":
					print(li)
					li=li.rstrip("\n")
					li=li.split(" ")
					if index==0 :
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
			self.csv=1
		else:
			print("command line input mode")
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

	def voltage_stable_part(self,x_begin,x_end,y_begin,y_end,voltage):
		cal_x_begin=int(x_begin*10)
		cal_x_end=int(x_end*10)
		cal_y_begin=int(y_begin*10)
		cal_y_end=int(y_end*10)
		dot_num=int((cal_x_end-cal_x_begin+1)*(cal_y_end-cal_y_begin+1))
		tmp_v=np.ones(dot_num,dtype="int32")*int(voltage)*100
		tmp_x=np.tile(np.arange(cal_x_begin,cal_x_end+1,dtype="int32"),(cal_y_end-cal_y_begin+1))
		tmp_tmp_y=np.arange(cal_y_begin,cal_y_end+1,dtype="int32")
		tmp_y=np.outer(tmp_tmp_y,np.ones(cal_x_end-cal_x_begin+1,dtype="int32"))
		tmp_y=tmp_y.reshape(-1,)
		self.x=np.hstack((self.x,tmp_x))
		self.y=np.hstack((self.y,tmp_y))
		self.v=np.hstack((self.v,tmp_v))
		self.voltage=voltage

	def parameter_listener(self):
		if(self.csv):
			return
		else:
			self.deltaVa=float(input("input 1st step delta Va [V]"))
			self.da==float(input("input d [mm] (space between electrodes)"))
			self.aa=float(input("input a [mm] (thickness of electrode)"))
			self.stepa=int(input("input number of step"))

	def report(self,index=0):
		if index>0:
			print("now:{} step".format(index))
			print("now nx={05d} (grid_size:0.1^3), now voltage={7.2f}[V]".format(self.x_distance,self.voltage))

	def voltage_descending_part(self,index):
		if(self.csv):
			self.deltaVa=self.deltaV_list[index]
			self.da=self.d_list[index]
			self.aa=self.a_list[index]
			self.stepa=self.step_list[index]
		voltage=self.voltage
		for i in range(self.stepa):
			voltage-=self.deltaVa
			self.voltage_stable_part(
				self.x_distance+self.da,
				self.x_distance+self.aa+self.da,
				self.phib,
				self.phib+self.wall,voltage
			)
			self.x_distance+=self.da+self.aa
	
	def make_tail_part(self):
		self.voltage_stable_part(
			self.x_distance,
			self.x_distance+self.lc,
			self.phib,
			self.phib+self.wall,
			0
		)
		self.x_distance+=self.lc
		self.voltage_stable_part(
			self.x_distance+0.1,
			self.x_distance+10,
			self.phic,
			self.phib+self.wall,
			0
		)
	def file_output(self):

		header="""begin_potential_array
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
		np.savetxt("result.txt",result.T,fmt="%.0f",header=header,comments="",footer=footer)
		# f=open("result.patxt",'w')
		# # f.seek(0,0)
		# g=open("result.txt")
		# data=g.read()
		# f.write('begin_potential_array\n')
		# f.write('begin_header\n')
		# f.write('    mode -1\n')
		# f.write('    symmetry cylindrical\n')
		# f.write('     max_voltage 500000\n')
		# f.write('    nz 1\n')
		# f.write('    mirror_x 0\n')
		# f.write('    mirror_y 1\n')
		# f.write('    mirror_z 0\n')
		# f.write('    field_type electrostatic\n')
		# f.write('    ng 100\n')
		# f.write('    dx_mm 0.1\n')
		# f.write('    dy_mm 0.1\n')
		# f.write('    dz_mm 0.1\n')
		# f.write('    fast_adjustable 0\n')
		# f.write('    data_format x y z is_electrode potential\n')
		# f.write('end_header\n')
		# f.write('begin_points\n')
		# f.write(data)
		# f.close()

	def main(self):
		self.make_sample_holder()
		if self.csv:
			for i in range(len(self.d_list)):
				self.voltage_descending_part(i)
		else:
			i=0
			while True:
				answer2continueQ="X"
				while answer2continueQ!=("y"or"n"):
					input_answer=input("Do you wish to continue?")
				if input_answer=="y":
					self.parameter_listener()
					self.voltage_descending_part(i)
					i+=1
					self.report(index=i)
				else:
					break
		self.make_tail_part()
		self.file_output()

E=grad_potent()
E.main()








