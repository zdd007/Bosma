# -*- encoding=utf8 -*-
__author__ = "zhongdd"

from airtest.core.api import *

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

stop_app("com.bosma.smarthome")
sleep(2)
start_app("com.bosma.smarthome")
sleep(5)

def login():
    sleep(2)
    poco("com.bosma.smarthome:id/et_account").set_text("1451953028@qq.com")
    poco("com.bosma.smarthome:id/et_pwd").set_text("zdd123456")
    poco("com.bosma.smarthome:id/btn_login").click()
    
def FormatSDCard():    
    poco(text="格式化存储卡").click()
    sleep(1)
    #点击对话框的取消按钮
    poco(text="取消").click()
    #再进行一次格式化操作
    poco(text="格式化存储卡").click()
    poco(text="确定").click()
    
    
#如果已经登录，执行格式化SDCard操作
if poco(text="博冠智能").exists():
    sleep(1)
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()  
    sleep(3)
    if exists(Template(r"tpl1541051036321.png", record_pos=(0.424, -0.61), resolution=(1080, 1920))):
         #进入设备设备页面
        poco("com.bosma.smarthome:id/iv_livelist_right_setting").click()
        #滑动页面至底部查找“SD卡存储”选项,并点击"格式化存储卡"按钮
        poco.swipe([100/1920,800/1080],[100/1920,300/1080])
        poco(text="SD卡存储").click()
        if exists(Template(r"tpl1541128530234.png", record_pos=(0.015, 0.044), resolution=(1080, 1920))):
            poco("转到上一层级").click()
        else:      
            FormatSDCard() 
            assert_exists(Template(r"tpl1541049789801.png", record_pos=(0.01, 0.073), resolution=(1080, 1920)),"正在格式化大概60秒")
            sleep(60)
            assert_exists(Template(r"tpl1541050002568.png", record_pos=(0.014, -0.756), resolution=(1080, 1920)),"格式化成功")

    else:
        poco("转到上一层级").click()


    
#如果还没登录，先执行登录，再执行格式化SDCard操作
else:
    login()
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click() 
    sleep(3)
    if exists(Template(r"tpl1541051036321.png", record_pos=(0.424, -0.61), resolution=(1080, 1920))):
          #进入设备设备页面
        poco("com.bosma.smarthome:id/iv_livelist_right_setting").click()
        #滑动页面至底部查找“SD卡存储”选项,并点击"格式化存储卡"按钮
        poco.swipe([100/1920,800/1080],[100/1920,300/1080])
        poco(text="SD卡存储").click()
        if exists(Template(r"tpl1541128530234.png", record_pos=(0.015, 0.044), resolution=(1080, 1920))):
            poco("转到上一层级").click()
        else:      
            FormatSDCard() 
            assert_exists(Template(r"tpl1541049789801.png", record_pos=(0.01, 0.073), resolution=(1080, 1920)),"正在格式化大概60秒")
            sleep(60)
            assert_exists(Template(r"tpl1541050002568.png", record_pos=(0.014, -0.756), resolution=(1080, 1920)),"格式化成功")

    else:
        poco("转到上一层级").click()





