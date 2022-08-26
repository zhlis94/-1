# -0 python_ose 开源版本

> python_ose 开源版本上线，具体请看 api --> py_ose.md
>
> 注：功能比exe版本更为丰富



# -1 相关配置

> 注：exe程序如果出现闪退情况，是因为没有搭载 python3 环境 --> 环境搭载教程具体请看 py3_ins_environment.md

## 第一步：注册测试号

> 网址:  https://mp.weixin.qq.com/

![1](https://gitee.com/qishen-1/wxgzh/raw/master/img/1.png)

![2](https://gitee.com/qishen-1/wxgzh/raw/master/img/2.png)

![3](https://gitee.com/qishen-1/wxgzh/raw/master/img/3.png)

![4](https://gitee.com/qishen-1/wxgzh/raw/master/img/4.png)

![5](https://gitee.com/qishen-1/wxgzh/raw/master/img/5.png)

![6](https://gitee.com/qishen-1/wxgzh/raw/master/img/6.png)

![7](https://gitee.com/qishen-1/wxgzh/raw/master/img/7.png)

## 第二步：登陆刚注册的公众号

![8](https://gitee.com/qishen-1/wxgzh/raw/master/img/8.png)

![9](https://gitee.com/qishen-1/wxgzh/raw/master/img/9.png)

### 第三步：登陆测试号

> 注：如果exe中报`access_token`错误，就刷新此页面，重新填`id`和`serect`就行

![10](https://gitee.com/qishen-1/wxgzh/raw/master/img/10.png)

![11](https://gitee.com/qishen-1/wxgzh/raw/master/img/11.png)

![12](https://gitee.com/qishen-1/wxgzh/raw/master/img/12.png)

![13](https://gitee.com/qishen-1/wxgzh/raw/master/img/13.png)



# -2 修改config配置信息

> 下载下来后，打开对应的文件夹

如何下载？

![](https://gitee.com/qishen-1/wxgzh/raw/master/img/15.png)

![](https://gitee.com/qishen-1/wxgzh/raw/master/img/16.png)

找到这个config文件

![image-20220822131738651](https://gitee.com/qishen-1/wxgzh/raw/master/img/17.png)

打开修改

![14](https://gitee.com/qishen-1/wxgzh/raw/master/img/14.png)

# -3 运行exe

> 双击运行exe程序

![image-20220822131855242](https://gitee.com/qishen-1/wxgzh/raw/master/img/18.png)

# -4 报错信息

1. 如果出现闪退，请看 `-0`注释；

2. 如果出现`access_token`错误，请看`-1 第三步`注释；

3. 如果出现错误信息是`推送消息失败，请检查config.txt文件是否与程序位于统一路径`，请将`config`和`exe`放在同一个文件夹内；
4. 如果出现错误信息是`推送消息失败，请检查模板id是否正确`，请仔细检查模板id 复制时是不是多了个空格或者少了数据；
5. 如果出现错误信息是`推送消息失败，请检查微信号是否正确`，请仔细检查微信号 是否显示在测试号中；
6. 生日数据前面步骤有误，请将生日对应的模板从 `{{birth_day.DATA}}`改成`{{birthday.DATA}}`