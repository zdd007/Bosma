# -*- encoding=utf8 -*-
__author__ = "zhongdd"

from airtest.core.api import *

import datetime

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

stop_app("com.bosma.smarthome")
sleep(2)
start_app("com.bosma.smarthome")
sleep(5)

#定义一个变量给注册用
nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')#现在
registerEmail = nowTime + '@air.com'

def register():#正确信息
    poco("com.bosma.smarthome:id/et_nickname").set_text("丹丹")
    poco("com.bosma.smarthome:id/et_email").set_text(registerEmail)
    poco("com.bosma.smarthome:id/et_passwd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/et_repasswd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/btn_signup").click()

def register_havenotbeenregister():#账号已注册但未激活
    poco("com.bosma.smarthome:id/et_nickname").set_text("丹丹")
    poco("com.bosma.smarthome:id/et_email").set_text("njvdwy57438@chacuo.net")
    poco("com.bosma.smarthome:id/et_passwd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/et_repasswd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/btn_signup").click()

def register_havebeenregister():#账号已注册
    poco("com.bosma.smarthome:id/et_nickname").set_text("丹丹")
    poco("com.bosma.smarthome:id/et_email").set_text("1451953028@qq.com")
    poco("com.bosma.smarthome:id/et_passwd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/et_repasswd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/btn_signup").click()
       
def register_formatemail():#邮箱格式错误
    poco("com.bosma.smarthome:id/et_nickname").set_text("丹丹")
    poco("com.bosma.smarthome:id/et_email").set_text("145195302@")    
    poco.swipe([100/1920,800/1080],[100/1920,300/1080])    
    poco("com.bosma.smarthome:id/et_passwd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/et_passwd").click()
    poco("com.bosma.smarthome:id/et_email").click()
    poco("com.bosma.smarthome:id/et_nickname").click()
    poco("com.bosma.smarthome:id/et_email").click()

def register_PWDnotsame():#密码不一致
    poco("com.bosma.smarthome:id/et_nickname").set_text("丹丹")
    poco("com.bosma.smarthome:id/et_email").set_text("1451953028@qq.com")
    poco("com.bosma.smarthome:id/et_passwd").set_text("qwert123456")
    poco("com.bosma.smarthome:id/et_repasswd").set_text("qwert1234567")
    poco("com.bosma.smarthome:id/btn_signup").click()
    
def commom():
    register()
    assert_exists(Template(r"tpl1543995765133.png", record_pos=(-0.019, -0.571), resolution=(1440, 2560)),"注册成功啦！")
    poco("com.bosma.smarthome:id/tv_Login").click()
    poco("com.bosma.smarthome:id/tv_createaccout").click()
    
    register_havenotbeenregister()
    assert_exists(Template(r"tpl1543996432204.png", record_pos=(-0.015, -0.685), resolution=(1440, 2560)),"账号未激活")
    poco("com.bosma.smarthome:id/tv_Login").click()
    poco("com.bosma.smarthome:id/tv_createaccout").click()
    register_havebeenregister()
    assert_exists(Template(r"tpl1540448778051.png", record_pos=(-0.002, 0.199), resolution=(1080, 1920)),"此邮箱已注册") 
    poco("com.bosma.smarthome:id/tv_Login").click()
    poco("com.bosma.smarthome:id/tv_createaccout").click()
    
    register_formatemail()
    assert_exists(Template(r"tpl1540448615798.png", record_pos=(-0.001, -0.271), resolution=(1080, 1920)),"邮箱格式错误")


    register_PWDnotsame()
    assert_exists(Template(r"tpl1540448390640.png", record_pos=(0.001, 0.202), resolution=(1080, 1920)),"密码不一致")
   
if poco(text="博冠智能").exists():
    poco("转到上一层级").click()
    poco("com.bosma.smarthome:id/tv_menu_head_user_name").click()
    poco("com.bosma.smarthome:id/btn_logout").click()
    poco("com.bosma.smarthome:id/tv_createaccout").click()
    commom()

else:
    poco("com.bosma.smarthome:id/tv_createaccout").click()
    commom()

