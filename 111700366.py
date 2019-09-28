#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import json


'''省市字典集'''
Dict={
    '北京':['北京'],
    '上海':['上海'],
    '天津':['天津'],
    '重庆':['重庆'],
    '河北':['石家庄','唐山','秦皇岛','邯郸','邢台','保定','张家口','承德','沧州','廊坊','衡水',],
    '内蒙古':[
        '呼和浩特','包头','乌海','赤峰','通辽','鄂尔多斯','呼伦贝尔',
        '巴彦淖尔','乌兰察布','兴安','锡林郭勒','阿拉善'],
    '辽宁':['沈阳','大连','鞍山','抚顺','本溪','丹东','锦州','营口','阜新','辽阳','盘锦','铁岭','朝阳','葫芦岛'],
    '吉林':['长春','吉林','四平','辽源','通化','白山','松原','白城','延边朝鲜族'],
    '黑龙江':['哈尔滨','齐齐哈尔','鸡西','鹤岗','双鸭山','大庆','伊春','佳木斯','七台河','牡丹江','黑河','绥化','大兴安岭'],
    '山西':['太原','大同','阳泉','长治','晋城','朔州','晋中','运城','忻州','临汾','吕梁'],
    '江苏':[
        '南京','无锡','徐州','常州','苏州','南通','连云港','淮安','盐城','扬州','镇江','泰州','宿迁'],
    '浙江':['杭州','宁波','温州','嘉兴','湖州','绍兴','金华','衢州','台州','丽水'],
    '安徽':['合肥','芜湖','蚌埠','淮南','马鞍山','淮北','铜陵','安庆','黄山','滁州','阜阳','宿州','六安','亳州','池州','宣城'],
    '福建':['福州','厦门','莆田','三明','泉州','漳州','南平','龙岩','宁德'],
    '江西':['南昌','景德镇','萍乡','九江','新余','鹰潭','赣州','吉安','宜春','抚州','上饶'],
    '山东':['济南','青岛','淄博','枣庄','东营','烟台','潍坊','济宁','泰安','威海','日照','莱芜','临沂','德州','聊城','滨州','菏泽'],
    '河南':['郑州','开封','洛阳','平顶山','安阳','鹤壁','新乡','焦作','濮阳','许昌','漯河','三门峡','南阳','商丘','信阳','周口','驻马店','济源'],
    '湖北':['武汉','黄石','十堰','宜昌','襄阳','鄂州','荆门','孝感','荆州','黄冈','咸宁','随州','恩施','仙桃','潜江','天门','神农架'],
    '湖南':['长沙','株洲','湘潭','衡阳','邵阳','岳阳','常德','张家界','益阳','郴州','永州','怀化','娄底','湘西'],
    '广东':[
        '广州','韶关','深圳','珠海','汕头','佛山','江门','湛江',
        '茂名','肇庆','惠州','梅州','汕尾','河源','阳江','清远',
        '东莞','中山','潮州','揭阳','云浮'],
    '广西壮族':[
        '南宁','柳州','桂林','梧州','北海','防城港','钦州','贵港','玉林','百色','贺州','河池','来宾','崇左'],
    '海南':['海口','三亚','三沙','五指山','琼海','儋州','文昌','万宁','东方','定安','屯昌','澄迈','临高',
            '白沙黎族自治','昌江黎族自治','乐东黎族自治','陵水黎族自治','保亭黎族苗族自治','琼中黎族苗族自治'],
    '四川':[
        '成都','自贡','攀枝花','泸州','德阳','绵阳','广元','遂宁',
        '内江','乐山','南充','眉山','宜宾','广安','达州','雅安',
        '巴中','资阳','阿坝藏族羌族','甘孜藏族','凉山彝族'],
    '贵州':['贵阳','六盘水','遵义','安顺','铜仁','黔西南布依族苗族','毕节','黔东南苗族侗族','黔南布依族苗族'],
    '云南':[
        '昆明','曲靖','玉溪','保山','昭通','丽江','普洱','临沧','楚雄彝族','红河哈尼族彝族',
        '文山壮族苗族','西双版纳傣族','大理白族','德宏傣族景颇族','怒江傈僳族','迪庆藏族'],
    '西藏':['拉萨','昌都','山南','日喀则','那曲','阿里','林芝'],
    '陕西':['西安','铜川','宝鸡','咸阳','延安','汉中','榆林','安康','商洛'],
    '甘肃':['兰州','嘉峪关','金昌','白银','天水','武威','张掖','平凉','酒泉','庆阳','定西','陇南','甘南'],
    '青海':['西宁','海东','海北藏族','黄南藏族','海南藏族','果洛藏族','玉树藏族','海西蒙古族藏族'],
    '宁夏回族':['银川','石嘴山','吴忠','固原','中卫'],
    '新疆维吾尔':[
        '乌鲁木齐','克拉玛依','吐鲁番','哈密','昌吉','博尔塔拉蒙古',
        '巴音郭楞蒙古','阿克苏','克孜勒苏','喀什','和田','伊犁',
        '塔城','阿勒泰','石河子','阿拉尔','图木舒克','五家渠','北屯']
}

def dealname(text):
    name = re.search(r'^[\u4e00-\u9fa5]{2,5}', text)
    return name

def dealphonenumber(text):
    phonenum = re.search('\d{11}', text)
    return phonenum

def dealaddress(text,name,phonenum):
    if(name.group()):
        address = re.sub(name.group(), '', text)
    address = re.sub('\.', '', address)#删除.
    address = re.sub(',', '', address)#删除,
    address = re.sub(phonenum.group(), '', address)#删除手机号码
    return address

def matchaddress(address,name,phonenum,flag):
    '''匹配一级地址'''
    province = re.search('([\u4e00-\u9fa5]{2,7})?(?:省|自治区)', address)
    if(province!=None):
        length = len(province.group())
        loc = address.find(province.group())
        address2 = address[loc+length:]
        province = province.group()
        state = province.rstrip("省").rstrip("自治区")
    else:
        for state in Dict:
            if (re.search(state, address) != None):
                break
        length = len(state)
        loc = address.find(state)
        address2 = address[loc+length:]
        if((state!="北京") & (state!="上海") & (state!="天津") & (state!="重庆")):
            province = state+"省"
        else:
            province = state
            address2 = address
    '''匹配二级地址'''
    city = re.search(r'([\u4e00-\u9fa5]{2,7}?(?:市|自治州|盟|地区)^(超市))', address2)
    if(city!=None):
        length = len(city.group())
        loc = address2.find(city.group())
        address3 = address2[length+loc:]
        city = city.group()
    else:
        try:
            for d_city in Dict[state]:
                if(re.search(d_city,address2)!=None):
                    break
        except KeyError:
            return result
        length = len(d_city)
        loc = address2.find(d_city)
        if(loc<0):
            address3 = address2[loc+length-1:]
        else:
            address3 = address2[loc+length:]
        city = d_city+"市"

    '''匹配三级地址'''
    region = re.search('([\u4e00-\u9fa5]{1,9}?(?:市|区|县))', address3)
    if(region!=None):
        length =len(region.group())
        loc = address3.find(region.group())
        address4 = address3[loc+length:]
        region = region.group()
    else:
        region = ""
        address4 = address3

    '''匹配四级地址'''
    town = re.search('([\u4e00-\u9fa5]{2,7}?(?:街道|镇|乡))', address4)
    if(town!=None):
        length = len(town.group())
        loc = address4.find(town.group())
        address5 = address4[loc+length:]
        county = town.group()
    else:
        county = ""
        address5 = address4

    '''匹配五级地址'''
    road = re.search('[\u4e00-\u9fa5]{2,7}?路|街|巷(?:)', address5)
    if(road!=None):
        length = len(road.group())
        loc = address5.find(road.group())
        address6 = address5[loc+length:]
        road = road.group()
    else:
        road = ""
        address6 = address5

    '''匹配七级地址'''
    tag = re.search('\d{1,7}?(?:号|弄)', address6)
    if(tag!=None):
        length = len(tag.group())
        loc = address6.find(tag.group())
        address7 = address6[loc+length:]
        tag = tag.group()
    else:
        tag = ""
        address7 = address6

    if (flag.group()=='1'):
        result = {'姓名': name.group(), '手机': phonenum.group(),
                  '地址': [province, city, region, county, address5]}
    else:
        result = {'姓名': name.group(), '手机': phonenum.group(),
                  '地址': [province, city, region, county, road, tag, address7]}
    return result
while (1):    
    try:
        text = input()
        if(text=="END"):
            break
    except EOFError:
        break
    flag = re.search(r'^\d', text)
    text = re.sub('.!', '', text)
    name = dealname(text)
    phonenum = dealphonenumber(text)
    address = dealaddress(text, name, phonenum)
    result = matchaddress(address, name, phonenum, flag)
    print(json.dumps(result, ensure_ascii=False))






