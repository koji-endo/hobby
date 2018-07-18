Sub PDF形式で保存()
 
	Dim myFileName As String 'ファイル名
	Dim myFilePath As String '保存先のフォルダパス
	Dim myDoc As Document
	Dim intPos As Integer'ピリオドの位置

	Set myDoc = ActiveDocument

	'拡張子のない名称を取得
	myFileName = myDoc.Name
	intPos = InStrRev(myFileName, ".")
	myFileName = Left(myFileName, intPos - 1)

	'PDFファイルで保存
	myFilePath = myDoc.Path'Wordファイルと同じフォルダ
	myDoc.ExportAsFixedFormat _
	OutputFileName:=myFilePath & "\" & myFileName & ".pdf", _
	ExportFormat:=wdExportFormatPDF

	Set myDoc = Nothing

End Sub
