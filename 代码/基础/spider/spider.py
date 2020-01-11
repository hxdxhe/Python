# @Author : Aiopr
# @Email : 5860034@qq.com
from urllib import request
import re

class Spider:
    url = "https://www.huya.com/g/wzry"
    root_pattern = '<span class="txt">([\s\S]*?)</li>'
    name_pattern = '<i class="nick" title="[\s\S]*?">([\s\S]*?)</i>'
    number_pattern = '<i class="js-num">([\s\S]*?)</i>'

    # 读取地址
    def __fetch__content(self):   

        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls

    # 用正则表达式匹配出想要的内容
    def __analysis(self,htmls):

        root_html = re.findall(Spider.root_pattern,htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern,html)
            number = re.findall(Spider.number_pattern,html)
            anchor = {'name':name,'number':number}
            anchors.append(anchor)
        return anchors

    # 精炼代码
    def __refine(self,anchors):
        l = lambda anchor:{
            #如果有空格的话用strip()去除
            'name':anchor['name'][0],
            'number':anchor['number'][0]
        }
        return map(l,anchors)

    # 排序
    def __sort(self,anchors):

        #需要指定key函数  reverse=True 是降序排列
        anchors = sorted(anchors,key=self.__sord_seed,reverse=True)    
        return anchors

    # sorted中的key参数传参
    def __sord_seed(self,anchor):
        r = re.findall('\d*',anchor['number'])
        number = float(r[0])

        if '万' in anchor['number']:
            number *= 10000
        return number

    # 展示
    def __show(self,anchors):
        for rank in range(0,len(anchors)):
            print('【'+str(rank+1)+' 】'+':'+anchors[rank]['name']+'    '+anchors[rank]['number'])

    #向外部展示的方法
    def go(self):

        htmls = self.__fetch__content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        # print(anchors)

        self.__show(anchors)

    

# 调用
spider = Spider()
spider.go()