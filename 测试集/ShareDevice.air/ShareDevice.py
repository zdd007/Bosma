# -*- encoding=utf8 -*-
__author__ = "zhongdd"

from airtest.core.api import *

auto_setup(__file__)
from airtest.core.api import using
using("commomLogin.air")
from commomLogin import commom_login

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

stop_app("com.bosma.smarthome")
start_app("com.bosma.smarthome")
sleep(5)

#进入ipc设备列表
def findPage_IPC():
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()
    poco("com.bosma.smarthome:id/iv_livelist_right_setting").click()
    poco(text="设备分享").click()
    poco("com.bosma.smarthome:id/iv_toolbar_icon").click()

def commom():
    poco("com.bosma.smarthome:id/et_email").set_text("zengmq@bosma.com.cn")
    poco("com.bosma.smarthome:id/tv_toolbar_right_content").click()
    sleep(3)
    assert_exists(Template(r"tpl1540976380856.png", record_pos=(-0.011, -0.039), resolution=(1080, 1920)),"分享成功提示框出现！")
    #点击确定返回分享列表
    poco("com.bosma.smarthome:id/btnSingle").click()
    assert_exists(Template(r"tpl1544062975292.png", record_pos=(-0.201, -0.6), resolution=(1440, 2560)),"分享成功")


#如果已经登录，直接分享
if poco(text="博冠智能").exists():
    sleep(2)
    #进入ipc设备列表
    findPage_IPC()
    sleep(2)
    commom()
       
#如果还没登录，先执行登录，再分享
else:
    commom_login()
    sleep(2)
    findPage_IPC()
    sleep(2)
    commom()
    