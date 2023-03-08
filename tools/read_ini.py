# _*_coding:utf-8_*_
"""
@ Author:陈金泉
@ Date:2023/3/7 11:59
@ Description: 读取ini文件的一个option，并将里面的键值对生成一个字典格式返回
"""
import configparser


def read_ini(path, option_name, encoding='utf-8'):
    """
    :param path: ini文件的地址
    :param option_name: ini文件中需要读取的option的名称
    :param encoding: ini文件的编码方式，默认utf-8
    :return: 返回当前ini文件中，读取的option下所有的键值对组成的字典对象
    """

    cfp = configparser.ConfigParser()
    cfp.read(path, encoding=encoding)

    key_list = cfp.options(option_name)
    value_list = [cfp.get(option_name, key_list[i]) for i in range(len(key_list))]

    return dict(zip(key_list, value_list))
