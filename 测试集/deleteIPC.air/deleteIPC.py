# -*- encoding=utf8 -*-
__author__ = "zhongdd"

from airtest.core.api import *

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

stop_app("com.bosma.smarthome")
start_app("com.bosma.smarthome")
sleep(5)

def login():
    sleep(5)
    poco("com.bosma.smarthome:id/et_account").set_text("1451953028@qq.com")
    poco("com.bosma.smarthome:id/et_pwd").set_text("zdd123456")
    poco("com.bosma.smarthome:id/btn_login").click()
    
#如果已经登录，执行格式化SDCard操作
if poco(text="博冠智能").exists():
    sleep(1)
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()  
    sleep(3)
    if exists(Template(r"tpl1541051036321.png", record_pos=(0.424, -0.61), resolution=(1080, 1920))):
         #进入设备设备页面
        poco("com.bosma.smarthome:id/iv_livelist_right_setting").click()
        #滑动页面至底部查找“SD卡存储”选项,并点击"格式化存储卡"按钮
        poco.swipe([100/1920,950/1080],[100/1920,300/1080])
        poco("com.bosma.smarthome:id/btn_remove").click()
        #先点击取消按钮
        poco("com.bosma.smarthome:id/btnRight").click()
        #再进行删除确认操作
        poco("com.bosma.smarthome:id/btn_remove").click()
        poco("com.bosma.smarthome:id/btnLeft").click()
        #刷新之后进入设备列表查看设备是否已经删除
        poco.swipe([100/1920,950/1080],[100/1920,300/1080])
        poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()
        assert_exists(Template(r"tpl1541405725527.png", record_pos=(0.0, 0.336), resolution=(1080, 1920)),"删除ipc成功")

    else:
        poco("转到上一层级").click()


    
#如果还没登录，先执行登录，再执行格式化SDCard操作
else:
    login()
    sleep(1)
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()  
    sleep(3)
    if exists(Template(r"tpl1541051036321.png", record_pos=(0.424, -0.61), resolution=(1080, 1920))):
         #进入设备设备页面
        poco("com.bosma.smarthome:id/iv_livelist_right_setting").click()
        #滑动页面至底部查找“SD卡存储”选项,并点击"格式化存储卡"按钮
        poco.swipe([100/1920,950/1080],[100/1920,300/1080])
        poco("com.bosma.smarthome:id/btn_remove").click()
        #先点击取消按钮
        poco("com.bosma.smarthome:id/btnRight").click()
        #再进行删除确认操作
        poco("com.bosma.smarthome:id/btn_remove").click()
        poco("com.bosma.smarthome:id/btnLeft").click()
        #刷新之后进入设备列表查看设备是否已经删除
        poco.swipe([100/1920,950/1080],[100/1920,300/1080])
        poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()
        assert_exists(Template(r"tpl1541405725527.png", record_pos=(0.0, 0.336), resolution=(1080, 1920)),"删除ipc成功")

    else:
        poco("转到上一层级").click()






