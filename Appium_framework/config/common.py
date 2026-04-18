import os.path

import yaml
from appium.options.android import UiAutomator2Options
from appium import webdriver


def desired_caps():
    # 1.获取配置信息
    # 获取配置文件目录
    yaml_dir = os.path.dirname(__file__)
    # 获取完整路径
    yaml_path = os.path.join(yaml_dir, 'iqooneo5_conf.yaml')
    # 打开yaml文件
    yaml_file = open(yaml_path, 'r', encoding='utf-8')
    # 解析yaml文件
    data = yaml.load(yaml_file, Loader=yaml.FullLoader)

    capabilities = {}
    capabilities['platformName'] = data['platformName']
    capabilities['platformVersion'] = data['platformVersion']
    capabilities['deviceName'] = data['deviceName']
    capabilities['app'] = 'D:/Android/AppPackages/qq.apk'
    capabilities['appPackage'] = 'com.tencent.mobileqq'
    capabilities['appActivity'] = 'com.tencent.mobileqq.activity.SplashActivity'
    capabilities['noRest'] = 'false'

    yaml_file.close()

    appium_server_url = 'http://127.0.0.1:4723/wd/hub'

    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    driver.implicitly_wait(10)
    return driver