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
#如果已经登录，直接进去修改昵称
def login():
    sleep(2)
    poco("com.bosma.smarthome:id/et_account").click()

    poco("com.bosma.smarthome:id/et_account").set_text("1451953028@qq.com")
    poco("com.bosma.smarthome:id/et_pwd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/btn_login").click()
    
if poco(text="博冠智能").exists():
    sleep(1)
    poco("转到上一层级").click()
    sleep(1)
    poco("com.bosma.smarthome:id/tv_menu_head_user_name").click()
    sleep(1)
    poco("com.bosma.smarthome:id/cli_nickname").click()
    sleep(1)
    poco("com.bosma.smarthome:id/et_nick_input").set_text("zhongdandan")
    sleep(1)
    poco("com.bosma.smarthome:id/tv_toolbar_right_content").click()
    sleep(1)
    poco("转到上一层级").click()
#如果还没登录，先执行登录
else:
    login()
    poco("转到上一层级").click()
    poco("com.bosma.smarthome:id/tv_menu_head_user_name").click()
    poco("com.bosma.smarthome:id/cli_nickname").click()
    poco("com.bosma.smarthome:id/et_nick_input").set_text("zhongdandan")
    poco("com.bosma.smarthome:id/tv_toolbar_right_content").click()
    poco("转到上一层级").click()

    
    assert_exists(Template(r"tpl1540452504490.png", record_pos=(-0.253, -0.611), resolution=(1080, 1920)),"修改成功")