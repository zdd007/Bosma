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
start_app("com.bosma.smarthome")
sleep(5)


#进入分享列表页面
def findPage_ShareDevice():
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()
    poco("com.bosma.smarthome:id/iv_livelist_right_setting").click()
    poco(text="设备分享").click()
    
#如果已经登录，直接分享
if poco(text="博冠智能").exists():
    sleep(2)
    #进入ipc设备列表
    findPage_ShareDevice()
    sleep(2)
    if exists(Template(r"tpl1541038164678.png", record_pos=(0.307, -0.592), resolution=(1080, 1920))):
        poco("com.bosma.smarthome:id/tv_swipe_status").swipe([-0.4892, 0.0])
        poco("com.bosma.smarthome:id/tv_swipe_delete").click()
        assert_exists(Template(r"tpl1541038362006.png", record_pos=(-0.002, -0.747), resolution=(1080, 1920)),"删除成功")
    else:
        poco("转到上一层级").click()
    
#如果还没登录，先执行登录，再分享
else:
    commom_login()
    sleep(2)
    findPage_ShareDevice()
    sleep(2)
    if exists(Template(r"tpl1541038164678.png", record_pos=(0.307, -0.592), resolution=(1080, 1920))):
        poco("com.bosma.smarthome:id/tv_swipe_status").swipe([-0.4892, 0.0])
        poco("com.bosma.smarthome:id/tv_swipe_delete").click()
        assert_exists(Template(r"tpl1541038362006.png", record_pos=(-0.002, -0.747), resolution=(1080, 1920)),"删除成功")

    else:
        poco("转到上一层级").click()


