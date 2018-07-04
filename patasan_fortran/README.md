# patasan_fortran
## Downloadするファイル
- np_grad_potent.py  
pythonである程度効率よく書いたプログラムです。いわばfortranからの意訳です。

- grad_potent.py  
pythonでfortranから逐語訳したプログラムですが、途中までで終わっています。基本的に逐語訳です。
- read_data1.csv  
よくあるカンマ区切りではなく、半角スペース区切りです。
“#”はコメントアウトとして扱われます。(np_grad_potent.pyの中で読み込み時にそうなるよう処理しています。)

## 実行の仕方
コマンドプロンプトで```cd```を使ってダウンロードしたファイルがあるところまで降りていって、
### csv読み込みモード
```python np_grad_potent.py read_data1.csv ```
と入力します。
### コマンドライン入力モード
```python np_grad_potent.py```
もし動かなかったら、エラー画面のスクショを送ってください。

## pythonの魅力
pythonの魅力はデバッグのしやすさです。
配列でもなんでもprint関数を使えば表示できるので、変数に何が格納されているか見ることが簡単です。
もう一つはインタラクティブシェルを使った実験のしやすさです。
例えばnumpyのライブラリ関数であるhstack関数ですが、
```python
>python
>import numpy as np
>a=range(10)
>b=range(5)
>a
>b
>np.hstack((a,b))
>#実行結果: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4])
```
とやるとhstack関数が何をする関数か目的どおりに動いてくれるかがわかります。>の後(>は含まない)を1行ずつコマンドプロンプトに打ち込んでいってください。
