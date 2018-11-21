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
    poco("com.bosma.smarthome:id/et_account").click()
    poco("com.bosma.smarthome:id/et_account").set_text("1451953028@qq.com")
    poco("com.bosma.smarthome:id/et_pwd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/btn_login").click()

def login_newPassword():
    sleep(2)
    poco("com.bosma.smarthome:id/et_account").click()
    poco("com.bosma.smarthome:id/et_account").set_text("1451953028@qq.com")
    poco("com.bosma.smarthome:id/et_pwd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/btn_login").click()
    
def changePassword():
    sleep(2)
    poco("com.bosma.smarthome:id/et_oldpasswd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/et_passwd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/et_repasswd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/tv_toolbar_right_content").click()

def logout():
    poco("com.bosma.smarthome:id/btn_logout").click() 
#如果已经登录，直接进去修改昵称
if poco(text="博冠智能").exists():
    sleep(1)
    poco("转到上一层级").click()
    sleep(1)
    poco("com.bosma.smarthome:id/tv_menu_head_user_name").click()
    sleep(1)
    poco("com.bosma.smarthome:id/cli_changepw").click() 

    # poco("com.bosma.smarthome:id/tb_common_toolbar")
    sleep(1)
    changePassword()
    logout() 
    login_newPassword()
#如果还没登录，先执行登录
else:
    login()
    poco("转到上一层级").click()
    sleep(1)
    poco("com.bosma.smarthome:id/tv_menu_head_user_name").click()
    sleep(1)
    poco("com.bosma.smarthome:id/cli_changepw").click() 

    #poco("com.bosma.smarthome:id/tb_common_toolbar")
    sleep(1)
    changePassword()
    logout() 
    login_newPassword()

