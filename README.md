# 英明的健康打卡机制现在已经不要求了，辅导员不催了，综测也不扣了，总之没声了。估计也不太可能再实行。这个库可以归档了。


# 简介

* 基于pyautogui开发的自动完成兰州大学每日健康打卡，并通过pushplus推送结果。
* 随机延迟(30分钟内，可修改)
* 自动重试(2小时，可修改)

# 使用方法

1. clone 或者下载本仓库
2. 将browser_icon.png![browser_icon.png](assets/browser_icon-20220504224650-8cs4itb.png)改为您的浏览器图标。（您可以使用win + s截屏）
3. 选取一个您浏览器输入框左侧的图标，如火狐浏览器可以选择主页按钮。将input_field1.png替换为该图标。(若无法正常输入，请修改mouse(input_field1, offset=180)中offset 处的数值，该数值为向左偏移距离。）

    ![image.png](assets/image-20220504224936-a7aea8h.png)
4. 您可以将您的账号密码存入浏览器中以自动输入。截图后替换account.png。  
    ​![account.png](assets/account-20220504225224-trkv4fo.png)
5. 截取您浏览器的关闭按钮，替换close.png  
    ​![close.png](assets/close-20220504225304-lnzqi60.png)
6. ![image.png](assets/image-20220504225404-z2lkl0t.png)右键单击开始。点击“计算机管理”。
7. 点击“任务计划程序”![image.png](assets/image-20220504225535-p88b4s0.png)
8. 点击右侧“创建任务”  
    ​![image.png](assets/image-20220504225634-om3kc4e.png)
9. 输入名称，描述（可以不输入）
10. 依次点击操作，新建。
11. “程序或脚本”处输入您python解释器的位置，参数为main.py，“起始于”处输入main.py所在位置。  
     ​![image.png](assets/image-20220504225801-5jhptdo.png)
12. 点击确定。
13. 点击触发器，设置时间和重复次数。![image.png](assets/image-20220504230151-tgecjuw.png)
14. 点击确定。
15. 再次点击确定，完成。

# 结果推送功能（可选）

1. 进入push plus 官网。 [www.pushplus.plus](https://www.pushplus.plus/)![image.png](assets/image-20220504230629-7wnvq73.png)
2. 注册并登录。
3. 点击一对一推送。![image.png](assets/image-20220504230718-6ig05t9.png)
4. 复制token，黏贴至token = ''处，保存。  
    ​![image.png](assets/image-20220504230947-wfmthij.png)


# TO-DO

* mac，Linux适配
