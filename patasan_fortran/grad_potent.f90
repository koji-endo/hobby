program gradpotent
	implicit none
	real phia, phib, phic, la, lb, lc, da, db, dc, dd, de, df, dg, aa, ab, ac, ad, ae, af, ag, wall
	real deltaVa, deltaVb, deltaVc, deltaVd, deltaVe, deltaVf, deltaVg
	real voltage
	integer calphiain, calphibin, calphibout, calphic, calla, callb, callc, i, j, k
	integer calda, caldb, caldc, caldd, calde, caldf, caldg, calaa, calab, calac, calad, calae, calaf, calag
	real caldeltaVa, caldeltaVb, caldeltaVc, caldeltaVd, caldeltaVe, caldeltaVf, caldeltaVg
	integer stepa, stepb, stepc, stepd, stepe, stepf, stepg, p, calwall, nx, ny, distance
	integer x(10000000)
	integer y(10000000)
	real v(10000000)
	character answer*1



	write(*,*) 'input wall-length of electrode [mm]'	!! 電極の壁の厚さ、サンプルホルダー部分の空間の大きさ、段階電場までの距離を読み込み
	read(*,*) wall
	write(*,*) 'input phia [mm]'
	read(*,*) phia
	write(*,*) 'input la [mm]'
	read(*,*) la
	write(*,*) 'input phib [mm]'
	read(*,*) phib
	write(*,*) 'input lb [mm]'
	read(*,*) lb
	
	distance = 0					!! 計算領域のグリッドの取り方は0.1 mm立法、計算ソフトの都合上電圧は大きい値で読ませる
	voltage = 5000 * 100
	calwall = wall * 10
	p = 0
	calphiain = phia * 10/2
	calla = la * 10 + 100
	calphibin = phib * 10/2
	calphibout = calphibin + calwall - 1
	do i = calphiain, calphibout			!! サンプルホルダー部分の構成
		do j = 1, calla
			p = p + 1
			x(p) = distance + (j - 1)
			y(p) = i
			v(p) = voltage
		end do
	end do

	distance = calla
	write(*,31) 'la = ',la,'[mm], now nx = ',distance,'(grid size 0.1^3), now voltage = ',voltage/100,'[V]'
31	format(a, f4.1, a, i5, a, f7.2)

	callb = lb * 10
	do i = calphibin, calphibout			!! 段階電場までの筒（定電圧）の構成
		do j = 1, callb
			p = p + 1
			x(p) = distance + (j - 1)
			y(p) = i
			v(p) = voltage
		end do
	end do

	distance = distance + callb
	write(*,32) 'lb = ',lb,'[mm], now nx = ',distance,'(grid size 0.1^3), now voltage = ',voltage/100,'[V]'
32	format(a, f4.1, a, i5, a, f7.2)

	write(*,*) 'input 1st step delta Va [V]'		!! 段階電場一段階目
	read(*,*) deltaVa
	write(*,*) 'input d [mm] (space between electrodes)'
	read(*,*) da
	write(*,*) 'input a [mm] (thickness of electrode)'
	read(*,*) aa
	write(*,*) 'input number of 1st step'
	read(*,*) stepa
	
	caldeltaVa = deltaVa * 100
	calda = da * 10
	calaa = aa * 10
	do i = 1, stepa						!! 繰り返し構造の構成
		distance = distance + calda
		voltage = voltage - caldeltaVa
		do j = calphibin, calphibout
			do k = 1, calaa
				p = p + 1
				x(p) = distance + (k - 1)
				y(p) = j
				v(p) = voltage
			end do
		end do
		distance = distance + calaa
	end do

	write(*,33) 'delta Va = ',deltaVa,'[V], d = ',da,'[mm], a = ',aa,'[mm], ',stepa,' steps'
33	format(a, f5.2, a, f3.1, a, f3.1, a, i3)
	write(*,34) 'now nx = ',distance,'(grid size 0.1^3), now voltage = ',voltage/100,'[V]'
34	format(a, i5, a, f7.2)

71	write(*,*) 'continue? y (Yes) or n (No)'				!! 二段階目を続けるかどうかの確認
	read(*,*) answer
		if (answer == 'y') then
			write(*,*) 'input 2nd step delta Vb [V]'
			read(*,*) deltaVb
			write(*,*) 'input d [mm] (space between electrodes)'
			read(*,*) db
			write(*,*) 'input a [mm] (thickness of electrode)'
			read(*,*) ab
			write(*,*) 'input number of 2nd step'
			read(*,*) stepb
		else if (answer == 'n') then
			distance = distance + calda				!! 繰り返し最後の電極の後に隙間を空ける
			go to 80
		else
			go to 71
		end if
	
	caldeltaVb = deltaVb * 100				!! 以降、一段目と同様
	caldb = db * 10
	calab = ab * 10
	do i = 1, stepb
		distance = distance + caldb
		voltage = voltage - caldeltaVb
		do j = calphibin, calphibout
			do k = 1, calab
				p = p + 1
				x(p) = distance + (k - 1)
				y(p) = j
				v(p) = voltage
			end do
		end do
		distance = distance + calab
	end do

	write(*,35) 'delta Vb = ',deltaVb,'[V], d = ',db,'[mm], a = ',ab,'[mm], ',stepb,' steps'
35	format(a, f5.2, a, f3.1, a, f3.1, a, i3)
	write(*,36) 'now nx = ',distance,'(grid size 0.1^3), now voltage = ',voltage/100,'[V]'
36	format(a, i5, a, f7.2)

72	write(*,*) 'continue? y (Yes) or n (No)'
	read(*,*) answer
		if (answer == 'y') then
			write(*,*) 'input 3rd step delta Vc [V]'
			read(*,*) deltaVc
			write(*,*) 'input d [mm] (space between electrodes)'
			read(*,*) dc
			write(*,*) 'input a [mm] (thickness of electrode)'
			read(*,*) ac
			write(*,*) 'input number of 3rd step'
			read(*,*) stepc
		else if (answer == 'n') then
			distance = distance + caldb
			go to 80
		else
			go to 72
		end if
	
	caldeltaVc = deltaVc * 100
	caldc = dc * 10
	calac = ac * 10
	do i = 1, stepc
		distance = distance + caldc
		voltage = voltage - caldeltaVc
		do j = calphibin, calphibout
			do k = 1, calac
				p = p + 1
				x(p) = distance + (k - 1)
				y(p) = j
				v(p) = voltage
			end do
		end do
		distance = distance + calac
	end do

	write(*,37) 'delta Vc = ',deltaVc,'[V], d = ',dc,'[mm], a = ',ac,'[mm], ',stepc,' steps'
37	format(a, f5.2, a, f3.1, a, f3.1, a, i3)
	write(*,38) 'now nx = ',distance,'(grid size 0.1^3), now voltage = ',voltage/100,'[V]'
38	format(a, i5, a, f7.2)

73	write(*,*) 'continue? y (Yes) or n (No)'
	read(*,*) answer
		if (answer == 'y') then
			write(*,*) 'input 4th step delta Vd [V]'
			read(*,*) deltaVd
			write(*,*) 'input d [mm] (space between electrodes)'
			read(*,*) dd
			write(*,*) 'input a [mm] (thickness of electrode)'
			read(*,*) ad
			write(*,*) 'input number of 4th step'
			read(*,*) stepd
		else if (answer == 'n') then
			distance = distance + caldc
			go to 80
		else
			go to 73
		end if
	
	caldeltaVd = deltaVd * 100
	caldd = dd * 10
	calad = ad * 10
	do i = 1, stepd
		distance = distance + caldd
		voltage = voltage - caldeltaVd
		do j = calphibin, calphibout
			do k = 1, calad
				p = p + 1
				x(p) = distance + (k - 1)
				y(p) = j
				v(p) = voltage
			end do
		end do
		distance = distance + calad
	end do

	write(*,39) 'delta Vd = ',deltaVd,'[V], d = ',dd,'[mm], a = ',ad,'[mm], ',stepd,' steps'
39	format(a, f5.2, a, f3.1, a, f3.1, a, i3)
	write(*,40) 'now nx = ',distance,'(grid size 0.1^3), now voltage = ',voltage/100,'[V]'
40	format(a, i5, a, f7.2)

74	write(*,*) 'continue? y (Yes) or n (No)'
	read(*,*) answer
		if (answer == 'y') then
			write(*,*) 'input 5th step delta Ve [V]'
			read(*,*) deltaVe
			write(*,*) 'input d [mm] (space between electrodes)'
			read(*,*) de
			write(*,*) 'input a [mm] (thickness of electrode)'
			read(*,*) ae
			write(*,*) 'input number of 5th step'
			read(*,*) stepe
		else if (answer == 'n') then
			distance = distance + caldd
			go to 80
		else
			go to 74
		end if
	
	caldeltaVe = deltaVe * 100
	calde = de * 10
	calae = ae * 10
	do i = 1, stepe
		distance = distance + calde
		voltage = voltage - caldeltaVe
		do j = calphibin, calphibout
			do k = 1, calae
				p = p + 1
				x(p) = distance + (k - 1)
				y(p) = j
				v(p) = voltage
			end do
		end do
		distance = distance + calae
	end do

	write(*,41) 'delta Ve = ',deltaVe,'[V], d = ',de,'[mm], a = ',ae,'[mm], ',stepe,' steps'
41	format(a, f5.2, a, f3.1, a, f3.1, a, i3)
	write(*,42) 'now nx = ',distance,'(grid size 0.1^3), now voltage = ',voltage/100,'[V]'
42	format(a, i5, a, f7.2)

75	write(*,*) 'continue? y (Yes) or n (No)'
	read(*,*) answer
		if (answer == 'y') then
			write(*,*) 'input 6th step delta Vf [V]'
			read(*,*) deltaVf
			write(*,*) 'input d [mm] (space between electrodes)'
			read(*,*) df
			write(*,*) 'input a [mm] (thickness of electrode)'
			read(*,*) af
			write(*,*) 'input number of 6th step'
			read(*,*) stepf
		else if (answer == 'n') then
			distance = distance + calde
			go to 80
		else
			go to 75
		end if
	
	caldeltaVf = deltaVf * 100
	caldf = df * 10
	calaf = af * 10
	do i = 1, stepf
		distance = distance + caldf
		voltage = voltage - caldeltaVf
		do j = calphibin, calphibout
			do k = 1, calaf
				p = p + 1
				x(p) = distance + (k - 1)
				y(p) = j
				v(p) = voltage
			end do
		end do
		distance = distance + calaf
	end do

	write(*,43) 'delta Vf = ',deltaVf,'[V], d = ',df,'[mm], a = ',af,'[mm], ',stepf,' steps'
43	format(a, f5.2, a, f3.1, a, f3.1, a, i3)
	write(*,44) 'now nx = ',distance,'(grid size 0.1^3), now voltage = ',voltage/100,'[V]'
44	format(a, i5, a, f7.2)

76	write(*,*) 'continue? y (Yes) or n (No)'
	read(*,*) answer
		if (answer == 'y') then
			write(*,*) 'input 7th step delta Vg [V]'
			read(*,*) deltaVg
			write(*,*) 'input d [mm] (space between electrodes)'
			read(*,*) dg
			write(*,*) 'input a [mm] (thickness of electrode)'
			read(*,*) ag
			write(*,*) 'input number of 7th step'
			read(*,*) stepg
		else if (answer == 'n') then
			distance = distance + caldf
			go to 80
		else
			go to 76
		end if
	
	caldeltaVg = deltaVg * 100
	caldg = dg * 10
	calag = ag * 10
	do i = 1, stepg
		distance = distance + caldg
		voltage = voltage - caldeltaVg
		do j = calphibin, calphibout
			do k = 1, calag
				p = p + 1
				x(p) = distance + (k - 1)
				y(p) = j
				v(p) = voltage
			end do
		end do
		distance = distance + calag
	end do

	write(*,45) 'delta Vg = ',deltaVg,'[V], d = ',dg,'[mm], a = ',ag,'[mm], ',stepg,' steps'
45	format(a, f5.2, a, f3.1, a, f3.1, a, i3)
	write(*,46) 'now nx = ',distance,'(grid size 0.1^3), now voltage = ',voltage/100,'[V]'
46	format(a, i5, a, f7.2)

	distance = distance + dg
80	write(*,*) 'input tale-length lc [mm]'		!! 最後のグランド電位部分の構成
	read(*,*) lc
	write(*,*) 'input aperture size phic [mm]'
	read(*,*) phic

	callc = lc * 10
	calphic = phic * 10/2
	voltage = 0
	do i = calphibin, calphibout
		do j = 1, callc
			p = p + 1
			x(p) = distance + (j - 1)
			y(p) = i
			v(p) = voltage
		end do
	end do

	distance = distance + callc
	do i = calphic, calphibout
		do j = 1, 10
			p = p + 1
			x(p) = distance + (j - 1)
			y(p) = i
			v(p) = voltage
		end do
	end do

	distance = distance + 10

	nx = distance
	ny = calphibout + 1

	open(18, file='test.patxt', status='replace')		!! .patxtファイルの出力

	! === PATXTファイル書き出し(ヘッダー) ===
	write (18,*) '# ASCII text representation of a SIMION PA file.'
	write (18,*) 'begin_potential_array'
	write (18,*) 'begin_header'
	write (18,*) '    mode -1'
	write (18,*) '    symmetry cylindrical'
	write (18,*) '     max_voltage 500000'
	write (18,21) '     nx ', nx
21	format(a, i5)
	write (18,22) '     ny ', ny
22	format(a, i3)
	write (18,*) '    nz 1'
	write (18,*) '    mirror_x 0'
	write (18,*) '    mirror_y 1'
	write (18,*) '    mirror_z 0'
	write (18,*) '    field_type electrostatic'
	write (18,*) '    ng 100'
	write (18,*) '    dx_mm 0.1'
	write (18,*) '    dy_mm 0.1'
	write (18,*) '    dz_mm 0.1'
	write (18,*) '    fast_adjustable 0'
	write (18,*) '    data_format x y z is_electrode potential'
	write (18,*) 'end_header'
	write (18,*) 'begin_points'

	! === 各電極情報書き出し ===
	do i = 1, p
		write (18, 99) x(i), y(i), ' 0 1 ', v(i)
99		format(i5, i4, a, f8.1)
	end do

	! === PATXTファイル書き出し(フッター) ===
	write (18,*) 'end_points'
	write (18,*) 'end_potential_array'

	close(18)

end program gradpotent

