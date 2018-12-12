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

 
def commom():
    #进入设备设备页面
    poco("com.bosma.smarthome:id/iv_livelist_right_setting").click()
    poco.swipe([100/1920,800/1080],[100/1920,300/1080])    
    #poco(text="事件").click()
    poco("com.bosma.smarthome:id/ci_online_alerts").child("android.widget.LinearLayout").click()
    sleep(2)
    poco(text="从不").click()
    poco("转到上一层级").click()
    sleep(2)
    # poco(text="事件").click()#这个？对当然不行，有两个事件的textpoco("com.bosma.smarthome:id/tb_common_toolbar")
    poco("com.bosma.smarthome:id/ci_online_alerts").child("android.widget.LinearLayout").click()

    sleep(2) 
    assert_exists(Template(r"tpl1542351946712.png", record_pos=(-0.006, -0.476), resolution=(1080, 1920)),"从不录像设置成功")        
    poco(text="仅侦测事件发生时").click()
    poco("转到上一层级").click()
    sleep(2)   
    poco("com.bosma.smarthome:id/ci_online_alerts").child("android.widget.LinearLayout").click()
    #poco(text="事件").click()
    sleep(2)
    assert_exists(Template(r"tpl1544062192428.png", record_pos=(-0.003, -0.237), resolution=(1440, 2560)),"仅侦测事件发生时录像设置成功")
    poco(text="全时录像").click()
    poco("转到上一层级").click()
    sleep(2)   
    poco("com.bosma.smarthome:id/ci_online_alerts").child("android.widget.LinearLayout").click()
    #poco(text="事件").click()
    sleep(2)
    assert_exists(Template(r"tpl1542352058621.png", record_pos=(-0.29, -0.022), resolution=(1080, 1920)),"全时录像设置成功")

    
#如果已经登录，执行格式化SDCard操作
if poco(text="博冠智能").exists():
    sleep(1)
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()  
    sleep(3)
    if exists(Template(r"tpl1541051036321.png", record_pos=(0.424, -0.61), resolution=(1080, 1920))):
        commom()
        
        
    else:
        poco("转到上一层级").click()
        assert_exists(Template(r"tpl1544062278615.png", record_pos=(0.006, -0.747), resolution=(1440, 2560)),"账号下没有设备")
        
else:
    commom_login()
    sleep(1)
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()  
    sleep(3)
    if exists(Template(r"tpl1541051036321.png", record_pos=(0.424, -0.61), resolution=(1080, 1920))):
        commom()                
    else:
        poco("转到上一层级").click()
        assert_exists(Template(r"tpl1544062278615.png", record_pos=(0.006, -0.747), resolution=(1440, 2560)),"账号下没有设备")




