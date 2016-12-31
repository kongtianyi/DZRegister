#coding:utf-8

import time
from selenium import webdriver

class DZRegister():

    def __init__(self, url, codeType="utf-8"):
        # 签到页的url
        self.url = url
        # 网站编码类型,目前没用= =，为以后签到需要输入心情的做准备
        self.codeType = codeType
        # 因为不会配置cookie，PhantomJS不能用
        # self.driver = webdriver.PhantomJS()
        # 使用本地的Firefox配置（为了有本地cookie），如果不用的话，默认启动的是一个崭新的Firefox，不带本地cookie
        self.profile = webdriver.FirefoxProfile("/home/kongtianyi/.mozilla/firefox/5dz1e739.default-1482899165817")
        self.driver = webdriver.Firefox(self.profile)


    def login(self, loginUrl, user, pw):
        '''
        仅限登陆不需要验证码的网站,使用此方法可以不使用本地的Firefox配置
        '''
        # 浏览器窗口最大化
        self.driver.maximize_window()
        # 浏览器地址跳到登录页
        self.driver.get(loginUrl)
        # 给点时间加载页面元素
        time.sleep(5)
        # 填写帐号密码并点登录
        self.driver.find_element_by_name("username").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(pw)
        self.driver.find_element_by_name("loginsubmit").click()
        # 登录需要一定的跳转时间，根据网速来设定合适的值
        time.sleep(10)

    # 这样配置cookie无效，以后不知道能不能解决……
    # def transCookies(self, cookies):
    #     '''
    #     把从调试工具中复制出来的cookie串转化成[(key1,value1),(key2,value2),……]形式的列表
    #     '''
    #     itemList = []
    #     items = cookies.split(';')
    #     for item in items:
    #         key = item.split('=')[0].replace(' ', '')
    #         value = item.split('=')[1]
    #         itemList.append((key, value))
    #     return itemList
    #
    # def setCookies(self, cookiesList):
    #     '''
    #     给webdirver设置cookies
    #     :param cookiesList: [(key1,value1),(key2,value2),……]形式的cookie列表
    #     '''
    #     for item in cookiesList:
    #         self.driver.add_cookie({'name': item[0], 'value': item[1]})
    #     print "Cookies setting seccess."

    def register(self):
        '''
        签到,要说明的是不同的站点的按钮的xpath会不同，因为是单页，直接在开发者工具里复制XPath即可
        '''
        # 浏览器窗口最大化
        self.driver.maximize_window()
        # 浏览器地址跳到签到页
        self.driver.get(self.url)
        time.sleep(3)
        # 选择一个心情,这个是难过，无所谓了～
        self.driver.find_element_by_id("ng").click()
        time.sleep(3)
        # 自动填充签到信息
        try:
            self.driver.find_element_by_xpath("//*[@id='qiandao']/table[@class='tfm']/tbody/tr[1]/td/label[2]").click()
        except:
            print "此论坛签到不需发表文字。"
        time.sleep(3)
        # 点击签到按钮
        # 红客联盟的
        # self.driver.find_element_by_xpath("//*[@id='qiandao']/table[1]/tbody/tr/td/div/a/img").click()
        # 精易论坛的
        self.driver.find_element_by_xpath("//*[@id='ct']/div[1]/div[1]/form/table[1]/tbody/tr/td/input").click()
        # 给他点时间再退出，学校网太渣了实在
        time.sleep(5)

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    # dzr = DZRegister("http://www.cnhonkerarmy.com/plugin.php?id=dsu_paulsign:sign", "gbk")
    # dzr.login("http://www.cnhonkerarmy.com/member.php?mod=logging&action=login")

    dzr = DZRegister("http://bbs.125.la/plugin.php?id=dsu_paulsign:sign")
    # cookies = "lDlk_ecc9_nofavfid=1; lDlk_ecc9_smile=4D1; lDlk_ecc9_saltkey=gYMBj3gy; lDlk_ecc9_lastvisit=1483188354; lDlk_ecc9_sendmail=1; lDlk_ecc9_ulastactivity=b6aebcSuaMxORqTvM6UxGDACeK1nFuF9i6y90tvvi4KBNL7QbRK%2B; lDlk_ecc9_auth=94f0jARVsZAWBu0TtJn0hBl58DHZVxjK5qnJ80aqz8K5dhrRgkPiMquCKywcfkg%2BhVtJNQ0qQNMxZRyQ3A5BpV20hyY; lDlk_ecc9_lastcheckfeed=363083%7C1483191968; lDlk_ecc9_onlineusernum=3773; PHPSESSID=334velad4c54vnmjt0ttggia91; lDlk_ecc9_myrepeat_rr=R0; lDlk_ecc9_sid=VPUcVl; Hm_lvt_fa32dadde3745af309b587b38d20ea1d=1483191955; Hm_lpvt_fa32dadde3745af309b587b38d20ea1d=1483191969; lDlk_ecc9_lastact=1483191969%09home.php%09spacecp; lDlk_ecc9_connect_is_bind=1; tjpctrl=1483193769841"
    # cookiesList = dzr.transCookies(cookies)
    # dzr.setCookies(cookiesList)

    dzr.register()
    dzr.close()