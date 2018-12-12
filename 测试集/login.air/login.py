# -*- encoding=utf8 -*-
__author__ = "zhongdd"

from airtest.core.api import *
auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

stop_app("com.bosma.smarthome")
start_app("com.bosma.smarthome")
sleep(2)

#正确登录
def login_correct():
    poco("com.bosma.smarthome:id/et_account").set_text('1451953028@qq.com')
    poco("com.bosma.smarthome:id/et_pwd").set_text('zdd123456')
    poco("com.bosma.smarthome:id/btn_login").click()
    sleep(2)
    
#账号或密码错误    
def login_wrongPassword():
    poco("com.bosma.smarthome:id/et_account").set_text('1451953028@qq.com')
    poco("com.bosma.smarthome:id/et_pwd").set_text('zdd123456789')
    poco("com.bosma.smarthome:id/btn_login").click()
    sleep(2)

#账号未激活
def login_AccountNotActivatesd():
    poco("com.bosma.smarthome:id/et_account").set_text('syclvj79850@chacuo.net')
    poco("com.bosma.smarthome:id/et_pwd").set_text('zdd123456789')
    poco("com.bosma.smarthome:id/btn_login").click()
    sleep(2)

#邮箱格式不正确    
def login_notformatAccount():
    poco("com.bosma.smarthome:id/et_account").set_text('1451953028')
    poco("com.bosma.smarthome:id/et_pwd").click()
    #poco录制不了软键盘，所以将页面拉上去
    poco.swipe([100/1920,800/1080],[100/1920,300/1080]) 
    
    
#密码格式不正确
def login_notfomatPassword():
    poco("com.bosma.smarthome:id/et_account").set_text('1451953028@qq.com')
    poco("com.bosma.smarthome:id/et_pwd").set_text('zdd')
    poco("com.bosma.smarthome:id/et_account").click()
    sleep(2)
    
def common():
    login_correct()
    assert_exists(Template(r"tpl1543978665988.png", record_pos=(0.006, -0.754), resolution=(1440, 2560)),"登录成功")
    poco("转到上一层级").click()
    poco("com.bosma.smarthome:id/tv_menu_head_user_name").click()
    poco("com.bosma.smarthome:id/btn_logout").click()
    sleep(1)
    login_AccountNotActivatesd()
    assert_exists(Template(r"tpl1543989497028.png", record_pos=(-0.003, -0.039), resolution=(1440, 2560)),"账号未激活")
    poco("com.bosma.smarthome:id/btnSingle").click()
    sleep(1)
    login_wrongPassword()
    assert_exists(Template(r"tpl1543979621042.png", record_pos=(-0.001, -0.037), resolution=(1440, 2560)),"邮箱或密码错误")
    poco("com.bosma.smarthome:id/btnSingle").click()
    
    login_notformatAccount()
    assert_exists(Template(r"tpl1543989992577.png", record_pos=(-0.007, -0.257), resolution=(1440, 2560)),"邮箱格式错误")
    
    login_notfomatPassword()
    assert_exists(Template(r"tpl1543990117038.png", record_pos=(-0.001, -0.27), resolution=(1440, 2560)),"密码格式错误提示")

    
    
if exists(Template(r"tpl1543978665988.png", record_pos=(0.006, -0.754), resolution=(1440, 2560))):
    poco("转到上一层级").click()
    poco("com.bosma.smarthome:id/tv_menu_head_user_name").click()
    poco("com.bosma.smarthome:id/btn_logout").click()
    sleep(1)
    common()
    
else:
    common()
    
