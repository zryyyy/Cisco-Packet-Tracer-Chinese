# Cisco Packet Tracer Chinese
Cisco Packet Tracer 汉化

目前版本：8.2.1

基本全部参考[EmotionalAmo](https://github.com/EmotionalAmo)大佬，在用谷歌翻译完后自己稍微改了一些觉得生硬的地方，如果有翻译错误请提交 Issues

[EmotionalAmo/Cisco-Packet-Tracer-Chinese: 思科模拟器汉化 Cisco-Packet-Tracer-Chinese (github.com)](https://github.com/EmotionalAmo/Cisco-Packet-Tracer-Chinese/tree/master)

### 使用方法

#### 直接使用

1. 下载项目中的`chinese.8.2.1.ptl`文件，放到`C:\Program Files\Cisco Packet Tracer 8.2.1\languages\`目录下
2. 在放完文件后打开软件，依次点击`Options\Preferences\Interface`，选择`chinese.8.2.1.ptl`后点击`Change Language`重启后即可更改语言



#### 自己翻译

1. 提取`C:\Program Files\Cisco Packet Tracer 8.2.1\languages\`目录下的`template.ts`文件，复制到项目文件夹下
2. 运行`main.py`（需要安装pygtrans这个库）
3. 在程序运行结束后会得到`chinese.8.2.1.ts`这个文件，使用在安装Packet Tracer时一起安装的Qt Linguist打开，然后点击`发布`后会得到`chinese.8.2.1.qm`文件
4. 将`chinese.8.2.1.qm`的后缀改为`.ptl`即可



有什么问题或者该更新了提 Issues 叫我！！！
