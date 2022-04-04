#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


RAKUTEN_API_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"


def main():
    '''
    [課題]
    (1)
    楽天APIを使用して、以下の情報を取得してみよう!
    - 商品の価格
    - 商品のURL
    - 商品の説明
    - JANコード(難易度高: URLや商品説明欄から13桁の数値があった場合、それを取得するよう実装してみてください！)

    (2)
    結果をCSVファイルとして出力してみよう

    [準備]
    1. 仮想環境を構築(terminalで以下のコマンドを実行する)
        python -m venv venv

    2. 仮想環境に入る(terminalで以下のコマンドを実行する)
        source venv/bin/activate

    3. 仮想環境の中でライブラリをインストール(terminalで以下のコマンドを実行する)
        pip install --upgrade pip
        pip install requests
    '''


if __name__ == "__main__":
    main()
