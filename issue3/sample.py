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
    pip install -r requirements.txt
"""

import time

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def create_chrome_driver():

    options = ChromeOptions()
    # UserAgent
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
    options.add_argument('--ignore-ssl-errors')
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["acceptInsecureCerts"] = True
    options.add_argument("--window-size=1400,900")
    options.add_argument('--incognito')
    options.add_experimental_option("detach", True)

    return Chrome(executable_path=ChromeDriverManager().install(),
                  options=options,
                  desired_capabilities=capabilities)


def main():

    # driverを生成
    driver = create_chrome_driver()

    # URLを開く
    driver.get("https://www.amazon.co.jp/")

    # 検索フォームにキーワードを入力する
    keyword = "ねこ"
    form_element = driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
    form_element.send_keys(keyword)
    time.sleep(1)

    # 検索ボタンをクリックする
    search_button_element = driver.find_element(
        By.CSS_SELECTOR, "#nav-search-submit-button")
    search_button_element.click()
    time.sleep(3)

    # 検索結果から商品名を取得する
    elements = driver.find_elements(By.CSS_SELECTOR, ".a-size-base-plus.a-color-base.a-text-normal")
    for element in elements:
        print(element.text)
        print("###########")

    # driverを削除する
    driver.close()
    driver.quit()


if __name__ == "__main__":
    main()
