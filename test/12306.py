import sysimport time
import requests
from PIL import Image
import json
import os
 
import Headers
import SessionUtils
import UrlUtils
 
 
class Ticket(object):
    def __init__(self):
        self.answer = {
            "1": "40,40",
            "2": "110,40",
            "3": "180,40",
            "4": "260,40",
            "5": "40,120",
            "6": "110,120",
            "7": "180,120",
            "8": "260,120",
        }
        self.answer_code=''
        self.tk = ''
 
    def getDEVICEID(self):
        r = requests.get(UrlUtils.DEVICE_url, headers=Headers.BaseHead).text
        try:
            dic = json.loads(r[18:-2].replace(" ", ""))
        except Exception:
            return ""
        return dic
 
    # 初始化  获取设备id 设置为cookie 必须
    def initialize(self):
        dic = self.getDEVICEID()
        if dic == "":
            print("网络获取指纹失败!使用默认id")
            RAIL_EXPIRATION = "1576651914389"
            RAIL_DEVICEID = "lBJStCNl0YGo_HVkGtwOo2LWziXcwzpIk5gc2vAILNYdRfaeZ04nJtZ1JZwgQIssMDksn10rAz6Hz-bekeufhAusaKJId8f2BCg05ocgrzc8-chv8h4IB-lQ9H04XjLXr2fbnHw-SLZga3PewEfgPz2s-mhp7NAz"
        else:
            print("网络获取指纹成功!")
            RAIL_EXPIRATION = dic["exp"]
            RAIL_DEVICEID = dic['dfp']
        SessionUtil.setCookie("RAIL_EXPIRATION", RAIL_EXPIRATION)
        SessionUtil.setCookie("RAIL_DEVICEID", RAIL_DEVICEID)
 
    def conf(self):
        res = SessionUtil.session.post(url=UrlUtils.Conf_url, data=None, headers=Headers.ConFHeader)
 
    def uamtkstatic(self):
        data = {
            'appid': 'otn'
        }
        SessionUtil.session.post(url=UrlUtils.UamtkStatic_url, data=data, headers=Headers.UamtkStaticHead)
 
    def get_img_code(self):
        try:
            img = SessionUtil.session.get(url=UrlUtils.Down_mg_url, headers=Headers.BaseHead).content
            with open('code.jpg', 'wb') as f:
                f.write(img)
        except Exception:
            print("下载图片错误! 等待重试~~")
            time.sleep(1)
            self.get_img_code()
 
    def check_img(self):
        try:
            Image.open('code.jpg').show()
        except Exception:
            time.sleep(2)
            Image.open('code.jpg').show()
        print("+---1-------+----------+----------+----------+")
        print("|    1     |    2     |    3     |    4     |")
        print("|----------|----------|----------|----------|")
        print("|    5     |    6     |    7     |    8     |")
        print("+----------+----------+----------+----------+")
        input_code = input("请在1—8中选择输入验证图片编号，以半角','隔开。(例如：1,3,5):")
        answer_code = ''
        try:
            for i in input_code.split(','):
                answer_code += ',' + self.answer[i] if (i is not input_code[0]) else self.answer[i]
        except Exception as e:
            print('输入错误请重新输入!')
            self.check_img()
        data = {
            'answer': answer_code,
            'rand': 'sjrand',
            'login_site': 'E',
        }
        response = SessionUtil.session.get(url=UrlUtils.Check_img_url, params=data, headers=Headers.BaseHead, )
        check_result = json.loads(response.text)
        print(check_result)
        try:
            if check_result['result_code'] == '4':
                print('*' * 20 + '验证码正确' + '*' * 20)
                self.answer_code=answer_code
            else:
                self.get_img_code()
                self.check_img()
        except Exception:
            self.get_img_code()
            self.check_img()
 
    # 校验密码正确
    def login(self, answer_code):
        user = ''
        password = ''
        try:
            with open("user.conf", "r", encoding="utf-8") as  f:
                user = f.readline().strip().replace("[", '').replace("]", '').replace("name=", '')
                password = f.readline().strip().replace("[", '').replace("]", '').replace("pwd=", '')
                if user == "" or password == "":
                    raise Exception
        except Exception:
            user = input("账号____:")
            password = input("密码____:")
 
        formdata = {
            'username': user,
            'password': password,
            'appid': 'otn',
            'answer': answer_code
        }
        login_result = SessionUtil.session.post(url=UrlUtils.Login_url, data=formdata, headers=Headers.BaseHead)
        login_result.encoding = 'utf-8'
        login_result = login_result.json()
        print(login_result)
        if login_result["result_code"] != 0:  #{'result_message': '登录名不存在。', 'result_code': 1}
            sys.exit(0)
 
    # 二次校验
    def userLogin(self):
        # 获取一系列的cookie值才能真正的登录成功
        response = SessionUtil.session.get(url=UrlUtils.UserLogin_url, headers=Headers.UserLoginHead)
        # 更新JSESSIONID  route
        response = SessionUtil.session.get(url=UrlUtils.Redirect_UserLogin_Url, headers=Headers.RedirectHead)
 
    def uamtk(self):
        # 获取 tk 下一个请求需要提交 tk 值
        data = {'appid': 'otn'}
        uamtk_page = SessionUtil.session.post(url=UrlUtils.Uamtk_url, data=data, headers=Headers.UamtkHeader)
        uamtk_page.encoding = 'utf-8'
        try:
            result = uamtk_page.json()
            print(result)
            if result['result_code'] != 0:
                raise Exception(result['result_message'])
            tk = result['newapptk']
            self.tk = tk
        except Exception:
            print("获取tk失败!")
            print("重试")
            self.run()
 
    def Uamauthclient(self):
        data = {'tk': self.tk}
        response = SessionUtil.session.post(url=UrlUtils.Uamauthclient_url, data=data,
                                            headers=Headers.UamauthclientHeader)
        res = response.text
        try:
            dic = json.loads(res)
            print(dic)
            print(dic["username"] + ",欢迎登录!")
        except:
            print("登录失败!")
            self.run()
        # '{"result_code":0,"result_message":"验证通过","username":"XXX","apptk":"36yslXHez3_68-LtHvhI61mZkranjdw6kT9j4UMwEqrw1w0"}'
 
    def saveCookie(self):
        SessionUtil.save_cookies("12306cookies.txt")
 
    def getInfo(self):
 
        try:
            re = SessionUtil.session.post("https://kyfw.12306.cn/otn/modifyUser/initQueryUserInfoApi",
                                          headers=Headers.UserInfoHead)
            print(re.text)
        except:
            print("获取失败")
 
    def run(self):
        self.initialize()
        self.conf()
        self.uamtkstatic()
        self.get_img_code()
        self.check_img()
        self.login(self.answer_code)
        self.userLogin()
        self.uamtk()
        self.Uamauthclient()
        self.saveCookie()
        self.conf()
        self.getInfo()
 
 
if __name__ == '__main__':
    t = Ticket()
    result = "":
    try:
         with open("12306cookies.txt", "r", encoding="utf-8") as fr:
            result = fr.read()
     except Exception:
         pass
    if result != "":
        SessionUtil.load_cookies("12306cookies.txt")
        t.initialize()
        t.conf()
        t.uamtkstatic()
        t.userLogin()
        t.uamtk()
        t.Uamauthclient()
        t.getInfo()
    else:
        t.run()