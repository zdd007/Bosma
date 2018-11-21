# -*- encoding=utf8 -*-
__author__ = "zhongdd"

from airtest.core.api import *

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

stop_app("com.bosma.smarthome")
sleep(2)
start_app("com.bosma.smarthome")
sleep(2)

def register():#正确信息
    poco("com.bosma.smarthome:id/et_nickname").set_text("ddtest")
    poco("com.bosma.smarthome:id/et_email").set_text("jminte01564@chacuo.net")
    poco("com.bosma.smarthome:id/et_passwd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/et_repasswd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/btn_signup").click()

def register_havebeenregister():
    poco("com.bosma.smarthome:id/et_nickname").set_text("dandan")
    poco("com.bosma.smarthome:id/et_email").set_text("1451953028@qq.com")
    poco("com.bosma.smarthome:id/et_passwd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/et_repasswd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/btn_signup").click()
    
def register_formatemail():
    poco("com.bosma.smarthome:id/et_nickname").set_text("dandan")
    poco("com.bosma.smarthome:id/et_email").set_text("1451953028@qq")
    poco("com.bosma.smarthome:id/et_passwd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/et_repasswd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/btn_signup").click()

def register_PWDnotsame():
    poco("com.bosma.smarthome:id/et_nickname").set_text("dandan")
    poco("com.bosma.smarthome:id/et_email").set_text("1451953028@qq.com")
    poco("com.bosma.smarthome:id/et_passwd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/et_repasswd").set_text("qwert1234567")
    poco("com.bosma.smarthome:id/btn_signup").click()
    
if poco(text="博冠智能").exists():
    poco("转到上一层级").click()
    poco("com.bosma.smarthome:id/tv_menu_head_user_name").click()
    poco("com.bosma.smarthome:id/btn_logout").click()
else:
    poco("com.bosma.smarthome:id/tv_createaccout").click()

register()
assert_exists(Template(r"tpl1540447015743.png", record_pos=(-0.011, -0.571), resolution=(1080, 1920)),"注册成功啦！")
sleep(3)

register_havebeenregister()
assert_exists(Template(r"tpl1540448778051.png", record_pos=(-0.002, 0.199), resolution=(1080, 1920)),"此邮箱已注册")

register_formatemail()
assert_exists(Template(r"tpl1540448615798.png", record_pos=(-0.001, -0.271), resolution=(1080, 1920)),"邮箱格式错误")


register_PWDnotsame()
assert_exists(Template(r"tpl1540448390640.png", record_pos=(0.001, 0.202), resolution=(1080, 1920)),"密码不一致")