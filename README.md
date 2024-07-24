# Cisco Packet Tracer Chinese
Cisco Packet Tracer 汉化

目前版本：8.2.1（理论上支持 8.2.2 ）

基本全部参考 [EmotionalAmo](https://github.com/EmotionalAmo) 大佬的代码，在用谷歌翻译完后略微修改了一些翻译错误和生硬部分，如有翻译问题或建议请提交 Issues

[EmotionalAmo/Cisco-Packet-Tracer-Chinese: 思科模拟器汉化 Cisco-Packet-Tracer-Chinese (github.com)](https://github.com/EmotionalAmo/Cisco-Packet-Tracer-Chinese/tree/master)

### 使用方法

#### 直接使用

##### Windows

1. 下载项目中的 `chinese.8.2.1.ptl` 文件，放到 `C:\Program Files\Cisco Packet Tracer 8.2.1\languages\` 目录下
2. 在放完文件后打开软件，依次点击 `Options\Preferences\Interface` ，选择 `chinese.8.2.1.ptl` 后点击 `Change Language` 重启后即可更改语言

##### MacOS

感谢 [sgzkk](sgzkk@qq.com) 提供的详细步骤（以 MacOS 10.15.7 为例）

1. 打开 `访达`，右上角 `搜索栏`，搜索 `Cisco`，点击进入蓝色 `Cisco Packet Tracer x.x.x` 文件夹，双指同时点击触摸板（右键单击） `Cisco Packet Tracer x.x.x` 图标，点击弹出菜单中 `显示包内容`，点击 `Contents` 文件夹，点击 `LANGUAGES` 文件夹（理论文件夹路径如图所示），粘贴 `chinese.8.2.1.ptl`

   ![mac](https://github.com/zryyyy/Cisco-Packet-Tracer-Chinese/blob/main/img/mac.png)

2. 打开 Cisco pt 程序，点击右上角 Cisco Packet Tracer，点击 `preferences`，弹出窗口中下拉滚动条，在 `select language` 区块点击选择 `Chinese 8.2.1.ptl`，点击右下角的 `change language`，在弹出窗口中点击 `OK`。重启 Cisco Packet Tracer，即可进入简体界面

3. 如需要改回英文界面，点击 `选项`，`偏好设置`，`选择语言`，`default.ptl`，点右下角 `改变语言`，点击弹出窗口的 `OK`，重启即可回到英文界面



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