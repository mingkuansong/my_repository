import time

from appium.webdriver.common.appiumby import AppiumBy

from config.common import desired_caps

def login_test(username, password):
    print('进入测试用例函数')
    driver = desired_caps()
    # 进入登录界面
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="同意"]').click()
    driver.find_element(by=AppiumBy.ID, value='com.tencent.mobileqq:id/btn_login').click()
    time.sleep(3)
    driver.find_element(by=AppiumBy.ID, value='com.tencent.mobileqq:id/vdk').click()
    driver.find_element(by=AppiumBy.ID, value='com.tencent.mobileqq:id/ula').click()
    time.sleep(3)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.AutoCompleteTextView[@content-desc="请输入QQ号码或手机号或QID或邮箱"]').send_keys(username)
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@content-desc="密码 安全"]').send_keys(password)
    time.sleep(2)
    driver.find_element(by=AppiumBy.ID, value='com.tencent.mobileqq:id/ul0').click()
    time.sleep(3)
    try:
        driver.find_element(by=AppiumBy.ID, value='com.tencent.mobileqq:id/unu')
    except:
        print('登录失败！')
        return False
    else:
        print('登录成功')
        return True
