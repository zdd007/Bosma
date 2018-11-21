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

def logout():
    poco("转到上一层级").click()
    poco("com.bosma.smarthome:id/tv_menu_head_user_name").click()
    poco("com.bosma.smarthome:id/btn_logout").click()

#如果已经登录，先退出登录，再进入忘记密码页面
if poco(text="博冠智能").exists():
    sleep(1)
    logout()
    #进入忘记密码页面
    poco("com.bosma.smarthome:id/tv_forgetpsw").click()
    poco("com.bosma.smarthome:id/et_email").set_text("1451953028@qq.com")
    poco("com.bosma.smarthome:id/btn_reset_passwd").click()
    assert_exists(Template(r"tpl1541058815758.png", record_pos=(-0.005, -0.119), resolution=(1080, 1920)),"发送邮件成功")

      
#如果没有登录，直接进去忘记密码页面
else:
    #进入忘记密码页面
    poco("com.bosma.smarthome:id/tv_forgetpsw").click()
    poco("com.bosma.smarthome:id/et_email").set_text("1451953028@qq.com")
    poco("com.bosma.smarthome:id/btn_reset_passwd").click()
    assert_exists(Template(r"tpl1541058815758.png", record_pos=(-0.005, -0.119), resolution=(1080, 1920)),"发送邮件成功")


