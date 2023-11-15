# Drft2List-Lite-StrmLit

App URL: https://3centi-drft2list-lite-strmlit-main-cj7uyx.streamlit.app/

var. 1.0

## 使い方・概要・作成背景

### 使い方

こちらの Notion サイトから確認することもできます。
https://marked-jaborosa-40b.notion.site/Draft-to-List-Lite-f5f3e4872df14b2e83c3ca8bf2fb2b32

1. "Enter password/パスワードを入力"のところにパスワードを入力し、エンターを押す。
2. "Drag and drop file here"に指定の CSV ファイルをドラッグ&ドロップする。（上記の Notion サイトにサンプルデータがあります）
3. エラー(UnicodeDecodeError)が出ている場合は、左のサイドバーの"Encoding/文字コード"を違う文字コードにする。(デフォルトは UTF-8 ですが、特に Windows 上で Excel を CSV に変換した場合は、文字コードを CP932 にするとエラーが消える場合があります)
4. "Download the list as ~~"をクリックすると、下にプレビューされている表の CSV ファイルがダウンロードされます。

### 概要

この Web アプリでは、以下の様式の生徒名簿（以下、ドラフト）をリストに変換します。

_イメージ_

ドラフト

![sample_draft_image](https://github.com/3centi/Drft2List-Lite-StrmLit/assets/104761003/d25d1dc7-d34d-4538-82a4-2fcc659617cd)

(注意:上記の画像にある表は Excel ですが、実際にリストに変換をする際には、事前に CSV に変換させる必要があります)

**↓ 変換**

リスト
| No | 氏名 | クラス | 曜日 | 時間 | 教室 | 先生 |
| --- | ----- | ------ | ---- | ---- | ---- | ---- |
| 1 | Lucia | E2 | Tue | 1600 | 101 | Jobs |
| 2 | Emily | E2 | Tue | 1600 | 101 | Jobs |
| ︙ | ︙ | ︙ | ︙ | ︙ | ︙ | ︙ |

### 作成背景

作成者である私が勤めているバイト先では、主に上記のドラフトを使用して在籍生徒の管理をしています。ただしこのような様式のままでは、Microsoft Word の差し込み印刷や名前シールの作成などの際に不便でした。そのため、差し込み印刷や名前シール作成をしやすいリストの様式に変換するアプリを作成しました。

## 使用言語・OS・バージョン

### 使用言語

Python 3.9

### 使用した外部ライブラリ

Streamlit

## 環境構築の手順（ローカル環境でも使用する場合）

### python3.9 など(anaconda)のインストール

省略

### streamlit のインストールと使用方法について

次の公式サイトをご確認ください:
https://docs.streamlit.io/library/get-started
