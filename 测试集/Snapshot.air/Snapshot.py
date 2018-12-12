# -*- encoding=utf8 -*-
__author__ = "zhongdd"

from airtest.core.api import *
from airtest.core.api import using
using("commomLogin.air")
from commomLogin import commom_login

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

stop_app("com.bosma.smarthome")
sleep(2)
start_app("com.bosma.smarthome")
sleep(5)

#如果已经登录，执行格式化SDCard操作
if poco(text="博冠智能").exists():
    sleep(1)
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()  
    sleep(3)
    if exists(Template(r"tpl1541051036321.png", record_pos=(0.424, -0.61), resolution=(1080, 1920))):
        #点击进入liveview页面
        poco("com.bosma.smarthome:id/iv_liveview").click()
        sleep(5)
        if exists(Template(r"tpl1541403140125.png", record_pos=(-0.002, -0.386), resolution=(1080, 1920))):
            poco("转到上一层级").click()
        else:
            poco("com.bosma.smarthome:id/rb_capture").click()      
            assert_exists(Template(r"tpl1541403372476.png", record_pos=(0.135, 0.502), resolution=(1080, 1920)),"截图成功")
    
#如果还没登录，先执行登录，再执行格式化SDCard操作
else:
    commom_login()
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()  
    sleep(3)
    if exists(Template(r"tpl1541051036321.png", record_pos=(0.424, -0.61), resolution=(1080, 1920))):
        #点击进入liveview页面
        poco("com.bosma.smarthome:id/iv_liveview").click()
        sleep(5)
        if exists(Template(r"tpl1541403140125.png", record_pos=(-0.002, -0.386), resolution=(1080, 1920))):
            poco("转到上一层级").click()
        else:
            poco("com.bosma.smarthome:id/rb_capture").click()      
            assert_exists(Template(r"tpl1541403372476.png", record_pos=(0.135, 0.502), resolution=(1080, 1920)),"截图成功")
    
