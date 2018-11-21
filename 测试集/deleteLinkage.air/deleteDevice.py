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
    
#进入外设列表页面
def findPage_linkage():
    poco(text="更多").click()

#进入ipc设备列表页面
def findPage_ipc():
    poco(text="网关").click()
    
#删除外设
def delete_linkage():
    sleep(2) 
    poco("com.bosma.smarthome:id/gv_scenes").child("com.bosma.smarthome:id/ll_item_container")[0].click() 
    #删除设备按钮
    poco("com.bosma.smarthome:id/btn_door_remove").click()
    #取消删除
    poco("com.bosma.smarthome:id/btnRight").click()
    #重新进行删除，点击确定按钮
    poco("com.bosma.smarthome:id/btn_door_remove").click()
    poco("com.bosma.smarthome:id/btnLeft").click()
    assert_exists(Template(r"tpl1540969536868.png", record_pos=(0.001, -0.751), resolution=(1080, 1920)),"删除成功")


    
#如果已经登录，直接发送反馈
if poco(text="博冠智能").exists():
    sleep(2)
    if exists(Template(r"tpl1540966192225.png", threshold=0.7, target_pos=5, rgb=True, record_pos=(-0.057, 0.08), resolution=(1080, 1920))):
        poco("转到上一层级").click()
    else:
        findPage_linkage()
        delete_linkage()
        sleep(2) 

#如果还没登录，先执行登录，再发送反馈
else:
    login()
    sleep(2)  
    if exists(Template(r"tpl1540966192225.png", threshold=0.7, target_pos=5, rgb=True, record_pos=(-0.057, 0.08), resolution=(1080, 1920))):
        poco("转到上一层级").click()
    else:
        findPage_linkage()
        delete_linkage()
        sleep(2) 



    