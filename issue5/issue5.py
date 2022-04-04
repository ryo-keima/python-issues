#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from config import logging_config  # loggingの設定を読み込むためimportしている
from chrome_driver import ChromeDriver

logger = logging.getLogger(__name__)


def main():
    """
    [目標]
    Pythonのクラスについて理解を深めよう!

    [課題]
    LancersのHPから、仕事情報を取得して、CSVファイルとして出力してみよう!
    https://www.lancers.jp/work/search?open=1&ref=header_menu

    [スクレイピング&ファイル出力する情報]
    - 記事タイトル
    - 記事URL
    - 投稿者名
    - 投稿者URL

    [条件]
    1. chrome_driver.pyを利用してスクレイピングしてみよう!(足りないメソッドがあったら実装してみよう!)
    2. output.pyのOutputクラスにファイルの出力に関する処理を実装してみよう!
    """

    logger.info("Start")

    chrome_driver = ChromeDriver()
    chrome_driver.open_url(
        "https://www.lancers.jp/work/search?open=1&ref=header_menu")

    # 以下に続きを実装してみよう！

    chrome_driver.close_driver()


if __name__ == "__main__":
    main()
