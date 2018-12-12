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

   
def changeDeviceNanme():
    sleep(2)
    #进入设备设备页面
    poco("com.bosma.smarthome:id/iv_livelist_right_setting").click()
    sleep(1)
    #点击修改名称小图标，并设置名称字符
    poco("com.bosma.smarthome:id/tv_device_name").click()
    poco("com.bosma.smarthome:id/et_devname_input").set_text("aaaa")
    #返回上一层进行保存
    poco("转到上一层级").click()
    #返回到首页进行刷新
    poco("转到上一层级").click()
    poco("转到上一层级").click()
    poco.swipe([100/1920,300/1080],[100/1920,900/1080])
    sleep(3)
    
#如果已经登录，执行修改设备名称操作
if poco(text="博冠智能").exists():
    sleep(1)
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click() 
    #如果有设备，就进行设备列表里的第一个设备的修改名称
    
    if exists(Template(r"tpl1541040369573.png", record_pos=(0.424, -0.619), resolution=(1080, 1920))):
        changeDeviceNanme() 
        poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()
        sleep(2)
        assert_exists(Template(r"tpl1542351090758.png", record_pos=(-0.094, -0.589), resolution=(1080, 1920)),"修改成功")
    else:
        poco("转到上一层级").click()


    
#如果还没登录，先执行登录
else:
    commom_login()
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click() 
    if exists(Template(r"tpl1541040369573.png", record_pos=(0.424, -0.619), resolution=(1080, 1920))):

        changeDeviceNanme() 
        poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()
        sleep(2)
        assert_exists(Template(r"tpl1542351090758.png", record_pos=(-0.094, -0.589), resolution=(1080, 1920)),"修改成功")


    else:
        poco("转到上一层级").click()



