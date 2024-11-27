import sys

def main():
    try:
        # 標準入力から値を受け取る
        input_value = sys.stdin.read().strip()
        # 数値に変換して2乗を計算
        number = float(input_value)
        result = number ** 2
        # 結果を出力
        print(result)
    except ValueError:
        # 数値以外が入力された場合のエラーメッセージ
        print("Error: 入力は数値である必要があります。")

if __name__ == "__main__":
    main()
