import json

def sol_p_c(msg):
    # 读入地址文件
    fp = open('address.txt', mode="r", encoding="utf-8", errors="ignore")
    addr = eval(fp.read())
    # 分离出省市,并处理
    province = ""
    city = ""
    for key in addr.keys():
        if (msg.find(key) >= 0):
            if (msg[len(key)] == '省'):
                province = key
                msg = msg[len(key) + 1:]
            else:
                province = key
                msg = msg[len(key):]

            for ad in addr[key]:
                if (msg.find(ad) >= 0):
                    if (msg[len(ad)] == '市'):
                        city = ad
                        msg = msg[len(ad) + 1:]
                        break
                    else:
                        city = ad
                        msg = msg[len(ad):]
                        break

            break

    if (province == '北京' or province == '天津' or province == '重庆' or province == '上海'):
        if (msg[0] == '市'):
            msg = msg[1:]
        city = province
    elif (province != "" and province[len(province) - 1] != '区'):
        province += '省'

    if (city.find('区') == -1 and city.find('自治州') == -1 and city.find('盟') == -1):
        if (city != ''):
            city += '市'
    return msg, province, city


def sol_county(msg):
    # 处理县级地址
    county = ""
    pos = 999
    tmp = ['区', '县', '市']
    for x in tmp:
        if (msg.find(x) >= 0):
            pos = min(pos, msg.find(x))

    if (pos != 999 and pos < 5):
        county = msg[:pos + 1]
        msg = msg[pos + 1:]
    return msg, county


def sol_town(msg):
    # 处理乡级地址
    town = ""
    add_len = 0
    pos = 999
    tmp = ['街道', '镇', '乡', '开发区']

    for x in tmp:
        now = msg.find(x)
        if (now >= 0 and now <= pos):
            pos = now
            add_len = len(x)

    if (pos != 999 and (pos < 5 or add_len == 3)):
        town = msg[:pos + add_len]
        msg = msg[pos + add_len:]
    return msg, town

while 1:
    try:
        msg=input()
        if(msg=="END"):
            break
    except EOFError:
        break
    # 处理难度等级，并把无用的标点符号处理掉
    op = int(msg[0])
    msg = msg[2:]
    msg = msg[:len(msg) - 1]
    cnt = 0
    person = {"姓名": "", "手机": "", "地址": []}

    # 分离出姓名
    while (msg[cnt] != ','):
        cnt += 1
    name = msg[:cnt]

    # 分理出手机号
    msg = msg[cnt + 1:]
    kcnt = 0
    cnt = 0
    while (1):
        if (msg[cnt] >= '0' and msg[cnt] <= '9'):
            kcnt += 1
        else:
            kcnt = 0
        if (kcnt == 11):
            phone = msg[cnt - 10:cnt + 1]
            msg = msg[:cnt - 10] + msg[cnt + 1:]
            break
        cnt += 1


    msg, province, city = sol_p_c(msg)
    msg, county = sol_county(msg)
    msg, town = sol_town(msg)

    # 把处理过后的信息赋值给person,person是最后输出的变量
    person['姓名'] = name
    person['手机'] = phone
    person['地址'].append(province)
    person['地址'].append(city)
    person['地址'].append(county)
    person['地址'].append(town)

    # 第一难度的最终处理
    if (op == 1):
        person['地址'].append(msg)
    else:
        # 第二难度的处理,包括街道,街道号,详细地址
        tmp = ['路', '街', '巷', '社区', '村', '道', '里']
        road = ""
        add_len = 0
        pos = 999
        for x in tmp:
            now = msg.find(x)
            if (now >= 0 and now <= pos):
                pos = now
                add_len = len(x)

        if (pos != 999 and pos < 6):
            road = msg[:pos + 1]
            msg = msg[pos + 1:]

        tmp = ['号', '弄']
        street_num = ""
        add_len = 0
        pos = 999
        for x in tmp:
            now = msg.find(x)
            if (now >= 0 and now <= pos):
                pos = now
                add_len = len(x)

        if (pos != 999 and pos < 5):
            street_num = msg[:pos + 1]
            msg = msg[pos + 1:]
        person['地址'].append(road)
        person['地址'].append(street_num)
        person['地址'].append(msg)

    # 转换成json格式
    person=json.dumps(person)
    print(person)
