import time

DEVICE_url = 'https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=cS6Aw4inWV&hashCode=lZGX9bmwQGHuZPviiiBCrtoNPyHZ4pBG3jvF2dybZ6o&FMQw=0&q4f3=zh-CN&VySQ=FGGxHVb3AzlSM-oikvoZfGsTbD48DQud&VPIf=1&custID=133&VEek=unknown&dzuS=32.0 r0&yD16=0&EOQP=38437f3289ca7a613bb292a3de0dba2b&jp76=df7f80581243b062f0c64efc90666cd0&hAqN=Win32&platform=WEB&ks0Q=7523081fcf2454464b148398defb390a&TeRS=864x1536&tOHY=24xx864x1536&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36&E3gR=7a13398746be6f51fe069c8a25001f12×tamp=' + str(
    round(time.time() * 1000))

# 验证码下载地址
Down_mg_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&{}'.format(
    int(time.time() * 1000))

# 验证码 验证地址
Check_img_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
# 登录地址 校验账号密码
Login_url = 'https://kyfw.12306.cn/passport/web/login'

# 二次校验
UserLogin_url = 'https://kyfw.12306.cn/otn/login/userLogin'

# 重定向二次校验
Redirect_UserLogin_Url = 'https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin'

# 获取 tk关键 url
Uamtk_url = 'https://kyfw.12306.cn/passport/web/auth/uamtk'

# 使用tk 校验
Uamauthclient_url = 'https://kyfw.12306.cn/otn/uamauthclient'

# 使用cookie直接 请求这个就可以访问 api
Conf_url = 'https://kyfw.12306.cn/otn/login/conf'

UamtkStatic_url = 'https://kyfw.12306.cn/passport/web/auth/uamtk-static'

initMy12306Api_url = "https://kyfw.12306.cn/otn/index/initMy12306Api"