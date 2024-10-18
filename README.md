# Cisco Packet Tracer Chinese
Cisco Packet Tracer 汉化

目前版本：8.2.2（8.2.2 需要使用 Qt Linguist 打包，如果觉得麻烦可以继续使用 8.2.1）

参考 [EmotionalAmo](https://github.com/EmotionalAmo) 大佬的代码，在用谷歌翻译完后修改了一些翻译错误和生硬部分，如有翻译问题或建议请提 Issues 或 PR

[EmotionalAmo/Cisco-Packet-Tracer-Chinese: 思科模拟器汉化 Cisco-Packet-Tracer-Chinese (github.com)](https://github.com/EmotionalAmo/Cisco-Packet-Tracer-Chinese/tree/master)

### 使用方法

#### 直接使用

##### Windows

1. 下载项目中的 `chinese.x.x.x.ptl` 文件，放到 `C:\Program Files\Cisco Packet Tracer x.x.x\languages\` 目录下

2. 在放完文件后打开软件，依次点击 `Options\Preferences\Interface` ，选择 `chinese.x.x.x.ptl` 后点击 `Change Language` 重启后即可更改语言

- *注：把版本号替换为已安装PT的版本号即可*


##### MacOS

感谢 [sgzkk](mailto:sgzkk@qq.com) 提供的详细步骤（以 MacOS 10.15.7 为例）

1. 打开 `访达`，右上角 `搜索栏`，搜索 `Cisco`，点击进入蓝色 `Cisco Packet Tracer x.x.x` 文件夹，双指同时点击触摸板（右键单击） `Cisco Packet Tracer x.x.x` 图标，点击弹出菜单中 `显示包内容`，点击 `Contents` 文件夹，点击 `LANGUAGES` 文件夹（理论文件夹路径如图所示），粘贴 `chinese.x.x.x.ptl`

   ![mac](https://github.com/zryyyy/Cisco-Packet-Tracer-Chinese/blob/main/img/mac.png)

2. 打开 Cisco pt 程序，点击右上角 Cisco Packet Tracer，点击 `preferences`，弹出窗口中下拉滚动条，在 `select language` 区块点击选择 `Chinese x.x.x.ptl`，点击右下角的 `change language`，在弹出窗口中点击 `OK`。重启 Cisco Packet Tracer，即可进入简体界面

3. 如需要改回英文界面，点击 `选项`，`偏好设置`，`选择语言`，`default.ptl`，点右下角 `改变语言`，点击弹出窗口的 `OK`，重启即可回到英文界面

- *注：把版本号替换为已安装PT的版本号即可*


#### 自己翻译

1. 提取 `C:\Program Files\Cisco Packet Tracer x.x.x\languages\` 目录下的 `template.ts` 文件，复制到项目文件夹下

2. 运行 `main.py` （需要安装 pygtrans `pip install pygtrans` ）

3. 在程序运行结束后会得到 `chinese.8.2.2.ts` 这个文件，使用在安装 Packet Tracer 时一起安装的 Qt Linguist 打开，然后点击 `发布` 后会得到 `chinese.8.2.2.qm` 文件

4. 将 `chinese.8.2.2.qm` 的后缀改为 `.ptl` 即可


##### 使用百度

1. ...

2. 安装依赖，申请百度的 [API](https://api.fanyi.baidu.com/)

3. 把 `baidu.py` 中的 APPID 和 SECRET_KEY 替换为刚刚申请的并运行

4. ...

- *注：翻译一次大约消耗三十万字符，每月免费额度为一百万字符*

有问题请提 Issues 或 PR ！！！(●'◡'●)


### BTW

#### 2024.5.13

以后更新会减少，因为计算机网络的课结束了😎

#### 2024.10.18

8.2.2 翻译需要手动打包，但是非常简单
