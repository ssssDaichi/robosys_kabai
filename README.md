# robosys_kabai
ロボットシステム学 課題1
# 課題用リポジトリ

このリポジトリは、ロボットシステム学の課題で作成したものです。

## コマンドの説明

### 数値を2乗するコマンド

#### 概要
このスクリプトは、標準入力から受け取った数値を2乗し、その結果を標準出力に返します。

#### 使用方法
以下のように実行してください：
```bash
echo [数値] | python3 square_number.py

#### 例
入力が5の場合：echo 5 | python3 square_number.py
出力：25.0
入力が数値でない場合：echo "abc" | python3 square_number.py
出力：Error: 入力は数値である必要があります。
