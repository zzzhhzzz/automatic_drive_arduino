# 无人驾驶小车说明文档

<center>
 <img src=".\Xmind\无人驾驶小车.png">
</center>

## 一、驱动开发

第一部分为小车驱动，可使用arduino IDE开发，其中LED灯的亮灭通过控制引脚高低电平即可，电机与舵机的控制使用pwm信号，摄像头则需要连接控制板热点，通过收发请求的方式调控。使用c++的命令可以将其分别封装为函数，这些函数在接下来的几步中都是基础，故在此不进行单独效果演示。

驱动开发函数封装可在以下目录查看：

```python
"./pythonUI/automatic_drive_arduino/automatic_drive_arduino.ino"
"./web_control/web_control.ino"
```

## 二、电脑上位机控制

使用Tkinter作为UI的开发工具，调用了CustomTKinter库作为设计辅助。而连接控制小车是通过开启开发板热点，电脑连接热点，使用python的requests模块收发http请求的方法完成。

UI界面设计如下：

<center>
 <img src=".\images\UI界面.png">
</center>

在UI界面，用户可以通过鼠标键盘操作实现控制小车行走，调节速度与方向参数，打印小车传感器数据，实时监控小车摄像头，在监控摄像头过程中还可通过键盘操作保存摄像头照片并直接传输至电脑本地，进行数据采集。

代码目录：

```python
"./pythonUI/automatic_drive_arduino/pythonUI.py"
```

## 三、手机web操控

在esp32上开发html前端，同样可以实现上述功能，前端设计如下：

<center>
 <img src=".\images\web前端.jpg">
</center>

代码目录：

```python
"./web_control/web_control.ino"
```

参考课程：

```python
"""
https://space.bilibili.com/1872807136/channel/collectiondetail?sid=609260
引航计划系列课-第三期暑期实训小车营
"""
```

## 四、无人驾驶实现

### 4.1easydata与easyDL

训练数据集部分展示：

<center>
 <img src=".\images\datasets.jpg">
</center>

数据集导出目录：

```python
"./easydl/dataset/"
```

esayDL模型部署接口：

```python
"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/segmentation/roadsegimage"
```



<center>
 <img src=".\images\easyDL.jpg">
</center>

评估结果：

<center>
 <img src=".\images\easyDL评估.jpg">
</center>

接口调用代码目录：

```python
"./easydl/api.py"
```

### 4.2鸟瞰图转换

<center>
 <img src=".\Xmind\鸟瞰透视变换算法.png">
</center>

### 4.3A*算法

<center>
 <img src=".\Xmind\A星算法.png">
</center>

代码目录：

```python
"./automatic_drive/"
```

本部分代码参考资料：

```pythpn
"人工智能引航计划公益课"
"https://space.bilibili.com/1872807136?spm_id_from=333.337.0.0"
```

