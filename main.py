import pyautogui
from PIL import Image
import pyperclip
import requests
import json
import random
import time
import eventlet


def mouse(img, clicks_num=1, offset=0):
    for i in range(100):
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        if location is not None:
            pyautogui.click(location.x + offset, location.y, clicks=clicks_num, interval=0.2,
                            duration=0.2, button='left')
            break

        # print('Failed, try again in 0.1 seconds.')
        time.sleep(0.1)  # 0.1秒后重试
        # print('等待重试...' + str(i))
    else:
        start_reporting()


def start_reporting():
    # 读取图片
    browser_icon = Image.open('images/browser_icon.png')
    input_field1 = Image.open('images/input_field1.png')
    input_field2 = Image.open('images/input_field2.png')
    account = Image.open('images/account.png')
    login = Image.open('images/login.png')
    health_report = Image.open('images/health_report.png')
    enter_health_report = Image.open('images/enter_health_report.png')
    report = Image.open('images/report.png')
    close = Image.open('images/close.png')
    # 开始打卡
    mouse(browser_icon)
    mouse(input_field1, offset=180)
    pyperclip.copy('my.lzu.edu.cn')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    if pyautogui.locateCenterOnScreen(health_report, confidence=0.9) is None:
        mouse(input_field2)
        mouse(account)
        mouse(login)
    mouse(health_report, clicks_num=0)
    mouse(enter_health_report)
    mouse(report)
    mouse(close)
    push(True)  # 成功，推送相关结果
    quit()  # 结束程序


# 推送结果
def push(state):
    token = ''  # 在这里输入您的token，如您不需要可以忽略
    if token == '':
        return
    title_success = '自动健康打卡-成功'
    title_fail = '自动健康打卡-失败'
    content_success = '今日健康打卡已完成！'
    content_fail = '健康打卡失败，请尽快手动打卡！'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/79.0.3945.93 Mobile Safari/537.36",
        'Content-Type': 'application/json'
    }
    url = 'http://www.pushplus.plus/send'
    if state:
        # print(title_success)
        data = {'token': token, 'title': title_success, 'content': content_success, 'template': 'html'}
        res = requests.post(headers=headers, url=url, data=json.dumps(data), timeout=10)
    else:
        # print(title_fail)
        data = {'token': token, 'title': title_fail, 'content': content_fail, 'template': 'html'}
        res = requests.post(headers=headers, url=url, data=json.dumps(data), timeout=10)
    print(res.text)


# 30 分钟内的延迟
delay = random.uniform(1, 1800)
time.sleep(delay)

eventlet.monkey_patch()
try:
    with eventlet.Timeout(7200, True):  # 设置重试时间为两个小时
        start_reporting()
except eventlet.timeout.Timeout:
    push(False)  # 失败，推送相关结果
