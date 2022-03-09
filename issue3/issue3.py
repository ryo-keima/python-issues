#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    """
    ここにスクレイピングのプログラムを実装してみよう！
    """

    # driverを削除する
    driver.close()
    driver.quit()

if __name__ == "__main__":
    main()
