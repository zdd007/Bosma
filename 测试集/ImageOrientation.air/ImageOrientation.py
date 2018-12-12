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
   
#如果已经登录，先退出登录，再进入忘记密码页面
if poco(text="博冠智能").exists():
    sleep(1)
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()  
    sleep(1)
    if exists(Template(r"tpl1541051036321.png", record_pos=(0.424, -0.61), resolution=(1080, 1920))):
         #进入设备设置页面
        poco("com.bosma.smarthome:id/iv_livelist_right_setting").click()
        poco(text="旋转图像").click()
        poco(text="垂直翻转").click()
        poco("转到上一层级").click()
        sleep(3)
        poco(text="旋转图像").click()
        sleep(2)
        assert_exists(Template(r"tpl1542175836080.png", record_pos=(-0.001, -0.394), resolution=(1080, 1920)),"垂直翻转设置成功")
        poco(text="水平翻转").click()
        poco("转到上一层级").click()
        sleep(3)
        poco(text="旋转图像").click()
        sleep(2)
        assert_exists(Template(r"tpl1542176057190.png", record_pos=(-0.006, -0.191), resolution=(1080, 1920)),"水平翻转设置成功")
        poco(text="180°翻转").click()     
        poco("转到上一层级").click()
        sleep(3)
        poco(text="旋转图像").click()
        sleep(2)
        assert_exists(Template(r"tpl1542176164727.png", record_pos=(-0.011, 0.003), resolution=(1080, 1920)),"180度翻转设置成功")
       
    else:
        poco("转到上一层级").click()


      
#如果没有登录，先进行登录
else:
    commom_login()
    sleep(1)
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()  
    sleep(1)
    if exists(Template(r"tpl1541051036321.png", record_pos=(0.424, -0.61), resolution=(1080, 1920))):
         #进入设备设置页面
        poco("com.bosma.smarthome:id/iv_livelist_right_setting").click()
        poco(text="旋转图像").click()
        poco(text="垂直翻转").click()
        poco("转到上一层级").click()
        sleep(3)
        poco(text="旋转图像").click()
        sleep(2)
        assert_exists(Template(r"tpl1542175836080.png", record_pos=(-0.001, -0.394), resolution=(1080, 1920)),"垂直翻转设置成功")
        poco(text="水平翻转").click()
        poco("转到上一层级").click()
        sleep(3)
        poco(text="旋转图像").click()
        sleep(2)
        assert_exists(Template(r"tpl1542176057190.png", record_pos=(-0.006, -0.191), resolution=(1080, 1920)),"水平翻转设置成功")
        poco(text="180°翻转").click()     
        poco("转到上一层级").click()
        sleep(3)
        poco(text="旋转图像").click()
        sleep(2)
        assert_exists(Template(r"tpl1542176164727.png", record_pos=(-0.011, 0.003), resolution=(1080, 1920)),"180度翻转设置成功")
       
    else:
        poco("转到上一层级").click()

