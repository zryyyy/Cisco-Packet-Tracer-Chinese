# Cisco Packet Tracer Chinese
Cisco Packet Tracer 汉化

目前版本：8.2.1（理论上支持 8.2.2 ）

基本全部参考 [EmotionalAmo](https://github.com/EmotionalAmo) 大佬的代码，在用谷歌翻译完后略微修改了一些翻译错误和生硬部分，如有翻译问题或建议请提交 Issues

[EmotionalAmo/Cisco-Packet-Tracer-Chinese: 思科模拟器汉化 Cisco-Packet-Tracer-Chinese (github.com)](https://github.com/EmotionalAmo/Cisco-Packet-Tracer-Chinese/tree/master)

### 使用方法

#### 直接使用

1. 下载项目中的 `chinese.8.2.1.ptl` 文件，放到 `C:\Program Files\Cisco Packet Tracer 8.2.1\languages\` 目录下
2. 在放完文件后打开软件，依次点击 `Options\Preferences\Interface` ，选择 `chinese.8.2.1.ptl` 后点击 `Change Language` 重启后即可更改语言



#### 自己翻译

1. 提取 `C:\Program Files\Cisco Packet Tracer x.x.x\languages\` 目录下的 `template.ts` 文件，复制到项目文件夹下
2. 运行 `main.py` （需要安装 pygtrans 这个库）
3. 在程序运行结束后会得到 `chinese.8.2.1.ts` 这个文件，使用在安装 Packet Tracer 时一起安装的 Qt Linguist 打开，然后点击 `发布` 后会得到 `chinese.8.2.1.qm` 文件
4. 将 `chinese.8.2.1.qm` 的后缀改为 `.ptl` 即可



有什么问题或者该更新了提 Issues 叫我！！！



### BTW

#### 2024.5.13

理论上这次的更新是最后一次更新，因为计算机网络的课结束了😎

关于 8.2.2 版本：目前还没发现翻译的文件出现问题
