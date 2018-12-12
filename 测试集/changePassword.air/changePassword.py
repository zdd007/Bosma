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

def login_newPassword():
    sleep(2)
    poco("com.bosma.smarthome:id/et_account").set_text("1451953028@qq.com")
    poco("com.bosma.smarthome:id/et_pwd").set_text("test123456")
    poco("com.bosma.smarthome:id/btn_login").click()
    
def changePassword():
    #进入修改密码页面
    poco("转到上一层级").click()
    poco("com.bosma.smarthome:id/tv_menu_head_user_name").click()
    poco("com.bosma.smarthome:id/cli_changepw").click() 
    sleep(1)   
    poco("com.bosma.smarthome:id/et_oldpasswd").set_text("zdd123456")
    poco("com.bosma.smarthome:id/et_passwd").set_text("test123456")
    poco("com.bosma.smarthome:id/et_repasswd").set_text("test123456")
    poco("com.bosma.smarthome:id/tv_toolbar_right_content").click()
   
def changePasswordSecond():
    #进入修改密码页面
    poco("转到上一层级").click()
    poco("com.bosma.smarthome:id/tv_menu_head_user_name").click()
    poco("com.bosma.smarthome:id/cli_changepw").click() 
    sleep(1)   
    poco("com.bosma.smarthome:id/et_oldpasswd").set_text("test123456")
    poco("com.bosma.smarthome:id/et_passwd").set_text("zdd123456")
    poco("com.bosma.smarthome:id/et_repasswd").set_text("zdd123456")
    poco("com.bosma.smarthome:id/tv_toolbar_right_content").click()

def logout():
    poco("com.bosma.smarthome:id/btn_logout").click() 
    
#如果已经登录，直接进去修改密码
if poco(text="博冠智能").exists():
    changePassword()
    sleep(2)
    logout() 
    login_newPassword()
    assert_exists(Template(r"tpl1543802903115.png", record_pos=(0.006, -0.739), resolution=(1440, 2560)),"登录成功")
    sleep(2)
    #执行成功后，将密码改为原来的密码
    changePasswordSecond()
    
#如果还没登录，先执行登录
else:
    commom_login()
    changePassword()
    sleep(2)
    logout() 
    login_newPassword()
    assert_exists(Template(r"tpl1543802903115.png", record_pos=(0.006, -0.739), resolution=(1440, 2560)),"登录成功")
    sleep(2)
    #执行成功后，将密码改为原来的密码
    changePasswordSecond()


