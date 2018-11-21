# -*- encoding=utf8 -*-
__author__ = "zhongdd"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

stop_app("com.bosma.smarthome")
start_app("com.bosma.smarthome")
sleep(5)

def login():
    sleep(5)
    poco("com.bosma.smarthome:id/et_account").set_text("1451953028@qq.com")
    poco("com.bosma.smarthome:id/et_pwd").set_text("zdd123456")
    poco("com.bosma.smarthome:id/btn_login").click()
 
def find_page():
    poco("转到上一层级").click()
    poco(text="意见反馈").click()

#正常流程发送反馈
def SendFeedback_normal():
    sleep(2)
    poco("com.bosma.smarthome:id/et_content").set_text("这是一个好产品，谢谢合作")
    poco("com.bosma.smarthome:id/tv_toolbar_right_content").click()
    assert_exists(Template(r"tpl1540865085651.png", record_pos=(-0.003, -0.088), resolution=(1080, 1920)),"发送成功")
    
#反馈内容为空    
def SendFeedback_abnormal():
    sleep(2)
    poco("com.bosma.smarthome:id/tv_toolbar_right_content").click()
    assert_exists(Template(r"tpl1540867730566.png", record_pos=(-0.001, -0.089), resolution=(1080, 1920)),"反馈内容不能为空")

    
#如果已经登录，直接发送反馈
if poco(text="博冠智能").exists():
    sleep(2)
    #进入Feedback页面
    find_page()
    sleep(2)
    SendFeedback_normal()
    #sleep(1)
    #SendFeedback_abnormal()
    
#如果还没登录，先执行登录，再发送反馈
else:
    login()
    sleep(2)
    find_page()
    sleep(2)
    SendFeedback_normal()
    #sleep(1)
    #SendFeedback_abnormal()    
    
