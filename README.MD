# ATCODER-ACTIVITY
 
atcoder関連の私的活動記録


# 環境

## Atcoder側
- 言語:Python3
- 言語処理系:PyPy3 まれに Python3

PyPyはjitコンパイラで最適化しているので、最適化をしないPython(より正確にはCPython, Cythonではない)より基本早くなります。


一部Pythonのほうが早いケースがありますが、特性理解やパラメータ設定してあげればPythonが必要なケースはあまりない認識です。例えば再帰関数はPyPyそのままだと苦手ですが、スタックで代用 or `pypyjit.set_param("max_unroll_recursion=-1")`でjitコンパイラの挙動を設定することで十分な速度を稼げます。

ただ、GCの仕組みの違いや、最適化にかかる初期時間・メモリ消費等でどうしようもない時があるので、そういうときはPython使います。（文字列処理でちょいちょい起きる認識）

## ローカル側

- OS: Windows 10 + WSL2-Ubuntu18.04
- エディタ: VSCode + Remote Development
- 言語処理系：pyenv+venv　-> Python3.8.2, PyPy3.7-7.3.0

当初はWin環境直でpylauncherとvenvで組んでましたが、Winだと後述するatcoder-toolsがテストが動かないので（ソース読む限り実行可能ファイルを選択する手法がwinとlinuxで違っているためとみられる）、こういった構成にしています。

ただ、pyenvは追加インストールとかパスの設定とかが必要でややこしいのに対して、winのpython公式同梱のpylauncherがpythonのマイナーバージョン（3.8と3.10とか。3.8.2と3.8.5とかは×）までなら環境が併存できるので好きです。

venvはlinuxでもwinでも標準ライブラリに入っている仮想環境作成ツールなので、特にOSがpythonに依存してしまっているubuntuでは環境分離のために使った方がいいです。(atcoderで入るライブラリ程度ではどうこうないと思いますが、習慣としておすすめします。)

また、ubuntu20.04ならOS同梱のPython3.8.2でatcoder側のバージョンと同じなので、pyenv無しでvenvだけで大丈夫だと思います。

# その他

## atcoder-toolsの利用

atcoderをする上での強力な支援ツールです。atcoder-cli同様、test setの取得や提出ができるほか、こやつの強力なところは、
下記みたいな感じで問題文を解析して標準入力を適切な変数に設定するところまでコードを自動生成してくれます。

```Python
#!/usr/bin/env python3
import sys

def solve(N: int, D: "List[int]", C: "List[int]", S: "List[int]"):

    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = [int()] * (N)  # type: "List[int]"
    C = [int()] * (N)  # type: "List[int]"
    S = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        D[i] = int(next(tokens))
        C[i] = int(next(tokens))
        S[i] = int(next(tokens))
    solve(N, D, C, S)


if __name__ == "__main__":
    main()
```

…で、強力なのは確かなのですが、問題文が複雑で生成に失敗したり、自動生成された部分起因でたまにばぐったりするので、（たぶん入力バッファのサイズの問題）、そのあたり特性を理解して使える必要があります。

という訳で私は時間制限のあるRatedやバーチャルコンテストでは使ったことはありません。過去問解くとき用のちょっとした時間削減といった位置づけです。

また、後続のsnippet利用を使うと入力部分を大幅に削れて優位性が薄れていることを考えると、機能的に簡素なatcoder-cliに移行しようか悩み中です。



## VSCodeのSnippetの利用

要は辞書登録です。`.vscode/python.code-snippets` に下記のように記載すると、`mii` とタイプして出てくるサジェストを選べば `A,B=map(int,input().split())` と出てきます。入力周りはほぼ形が決まっているので、タイプ量を減らすのもそうですが、しょうもないミスを回避におすすめです。

```json
{
	"multi int input": {
		"prefix": [
			"mii"
		],
		"body": [
			"${1:A,B}=map(int,input().split())"
		],
		"description": "multi int input"
	},
}
```

ただ、たまに想定外の入力に対処することを考えると、初心者の方はいきなりこれに頼るより、ある程度入力受付のコードの意味を理解してある程度応用力がついてから手を出すべきだと考えます。


## gitの利用

バージョン管理ツールです。別に複雑な開発をするわけではないので必須ではないのですが、自力回答でcommitしておいて、解説閲覧後のコードとの差分をとるなどいろいろ便利です。

また、手元にデスクトップPCとノートPCの両方で作業するケースがあるので、github.com経由でコードを共有しています。

当初はonedrive経由で共有していたのですが、ダウンロードが地味に時間がかかるのが嫌だったのと、冒頭Win->WSL2への環境移行時に、WSL2側から(onedriveフォルダのある)win側のファイルにアクセスするのは非常に低速な関係でgithub経由に移行しました。