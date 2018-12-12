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
    sleep(1)
    poco("转到上一层级").click()
    sleep(1)
    poco("com.bosma.smarthome:id/tv_menu_head_user_name").click()
    poco("com.bosma.smarthome:id/cli_nickname").click()
    poco("com.bosma.smarthome:id/et_nick_input").set_text("zhongdandan")
    poco("com.bosma.smarthome:id/tv_toolbar_right_content").click()
    poco("转到上一层级").click() 
 
def commom_changeSceond():
    poco("com.bosma.smarthome:id/tv_menu_head_user_name").click()
    poco("com.bosma.smarthome:id/cli_nickname").click()
    poco("com.bosma.smarthome:id/et_nick_input").set_text("丹丹")
    poco("com.bosma.smarthome:id/tv_toolbar_right_content").click()
    
if poco(text="博冠智能").exists():
    commom()
    assert_exists(Template(r"tpl1540452504490.png", record_pos=(-0.253, -0.611), resolution=(1080, 1920)),"修改成功")
    #执行结果为true时，将昵称改成另一个名字
    commom_changeSceond()

#如果还没登录，先执行登录
else:
    commom_login()
    commom()
    assert_exists(Template(r"tpl1540452504490.png", record_pos=(-0.253, -0.611), resolution=(1080, 1920)),"修改成功")
    #执行结果为true时，将昵称改成另一个名字
    commom_changeSceond()