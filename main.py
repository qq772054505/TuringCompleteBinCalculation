import cv2
import numpy as np
import pyautogui
import time
from pathlib import Path

def find_buttons_and_click(target_values):
    # 捕获屏幕
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    # 对于每个目标值，我们需要找到对应的按钮
    for value in target_values:
        # 这里假设我们已经有了按钮的模板图片，需要将其加载进来
        fileName = f'unselected_{value}.jpg'
        filePath = Path("./Resource") / fileName
        template = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)
        w, h = template.shape[::-1]
        # 将屏幕截图转换为灰度图像
        gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        print(f"读取{fileName}成功")


        # # 模板匹配
        # res = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
        # threshold = 0.8
        # loc = np.where(res >= threshold)

        # # 对于每个找到的位置，执行点击操作
        # for pt in zip(*loc[::-1]):
        #     center_x, center_y = pt[0] + w//2, pt[1] + h//2
        #     pyautogui.click(center_x, center_y)
        #     print(f"Clicked on button {value} at ({center_x}, {center_y})")
        #     time.sleep(0.5)  # 稍作延迟以模拟人类操作

# 假设我们要点击的按钮值
values_to_click = [128, 64, 32, 16, 8, 4, 2, 1]
find_buttons_and_click(values_to_click)
