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
    
 #如果已经登录，执行格式化SDCard操作
if poco(text="博冠智能").exists():
    sleep(1)
    touch(Template(r"tpl1542363340210.png", record_pos=(-0.344, 0.763), resolution=(1080, 1920)))
    assert_exists(Template(r"tpl1542363371678.png", record_pos=(-0.299, 0.594), resolution=(1080, 1920)),"布防设置成功")
    touch(Template(r"tpl1542363401554.png", record_pos=(0.001, 0.764), resolution=(1080, 1920)))
    assert_exists(Template(r"tpl1542363413728.png", record_pos=(-0.314, 0.587), resolution=(1080, 1920)),"撤防设置成功")
    touch(Template(r"tpl1542363434417.png", record_pos=(0.334, 0.772), resolution=(1080, 1920)))
    assert_exists(Template(r"tpl1542363450338.png", record_pos=(-0.307, 0.594), resolution=(1080, 1920)),"隐私模式设置成功")

    
else:
    login()
    sleep(2)
    touch(Template(r"tpl1542363340210.png", record_pos=(-0.344, 0.763), resolution=(1080, 1920)))
    assert_exists(Template(r"tpl1542363371678.png", record_pos=(-0.299, 0.594), resolution=(1080, 1920)),"布防设置成功")
    touch(Template(r"tpl1542363401554.png", record_pos=(0.001, 0.764), resolution=(1080, 1920)))
    assert_exists(Template(r"tpl1542363413728.png", record_pos=(-0.314, 0.587), resolution=(1080, 1920)),"撤防设置成功")
    touch(Template(r"tpl1542363434417.png", record_pos=(0.334, 0.772), resolution=(1080, 1920)))
    assert_exists(Template(r"tpl1542363450338.png", record_pos=(-0.307, 0.594), resolution=(1080, 1920)),"隐私模式设置成功")
sleep(2)
    
