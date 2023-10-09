from xml.etree import ElementTree as ET

from pygtrans import Translate

global temp


def trans(eng):
    return Translate().translate(eng, target='zh-CN').translatedText


print("开始翻译")
tree = ET.parse("template.ts")

for children in tree.iter():
    if children.tag == 'source':
        temp = trans(str(children.text))
    if children.tag == 'translation':
        children.text = str(temp)  # type: ignore

print("翻译完成，正在生成文件")
tree.write('chinese.8.2.1.ts', encoding='UTF-8')