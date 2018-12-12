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
    #分享控件
    poco("com.bosma.smarthome:id/iv_toolbar_sub_icon").click()
    assert_exists(Template(r"tpl1544081980683.png", record_pos=(-0.001, -0.739), resolution=(1440, 2560)),"分享控件跳转正常")
    sleep(1)
    poco("转到上一层级").click()
    sleep(10)
    #s设备设置控件
    poco("com.bosma.smarthome:id/iv_toolbar_icon").click()
    assert_exists(Template(r"tpl1544082053345.png", record_pos=(0.001, -0.745), resolution=(1440, 2560)),"设备设置控件跳转正常")
    sleep(1)
    poco("转到上一层级").click()
    sleep(10)
    #监听控件
    poco("com.bosma.smarthome:id/rb_liveview_audio_listen").click()
    assert_exists(Template(r"tpl1544083018055.png", record_pos=(-0.174, 0.755), resolution=(1440, 2560)),"监听控件打开正常")
    sleep(1)
    #自动巡航控件
    poco("com.bosma.smarthome:id/turn_screen").click()
    assert_exists(Template(r"tpl1544083776388.png", record_pos=(-0.01, 0.51), resolution=(1440, 2560)),"自动巡航控件打开正常")
    sleep(1)
    #取消巡航
    poco("com.bosma.smarthome:id/turn_screen").click()
    #对比度调整
    poco("com.bosma.smarthome:id/rb_contast").click()
    sleep(8)
    assert_exists(Template(r"tpl1544084544353.png", record_pos=(0.006, 0.007), resolution=(1440, 2560)),"对比度调整控件打开正常")
    sleep(1)
    poco("com.bosma.smarthome:id/sb_sharpness").swipe([300/1920,100/1080],[500/1920,100/1080])
    poco("com.bosma.smarthome:id/bt_image_param_cancel").click()
    assert_exists(Template(r"tpl1544084680101.png", record_pos=(-0.001, 0.46), resolution=(1440, 2560)),"调整关闭成功")
    

if poco(text="博冠智能").exists():
    sleep(1)
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()         
    if exists(Template(r"tpl1541040369573.png", record_pos=(0.424, -0.619), resolution=(1080, 1920))):
        poco("com.bosma.smarthome:id/iv_liveview").click()
        sleep(10)
        if exists(Template(r"tpl1544148303628.png", record_pos=(0.013, -0.288), resolution=(1440, 2560))):
            poco("转到上一层级").click()       
            assert_exists(Template(r"tpl1544148466102.png", record_pos=(-0.011, -0.747), resolution=(1440, 2560)),"设备掉线中，退出liveview页面")

        else:
            commom()            
    else:
        poco("转到上一层级").click()
        assert_exists(Template(r"tpl1544148556087.png", record_pos=(0.004, -0.742), resolution=(1440, 2560)),"账号下没有设备，退出操作")
       
else:
    commom_login()
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click() 
    if exists(Template(r"tpl1541040369573.png", record_pos=(0.424, -0.619), resolution=(1080, 1920))):
        poco("com.bosma.smarthome:id/iv_liveview").click()
        sleep(5)
        if assert_exists(Template(r"tpl1544148303628.png", record_pos=(0.013, -0.288), resolution=(1440, 2560))):
            poco("转到上一层级").click()       
            assert_exists(Template(r"tpl1544148466102.png", record_pos=(-0.011, -0.747), resolution=(1440, 2560)),"设备掉线中，退出liveview页面")

        else:
            commom()         

   
    else:
        poco("转到上一层级").click()
        assert_exists(Template(r"tpl1544148556087.png", record_pos=(0.004, -0.742), resolution=(1440, 2560)),"账号下没有设备，退出操作")




