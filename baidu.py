import requests
import hashlib
import random
from xml.etree import ElementTree as ET

# 请将以下 APPID 和 SECRET_KEY 替换为您自己的
APPID = '您的APPID'
SECRET_KEY = '您的密钥'

def trans(q, from_lang='auto', to_lang='zh'):
    '''
    使用百度翻译API进行翻译
    '''
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    salt = str(random.randint(32768, 65536))  # 生成随机数
    sign_str = APPID + q + salt + SECRET_KEY
    sign = hashlib.md5(sign_str.encode('utf-8')).hexdigest()
    params = {
        'q': q,
        'from': from_lang,
        'to': to_lang,
        'appid': APPID,
        'salt': salt,
        'sign': sign
    }
    response = requests.get(url, params=params)
    result = response.json()
    if 'trans_result' in result:
        return result['trans_result'][0]['dst']
    else:
        print('翻译出错，错误码：', result.get('error_code'), '错误信息：', result.get('error_msg'))
        return q  # 出错时返回原文本

print("开始翻译")
tree = ET.parse("template.ts")

for child in tree.iter():
    if child.tag == 'source' and child.text:
        temp = trans(child.text)
    if child.tag == 'translation':
        child.text = temp  # 更新翻译文本

print("翻译完成，正在生成文件")
tree.write('chinese-baidu.8.2.2.ts', encoding='UTF-8')