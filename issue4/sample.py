#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
< 準備 >
1. 仮想環境を構築(terminalで以下のコマンドを実行する)
    python -m venv venv

2. 仮想環境に入る(terminalで以下のコマンドを実行する)
    source venv/bin/activate

3. 仮想環境の中でライブラリをインストール(terminalで以下のコマンドを実行する)
    pip install --upgrade pip
    pip install requests
"""

import requests


def main():

    RAKUTEN_API_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    KEYWORD = "ねこ"

    payload = {
        # App ID
        "applicationId": "XXXXXXXXXXXXXXX",  # 自身のアプリIDを指定する
        # Page number
        "page": 1,
        # Keyword
        "keyword": KEYWORD
    }

    response = requests.get(RAKUTEN_API_URL, params=payload)
    items = response.json()

    for item in items["Items"]:
        # 商品名を取得
        item_name = item["Item"]["itemName"]
        print(item_name, end="\n\n")


if __name__ == "__main__":
    main()
