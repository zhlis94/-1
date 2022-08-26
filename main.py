import time
import random
import requests
# !/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import random
import time
import urllib
import urllib.request as request
import urllib.error as error
import json
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage

"""
聚合数据  非vip用户接口数每日最大请求 30 次 
"""

# 秘钥key
joke_key = 'd1b101fe85a65546b4f51dd810221e2c'  # 鸡汤秘钥
weather_key = 'f198abcc3dbf38e9f2a5a71faf741a5c'  # 天气秘钥


# 读取信息
def imp_mes():
    try:
        with open('config.txt') as f:
            message = f.read()
            mes = eval(message)
            return mes
    except Exception as e:
        print('config.txt与exe程序不在同一路径内！(解决方法:放入同一个文件夹)')
        input('按任意键结束...')


# 颜色接口
def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


# 日期接口
def get_days(birthday, love_day):
    currentTime = datetime.datetime.now()
    now_time = currentTime.date()
    birth_day = str(datetime.datetime.strptime(birthday, '%Y-%m-%d').date())
    love_Day = datetime.datetime.strptime(love_day, '%Y-%m-%d').date()
    str_now_time = str(now_time)
    str_year = int(str(str_now_time).split('-')[0])
    birth_day = str(birth_day.replace(str(birth_day.split('-')[0]), str(str_year + 1)))
    date = birth_day.replace(str(birth_day.split('-')[0]), str(str_year + 1))
    str_time = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    delta_birth = str_time - now_time
    if delta_birth.days > 365:
        birth_day = str(birth_day.replace(str(birth_day.split('-')[0]), str(str_year)))
        date = birth_day.replace(str(birth_day.split('-')[0]), str(str_year))
        str_time = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        delta_birth = str_time - now_time
    delta_love = now_time - love_Day
    day_list = [now_time, delta_birth.days, delta_love.days]
    return day_list
# 当天时间接口
def getweek():
    """
    TODO:
    Wednesday 匹配数据出错，暂时无法解决
    :return:
    """
    try:
        week_en = time.strftime("%A", time.localtime(time.time()))
        week_list = {
            "Monday": "星期一",
            "Tuesday": "星期二",
            "Wednesday ": "星期三",
            "Thursday": "星期四",
            "Friday": "星期五",
            "Saturday": "星期六",
            "Sunday": "星期日"
        }
        currentTime = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        week = week_list[week_en]
        day = currentTime + ' ' + week
        return day
    except Exception as e:
        currentTime = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        day = currentTime + '  星期三'
        return day


# 天气预报接口
def weather():
    api_url = 'http://apis.juhe.cn/simpleWeather/query'
    params_dict = {
        "city": city,  # 查询天气的城市名称，如：北京、苏州、上海
        "key": weather_key,  # 您申请的接口API接口请求Key
    }
    params = urllib.parse.urlencode(params_dict)
    try:
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
            try:
                result = json.loads(content)
                error_code = result['error_code']
                if (error_code == 0):
                    temperature = result['result']['realtime']['temperature']
                    today_temperature = result['result']['future'][0]['temperature']
                    humidity = result['result']['realtime']['humidity']
                    info = result['result']['realtime']['info']
                    power = result['result']['realtime']['power']
                    aqi = result['result']['realtime']['aqi']
                    wea_dict = {
                        'temperature': temperature,
                        'today_temperature': today_temperature,
                        'humidity': humidity,
                        'info': info,
                        'power': power,
                        'aqi': aqi,
                    }
                    return wea_dict
                else:
                    print("请求失败:%s %s" % (result['error_code'], result['reason']))
                    input('按任意键结束...')
            except Exception as e:
                print("网络环境波动，请求异常")
                input('按任意键结束...')
        else:
            # 可能网络异常等问题，无法获取返回内容，请求异常
            print("网络环境波动，请求异常")
            input('按任意键结束...')
    except Exception as err:
        print("网络环境波动，请求异常")
        input('按任意键结束...')


# 笑话接口
def joke():
    api_url = 'https://apis.juhe.cn/fapig/soup/query'
    params_dict = {
        "key": joke_key,  # 您申请的接口API接口请求Key
    }
    params = urllib.parse.urlencode(params_dict)
    req = request.Request(api_url, params.encode())
    response = request.urlopen(req)
    content = response.read()
    res = json.loads(content)
    joke = res['result']['text']
    return joke


def live():
    """
    请注意 city=省份 或者城市(不带市-->杭州） 或者 区(如-->余杭)
    :return:
    """
    api_url = 'https://www.tianqiapi.com/life/lifepro?appid=73823423&appsecret=YUYt9ldh&city=' + city
    response = requests.get(url=api_url)
    data = response.json()
    try:
        if data['errcode']:
            print('城市或区域命名不规范(杭州市-->杭州，余杭区-->余杭)')
            input('按任意键结束...')
    except Exception as e:
        pass

    living_index = {
        "spf": data['data']['fangshai']['level'] + ', 建议' + data['data']['fangshai']['desc'],  # 防晒spf
        "dressing": data['data']['chuanyi']['level'] + ', ' + data['data']['chuanyi']['desc'],  # 穿衣指数
        "morning_exercise": data['data']['chenlian']['level'] + ', ' + data['data']['chenlian']['desc'],  # 晨练
        "get_cold": data['data']['ganmao']['level'] + ', ' + data['data']['ganmao']['desc'],  # 感冒系数
        "air_conditioner": data['data']['kongtiao']['level'] + ', ' + data['data']['kongtiao']['desc']  # 空调
    }
    return living_index


# 天气预警
def _weather():
    api_url = 'https://v0.yiketianqi.com/api?unescape=1&version=v63&appid=73823423&appsecret=YUYt9ldh&city=' + city
    response = requests.get(url=api_url)
    data = response.json()
    try:
        if data['errcode']:
            print('城市或区域命名不规范(杭州市-->杭州，余杭区-->余杭)')
            input('按任意键结束...')
    except Exception as e:
        pass

    try:
        if not data['alarm']:
            wea_data = {
                "air_tips": data['air_tips'],  # 小建议
                "alarm": '此地区暂时没有天气预警哦！',
                "next_hours": '此地区暂时没有天气预警哦！',
            }
        else:
            wea_data = {
                "air_tips": data['air_tips'],  # 小建议
                "alarm": '请注意：' + data['alarm'][0]['alarm_title'],  # 天气预警
                "next_hours": data['hours'][1]['hours'] + '的天气状况：' + data['hours'][1]['wea'],  # 下个小时的天气
            }
        return wea_data
    except Exception as e:
        return '该区域暂不支持天气预警！'


if imp_mes():
    # 微信Key
    appID = imp_mes()['appID']
    appsecret = imp_mes()['appsecret']
    # 关注的成员ID
    user_id = imp_mes()['user_id']
    # 模板ID
    template_id = imp_mes()['template_id']
    # 所在地
    city = imp_mes()['city']
    # 生日
    birthday = imp_mes()['birthday']
    # 恋爱开始日
    love_day = imp_mes()['love_day']
    # 推送消息
    client = WeChatClient(appID, appsecret)
    wm = WeChatMessage(client)

    try:
        for user_id in user_id:
            weather = weather()
            data = {
                "date": {"value": getweek(), "color": get_random_color()},  # 日期
                "city": {"value": city, "color": get_random_color()},  # 城市
                "now_temperature": {"value": weather['temperature'], "color": get_random_color()},  # 现在的温度
                "temperature": {"value": weather['today_temperature'], "color": get_random_color()},  # 今天的温度
                "humidity": {"value": weather['humidity'], "color": get_random_color()},  # 湿度
                "weather": {"value": weather['info'], "color": get_random_color()},  # 天气
                "wind": {"value": weather['power'], "color": get_random_color()},  # 风力
                "air_quality": {"value": weather['aqi'], "color": get_random_color()},  # 空气质量
                "morning_exercise": {"value": live()['morning_exercise'], "color": get_random_color()},  # 晨练
                "dressing": {"value": live()['dressing'], "color": get_random_color()},  # 穿衣
                "get_cold": {"value": live()['get_cold'], "color": get_random_color()},  # 感冒系数
                "air_conditioner": {"value": live()['air_conditioner'], "color": get_random_color()},  # 是否适合开空调
                "spf": {"value": live()['spf'], "color": get_random_color()},  # 防晒指数
                "air_tips": {"value": _weather()['air_tips'], "color": get_random_color()},  # 天气贴士
                "alarm": {"value": _weather()['alarm'], "color": get_random_color()},  # 气象预警
                "next_hours": {"value": _weather()['next_hours'], "color": get_random_color()},  # 下一时间段的天气预警
                "birthday": {"value": get_days(birthday, love_day)[1], "color": get_random_color()},  # 生日
                "love_day": {"value": get_days(birthday, love_day)[2], "color": get_random_color()},  # 恋爱日
                "joke": {"value": joke(), "color": get_random_color()},  # 鸡汤
            }
            resp = wm.send_template(user_id, template_id, data)
            print('发送成功!')
            input('按任意键结束...')
    except Exception as e:
        print('user_id或template_id不正确，请仔细检查！')
        input('按任意键结束...')
