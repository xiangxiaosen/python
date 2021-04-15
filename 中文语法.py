import re, os, stat, gzip, time, hmac, queue, base64, random, hashlib, hashlib, itertools, datetime, calendar,threading, tkinter,socket,struct
import execjs  # JS模块，需要安装pyexecjs
import requests  # 网页请求模块，需要安装requests
import pymysql  # Mysql模块，需要安装PyMysql
from urllib import parse
from tkinter import messagebox
from pypinyin import Style, pinyin  #需要安装拼音库 pypinyin
from requests.packages.urllib3.exceptions import InsecureRequestWarning

讯代理_代理地址 = 'forward.xdaili.cn:80'

文件打开方式_只读 = 'r'
文件打开方式_二进制_只读 = 'rb'
文件打开方式_读写 = 'r+'
文件打开方式_二进制_读写 = 'rb+'
文件打开方式_覆盖写入 = 'w'  # 文件不存在会创建新文件
文件打开方式_二进制_覆盖写入 = 'wb'  # 文件不存在会创建新文件
文件打开方式_覆盖读写 = 'w+'  # 文件不存在会创建新文件
文件打开方式_二进制_覆盖读写 = 'wb+'  # 文件不存在会创建新文件
文件打开方式_追加写入 = 'a'  # 文件不存在会创建新文件
文件打开方式_二进制_追加写入 = 'ab'  # 文件不存在会创建新文件
文件打开方式_追加读写 = 'a+'  # 文件不存在会创建新文件
文件打开方式_二进制_追加读写 = 'ab+'  # 文件不存在会创建新文件

time_时间格式_取简化星期名称 = '%a'  # 本地(local) 简化星期名称
time_时间格式_取完整星期名称 = '%A'  # 本地完整星期名称
time_时间格式_取简化月份名称 = '%b'  # 本地简化月份名称
time_时间格式_取整月份名称 = '%B'  # 本地完整月份名称
time_时间格式_取日期和时间 = '%c'  # 本地相应的日期和时间表示
time_时间格式_取日 = '%d'  # 一个月中的第几天（01-31）
time_时间格式_取时24 = '%H'  # 一天中的第几个小时（24小时制00-23）
time_时间格式_取时12 = '%I'  # 第几个小时（12小时制01-12）
time_时间格式_取一年中的第几天 = '%j'  # 一年中的第几天（001-366）
time_时间格式_取月份 = '%m'  # 月份（01-12）
time_时间格式_取分钟 = '%M'  # 分钟数（00-59）
time_时间格式_取am或pm相应符 = '%p'  # 本地am或pm的相应符
time_时间格式_取秒 = '%S'  # 秒（01-60）
time_时间格式_取年中第几星期U = '%U'  # 一年中的星期数。（00-53 星期天是一个星期的开始）第一个星期天之前的所有天数都放在第0周
time_时间格式_取星期几 = '%w'  # 一个星期中的第几天（0-6 0是星期天）
time_时间格式_取年中第几星期W = '%W'  # 和%U基本相同，不同的是%W以星期一为一个星期的开始
time_时间格式_取日月年 = '%x'  # 本地相应日期
time_时间格式_取时分秒 = '%X'  # 本地相应时间
time_时间格式_取年份 = '%y'  # 去掉世纪的年份（00-99）
time_时间格式_取完整年份 = '%Y'  # 完整的年份
time_时间格式_取时区 = '%z'  # 时区的名字

def 调试输出(欲输出的内容):
    print(欲输出的内容)


def 到文本(欲转换的数据, 编码方式=None):
    try:
        if 编码方式 == None:
            return str(欲转换的数据)
        else:
            return str(欲转换的数据, 编码方式)
    except Exception as error:
        print('到文本：运行出错|' + str(error))
        return ''


def 到整数(欲转换的数据):
    try:
        return int(欲转换的数据)
    except Exception as error:
        print('到整数：运行出错|' + str(error))
        return -1


def 到数值(欲转换的数据):
    try:
        return float(欲转换的数据)
    except Exception as error:
        print('到数值：运行出错|' + str(error))
        return -1.0


def 对象到文本(欲转换的数据):
    try:
        return repr(欲转换的数据)
    except Exception as error:
        print('对象到文本：运行出错|' + str(error))
        return ''


def 到元组(欲转换的数据):
    try:
        return tuple(欲转换的数据)
    except Exception as error:
        print('到元组：运行出错|' + str(error))
        return ()


def 到列表(欲转换的数据):
    try:
        return list(欲转换的数据)
    except Exception as error:
        print('到列表：运行出错|' + str(error))
        return []


def 到字典(欲转换的数据):
    try:
        return dict(欲转换的数据)
    except Exception as error:
        print('到字典：运行出错|' + str(error))
        return {}


def 到字节(欲转换的数据, 编码方式=None):
    '传入字符串类型需要传编码'
    try:
        if 编码方式 == None:
            return bytes(欲转换的数据)
        else:
            return bytes(欲转换的数据, 编码方式)
    except Exception as error:
        print('到字节：运行出错|' + str(error))
        return b''


def 到字节数组(欲转换的数据, 编码方式=None):
    '可变的字节序列，相当于bytes的可变版本'
    try:
        if 编码方式 == None:
            return bytearray(欲转换的数据)
        else:
            return bytearray(欲转换的数据, 编码方式)
    except Exception as error:
        print('到字节数组：运行出错|' + str(error))
        return bytearray(b'')


def 序列_是否都为真(欲检验的序列):
    '判断传入的列表 字典 元组 range是否都为真,字典检验的是键,空列表为真 空元组为假'
    try:
        return all(欲检验的序列)
    except Exception as error:
        print('序列_是否都为真：运行出错|' + str(error))
        return False


def 序列_是否有真(欲检验的序列):
    '判断传入的列表 字典 元组 range是否有一个值为真,字典检验的是键,空列表 0 空文本都为假'
    try:
        return any(欲检验的序列)
    except Exception as error:
        print('序列_是否都为真：运行出错|' + str(error))
        return False


def 字节数组_清空(字节数组):
    '成功返回True,失败返回False'
    if isinstance(字节数组, bytearray) != True:
        print('字节数组_清空：传入参数有误')
        return False
    字节数组.clear()
    return True


def 字节数组_顺序反转(字节数组):
    '成功返回True,失败返回False'
    if isinstance(字节数组, bytearray) != True:
        print('字节数组_顺序反转：传入参数有误')
        return False
    字节数组.reverse()
    return True


def 取数据类型(欲查询的数据):
    return type(欲查询的数据)


def 取数据长度(欲查询的数据):
    '成功返回长度,失败返回-1'
    try:
        return len(欲查询的数据)
    except Exception as error:
        print('取数据长度：运行出错|' + str(error))
        return -1


def 集合(集合的数据):
    try:
        return set(集合的数据)
    except Exception as error:
        print('集合：运行出错|' + str(error))
        return set()


def 文本_取出现次数(原文本, 欲查询的文本, 开始的位置=0, 结束的位置=0):
    '成功返回次数,失败返回-1,,在字符串里边出现的次数，start 和 end 参数表示范围，可选'
    if isinstance(原文本, str) != True or isinstance(欲查询的文本, str) != True or isinstance(开始的位置, int) != True or isinstance(
            结束的位置, int) != True:
        print('文本_取出现次数：传入参数有误')
        return -1
    elif 结束的位置 < 1:
        结束的位置 = len(原文本)
    return 原文本.count(欲查询的文本, 开始的位置, 结束的位置)


def 文本_是否指定文本结尾(原文本, 结尾的文本, 开始的位置=0, 结束的位置=0):
    '如果字符串为指定的后缀返回True，否则返回False'
    if isinstance(原文本, str) != True or isinstance(结尾的文本, str) != True or isinstance(开始的位置, int) != True or isinstance(
            结束的位置, int) != True:
        print('文本_是否指定文本结尾：传入参数有误')
        return False
    elif 结束的位置 < 1:
        结束的位置 = len(原文本)
    return 原文本.endswith(结尾的文本, 开始的位置, 结束的位置)


def 文本_是否指定文本开头(原文本, 开头的文本, 开始的位置=0, 结束的位置=0):
    '如果字符串为指定的开头返回True，否则返回False'
    if isinstance(原文本, str) != True or isinstance(开头的文本, str) != True or isinstance(开始的位置, int) != True or isinstance(
            结束的位置, int) != True:
        print('文本_是否指定文本开头：传入参数有误')
        return False
    elif 结束的位置 < 1:
        结束的位置 = len(原文本)
    return 原文本.startswith(开头的文本, 开始的位置, 结束的位置)


def 文本_TAB转空格(原文本, 转换的数量=8):
    '失败出错返回空文本,把字符串中的 tab 符号（\t）转换为空格，如不指定参数，默认的空格数是 tabsize=8'
    if isinstance(原文本, str) != True or isinstance(转换的数量, int) != True:
        return '文本_TAB转空格：传入参数有误'
    try:
        return 原文本.expandtabs(tabsize=转换的数量)  # 默认数量比传入的少不知道为啥
    except Exception as error:
        print('文本_TAB转空格：运行出错|' + str(error))
        return ''


def 文本_寻找文本(原文本, 欲寻找的文本, 开始的位置=0, 结束的位置=0):
    '失败出错返回-1,检测是否包含在字符串中，如果有则返回索引值，否则返回 -1，start 和 end 参数表示范围，可选'
    if isinstance(原文本, str) != True or isinstance(欲寻找的文本, str) != True or isinstance(开始的位置, int) != True or isinstance(
            结束的位置, int) != True:
        print('文本_寻找文本：传入参数有误')
        return -1
    elif 结束的位置 < 1:
        结束的位置 = len(原文本)
    try:
        return 原文本.find(欲寻找的文本, 开始的位置, 结束的位置)
    except Exception as error:
        print('文本_寻找文本：运行出错|' + str(error))
        return -1


def 文本_倒找文本(原文本, 欲寻找的文本, 开始的位置=0, 结束的位置=0):
    '失败出错返回-1,类似于 find() 方法，不过是从右边开始查找'
    if isinstance(原文本, str) != True or isinstance(欲寻找的文本, str) != True or isinstance(开始的位置, int) != True or isinstance(
            结束的位置, int) != True:
        print('文本_倒找文本：传入参数有误')
        return -1
    elif 结束的位置 < 1:
        结束的位置 = len(原文本)
    try:
        return 原文本.rfind(欲寻找的文本, 开始的位置, 结束的位置)
    except Exception as error:
        print('文本_倒找文本：运行出错|' + str(error))
        return -1


def 文本_寻找文本index(原文本, 欲寻找的文本, 开始的位置=0, 结束的位置=0):
    '失败出错返回-1,跟 find 方法一样，不过如果 sub 不在 string 中会产生一个异常'
    if isinstance(原文本, str) != True or isinstance(欲寻找的文本, str) != True or isinstance(开始的位置, int) != True or isinstance(
            结束的位置, int) != True:
        print('文本_寻找文本index：传入参数有误')
        return -1
    elif 结束的位置 < 1:
        结束的位置 = len(原文本)
    try:
        return 原文本.index(欲寻找的文本, 开始的位置, 结束的位置)
    except Exception as error:
        print('文本_寻找文本index：运行出错|' + str(error))
        return -1


def 文本_倒找文本index(原文本, 欲寻找的文本, 开始的位置=0, 结束的位置=0):
    '失败出错返回-1,类似于 index() 方法，不过是从右边开始'
    if isinstance(原文本, str) != True or isinstance(欲寻找的文本, str) != True or isinstance(开始的位置, int) != True or isinstance(
            结束的位置, int) != True:
        print('文本_倒找文本index：传入参数有误')
        return -1
    elif 结束的位置 < 1:
        结束的位置 = len(原文本)
    try:
        return 原文本.rindex(欲寻找的文本, 开始的位置, 结束的位置)
    except Exception as error:
        print('文本_寻找文本rindex：运行出错|' + str(error))
        return -1


def 文本_是否全十进制数字U(原文本):
    '返回True,False,如果字符串只包含十进制数字则返回 True，否则返回False。这种方法是只针对unicode对象'
    if isinstance(原文本, str) != True:
        print('文本_是否全十进制数字U：传入参数有误')
        return False
    return 原文本.isdecimal()


def 文本_是否全数字字母(原文本):
    '返回True,False,如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True，否则返回 False'
    if isinstance(原文本, str) != True:
        print('文本_是否全数字字母：传入参数有误')
        return False
    return 原文本.isalnum()


def 文本_是否全数字(原文本):
    '返回True,False,如果字符串只包含数字则返回 True，否则返回 False'
    if isinstance(原文本, str) != True:
        print('文本_是否全数字：传入参数有误')
        return False
    return 原文本.isdigit()


def 文本_是否全数字U(原文本):
    '返回True,False,检测字符串是否只由数字组成，是则返回True，否则返回False。这种方法是只针对unicode对象'
    if isinstance(原文本, str) != True:
        print('文本_是否全数字U：传入参数有误')
        return False
    return 原文本.isnumeric()


def 文本_是否全空格(原文本):
    '返回True,False,如果字符串中只包含空格，则返回 True，否则返回 False'
    if isinstance(原文本, str) != True:
        print('文本_是否全空格：传入参数有误')
        return False
    return 原文本.isspace()


def 文本_是否标题化(原文本):
    '返回True,False,如果字符串是标题化（所有的单词都是以大写开始，其余字母均小写），则返回 True，否则返回 False'
    if isinstance(原文本, str) != True:
        print('文本_是否标题化：传入参数有误')
        return False
    return 原文本.istitle()


def 文本_是否全小写(原文本):
    '返回True,False,如果字符串中至少包含一个区分大小写的字符，并且这些字符都是小写，则返回 True，否则返回 False'
    if isinstance(原文本, str) != True:
        print('文本_是否全小写：传入参数有误')
        return False
    return 原文本.islower()


def 文本_是否全大写(原文本):
    '返回True,False,如果字符串中至少包含一个区分大小写的字符，并且这些字符都是大写，则返回 True，否则返回 False'
    if isinstance(原文本, str) != True:
        print('文本_是否全大写：传入参数有误')
        return False
    return 原文本.isupper()


def 文本_是否全字母(原文本):
    '返回True,False,如果字符串至少有一个字符并且所有字符都是字母则返回 True，否则返回 False'
    if isinstance(原文本, str) != True:
        print('文本_是否全字母：传入参数有误')
        return False
    return 原文本.isalpha()


def 文本_标题化(原文本):
    '失败返回空文本,返回标题化（所有的单词都是以大写开始，其余字母均小写）的字符串'
    if isinstance(原文本, str) != True:
        print('文本_标题化：传入参数有误')
        return ''
    return 原文本.title()


def 文本_首字母转大写(原文本):
    '失败返回空文本,把字符串的第一个字符改为大写'
    if isinstance(原文本, str) != True:
        print('文本_首字母转大写：传入参数有误')
        return ''
    return 原文本.capitalize()


def 文本_到小写(原文本):
    '失败返回空文本,把整个字符串的所有字符改为小写'
    if isinstance(原文本, str) != True:
        print('文本_到小写：传入参数有误')
        return ''
    return 原文本.casefold()


def 文本_到大写(原文本):
    '失败返回空文本,转换字符串中的所有小写字符为大写'
    if isinstance(原文本, str) != True:
        print('文本_到大写：传入参数有误')
        return ''
    return 原文本.upper()


def 文本_大小写字符到小写(原文本):
    '失败返回空文本,转换字符串中所有大写字符为小写'
    if isinstance(原文本, str) != True:
        print('文本_大小写字符到小写：传入参数有误')
        return ''
    return 原文本.lower()


def 文本_大小写翻转(原文本):
    '失败返回空文本,翻转字符串中的大小写'
    if isinstance(原文本) != True:
        print('文本_大小写翻转：传入参数有误')
        return ''
    return 原文本.swapcase()


def 文本_拼接(连接符, 欲拼接的序列):
    '失败返回空文本,以字符串作为分隔符，插入到 sub 中所有的字符之间'
    if isinstance(连接符, str) != True:
        print('文本_拼接：传入参数有误')
        return ''
    try:
        return 连接符.join(欲拼接的序列)
    except Exception as error:
        print('文本_拼接：运行出错|' + str(error))
        return ''


def 文本_居中(原文本, 填充目标长度=0):
    '失败返回空文本,返回一个居中的字符串，并使用空格填充长度'
    if isinstance(原文本, str) != True or isinstance(填充目标长度, int) != True:
        print('文本_居中：传入参数有误')
        return ''
    return 原文本.center(填充目标长度)


def 文本_左对齐(原文本, 填充目标长度=0):
    '失败返回空文本,返回一个左对齐的字符串，并使用空格填充长度'
    if isinstance(原文本, str) != True or isinstance(填充目标长度, int) != True:
        print('文本_左对齐：传入参数有误')
        return ''
    return 原文本.ljust(填充目标长度)


def 文本_右对齐(原文本, 填充目标长度=0):
    '失败返回空文本,返回一个右对齐的字符串，并使用空格填充长度'
    if isinstance(原文本, str) != True or isinstance(填充目标长度, int) != True:
        print('文本_右对齐：传入参数有误')
        return ''
    return 原文本.rjust(填充目标长度)


def 文本_右对齐0(原文本, 填充目标长度):
    '失败返回空文本,返回一个右对齐的字符串，并使用0填充长度'
    if isinstance(原文本, str) != True or isinstance(填充目标长度, int) != True:
        print('文本_右对齐0：传入参数有误')
        return ''
    return 原文本.zfill(填充目标长度)


def 文本_删左边全部空格(原文本):
    '失败返回空文本,去掉字符串左边的所有空格'
    if isinstance(原文本, str) != True:
        print('文本_删左边全部空格：传入参数有误')
        return ''
    return 原文本.lstrip()


def 文本_删右边全部空格(原文本):
    '失败返回空文本,去掉字符串右边的所有空格'
    if isinstance(原文本, str) != True:
        print('文本_删右边全部空格：传入参数有误')
        return ''
    return 原文本.rstrip()


def 文本_删首尾指定字符(原文本, 欲删除的内容=' '):
    '失败返回空文本,删除字符串首尾指定的字符,默认删除首尾空格'
    if isinstance(原文本, str) != True or isinstance(欲删除的内容, str) != True:
        print('文本_删首尾指定字符：传入参数有误')
        return ''
    return 原文本.strip(欲删除的内容)


def 文本_三元分割_左(原文本, 分割标识):
    '失败返回('','',原文本),将字符串分割成三元元组，存放分割的前面，分割标识本身，分割的后面'
    if isinstance(原文本, str) != True or isinstance(分割标识, str) != True:
        print('文本_三元分割_左：传入参数有误')
        return ('', '', 原文本)
    return 原文本.partition(分割标识)


def 文本_三元分割_右(原文本, 分割标识):
    '失败返回('','',原文本),类似于 partition() 方法，不过是从右边开始查找'
    if isinstance(原文本, str) != True or isinstance(分割标识, str) != True:
        print('文本_三元分割_右：传入参数有误')
        return ('', '', 原文本)
    return 原文本.rpartition(分割标识)


def 文本_子文本替换(原文本, 要替换的文本, 用作替换的文本, 替换的次数=-1):
    '失败返回空文本'
    if isinstance(原文本, str) != True or isinstance(要替换的文本, str) != True or isinstance(用作替换的文本,
                                                                                     str) != True or isinstance(替换的次数,
                                                                                                                int) != True:
        print('文本_子文本替换：传入参数有误')
        return ''
    return 原文本.replace(要替换的文本, 用作替换的文本, 替换的次数)


def 文本_分割文本(原文本, 分割标识=' ', 分割次数=-1):
    '失败返回空列表,如果分割次数被指定，则返回分割次数+1的列表，后面的不做分割在最后一个列表里'
    if isinstance(原文本, str) != True or isinstance(分割标识, str) != True or isinstance(分割次数, int) != True:
        print('文本_分割文本：传入参数有误')
        return []
    return 原文本.split(分割标识, 分割次数)


def 文本_换行分割(原文本, 保留换行=False):
    '失败返回空列表,用换行符做分割，可设置分割后是否保留换行符'
    if isinstance(原文本, str) != True or isinstance(保留换行, bool) != True:
        print('文本_换行分割：传入参数有误')
        return []
    return 原文本.splitlines(保留换行)


def 文本_生成翻译表(原文本, 翻译文本, 翻译表类型=0):
    '失败返回空字典,类型0是str 1是bytes  2是bytearray'
    if isinstance(原文本, str) != True or isinstance(翻译文本, str) != True or isinstance(翻译表类型, int) != True:
        print('文本_生成翻译表：传入参数有误')
        return {}
    elif 翻译表类型 < 0:
        翻译表类型 = 0
    elif 翻译表类型 > 2:
        翻译表类型 = 2
    try:
        if 翻译表类型 == 0:
            return str.maketrans(原文本, 翻译文本)
        elif 翻译表类型 == 1:
            return bytes.maketrans(原文本, 翻译文本)
        elif 翻译表类型 == 2:
            return bytearray.maketrans(原文本, 翻译文本)
    except Exception as error:
        print('文本_生成翻译表：运行出错|' + str(error))
        return {}


def 文本_转换字符(原文本, 翻译表, 过滤的内容=None):
    '失败返回空文本,配合生成的翻译表批量转换字符串中的字符，不想显示的可以过滤不做转换,使用过滤功能用bytes类型'
    if isinstance(原文本, (str, bytes, bytearray)) != True or isinstance(翻译表, dict) != True:
        print('文本_转换字符：传入参数有误')
        return ''
    try:
        if 过滤的内容 == None:
            return 原文本.translate(翻译表)
        else:
            return 原文本.translate(翻译表, 过滤的内容)
    except Exception as error:
        print('文本_转换字符：运行出错|' + str(error))
        return ''


def 文本_按键名转键值(按键名):
    "失败返回-1,传入按键名 如 A  或者1  2 3  返回整数的键值"
    if isinstance(按键名, str) != True:
        print('文本_按键名转键值：传入参数有误')
        return -1
    try:
        return ord(按键名)
    except Exception as error:
        print('文本_按键名转键值：运行出错|' + str(error))
        return -1


def 文本_键值转按键名(键值):
    '失败返回空文本,传入整数的键值 返回对应键值的键符'
    if isinstance(键值, int) != True:
        print('文本_键值转按键名：传入参数有误')
        return ''
    try:
        return chr(键值)
    except Exception as error:
        print('文本_键值转按键名：运行出错|' + str(error))
        return ''


def 文本_取出中间文本(原文本, 前面的文本, 后面的文本, 开始的位置=0):
    '失败返回空文本'
    if isinstance(原文本, str) != True or isinstance(前面的文本, str) != True or isinstance(后面的文本, str) != True or isinstance(
            开始的位置, int) != True:
        print('文本_取出中间文本：传入参数有误')
        return ''
    elif 原文本.find(前面的文本, 开始的位置) != -1 and 原文本.find(后面的文本, 开始的位置 + len(前面的文本)) != -1:
        return 原文本[原文本.find(前面的文本, 开始的位置) + len(前面的文本):原文本.find(后面的文本, 原文本.find(前面的文本) + len(前面的文本))]
    else:
        return ""


def 文本_取文本左边(原文本, 指定的文本):
    if isinstance(原文本, str) != True or isinstance(指定的文本, str) != True:
        print('文本_取文本左边：传入参数有误')
        return ''
    elif 原文本.find(指定的文本) != -1:
        return 原文本[0:原文本.find(指定的文本)]
    else:
        return ""


def 文本_取文本右边(原文本, 指定的文本):
    if isinstance(原文本, str) != True or isinstance(指定的文本, str) != True:
        print('文本_取文本右边：传入参数有误')
        return ''
    elif 原文本.rfind(指定的文本) != -1:
        return 原文本[原文本.rfind(指定的文本) + len(指定的文本):len(原文本)]
    else:
        return ""


def 文本_取左边(原文本, 要取出的数量):
    if isinstance(原文本, str) != True or isinstance(要取出的数量, int) != True:
        print('文本_取左边：传入参数有误')
        return ''
    return 原文本[0:要取出的数量]


def 文本_取右边(原文本, 要取出的数量):
    if isinstance(原文本, str) != True or isinstance(要取出的数量, int) != True:
        print('文本_取右边：传入参数有误')
        return ''
    return 原文本[len(原文本) - 要取出的数量:len(原文本)]


def 文本_取字符长度(原文本):
    '失败出错返回-1,这里只做字符串跟整数的长度返回'
    if isinstance(原文本, (str, int)) != True:
        print('文本_取字符长度：传入参数有误')
        return -1
    return len(str(原文本))


def 文本_取随机IP():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))


def 文本_取随机邮箱():
    邮箱后缀 = ['@qq.com', '@sina.com', '@126.com', '@163.com', '@hotmail.com', '@139.com', '@189.com', '@sohu.com',
            '@21cn.com', '@189.com', '@tom.com', '@aol.com', '@263.com', '@aliyun.com', '@foxmail.com', '@yeah.net']
    return 变量_取出随机元素([文本_取随机字母(int(文本_取随机范围数字(5, 9))), 文本_取随机数字(int(文本_取随机范围数字(5, 9))),
                      文本_取随机字符(int(文本_取随机范围数字(5, 9)))]) + 变量_取出随机元素(邮箱后缀)


def 文本_取随机手机号():
    号码前缀 = ['130', '131', '132', '134', '135', '136', '137', '138', '139', '147', '150', '151', '152', '153', '155',
            '156', '157', '158', '159', '170', '171', '180', '182', '183', '185', '186', '187', '188', '189']
    return 变量_取出随机元素(号码前缀) + 文本_取随机数字(8)


def 文本_取随机字母(取出的数量=1, 类型=0):
    '失败返回空文本,类型 0是小写 1是大写 2是混合'
    if isinstance(取出的数量, int) != True or isinstance(类型, int) != True:
        print('文本_取随机字母：传入参数有误')
        return ''
    if 取出的数量 < 1 or 取出的数量 > 9999999:
        取出的数量 = 1
    if 类型 < 0 or 类型 > 9999999:
        类型 = 0
    字母 = 'abcdefghijklnmopqrstuvwxyz'
    文本 = ''
    if 类型 == 0:
        for x in range(取出的数量):
            文本 = 文本 + 变量_取出随机元素(字母)
    elif 类型 == 1:
        for x in range(取出的数量):
            文本 = 文本 + 变量_取出随机元素(字母).upper()
    else:
        for x in range(取出的数量):
            随机数 = 文本_取随机范围数字(1, 2)
            if 随机数 == "1":
                文本 = 文本 + 变量_取出随机元素(字母)
            else:
                文本 = 文本 + 变量_取出随机元素(字母).upper()
    return 文本


def 文本_取随机数字(取出的数量=1, 是否排除0开头=False):
    '失败返回空文本'
    if isinstance(取出的数量, int) != True or isinstance(是否排除0开头, bool) != True:
        print('文本_取随机数字：传入参数有误')
        return ''
    if 取出的数量 < 1 or 取出的数量 > 9999999:
        取出的数量 = 1
    文本 = ''
    if 是否排除0开头 == False:
        for x in range(取出的数量):
            文本 = 文本 + 文本_取随机范围数字(0, 9)
    else:
        文本 = 文本 + 文本_取随机范围数字(1, 9)
        for x in range(取出的数量 - 1):
            文本 = 文本 + 文本_取随机范围数字(0, 9)
    return 文本


def 文本_取随机字符(取出的数量=1):
    '失败返回空文本,包括0-9 a-z A-Z'
    if isinstance(取出的数量, int) != True:
        print('文本_取随机字符：传入参数有误')
        return ''
    if 取出的数量 < 1 or 取出的数量 > 9999999:
        取出的数量 = 1
    字符 = '0123456789abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ'
    文本 = ''
    for x in range(取出的数量):
        文本 = 文本 + 变量_取出随机元素(字符)
    return 文本


def 文本_取随机姓氏(取常见姓氏=False):
    '失败返回空文本,常见姓氏为自己设置挑选的,仅做参考'
    if isinstance(取常见姓氏, bool) != True:
        print('文本_取随机姓氏：传入参数有误')
        return ''
    百家姓 = """赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺
    倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫柯房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊于惠甄曲家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭历戎祖武符刘景詹束龙叶幸司韶郜黎蓟溥印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阳郁胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍却璩桑桂濮牛寿通边扈燕冀浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄
    阙东欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相查后荆红游竺权逮盍益桓公"""
    常见百家姓 = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛范彭郎鲁韦昌马苗凤花方俞任袁柳史唐费薛雷贺罗毕于齐萧尹姚顾孟平黄宋庞项祝董梁杜阮刘万丁石洪白田夏'
    if 取常见姓氏 == False:
        取出的姓氏 = ''
        while 取出的姓氏 == '' or 取出的姓氏 == '\n':
            取出的姓氏 = 变量_取出随机元素(百家姓)
        return 取出的姓氏
    else:
        return 变量_取出随机元素(常见百家姓)


def 文本_取随机汉字(取出的数量=1):
    '失败返回空文本,只有部分常见字'
    if isinstance(取出的数量, int) != True:
        print('文本_取随机汉字：传入参数有误')
        return ''
    if 取出的数量 < 1 or 取出的数量 > 9999999:
        取出的数量 = 1
    ming = [
        '的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地', '为',
        '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自', '以',
        '会', '家', '可', '下', '而', '过', '天', '去', '能', '对', '小', '多', '然', '于', '心', '学', '么', '之', '都', '好',
        '看', '起', '发', '当', '没', '成', '只', '如', '事', '把', '还', '用', '第', '样', '道', '想', '作', '种', '开', '美',
        '总', '从', '无', '情', '己', '面', '最', '女', '但', '现', '前', '些', '所', '同', '日', '手', '又', '行', '意', '动',
        '方', '期', '它', '头', '经', '长', '儿', '回', '位', '分', '爱', '老', '因', '很', '给', '名', '法', '间', '斯', '知',
        '世', '什', '两', '次', '使', '身', '者', '被', '高', '已', '亲', '其', '进', '此', '话', '常', '与', '活', '正', '感',
        '见', '明', '问', '力', '理', '尔', '点', '文', '几', '定', '本', '公', '特', '做', '外', '孩', '相', '西', '果', '走',
        '将', '月', '十', '实', '向', '声', '车', '全', '信', '重', '三', '机', '工', '物', '气', '每', '并', '别', '真', '打',
        '太', '新', '比', '才', '便', '夫', '再', '书', '部', '水', '像', '眼', '等', '体', '却', '加', '电', '主', '界', '门',
        '利', '海', '受', '听', '表', '德', '少', '克', '代', '员', '许', '稜', '先', '口', '由', '死', '安', '写', '性', '马',
        '光', '白', '或', '住', '难', '望', '教', '命', '花', '结', '乐', '色', '更', '拉', '东', '神', '记', '处', '让', '母',
        '父', '应', '直', '字', '场', '平', '报', '友', '关', '放', '至', '张', '认', '接', '告', '入', '笑', '内', '英', '军',
        '候', '民', '岁', '往', '何', '度', '山', '觉', '路', '带', '万', '男', '边', '风', '解', '叫', '任', '金', '快', '原',
        '吃', '妈', '变', '通', '师', '立', '象', '数', '四', '失', '满', '战', '远', '格', '士', '音', '轻', '目', '条', '呢',
        '病', '始', '达', '深', '完', '今', '提', '求', '清', '王', '化', '空', '业', '思', '切', '怎', '非', '找', '片', '罗',
        '钱', '紶', '吗', '语', '元', '喜', '曾', '离', '飞', '科', '言', '干', '流', '欢', '约', '各', '即', '指', '合', '反',
        '题', '必', '该', '论', '交', '终', '林', '请', '医', '晚', '制', '球', '决', '窢', '传', '画', '保', '读', '运', '及',
        '则', '房', '早', '院', '量', '苦', '火', '布', '品', '近', '坐', '产', '答', '星', '精', '视', '五', '连', '司', '巴',
        '奇', '管', '类', '未', '朋', '且', '婚', '台', '夜', '青', '北', '队', '久', '乎', '越', '观', '落', '尽', '形', '影',
        '红', '爸', '百', '令', '周', '吧', '识', '步', '希', '亚', '术', '留', '市', '半', '热', '送', '兴', '造', '谈', '容',
        '极', '随', '演', '收', '首', '根', '讲', '整', '式', '取', '照', '办', '强', '石', '古', '华', '諣', '拿', '计', '您',
        '装', '似', '足', '双', '妻', '尼', '转', '诉', '米', '称', '丽', '客', '南', '领', '节', '衣', '站', '黑', '刻', '统',
        '断', '福', '城', '故', '历', '惊', '脸', '选', '包', '紧', '争', '另', '建', '维', '绝', '树', '系', '伤', '示', '愿',
        '持', '千', '史', '谁', '准', '联', '妇', '纪', '基', '买', '志', '静', '阿', '诗', '独', '复', '痛', '消', '社', '算',
        '义', '竟', '确', '酒', '需', '单', '治', '卡', '幸', '兰', '念', '举', '仅', '钟', '怕', '共', '毛', '句', '息', '功',
        '官', '待', '究', '跟', '穿', '室', '易', '游', '程', '号', '居', '考', '突', '皮', '哪', '费', '倒', '价', '图', '具',
        '刚', '脑', '永', '歌', '响', '商', '礼', '细', '专', '黄', '块', '脚', '味', '灵', '改', '据', '般', '破', '引', '食',
        '仍', '存', '众', '注', '笔', '甚', '某', '沉', '血', '备', '习', '校', '默', '务', '土', '微', '娘', '须', '试', '怀',
        '料', '调', '广', '蜖', '苏', '显', '赛', '查', '密', '议', '底', '列', '富', '梦', '错', '座', '参', '八', '除', '跑',
        '亮', '假', '印', '设', '线', '温', '虽', '掉', '京', '初', '养', '香', '停', '际', '致', '阳', '纸', '李', '纳', '验',
        '助', '激', '够', '严', '证', '帝', '饭', '忘', '趣', '支', '春', '集', '丈', '木', '研', '班', '普', '导', '顿', '睡',
        '展', '跳', '获', '艺', '六', '波', '察', '群', '皇', '段', '急', '庭', '创', '区', '奥', '器', '谢', '弟', '店', '否',
        '害', '草', '排', '背', '止', '组', '州', '朝', '封', '睛', '板', '角', '况', '曲', '馆', '育', '忙', '质', '河', '续',
        '哥', '呼', '若', '推', '境', '遇', '雨', '标', '姐', '充', '围', '案', '伦', '护', '冷', '警', '贝', '著', '雪', '索',
        '剧', '啊', '船', '险', '烟', '依', '斗', '值', '帮', '汉', '慢', '佛', '肯', '闻', '唱', '沙', '局', '伯', '族', '低',
        '玩', '资', '屋', '击', '速', '顾', '泪', '洲', '团', '圣', '旁', '堂', '兵', '七', '露', '园', '牛', '哭', '旅', '街',
        '劳', '型', '烈', '姑', '陈', '莫', '鱼', '异', '抱', '宝', '权', '鲁', '简', '态', '级', '票', '怪', '寻', '杀', '律',
        '胜', '份', '汽', '右', '洋', '范', '床', '舞', '秘', '午', '登', '楼', '贵', '吸', '责', '例', '追', '较', '职', '属',
        '渐', '左', '录', '丝', '牙', '党', '继', '托', '赶', '章', '智', '冲', '叶', '胡', '吉', '卖', '坚', '喝', '肉', '遗',
        '救', '修', '松', '临', '藏', '担', '戏', '善', '卫', '药', '悲', '敢', '靠', '伊', '村', '戴', '词', '森', '耳', '差',
        '短', '祖', '云', '规', '窗', '散', '迷', '油', '旧', '适', '乡', '架', '恩', '投', '弹', '铁', '博', '雷', '府', '压',
        '超', '负', '勒', '杂', '醒', '洗', '采', '毫', '嘴', '毕', '九', '冰', '既', '状', '乱', '景', '席', '珍', '童', '顶',
        '派', '素', '脱', '农', '疑', '练', '野', '按', '犯', '拍', '征', '坏', '骨', '余', '承', '置', '臓', '彩', '灯', '巨',
        '琴', '免', '环', '姆', '暗', '换', '技', '翻', '束', '增', '忍', '餐', '洛', '塞', '缺', '忆', '判', '欧', '层', '付',
        '阵', '玛', '批', '岛', '项', '狗', '休', '懂', '武', '革', '良', '恶', '恋', '委', '拥', '娜', '妙', '探', '呀', '营',
        '退', '摇', '弄', '桌', '熟', '诺', '宣', '银', '势', '奖', '宫', '忽', '套', '康', '供', '优', '课', '鸟', '喊', '降',
        '夏', '困', '刘', '罪', '亡', '鞋', '健', '模', '败', '伴', '守', '挥', '鲜', '财', '孤', '枪', '禁', '恐', '伙', '杰',
        '迹', '妹', '藸', '遍', '盖', '副', '坦', '牌', '江', '顺', '秋', '萨', '菜', '划', '授', '归', '浪', '听', '凡', '预',
        '奶', '雄', '升', '碃', '编', '典', '袋', '莱', '含', '盛', '济', '蒙', '棋', '端', '腿', '招', '释', '介', '烧', '误',
        '乾', '坤']
    文本 = ''
    for x in range(取出的数量):
        文本 = 文本 + 变量_取出随机元素(ming)
    return 文本


def 文本_取随机范围数字(最小值, 最大值, 是否返回整数=False):
    '出错返回0,如果设置返回整数则返回int类型'
    if isinstance(最小值, (int, str)) != True or isinstance(最大值, (int, str)) != True:
        print('文本_取随机范围数字：传入参数有误')
        return 0
    elif int(最小值) > int(最大值):
        return 0
    try:
        if 是否返回整数 == False:
            return str(random.randint(int(最小值), int(最大值)))
        else:
            return random.randint(int(最小值), int(最大值))
    except Exception as error:
        print('文本_取随机范围数字：运行出错|' + str(error))
        return 0


def 文本_到时间_datetime(时间文本, 时间格式='%Y-%m-%d %H:%M:%S'):
    '失败返回空文本,把文本格式的时间转成datetime的时间格式，文本跟时间格式要匹配'
    if isinstance(时间文本, str) != True or isinstance(时间格式, str) != True:
        print('文本_到时间_datetime：传入参数有误')
        return ''
    try:
        return datetime.datetime.strptime(时间文本, 时间格式)
    except Exception as error:
        print('文本_到时间_datetime：运行出错|' + str(error))
        return ''


def 文本_取中间_批量(原文本, 前面的文本, 后面的文本):
    搜索位置 = 0
    列表 = []
    if isinstance(原文本, str) != True or isinstance(前面的文本, str) != True or isinstance(后面的文本, str) != True:
        print('文本_取中间_批量：传入的参数有误')
        return []
    while 1 == 1:
        搜索位置 = 原文本.find(前面的文本, 搜索位置)
        if 搜索位置 != -1:
            后面的位置 = 原文本.find(后面的文本, 搜索位置 + len(前面的文本))
            if 后面的位置 != -1:
                搜索位置 = 搜索位置 + len(前面的文本)
                取出的文本 = 原文本[搜索位置:后面的位置]
                if len(取出的文本) > 0:
                    列表.append(取出的文本)
            else:
                break
        else:
            break
    return 列表


def 文本_拼音转换(原文本, 连接符='', 拼音风格=0, 遍历多音=False, 无拼音处理=0, 严格规范=False):
    '默认返回全拼,失败返回空,拼音风格:0是不带声调的全拼,1是带声调的全拼,2是取声母部分,3是取首字母,无拼音处理：0是保留原始字符,1是忽略该字符,2是 替换为去掉 \\u 的 unicode 编码字符串'
    if isinstance(原文本, str) != True or isinstance(连接符, str) != True or isinstance(拼音风格, int) != True or isinstance(遍历多音,
                                                                                                                   bool) != True or isinstance(
            无拼音处理, int) != True or isinstance(严格规范, bool) != True:
        print('文本_拼音转换：传入的参数有误')
        return ''
    if 拼音风格 > 3 or 拼音风格 < 0:
        拼音风格 = 0

    if 无拼音处理 > 2 or 无拼音处理 < 0:
        无拼音处理 = 0

    if 拼音风格 == 0:
        rStyle = Style.NORMAL
    elif 拼音风格 == 1:
        rStyle = Style.TONE
    elif 拼音风格 == 2:
        rStyle = Style.INITIALS
    elif 拼音风格 == 3:
        rStyle = Style.FIRST_LETTER

    if 无拼音处理 == 0:
        Errors = 'default'
    elif 无拼音处理 == 1:
        Errors = 'ignore'
    elif 无拼音处理 == 2:
        Errors = 'replace'
    try:
        拼音 = ''
        拼音列表 = pinyin(hans=原文本, style=rStyle, heteronym=遍历多音, errors=Errors, strict=严格规范)
        for x in 拼音列表:
            for i in x:
                拼音 = 拼音 + 连接符 + i
        return 拼音[1:]
    except Exception as error:
        print('文本_拼音转换：运行出错|' + str(error))
        return ''


def 数值_求次方(数值, 次方数):
    '出错返回-1'
    if isinstance(数值, (int, float)) != True or isinstance(次方数, (int, float)) != True:
        print('数值_求次方：传入参数有误')
        return -1
    try:
        return pow(数值, 次方数)
    except Exception as error:
        print('数值_求次方：运行出错|' + str(error))
        return -1


def 数值_四舍五入(数值, 保留位数=0):
    '出错返回-1'
    if isinstance(数值, (int, float)) != True or isinstance(保留位数, (int)) != True:
        print('数值_四舍五入：传入参数有误')
        return -1
    try:
        return round(数值, 保留位数)
    except Exception as error:
        print('数值_四舍五入：运行出错|' + str(error))
        return -1


def 数值_取绝对值(待处理的数值):
    "'出错返回-1',传入一个数值,正负数还是小数都返回正的数值"
    if isinstance(待处理的数值, (int, float)) != True:
        print('数值_取绝对值：传入参数有误')
        return -1
    return abs(待处理的数值)


def 数值_取上入整数(待处理的数值):
    "'出错返回-1',示例:1.1返回2"
    if isinstance(待处理的数值, (int, float)) != True:
        print('数值_取绝对值：传入参数有误')
        return -1
    return math.ceil(待处理的数值)


def 数值_取下入整数(待处理的数值):
    "'出错返回-1',示例:1.9返回1"
    if isinstance(待处理的数值, (int, float)) != True:
        print('数值_取绝对值：传入参数有误')
        return -1
    return math.floor(待处理的数值)


def 数值_取最大数(待处理的数值):
    "'出错返回-1',传入要对比的列表,如(1,2,3),返回里面最大的数字"
    try:
        return max(待处理的数值)
    except Exception as error:
        print('数值_取最大数：运行出错|' + str(error))
        return -1


def 数值_取最小数(待处理的数值):
    "'出错返回-1',传入要对比的列表,如(1,2,3),返回里面最小的数字"
    try:
        return min(待处理的数值)
    except Exception as error:
        print('数值_取最小数：运行出错|' + str(error))
        return -1


def 字典_取值并删除(字典, 键, 失败返回值=None):
    '失败返回空文本 如果查找键不存在则返回设置的失败返回值,该值可空'
    if isinstance(字典, dict) != True:
        print('字典_取值并删除：传入字典有误')
    try:
        if 失败返回值 == None:
            return 字典.pop(键)
        else:
            return 字典.pop(键, 失败返回值)
    except Exception as error:
        print('字典_取值并删除：运行出错|' + str(error))
        return ''


def 字典_取指定键值(字典, 键, 失败返回值=None):
    '失败返回空文本 如果查找键不存在则返回设置的失败返回值'
    if isinstance(字典, dict) != True:
        print('字典_取指定键值：传入字典有误')
    try:
        if 失败返回值 == None:
            return 字典.get(键)
        else:
            return 字典.get(键, 失败返回值)
    except Exception as error:
        print('字典_取指定键值：运行出错|' + str(error))
        return ''


def 字典_清空(字典):
    '清空字典内的全部元素,成功返回True 失败返回False'
    if isinstance(字典, dict) != True:
        print('字典_清空：传入字典有误')
    try:
        字典.clear()
        return True
    except Exception as error:
        print('字典_清空：运行出错|' + str(error))
        return False


def 字典_拷贝(新字典, 原字典):
    '成功返回True 失败返回False,直接赋值拷贝值会跟着原字典改变,用copy不会'
    if isinstance(新字典, dict) != True or isinstance(原字典, dict) != True:
        print('字典_拷贝：传入字典有误')
    try:
        新字典 = 原字典.copy()
        return True
    except Exception as error:
        print('字典_拷贝：运行出错|' + str(error))
        return False


def 字典_生成(键值列表, 键值):
    '失败返回空字典,传入键值列表创建字典,字典内的值都为设置的键值'
    if isinstance(键值列表, list) != True:
        print('字典_生成：传入字典有误')
    try:
        return dict.fromkeys(键值列表, 键值)
    except Exception as error:
        print('字典_生成：运行出错|' + str(error))
        return {}


def 字典_转列表(字典):
    '失败返回空列表,返回列表格式[(1,2),(2,3),(3,4)]'
    if isinstance(字典, dict) != True:
        print('字典_转列表：传入字典有误')
    try:
        return list(字典.items())
    except Exception as error:
        print('字典_转列表：运行出错|' + str(error))
        return []


def 字典_取全部键(字典):
    '失败返回空列表'
    if isinstance(字典, dict) != True:
        print('字典_取全部键：传入字典有误')
    try:
        return list(字典.keys())
    except Exception as error:
        print('字典_取全部键：运行出错|' + str(error))
        return []


def 字典_取全部值(字典):
    '失败返回空列表'
    if isinstance(字典, dict) != True:
        print('字典_取全部值：传入字典有误')
    try:
        return list(字典.values())
    except Exception as error:
        print('字典_取全部值：运行出错|' + str(error))
        return []


def 字典_取出并删除最后键值(字典):
    '失败返回空元组,删除字典中最后一个键跟值并以元组格式返回删除的键跟值'
    if isinstance(字典, dict) != True:
        print('字典_取出并删除最后键值：传入字典有误')
    try:
        return 字典.popitem()
    except Exception as error:
        print('字典_取出并删除最后键值：运行出错|' + str(error))
        return ()


def 字典_取值添加(字典, 键, 失败返回值=None):
    '失败返回空文本 如果查找键不存在则返回设置的失败返回值且为字典新建该键值'
    if isinstance(字典, dict) != True:
        print('字典_取值添加：传入字典有误')
    try:
        if 失败返回值 == None:
            return 字典.setdefault(键)
        else:
            return 字典.setdefault(键, 失败返回值)
    except Exception as error:
        print('字典_取值添加：运行出错|' + str(error))
        return ''


def 列表_转字典(列表1, 列表2):
    '传入两个列表转换成字典'
    if isinstance(列表1, list) != True or isinstance(列表2, list) != True:
        print('列表_转字典：传入列表有误')
    try:
        return dict(zip(列表1, 列表2))
    except Exception as error:
        print('列表_转字典：运行出错|' + str(error))
        return {}


def 列表_加入成员(列表, 要加入的值):
    '成功返回True 失败返回False'
    if isinstance(列表, list) != True:
        print('列表_加入成员：传入列表有误')
        return False
    try:
        列表.append(要加入的值)
        return True
    except Exception as error:
        print('列表_加入成员：运行出错|' + str(error))
        return False


def 列表_插入成员(列表, 位置, 要加入的值):
    '成功返回True 失败返回False,在指定位置插入指定值'
    if isinstance(列表, list) != True or isinstance(位置, int) != True:
        print('列表_插入成员：传入列表有误')
        return False
    try:
        列表.insert(位置, 要加入的值)
        return True
    except Exception as error:
        print('列表_插入成员：运行出错|' + str(error))
        return False


def 列表_取出现次数(列表, 要查询的数值):
    '失败未找到返回0,搜索时 True 会当成1   False 是0'
    if isinstance(列表, list) != True:
        print('列表_取出现次数：传入列表有误')
        return 0
    try:
        return 列表.count(要查询的数值)
    except Exception as error:
        print('列表_取出现次数：运行出错|' + str(error))
        return 0


def 列表_加入新列表(列表, 新的列表):
    '成功返回True 失败返回False,在列表后面追加新的列表或元组成员进去'
    if isinstance(列表, list) != True or isinstance(新的列表, (list, tuple)) != True:
        print('列表_加入新列表：传入列表有误')
        return False
    列表.extend(新的列表)
    return True


def 列表_查找成员位置(列表, 要查找的值):
    '失败返回-1'
    if isinstance(列表, list) != True:
        return -1
    try:
        if 要查找的值 in 列表 == True:
            return 列表.index(要查找的值)
        else:
            return -1
    except Exception as error:
        print('列表_查找成员位置：运行出错|' + str(error))
        return -1


def 列表_取值并删除(列表, 位置=None):
    '失败返回空文本,取出列表的一个成员值 并删除该成员,默认最后一个,位置为0则为第一个'
    if isinstance(列表, list) != True:
        print('列表_取值并删除：传入参数有误')
        return ''
    try:
        if 位置 == None:
            return 列表.pop()
        elif isinstance(位置, int) == True:
            return 列表.pop(位置)
        else:
            print('列表_取值并删除：传入参数有误')
            return ''
    except Exception as error:
        print('列表_取值并删除：运行出错|' + str(error))
        return ''


def 列表_删除指定值(列表, 要删除的值):
    '成功返回True 失败返回False,删除列表中找到的第一个值'
    if isinstance(列表, list) != True:
        print('列表_删除指定值：传入列表有误')
        return ''
    try:
        列表.remove(要删除的值)
        return True
    except Exception as error:
        print('列表_删除指定值：运行出错|' + str(error))
        return ''


def 列表_倒序排列(列表):
    '成功返回True 失败返回False,把列表的成员顺序到过来排序'
    if isinstance(列表, list) != True:
        print('列表_倒序排列：传入列表有误')
        return False
    列表.reverse()
    return True


def 列表_大小排序(列表, 排序方式=False):
    '成功返回True 失败返回False,排序的列表只能全为整数型的,排序方式True为从大到小,默认False从小到大'
    if isinstance(列表, list) != True or isinstance(排序方式, bool) != True:
        print('列表_大小排序：传入列表有误')
        return False
    列表.sort(reverse=排序方式)
    return True


def 时间_取指定格式时间(原时间='', 格式=time_时间格式_取时分秒):
    '失败返回空文本'
    if isinstance(原时间, str) != True or isinstance(格式, str) != True:
        print('时间_取指定格式时间：传入参数有误')
        return ''
    elif 原时间 == '':
        原时间 = time.time()
    try:
        lt = time.localtime(原时间)
        return time.strftime(格式, lt)
    except Exception as error:
        print('时间_取指定格式时间：运行出错|' + str(error))
        return ''


def 时间_亚马逊操作时间():
    '返回文本型亚马逊API需要的操作时间,2019-10-15T02:07:57Z'
    return datetime.datetime.utcnow().strftime("%Y" + "-" + "%m" + "-" + "%dT%H" + ":" + "%M" + ":" + "%S") + "Z"


def 时间_取启动时间():
    '返回浮点数时间，可以拿去计算启动时间'
    return time.clock()


def 时间_取现行时间time(时间格式="%Y-%m-%d %H:%M:%S"):
    '失败返回空文本,返回字符串格式的时间'
    if isinstance(时间格式, str) != True:
        print('时间_取现行时间time：传入列表有误')
        return ''
    try:
        return time.strftime(时间格式)
    except Exception as error:
        print('时间_取现行时间time：运行出错|' + str(error))
        return ''


def 时间_取日期(增减天数=0):
    '失败返回空文本,默认返回当天日期,-1表示取昨天'
    if isinstance(增减天数, int) != True:
        print('时间_取日期：传入列表有误')
        return ''
    if (增减天数 < 0):
        增减天数 = abs(增减天数)
        return str(datetime.date.today() - datetime.timedelta(days=增减天数))
    else:
        return str(datetime.date.today() + datetime.timedelta(days=增减天数))


def 时间_取某年某月日历(年份, 月份):
    '失败返回空文本,返回字符串格式的日历'
    if isinstance(年份, int) != True or isinstance(月份, int) != True:
        print('时间_取某年某月日历：传入列表有误')
        return ''
    try:
        return calendar.month(年份, 月份)
    except Exception as error:
        print('时间_取某年某月日历：运行出错|' + str(error))
        return ''


def 时间_取某年日历(年份):
    '失败返回空文本,返回字符串格式的日历'
    if isinstance(年份, int) != True:
        print('时间_取某年日历：传入列表有误')
        return ''
    try:
        return calendar.calendar(年份)
    except Exception as error:
        print('时间_取某年日历：运行出错|' + str(error))
        return ''


def 时间_是否为闰年(年份):
    '返回True跟False返回指定的年份是否为闰年，若是返回True，否则返回False'
    if isinstance(年份, int) != True:
        print('时间_是否为闰年：传入列表有误')
        return False
    try:
        return calendar.isleap(年份)
    except Exception as error:
        print('时间_是否为闰年：运行出错|' + str(error))
        return False


def 时间_指定范围闰年总数(开始年份, 结束年份):
    '失败返回0,返回[开始年份,结束年份)之间闰年的总和'
    if isinstance(开始年份, int) != True or isinstance(结束年份, int) != True:
        print('时间_指定范围闰年总数：传入列表有误')
        return 0
    try:
        return calendar.leapdays(开始年份, 结束年份)
    except Exception as error:
        print('时间_指定范围闰年总数：运行出错|' + str(error))
        return 0


def 时间_取某月天数(年份, 月份):
    '失败返回0'
    if isinstance(年份, int) != True or isinstance(月份, int) != True:
        print('时间_取某月天数：传入列表有误')
        return 0
    try:
        return calendar.monthrange(年份, 月份)[1]
    except Exception as error:
        print('时间_取某月天数：运行出错|' + str(error))
        return 0


def 时间_取某月一号星期几(年份, 月份):
    '失败返回-1,返回0-6 0是周1'
    if isinstance(年份, int) != True or isinstance(月份, int) != True:
        print('时间_取某月一号星期几：传入列表有误')
        return -1
    try:
        return calendar.monthrange(年份, 月份)[0]
    except Exception as error:
        print('时间_取某月一号星期几：运行出错|' + str(error))
        return -1


def 时间_取某天星期几(年份, 月份, 日期):
    '失败返回-1,返回0-6 0是周1'
    if isinstance(年份, int) != True or isinstance(月份, int) != True or isinstance(日期, int) != True:
        print('时间_取某天星期几：传入列表有误')
        return -1
    try:
        return calendar.weekday(年份, 月份, 日期)
    except Exception as error:
        print('时间_取某天星期几：运行出错|' + str(error))
        return -1


def 时间_取现行时间datetime():
    '返回datetime格式的时间'
    return datetime.datetime.now()


def 时间_取随机时间戳():
    "返回字符串类型的随机时间戳,0-1中间的数"
    return str(random.random())


def 时间_格式化(原时间, 时间格式="%Y-%m-%d %H:%M:%S"):
    '失败返回False,传入datetime时间，返回字符串类型时间'
    if isinstance(原时间, (str, datetime.datetime)) != True or isinstance(时间格式, str) != True:
        print('时间_格式化：传入参数有误')
        return False
    try:
        if isinstance(原时间, str) == True:
            return datetime.datetime.strftime(datetime.datetime.strptime(原时间, "%Y-%m-%d %H:%M:%S"), 时间格式)
        else:
            return datetime.datetime.strftime(原时间, 时间格式)
    except Exception as error:
        print('时间_格式化：运行出错|' + str(error))
        return False


def 时间_文本转datetime时间(原时间, 时间格式="%Y-%m-%d %H:%M:%S"):
    '失败返回False,返回字符串时间,时间格式要跟原时间格式匹配'
    if isinstance(原时间, str) != True or isinstance(时间格式, str) != True:
        print('时间_文本转datetime时间：传入参数有误')
        return False
    try:
        return datetime.datetime.strptime(原时间, 时间格式)
    except Exception as error:
        print('时间_文本转datetime时间：运行出错|' + str(error))
        return False


def 时间_datetime时间转文本(原时间, 时间格式="%Y-%m-%d %H:%M:%S"):
    '失败返回False'
    if isinstance(原时间, datetime.datetime) != True or isinstance(时间格式, str) != True:
        print('时间_datetime时间转文本：传入参数有误')
        return False
    try:
        return 原时间.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as error:
        print('时间_datetime时间转文本：运行出错|' + str(error))
        return False


def 时间_增减datetime(原时间, 增减部分, 增减数值, 操作类型=True):
    "失败返回False,返回datetime类型的时间,增减部分：1是星期,2是天,3是时,4是分,5是秒,6是毫秒,加时间就传正数,减时间传负数,操作类型：增加时间为True减少为False"
    if isinstance(原时间, datetime.datetime) != True or isinstance(增减部分, int) != True or isinstance(增减数值,
                                                                                                 int) != True or isinstance(
        操作类型, bool) != True:
        print('时间_增减datetime：传入参数有误')
        return False
    try:
        if 增减部分 == 1:
            时间差 = datetime.timedelta(weeks=增减数值)
        elif 增减部分 == 2:
            时间差 = datetime.timedelta(days=增减数值)
        elif 增减部分 == 3:
            时间差 = datetime.timedelta(hours=增减数值)
        elif 增减部分 == 4:
            时间差 = datetime.timedelta(minutes=增减数值)
        elif 增减部分 == 5:
            时间差 = datetime.timedelta(seconds=增减数值)
        elif 增减部分 == 6:
            时间差 = datetime.timedelta(milliseconds=增减数值)

        if 操作类型 == True:
            return 原时间 + 时间差
        else:
            return 原时间 - 时间差
    except Exception as error:
        print('时间_增减datetime：运行出错|' + str(error))
        return False


def 时间_取上月最后一天(年份=None, 月份=None):
    "失败返回False,返回datetime格式时间,年月格式为整数型如：年 2019 月 4,默认返回上个月的"
    if 年份 != None and 月份 != None:
        if isinstance(年份, (str, int)) != True or isinstance(月份, (str, int)) != True:
            print('时间_取上月最后一天：传入参数有误')
            return False
        try:
            return datetime.date(int(年份), int(月份), 1) - datetime.timedelta(1)
        except Exception as error:
            print('时间_取上月最后一天：运行出错|' + str(error))
            return False
    else:
        return datetime.date(datetime.date.today().year, datetime.date.today().month, 1) - datetime.timedelta(1)


def 时间_取时间间隔(原时间, 对比时间):
    "失败返回0,传入字符串类型的时间,可以用时间_取现行时间time获取,返回秒数,整数型"
    if isinstance(原时间, str) != True or isinstance(对比时间, str) != True:
        print('时间_取时间间隔：传入参数有误')
        return 0
    try:
        return int(time.mktime(time.strptime(对比时间, "%Y-%m-%d %H:%M:%S"))) - int(
            time.mktime(time.strptime(原时间, "%Y-%m-%d %H:%M:%S")))
    except Exception as error:
        print('时间_取时间间隔：运行出错|' + str(error))
        return 0


def 时间_时间转时间戳(原时间, 时间格式="%Y-%m-%d %H:%M:%S"):
    "失败返回空文本,传入字符串类型时间 时间_取现行时间time 命令获取 返回十位字符串类型时间戳"
    if isinstance(原时间, str) != True or isinstance(时间格式, str) != True:
        print('时间_时间到时间戳：传入参数有误')
        return ''
    try:
        return str(int(time.mktime(time.strptime(原时间, 时间格式))))
    except Exception as error:
        print('时间_时间到时间戳：运行出错|' + str(error))
        return ''


def 时间_时间戳转时间(时间戳, 格式='%Y:%m:%d %H:%M:%S'):
    '失败返回空文本,时间戳转换成时间文本，支持10位13位时间戳'
    if isinstance(时间戳, (str, int)) != True or isinstance(格式, str) != True:
        print('时间_时间戳转时间：传入的参数有误')
        return ''
    try:
        if len(str(时间戳)) == 13 and str(时间戳).isdigit() == True:
            return time.strftime(格式, time.localtime(int(int(时间戳) / 1000)))
        elif len(str(时间戳)) == 10 and str(时间戳).isdigit() == True:
            return time.strftime(格式, time.localtime(int(时间戳)))
        else:
            print("时间_时间戳转时间：传入的时间戳有误")
            return ''
    except Exception as error:
        print('时间_时间戳转时间：运行出错|' + str(error))
        return ''


def 时间_取现行时间戳(是否取十位=False):
    "返回字符串类型时间戳,默认取十三位时间戳"
    if 是否取十位 == True:
        return str(round(time.time()))
    else:
        return str(round(time.time() * 1000))


def 队列_创建队列(队列大小=0, Lifo=False):
    '如果maxsize小于1就表示队列长度无限,Lifo为真则队列是后进先出'
    if isinstance(队列大小, int) != True or isinstance(Lifo, bool) != True:
        return '队列_创建队列：传入参数有误'
    elif Lifo == False:
        return queue.Queue(maxsize=队列大小)
    else:
        return queue.LifoQueue(maxsize=队列大小)


def 队列_加入成员(队列, 要加入的值):
    '成功返回True,失败返回False'
    if isinstance(队列, (queue.Queue, queue.LifoQueue)) != True:
        print('队列_加入成员：传入参数有误')
        return False
    try:
        队列.put(要加入的值)
        return True
    except Exception as error:
        print('队列_加入成员：运行出错|' + str(error))
        return False


def 队列_取出成员(队列):
    "失败返回空文本,取出队列最前面或最后的一个值"
    if isinstance(队列, (queue.Queue, queue.LifoQueue)) != True:
        print('队列_加入成员：传入参数有误')
        return ''
    if 队列.qsize() <= 0:
        return ""
    else:
        return 队列.get()


def 队列_取队列成员数(队列):
    '失败返回0'
    if isinstance(队列, (queue.Queue, queue.LifoQueue)) != True:
        print('队列_取队列成员数：传入参数有误')
        return 0
    return 队列.qsize()


def 队列_清空队列(队列):
    '返回True,False'
    if isinstance(队列, (queue.Queue, queue.LifoQueue)) != True:
        print('队列_清空队列：传入参数有误')
        return False
    队列.queue.clear()
    return True


def 队列_是否为空(队列):
    '返回True,False'
    if isinstance(队列, (queue.Queue, queue.LifoQueue)) != True:
        print('队列_是否为空：传入参数有误')
        return False
    return 队列.empty()


def 队列_是否已满(队列):
    '返回True,False'
    if isinstance(队列, (queue.Queue, queue.LifoQueue)) != True:
        print('队列_是否已满：传入参数有误')
        return False
    return 队列.full()


def 正则_匹配(原文本, 匹配规则):
    '失败返回空列表,匹配成功返回匹配到的列表'
    if isinstance(原文本, str) != True or isinstance(匹配规则, str) != True:
        print('正则_匹配：传入的参数有误')
        return []
    try:
        return re.findall(匹配规则, 原文本)
    except Exception as error:
        print('正则_匹配：运行出错|' + str(error))
        return []


def 编码_编码(欲编码的内容, 编码格式='UTF-8', 错误处理='strict'):
    '失败返回空文本'
    if isinstance(欲编码的内容, str) != True or isinstance(错误处理, str) != True:
        print('编码_编码：传入的参数有误')
        return ''
    try:
        return 欲编码的内容.encode(encoding=编码格式, errors=错误处理)
    except Exception as error:
        print('编码_编码：运行出错|' + str(error))
        return ''


def 编码_解码(欲解码的内容, 解码格式='UTF-8', 错误处理='strict'):
    '失败返回空文本'
    if isinstance(欲解码的内容, str) != True or isinstance(错误处理, str) != True:
        print('编码_解码：传入的参数有误')
        return ''
    try:
        return 欲解码的内容.decode(encoding=解码格式, errors=错误处理)
    except Exception as error:
        print('编码_解码：运行出错|' + str(error))
        return ''


def 编码_UTF8编码(欲编码的内容):
    '失败返回空文本'
    if isinstance(欲遍码的内容, str) != True:
        print('编码_UTF8编码：传入的参数有误')
        return ''
    return 欲编码的内容.encode(encoding='UTF-8', errors='strict')


def 编码_UTF8解码(欲解码的内容):
    '失败返回空文本'
    if isinstance(欲解码的内容, str) != True:
        print('编码_UTF8解码：传入的参数有误')
        return ''
    return 欲解码的内容.decode(encoding='UTF-8', errors='strict')


def 编码_GBK编码(欲编码的内容):
    '失败返回空文本'
    if isinstance(欲编码的内容, str) != True:
        print('编码_GBK编码：传入的参数有误')
        return ''
    return 欲编码的内容.encode(encoding='GBK', errors='strict')


def 编码_GBK解码(欲解码的内容):
    '失败返回空文本'
    if isinstance(欲解码的内容, str) != True:
        print('编码_GBK解码：传入的参数有误')
        return ''
    return 欲解码的内容.decode(encoding='GBK', errors='strict')


def 编码_URL编码(欲编码的内容):
    '失败返回空文本'
    if isinstance(欲编码的内容, str) != True:
        print('编码_URL编码：传入的参数有误')
        return ''
    return parse.quote(欲编码的内容)


def 编码_URL解码(欲解码的内容):
    '失败返回空文本'
    if isinstance(欲解码的内容, str) != True:
        print('编码_URL解码：传入的参数有误')
        return ''
    return parse.unquote(欲解码的内容)


def 编码_ANSI到USC2(欲编码的内容):
    '失败返回空文本'
    if isinstance(欲编码的内容, (str, int)) != True:
        print('编码_ANSI到USC2：传入的参数有误')
        return ''
    return ascii(欲编码的内容)


def 编码_USC2到ANSI(欲编码的内容):
    '失败返回空文本'
    if isinstance(欲编码的内容, str) != True:
        print('编码_USC2到ANSI：传入的参数有误')
        return ''
    return 欲编码的内容.encode('utf-8').decode('unicode_escape')


def 编码_BASE64编码(欲编码的内容):
    '失败返回空文本'
    if isinstance(欲编码的内容, str) != True:
        print('编码_BASE64编码：传入的参数有误')
        return ''
    return base64.b64encode(欲编码的内容.encode('UTF-8')).decode("UTF-8")


def 编码_BASE64解码(欲解码的内容, 返回字节集=False):
    '失败返回空文本,字节集用于解码图片'
    if isinstance(欲解码的内容, str) != True:
        print('编码_BASE64解码：传入的参数有误')
        return ''
    try:
        if 返回字节集 == True:
            return base64.b64decode(欲解码的内容)
        else:
            return base64.b64decode(欲解码的内容).decode("UTF-8")
    except Exception as error:
        print('编码_BASE64解码：运行出错|' + str(error))
        return ''



def 加密_MD5(要加密的内容, 编码="utf-8"):
    '失败返回空文本'
    if isinstance(要加密的内容, str) != True or isinstance(编码, str) != True:
        print('加密_MD5：传入的参数有误')
        return ''
    try:
        MD5 = hashlib.md5()
        MD5.update(要加密的内容.encode(encoding=编码))
        return MD5.hexdigest()
    except Exception as error:
        print('加密_MD5：运行出错|' + str(error))
        return ''


def 加密_SHA(要加密的内容, 方式="SHA1"):
    '失败返回空文本,支持SHA1 224 256 384 512'
    if isinstance(要加密的内容, str) != True or isinstance(方式, str) != True:
        print('加密_SHA：传入的参数有误')
        return ''
    elif 方式 == "SHA1":
        sha = hashlib.sha1()
    elif 方式 == "SHA224":
        sha = hashlib.sha224()
    elif 方式 == "SHA256":
        sha = hashlib.sha256()
    elif 方式 == "SHA384":
        sha = hashlib.sha384()
    elif 方式 == "SHA512":
        sha = hashlib.sha512()
    else:
        print('加密_SHA：加密方式有误')
        return ''
    sha.update(str(要加密的内容).encode('utf-8'))
    return sha.hexdigest()


def 加密_SHA3(要加密的内容, 方式="SHA224"):
    '失败返回空文本,支持224 256 384 512'
    if isinstance(要加密的内容, str) != True or isinstance(方式, str) != True:
        print('加密_SHA3：传入的参数有误')
        return ''
    elif 方式 == "SHA224":
        sha = hashlib.sha3_224()
    elif 方式 == "SHA256":
        sha = hashlib.sha3_256()
    elif 方式 == "SHA384":
        sha = hashlib.sha3_384()
    elif 方式 == "SHA512":
        sha = hashlib.sha3_512()
    else:
        print('加密_SHA3：加密方式有误')
        return ''
    sha.update(要加密的内容.encode('utf-8'))
    return sha.hexdigest()


def 加密_HmacSHA256(key, 加密内容):
    '失败出错返回空文本'
    if isinstance(key, str) != True:
        print('加密_HmacSHA256：传入参数有误')
        return ''
    try:
        return base64.b64encode(hmac.new(bytes(key, encoding='utf-8'), bytes(加密内容, encoding='utf-8'),
                                         digestmod=hashlib.sha256).digest()).decode("utf-8")
    except Exception as error:
        print('加密_HmacSHA256：运行出错|' + str(error))
        return ''


def 加密_CRC32(要加密的内容):
    '失败返回空文本'
    if isinstance(要加密的内容, str) != True:
        print('加密_CRC32：传入的参数有误')
        return ''
    return binascii.crc32(要加密的内容.encode("utf-8"))


def JS_调试(JS代码, 方法名, 参数1=None, 参数2=None, 参数3=None, 参数4=None, 参数5=None, 参数6=None, 参数7=None, 参数8=None, 参数9=None,
          参数10=None):
    '失败返回空文本,用*args不知道怎么分配给下面参数'
    if isinstance(JS代码, str) != True or isinstance(方法名, str) != True:
        print('JS_调试：传入参数有误')
        return ''
    try:
        return execjs.compile(JS代码).call(方法名, 参数1, 参数2, 参数3, 参数4, 参数5, 参数6, 参数7, 参数8, 参数9, 参数10)
    except Exception as error:
        print('JS_调试：运行出错|' + str(error))
        return ''


def JS_加载(JS代码):
    '失败返回False,成功返回个对象给JS_运行调用'
    if isinstance(JS代码, str) != True:
        print('JS_加载：传入参数有误')
        return False
    try:
        return execjs.compile(JS代码)
    except Exception as error:
        print('JS_加载：运行出错|' + str(error))
        return False


def JS_运行(JS对象, 方法名, 参数1=None, 参数2=None, 参数3=None, 参数4=None, 参数5=None, 参数6=None, 参数7=None, 参数8=None, 参数9=None,
          参数10=None):
    ',失败返回空文本,通过JS_加载返回的对象'
    if isinstance(JS对象, execjs._external_runtime.ExternalRuntime.Context) != True or isinstance(方法名, str) != True:
        print('JS_加载：传入参数有误')
        return ''
    try:
        return JS对象.call(方法名, 参数1, 参数2, 参数3, 参数4, 参数5, 参数6, 参数7, 参数8, 参数9, 参数10)
    except Exception as error:
        print('JS_运行：运行出错|' + str(error))
        return ''


def GZIP_压缩(欲压缩的字节):
    '失败返回空字节'
    if isinstance(欲压缩的字节, bytes) != True:
        print('GZIP_压缩：传入的参数有误')
        return bytes()
    try:
        return gzip.compress(欲压缩的字节)
    except Exception as error:
        print('GZIP_压缩：运行出错|' + str(error))
        return bytes()


def GZIP_解压(欲解压的字节):
    '失败返回空字节'
    if isinstance(欲解压的字节, bytes) != True:
        print('GZIP_解压：传入的参数有误')
        return bytes()
    try:
        return gzip.decompress(欲解压的字节)
    except Exception as error:
        print('GZIP_解压：运行出错|' + str(error))
        return bytes()


def 文件_取运行目录():
    '返回当前运行目录'
    return os.getcwd()


def 文件_更改当前工作目录(路径):
    '成功返回True,失败返回False'
    if isinstance(路径, str) != True:
        print('文件_更改当前工作目录：传入参数有误')
        return False
    try:
        os.chdir(路径)
        return True
    except Exception as error:
        print('文件_更改当前工作目录：运行出错|' + str(error))
        return False


def 文件_更改当前进程目录(路径):
    '成功返回True,失败返回False'
    if isinstance(路径, str) != True:
        print('文件_更改当前进程目录：传入参数有误')
        return False
    try:
        os.chroot(路径)
        return True
    except Exception as error:
        print('文件_更改当前进程目录：运行出错|' + str(error))
        return False


def 文件_遍历指定路径文件(路径='.'):
    '失败返回空列表,.为单前目录，..为上级目录，返回列表格式不带路径的文件名'
    if isinstance(路径, str) != True:
        print('文件_遍历指定路径文件：传入参数有误')
        return []
    try:
        return os.listdir(路径)
    except Exception as error:
        print('文件_遍历指定路径文件：运行出错|' + str(error))
        return []


def 文件_遍历指定路径所有子目录(路径='.'):
    '失败返回空列表,成功返回列表：(路径, [包含目录], [包含文件]),用法 for root, dirs, files in os.walk("..", topdown=False):'
    if isinstance(路径, str) != True:
        print('文件_遍历指定路径所有子目录：传入参数有误')
        return ()
    try:
        return list(os.walk(路径))
    except Exception as error:
        print('文件_遍历指定路径所有子目录：运行出错|' + str(error))
        return []


def 文件_创建单层目录(路径):
    '成功返回True,失败返回False,创建单层目录，如该目录已存在抛出异常'
    if isinstance(路径, str) != True:
        print('文件_创建单层目录：传入参数有误')
        return False
    try:
        os.mkdir(路径)
        return True
    except Exception as error:
        print('文件_创建单层目录：运行出错|' + str(error))
        return False


def 文件_创建多层目录(路径):
    '成功返回True,失败返回False,创建单层目录，如该目录已存在抛出异常'
    if isinstance(路径, str) != True:
        print('文件_创建多层目录：传入参数有误')
        return False
    try:
        os.makedirs(路径)
        return True
    except Exception as error:
        print('文件_创建多层目录：运行出错|' + str(error))
        return False


def 文件_删除文件(路径):
    '成功返回True,失败返回False'
    if isinstance(路径, str) != True:
        print('文件_删除文件：传入参数有误')
        return False
    try:
        os.remove(路径)
        return True
    except Exception as error:
        print('文件_删除文件：运行出错|' + str(error))
        return False


def 文件_删除文件2(路径):
    '成功返回True,失败返回False,用于删除文件,如果文件是一个目录则返回一个错误'
    if isinstance(路径, str) != True:
        print('文件_删除文件：传入参数有误')
        return False
    try:
        os.unlink(路径)
        return True
    except Exception as error:
        print('文件_删除文件：运行出错|' + str(error))
        return False


def 文件_删除单层空目录(路径):
    '成功返回True,失败返回False,删除单层目录，如该目录非空则抛出异常'
    if isinstance(路径, str) != True:
        print('文件_删除单层空目录：传入参数有误')
        return False
    try:
        os.rmdir(路径)
        return True
    except Exception as error:
        print('文件_删除单层空目录：运行出错|' + str(error))
        return False


def 文件_删除多层空目录(路径):
    '成功返回True,失败返回False,递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常'
    if isinstance(路径, str) != True:
        print('文件_删除多层空目录：传入参数有误')
        return False
    try:
        os.removedirs(路径)
        return True
    except Exception as error:
        print('文件_删除多层空目录：运行出错|' + str(error))
        return False


def 文件_获取访问修改时间(路径):
    '失败返回False,成功返回对象.st_atime 是访问时间 返回对象.st_mtime 是修改时间，返回的是10位时间戳'
    if isinstance(路径, str) != True:
        print('文件_获取访问修改时间：传入参数有误')
        return False
    try:
        return os.stat(路径)
    except Exception as error:
        print('文件_获取访问修改时间：运行出错|' + str(error))
        return False


def 文件_设置访问修改时间(路径, 访问修改时间):
    '成功返回True,失败返回False,传入的修改时间为10位时间戳元组类型(访问时间戳,修改时间戳)'
    if isinstance(路径, str) != True or isinstance(访问修改时间, tuple) != True:
        print('文件_设置访问修改时间：传入参数有误')
        return False
    try:
        os.utime(路径, 访问修改时间)
        return True
    except Exception as error:
        print('文件_设置访问修改时间：运行出错|' + str(error))
        return False


def 文件_重命名(原文件名, 新文件名):
    '成功返回True,失败返回False'
    if isinstance(原文件名, str) != True or isinstance(新文件名, str) != True:
        print('文件_重命名：传入参数有误')
        return False
    try:
        os.rename(原文件名, 新文件名)
        return True
    except Exception as error:
        print('文件_重命名：运行出错|' + str(error))
        return False


def 文件_修改权限(路径, 权限类型=0):
    '成功返回True,失败返回False,权限类型： 0 设为只读 1 取消只读,更多权限参考 http://www.runoob.com/python/os-chmod.html'
    if isinstance(路径, str) != True or isinstance(权限类型, int) != True:
        print('文件_修改权限：传入参数有误')
        return False
    try:
        if 权限类型 == 0:
            os.chmod(路径, stat.S_IREAD)
            return True
        elif 权限类型 == 1:
            os.chmod(路径, stat.S_IWRITE)
            return True
        else:
            print('文件_修改权限：传入参数有误')
            return False
    except Exception as error:
        print('文件_修改权限：运行出错|' + str(error))
        return False


def 文件_是否为绝对路径(路径):
    '传入路径返回True或False'
    if isinstance(路径, str) != True:
        print('文件_是否为绝对路径：传入参数有误')
        return False
    try:
        return os.path.isabs(路径)
    except Exception as error:
        print('文件_是否为绝对路径：运行出错|' + str(error))
        return False


def 文件_是否为目录(路径):
    '传入路径返回True或False'
    if isinstance(路径, str) != True:
        print('文件_是否为目录：传入参数有误')
        return False
    try:
        return os.path.isdir(路径)
    except Exception as error:
        print('文件_是否为目录：运行出错|' + str(error))
        return False


def 文件_是否为文件(路径):
    '传入路径返回True或False'
    if isinstance(路径, str) != True:
        print('文件_是否为文件：传入参数有误')
        return False
    try:
        return os.path.isfile(路径)
    except Exception as error:
        print('文件_是否为文件：运行出错|' + str(error))
        return False


def 文件_是否存在(路径):
    '传入路径返回True或False'
    if isinstance(路径, str) != True:
        print('文件_是否存在：传入参数有误')
        return False
    try:
        return os.path.exists(路径)
    except Exception as error:
        print('文件_是否存在：运行出错|' + str(error))
        return False


def 文件_取文件大小(路径):
    '返回文件长度,失败返回-1'
    if isinstance(路径, str) != True:
        print('文件_取文件大小：传入参数有误')
        return -1
    try:
        return os.path.getsize(路径)
    except Exception as error:
        print('文件_取文件大小：运行出错|' + str(error))
        return -1


def 文件_取最近访问时间(路径):
    '返回时间戳,失败返回0'
    if isinstance(路径, str) != True:
        print('文件_取最近访问时间：传入参数有误')
        return 0
    try:
        return os.path.getatime(路径)
    except Exception as error:
        print('文件_取最近访问时间：运行出错|' + str(error))
        return 0


def 文件_取创建时间(路径):
    '返回时间戳,失败返回0'
    if isinstance(路径, str) != True:
        print('文件_取创建时间：传入参数有误')
        return 0
    try:
        return os.path.ctime(路径)
    except Exception as error:
        print('文件_取创建时间：运行出错|' + str(error))
        return 0


def 文件_取修改时间(路径):
    '返回时间戳,失败返回0'
    if isinstance(路径, str) != True:
        print('文件_取修改时间：传入参数有误')
        return 0
    try:
        return os.path.mtime(路径)
    except Exception as error:
        print('文件_取修改时间：运行出错|' + str(error))
        return 0


def 文件_取文件目录(路径):
    '失败返回空文本,去掉文件名，返回目录路径'
    if isinstance(路径, str) != True:
        print('文件_取文件目录：传入参数有误')
        return ''
    try:
        return os.path.dirname(路径)
    except Exception as error:
        print('文件_取文件目录：运行出错|' + str(error))
        return ''


def 文件_取路径文件名(路径):
    '失败返回空文本,去掉目录路径，返回文件名'
    if isinstance(路径, str) != True:
        print('文件_取路径文件名：传入参数有误')
        return ''
    try:
        return os.path.basename(路径)
    except Exception as error:
        print('文件_取路径文件名：运行出错|' + str(error))
        return ''


def 文件_文件扩展名分割(路径):
    '失败返回空元组,传入文件路径,返回元组类型 (文件名,扩展名)'
    if isinstance(路径, str) != True:
        print('文件_文件扩展名分割：传入参数有误')
        return ()
    try:
        return os.path.splitext(路径)
    except Exception as error:
        print('文件_文件扩展名分割：运行出错|' + str(error))
        return ()


def 文件_目录文件名分割(路径):
    '失败返回空元组,传入路径,返回元组类型 (目录,文件名)'
    if isinstance(路径, str) != True:
        print('文件_目录文件名分割：传入参数有误')
        return ()
    try:
        return os.path.split(路径)
    except Exception as error:
        print('文件_目录文件名分割：运行出错|' + str(error))
        return ()


def 文件_创建文件(路径):
    '成功返回True,失败返回False,创建空文件'
    if isinstance(路径, str) != True:
        print('文件_创建文件：传入参数有误')
        return False
    try:
        文件_写入文件(路径, '', 'w')
        return True
    except Exception as error:
        print('文件_创建文件：运行出错|' + str(error))
        return False


def 文件_检测权限(路径, 权限类型=0):
    '权限类型：0 是否存在 1 是否可读 2 是否可写 3 是否可执行，返回True或False'
    if isinstance(路径, str) != True or isinstance(权限类型, int) != True:
        print('文件_是否有权限：传入参数有误')
        return False
    try:
        if 权限类型 == 0:
            return os.access(路径, os.F_OK)
        elif 权限类型 == 1:
            return os.access(路径, os.R_OK)
        elif 权限类型 == 2:
            return os.access(路径, os.W_OK)
        elif 权限类型 == 3:
            return os.access(路径, os.X_OK)
        else:
            print('文件_是否有权限：传入参数有误')
            return False
    except Exception as error:
        print('文件_是否有权限：运行出错|' + str(error))
        return False


def 文件_写入文件(文件名, 写入的数据, 方式='a'):
    '成功返回True,失败返回False,如果文件不存在会创建新文件,方式默认为a 追加写入 覆盖写入用w'
    if isinstance(文件名, str) != True or isinstance(方式, str) != True:
        print('文件_写入文件：传入参数有误')
        return False
    try:
        with open(文件名, 方式, encoding="utf-8") as a:
            a.write(写入的数据)
        return True
    except Exception as error:
        print('文件_写入文件：运行出错|' + str(error))
        return False


def 文件_读取文件(文件名, 读取长度=-1, 方式='r'):
    '失败返回False,方式默认用r 二进制用rb 长度默认读取全部'
    if isinstance(文件名, str) != True or isinstance(方式, str) != True or isinstance(读取长度, int) != True:
        print('文件_读取文件：传入参数有误')
        return False
    try:
        with open(文件名, 方式, encoding="utf-8") as a:
            return a.read(读取长度)
    except Exception as error:
        print('文件_读取文件：运行出错|' + str(error))
        return False


def 文件_读取某行(文件名, 行位置=0, 方式='r'):
    '失败返回False,方式默认用r 二进制用rb,这里的行位置是字符串的位置 可以用寻找文本定位位置取出那一行,返回的是列表'
    if isinstance(文件名, str) != True or isinstance(方式, str) != True or isinstance(行位置, int) != True:
        print('文件_读取某行：传入参数有误')
        return False
    try:
        if 行位置 < 1:
            with open(文件名, 方式, encoding="utf-8") as a:
                return a.readline()
        else:
            with open(文件名, 方式, encoding="utf-8") as a:
                return a.readlines(行位置)
    except Exception as error:
        print('文件_读取某行：运行出错|' + str(error))
        return False


def 数据_排列(列表, 长度):
    '失败返回空列表,生产多种不相同组合，返回列表，列表里每个成员是元组'
    if isinstance(列表, list) != True or isinstance(长度, int) != True:
        print('数据_排列：传入参数有误')
        return []
    try:
        return list(itertools.permutations(列表, 长度))
    except Exception as error:
        print('数据_排列：运行出错|' + str(error))
        return []


def 数据_组合(列表, 长度):
    '失败返回空列表,生产多种不相同组合，但不会使用相同数值做顺序不一样的组合，返回列表，列表里每个成员是元组'
    if isinstance(列表, list) != True or isinstance(长度, int) != True:
        print('数据_组合：传入参数有误')
        return []
    try:
        return list(itertools.combinations(列表, 长度))
    except Exception as error:
        print('数据_组合：运行出错|' + str(error))
        return []


def 数据_排列组合(列表, 长度):
    '失败返回空列表,没看懂先放着吧'
    if isinstance(列表, list) != True or isinstance(长度, int) != True:
        print('数据_排列组合：传入参数有误')
        return []
    try:
        return list(itertools.product(列表, 长度))
    except Exception as error:
        print('数据_排列组合：运行出错|' + str(error))
        return []


def 进制_十到二(原内容):
    '失败返回空文本'
    if isinstance(原内容, int) != True:
        print('进制_十到二：传入参数有误')
        return ''
    try:
        return bin(原内容)
    except Exception as error:
        print('进制_十到二：运行出错|' + str(error))
        return ''


def 进制_十到八(原内容):
    '失败返回空文本'
    if isinstance(原内容, int) != True:
        print('进制_十到八：传入参数有误')
        return ''
    try:
        return oct(原内容)
    except Exception as error:
        print('进制_十到八：运行出错|' + str(error))
        return ''


def 进制_十到十六(原内容):
    '失败返回空文本'
    if isinstance(原内容, int) != True:
        print('进制_十到十六：传入参数有误')
        return ''
    try:
        return hex(原内容)
    except Exception as error:
        print('进制_十到十六：运行出错|' + str(error))
        return ''


def 进制_二到十(原内容):
    '失败返回00'
    if isinstance(原内容, str) != True:
        print('进制_二到十：传入参数有误')
        return '00'
    try:
        return int(原内容, base=2)
    except Exception as error:
        print('进制_二到十：运行出错|' + str(error))
        return '00'


def 进制_八到十(原内容):
    '失败返回00'
    if isinstance(原内容, str) != True:
        print('进制_八到十：传入参数有误')
        return '00'
    try:
        return int(原内容, base=8)
    except Exception as error:
        print('进制_八到十：运行出错|' + str(error))
        return '00'


def 进制_十六到十(原内容):
    '失败返回00'
    if isinstance(原内容, str) != True:
        print('进制_十六到十：传入参数有误')
        return '00'
    try:
        return int(原内容, base=16)
    except Exception as error:
        print('进制_十六到十：运行出错|' + str(error))
        return '00'


def 网页_取外网IP(返回地区=False):
    '失败返回空文本,使用ip138接口,如果设置返回地区则返回两个参数,ip,地区'
    if isinstance(返回地区, bool) != True:
        print('网页_取外网IP：传入参数有误')
        return ''
    try:
        网页源码 = requests.get("http://www.ip138.com", verify=False, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36"})
        网页源码.encoding = 'gbk'
        网页源码 = requests.get(文本_取出中间文本(网页源码.text, '<iframe src="', '" rel="nofollow'), verify=False)
        if 返回地区 == False:
            return 文本_取出中间文本(网页源码.text, '是：[', ']')
        else:
            return 文本_取出中间文本(网页源码.text, '是：[', ']'), 文本_取出中间文本(网页源码.text, "来自：", "\r")
    except Exception as error:
        print("网页_取外网IP：运行出错|" + str(error))
        return ''


def 网页_取外网IP_S(返回地区=False):
    '失败返回空文本,使用sohu接口,如果设置返回地区则返回两个参数,ip,地区'
    if isinstance(返回地区, bool) != True:
        print('网页_取外网IP_S：传入参数有误')
        return ''
    try:
        网页源码 = requests.get("http://pv.sohu.com/cityjson", verify=False, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36"})
        if 返回地区 == False:
            return 文本_取出中间文本(网页源码.text, 'cip": "', '"')
        else:
            return 文本_取出中间文本(网页源码.text, 'cip": "', '"'), 文本_取出中间文本(网页源码.text, 'cname": "', '"')
    except Exception as error:
        print("网页_取外网IP_S：运行出错|" + str(error))
        return ''


def 网页_访问_对象(请求地址, 请求方式=0, 提交的内容='', 提交的COOKIE='', 提交的协议头={}, 允许重定向=True, 上传文件=None, 代理地址=None, 最长等待=30, 编码方式=None,
             证书验证=False):
    "请求方式：0是GET 1是POST.提交的内容跟提交的Cookie可以是字符串也可以是字典。返回的Cookie是文本型,返回的协议头是字典,证书验证：默认为False,需要引用证书时传入证书路径,上传文件格式:{'upload': ('code.png', 图片字节集, 'image/png')}"
    网页 = 网页类型()
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    http = requests.session()
    # if type(上传文件) == dict:
    #     try:
    #         files = {'files': open(上传文件, 'rb')}
    #     except:
    #         上传文件= None
    # else:
    #     上传文件= None

    if 提交的协议头 == {} or 提交的协议头 == '':
        提交的协议头 = {"Accept": "*/*",
                  "Referer": 请求地址,
                  "Accept-Language": "zh-cn",
                  "Content-Type": "application/x-www-form-urlencoded",
                  "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36"}

    if type(提交的协议头) == str:
        if len(提交的协议头) > 3:
            协议头数组 = 文本_分割文本(提交的协议头, '\n')
            提交的协议头 = {}
            for x in 协议头数组:
                键 = 文本_删首尾指定字符(文本_取文本左边(x, ':'))
                值 = 文本_删首尾指定字符(文本_取文本右边(x, ':'))
                if 键 != '' and 值 != '':
                    提交的协议头[键] = 值
        else:
            提交的协议头 = {}

    if 请求方式 < 0 or 请求方式 > 1:
        请求方式 = 0
    if 最长等待 < 1 or 最长等待 > 60:
        最长等待 = 30
    if 代理地址 != None:
        代理地址 = {"http": "http://" + 代理地址, "https": "https://" + 代理地址}
    if 提交的COOKIE != '' and type(提交的COOKIE) == str:
        if 文本_寻找文本(提交的COOKIE, "=") == -1:
            提交的COOKIE = {}
        elif 文本_寻找文本(提交的COOKIE, ";") == -1:
            键 = 文本_删首尾指定字符(文本_取文本左边(提交的COOKIE, '='))
            值 = 文本_删首尾指定字符(文本_取文本右边(提交的COOKIE, '='))
            if 键 != '' and 值 != '':
                提交的COOKIE = {键: 值}
        else:
            COOKIE数组 = 文本_分割文本(提交的COOKIE, ';')
            提交的COOKIE = {}
            for x in COOKIE数组:
                键 = 文本_删首尾指定字符(文本_取文本左边(x, '='))
                值 = 文本_删首尾指定字符(文本_取文本右边(x, '='))
                if 键 != '' and 值 != '':
                    提交的COOKIE[键] = 值
    try:
        if 请求方式 == 0:
            网页对象 = http.get(文本_删首尾指定字符(请求地址), params=提交的内容, cookies=提交的COOKIE, headers=提交的协议头, allow_redirects=允许重定向,
                            files=上传文件,
                            proxies=代理地址, timeout=最长等待, verify=证书验证)
        else:
            网页对象 = http.post(文本_删首尾指定字符(请求地址), data=提交的内容, cookies=提交的COOKIE, headers=提交的协议头, allow_redirects=允许重定向,
                             files=上传文件,
                             proxies=代理地址, timeout=最长等待, verify=证书验证)

        if 编码方式 != None:
            网页对象.encoding = 编码方式
        网页.源码 = 网页对象.text
        返回的COOKIE = ''
        返回的COOKIE字典 = dict(网页对象.cookies)
        for x in 返回的COOKIE字典:
            返回的COOKIE = 返回的COOKIE + x + '=' + 返回的COOKIE字典[x] + '; '
        网页.Cookie = 返回的COOKIE
        网页.状态码 = 网页对象.status_code
        网页.协议头 = 网页对象.headers
    except Exception as error:
        print('网页_访问_对象：运行出错|' + str(error))

    return 网页


def 网页_COOKIE合并更新(原COOKIE, 新COOKIE):
    '返回更新后的COOKIE,所有COOKIE格式均为文本型'
    if isinstance(原COOKIE, str) != True or isinstance(新COOKIE, str) != True:
        print('网页_COOKIE合并更新：传入参数有误')
        return ''
    try:
        更新后的COOKIE = {}
        if 文本_寻找文本(原COOKIE, "=") != -1 and 文本_寻找文本(原COOKIE, ";") == -1:
            键 = 文本_删首尾指定字符(文本_取文本左边(原COOKIE, '='))
            值 = 文本_删首尾指定字符(文本_取文本右边(原COOKIE, '='))
            if 键 != '' and 值 != '':
                更新后的COOKIE[键] = 值
        else:
            COOKIE数组 = 文本_分割文本(原COOKIE, ';')
            for x in COOKIE数组:
                键 = 文本_删首尾指定字符(文本_取文本左边(x, '='))
                值 = 文本_删首尾指定字符(文本_取文本右边(x, '='))
                if 键 != '' and 值 != '':
                    更新后的COOKIE[键] = 值

        if 文本_寻找文本(新COOKIE, "=") != -1 and 文本_寻找文本(新COOKIE, ";") == -1:
            键 = 文本_删首尾指定字符(文本_取文本左边(新COOKIE, '='))
            值 = 文本_删首尾指定字符(文本_取文本右边(新COOKIE, '='))
            if 键 != '' and 值 != '':
                更新后的COOKIE[键] = 值
        else:
            COOKIE数组 = 文本_分割文本(新COOKIE, ';')
            for x in COOKIE数组:
                键 = 文本_删首尾指定字符(文本_取文本左边(x, '='))
                值 = 文本_删首尾指定字符(文本_取文本右边(x, '='))
                if 键 != '' and 值 != '':
                    更新后的COOKIE[键] = 值

        返回的COOKIE = ''
        for x in 更新后的COOKIE:
            返回的COOKIE = 返回的COOKIE + x + '=' + 更新后的COOKIE[x] + '; '
        return 返回的COOKIE
    except Exception as error:
        print('网页_COOKIE合并更新：运行出错|' + str(error))
        return ''


def 启动线程(函数名, 元组参数=(), 跟随主线程结束=False):
    "成功返回线程对象,失败返回False,参数用元组形式传入,返回线程对象,daemon属性为False，主线程结束时会检测该子线程是否结束"
    if isinstance(元组参数, tuple) != True:
        print('启动线程：传入参数有误')
        return False
    try:
        线程 = threading.Thread(target=函数名, args=元组参数, daemon=跟随主线程结束)
        线程.start()
        return 线程
    except Exception as error:
        print('启动线程：运行出错|' + str(error))
        return False


def 创建线程许可证():
    return threading.Lock()


def 进入许可区(许可证):
    '许可证如果错误则无效'
    try:
        许可证.acquire()
    except Exception as error:
        print('进入许可区：运行出错|' + str(error))
        return False


def 退出许可区(许可证):
    '许可证如果错误则无效'
    try:
        许可证.release()
    except Exception as error:
        print('退出许可区：运行出错|' + str(error))
        return False


def 程序_延时(延迟秒数):
    '延迟时间，可以用小数'
    if isinstance(延迟秒数, (int, float)) != True:
        print('程序_延时：传入参数有误')
        return False
    elif 延迟秒数 < 0:
        延迟秒数 = 1
    time.sleep(延迟秒数)


def 程序_退出():
    '终止当前进程,不知道有没有效'
    os.exit()


def 讯代理_计算协议头(单号, 秘钥):
    '失败返回空,返回讯代理Proxy-Authorization的完整值'
    if isinstance(单号, str) != True or isinstance(秘钥, str) != True:
        print('讯代理_计算协议头：传入参数有误')
        return ''
    时间戳 = 时间_取现行时间戳(True)
    sign = 加密_MD5("orderno=" + 单号 + "," + "secret=" + 秘钥 + "," + "timestamp=" + 时间戳).upper()
    return "sign=" + sign + "&" + "orderno=" + 单号 + "&" + "timestamp=" + 时间戳


def 系统_运行CMD命令(命令):
    '失败返回False,成功返回执行结果'
    if isinstance(命令, str) != True:
        print('系统_运行CMD命令：传入参数有误')
        return False
    try:
        f = os.popen('ipconfig')
        结果 = str(f.read())
        f.close()
        return 结果
    except Exception as error:
        print('系统_运行CMD命令：运行出错|' + str(error))
        return False


def 变量_取出随机元素(原参数):
    '失败返回False,注意,取出的类型看传入的参数,不一定是文本,可以传入字符 元组 列表'
    if isinstance(原参数, (str, list, tuple)) != True:
        print('变量_取出随机元素：传入参数有误')
        return False
    try:
        return random.choice(原参数)
    except Exception as error:
        print('变量_取出随机元素：运行出错|' + str(error))
        return False


def 信息框(标题='提示', 提示内容='你好易语言', 类型=0):
    '失败返回-1,,请在窗口代码下调用,0普通信息框,1带确认取消信息框,2黄色警告,3红色错误,4黄色警告重试'
    if isinstance(标题, str) != True or isinstance(提示内容, str) != True or isinstance(类型, int) != True or 类型 < 0 or 类型 > 4:
        print('信息框：传入参数有误')
        return -1
    try:
        if 类型 == 0:
            return messagebox.showinfo(标题, 提示内容)
        elif 类型 == 1:
            return messagebox.askokcancel(标题, 提示内容)  # 确定返回True 取消返回False
        elif 类型 == 2:
            return messagebox.showwarning(标题, 提示内容)
        elif 类型 == 3:
            return messagebox.showerror(标题, 提示内容)
        elif 类型 == 4:
            return messagebox.askretrycancel(标题, 提示内容)  # 重试返回True 取消返回False
    except Exception as error:
        print('信息框：运行出错|' + str(error))
        return -1


class 线程:
    def __init__(self):
        self.__线程列表 = []

    def 多线程(self, 函数名, 任务数, 线程数, 元组参数=(), 最长等待时间=0, 跟随主线程结束=False):
        '顺利执行返回True,否则返回False'
        if isinstance(任务数, int) != True or isinstance(线程数, int) != True or isinstance(元组参数,
                                                                                      tuple) != True or isinstance(
            最长等待时间, int) != True or isinstance(跟随主线程结束, bool) != True:
            print('多线程：传入参数有误')
            return False
        __多线程列表 = []
        剩余数 = 任务数
        try:
            while 剩余数 > 0:
                for x in __多线程列表:
                    if x.is_alive() == False:
                        __多线程列表.remove(x)
                if len(__多线程列表) >= 线程数:
                    time.sleep(0.1)
                else:
                    线程 = threading.Thread(target=函数名, args=元组参数, daemon=跟随主线程结束)
                    线程.start()
                    __多线程列表.append(线程)
                    剩余数 = 剩余数 - 1

            for i in __多线程列表:
                if 最长等待时间 <= 0:
                    i.join()
                else:
                    i.join(最长等待时间)
            print("多线程：任务全部执行完毕")
            return True
        except Exception as error:
            print('多线程：运行出错|' + str(error))
            return False

    def 启动线程(self, 函数名, 元组参数=(), 跟随主线程结束=False):
        "失败返回False,成功返回线程对象,参数用元组形式传入,daemon属性为False，主线程结束时会检测该子线程是否结束"
        if isinstance(元组参数, tuple) != True or isinstance(跟随主线程结束, bool) != True:
            print('启动线程：传入参数有误')
            return False
        try:
            线程 = threading.Thread(target=函数名, args=元组参数, daemon=跟随主线程结束)
            线程.start()
            self.__线程列表.append(线程)
            return 线程
        except Exception as error:
            print('启动线程：运行出错|' + str(error))
            return False

    def 等待线程结束(self, 最长等待时间=0):
        '顺利结束返回True,出错返回False如果启动线程参数daemon设置为True,则可以设置最长等待时间,超过时间强制结束线程'
        if isinstance(最长等待时间, (int, float)) != True:
            print('等待线程结束：传入参数有误')
            return False
        try:
            for i in self.__线程列表:
                if 最长等待时间 <= 0:
                    i.join()
                else:
                    i.join(最长等待时间)
            return True
        except Exception as error:
            print('等待线程结束：运行出错|' + str(error))
            return False

    def 取运行的线程数(self):
        '只返回该类创建后使用该类启动线程创建的线程数量'
        try:
            for x in self.__线程列表:
                if x.is_alive() == False:
                    self.__线程列表.remove(x)
            return len(self.__线程列表)
        except Exception as error:
            print('取运行的线程数：运行出错|' + str(error))
            return 0

    def 取运行中的线程对象(self):
        return threading.enumerate()

    def 线程是否在运行(self, 线程对象):
        '返回True或False'
        try:
            return 线程对象.is_alive()
        except Exception as error:
            print('线程是否在运行：运行出错|' + str(error))
            return False


class Mysql:

    def __init__(self):
        self.__数据库 = None
        self.__游标 = None
        self.__连接地址 = None
        self.__用户名 = None
        self.__密码 = None
        self.__数据库名 = None
        self.__端口号 = None
        self.__编码 = None
        self.__许可 = threading.Lock()

    def 连接(self, 连接地址, 用户名, 密码, 数据库名, 端口号, 编码='utf8'):
        '连接成功返回True,失败返回False'
        # self.__许可.acquire()
        if isinstance(连接地址, str) != True or isinstance(用户名, str) != True or isinstance(密码, str) != True or isinstance(
                数据库名, str) != True or isinstance(端口号, int) != True or isinstance(编码, str) != True:
            print('数据库_连接：传入参数有误')
            # self.__许可.release()
            return False
        try:
            self.__数据库 = pymysql.connect(host=连接地址, port=端口号, user=用户名, passwd=密码, db=数据库名, charset=编码)
            self.__游标 = self.__数据库.cursor()
            self.__连接地址 = 连接地址
            self.__用户名 = 端口号
            self.__密码 = 用户名
            self.__数据库名 = 密码
            self.__端口号 = 数据库名
            self.__编码 = 编码
            print('数据库连接成功')
            # self.__许可.release()
            return True
        except Exception as error:
            print('数据库_连接：运行出错|' + str(error))
            # self.__许可.release()
            return False

    def 关闭游标(self):
        '成功返回True,失败返回False'
        self.__许可.acquire()
        try:
            self.__游标.close()
            self.__许可.release()
            return True
        except Exception as error:
            print('数据库_关闭游标：运行出错|' + str(error))
            self.__许可.release()
            return False

    def 关闭连接(self):
        '成功返回True,失败返回False'
        self.__许可.acquire()
        try:
            self.__数据库.close()
            self.__许可.release()
            return True
        except Exception as error:
            print('数据库_关闭连接：运行出错|' + str(error))
            self.__许可.release()
            return False

    def 事务提交(self):
        '成功返回True,失败返回False'
        self.__许可.acquire()
        try:
            self.__数据库.commit()
            self.__许可.release()
            return True
        except Exception as error:
            print('数据库_事务提交：运行出错|' + str(error))
            self.__许可.release()
            return False

    def 事务回滚(self):
        '成功返回True,失败返回False'
        self.__许可.acquire()
        try:
            self.__数据库.rollback()
            self.__许可.release()
            return True
        except Exception as error:
            print('数据库_事务回滚：运行出错|' + str(error))
            self.__许可.release()
            return False

    def 执行SQL语句(self, Sql语句):
        '成功返回执行结果,失败返回False'
        self.__许可.acquire()
        if isinstance(Sql语句, str) != True:
            print('数据库_执行SQL语句：传入Sql语句有误')
            self.__许可.release()
            return False
        try:
            结果 = self.__游标.execute(Sql语句)
            self.__数据库.commit()
            self.__许可.release()
            return 结果
        except Exception as error:
            print('数据库_执行SQL语句：运行出错|' + str(error))
            self.__许可.release()
            return False

    def 获取所有记录列表(self):
        '成功返回一个列表,列表成员是元组,失败返回空列表'
        self.__许可.acquire()
        try:
            self.__许可.release()
            return self.__游标.fetchall()
        except Exception as error:
            print('数据库_获取所有记录列表：运行出错|' + str(error))
            self.__许可.release()
            return []

    def 保持在线(self):
        '返回True,False'
        self.__许可.acquire()
        try:
            self.__数据库.ping(reconnect=True)
            self.__许可.release()
            return True
        except Exception as error:
            self.__许可.release()
            return self.连接(连接地址=self.__连接地址, 用户名=self.__用户名, 密码=self.__密码, 数据库名=self.__数据库名, 端口号=self.__端口号,
                           编码=self.__编码)

    def 更新记录(self, 表名, 更新条件, 更新内容):
        "成功返回更新的数量,失败返回0,更新条件如果为空则全表更新"
        self.__许可.acquire()
        if isinstance(表名, str) != True or isinstance(更新条件, str) != True or isinstance(更新内容, str) != True:
            print('数据库_更新记录：传入参数有误')
            self.__许可.release()
            return 0
        Sql语句 = ""
        if 更新条件 == "":
            Sql语句 = "update " + 表名 + " set " + 更新内容
        else:
            Sql语句 = "update " + 表名 + " set " + 更新内容 + " where " + 更新条件 + ";"

        try:
            结果 = self.__游标.execute(Sql语句)
            self.__数据库.commit()
            self.__许可.release()
            return 结果
        except Exception as error:
            # self.__数据库.rollback()
            print('数据库_更新记录：运行出错|' + str(error))
            self.__许可.release()
            return 0

    def 查找记录(self, 表名, 字段名, 查找条件="", 搜索方式=0, 取出的数量=0, 排序=""):
        "失败返回空元组,字段名可以是* 表示全部字段,搜索方式 0为指定,1是模糊,取出的数量默认是0取出全部,排序order by 字段名 desc/asc"
        self.__许可.acquire()
        if isinstance(表名, str) != True or isinstance(字段名, str) != True or isinstance(查找条件, str) != True or isinstance(
                搜索方式, (str, int)) != True or isinstance(取出的数量, (str, int)) != True or isinstance(排序, str) != True:
            print('数据库_查找记录：传入参数有误')
            self.__许可.release()
            return ()
        文本 = ""
        Sql语句 = ""

        if str(搜索方式) == "0":
            if 查找条件 == "":
                Sql语句 = "select " + 字段名 + " from " + 表名
            else:
                Sql语句 = "select " + 字段名 + " from " + 表名 + " where " + 查找条件
        elif str(搜索方式) == "1":
            数组 = 查找条件.split(" and ")
            for x in 数组:
                文本 = 文本 + 文本_取文本左边(x, "=") + " like '%" + 文本_取出中间文本(x, "'", "'") + "%' and "
            Sql语句 = "select " + 字段名 + " from " + 表名 + " where " + 文本[0:len(文本) - 5]
        if 取出的数量 != 0:
            Sql语句 = Sql语句 + "limit " + str(取出的数量)
        Sql语句 = Sql语句 + 排序
        try:
            self.__游标.execute(Sql语句)
            结果 = self.__游标.fetchall()
            self.__数据库.commit()
            self.__许可.release()
            return 结果
        except Exception as error:
            # self.数据库.rollback()
            print('数据库_查找记录：运行出错|' + str(error))
            self.__许可.release()
            return ()

    def 增加记录(self, 表名, 字段名, 插入的内容):
        "失败返回-1,成功返回更新数量,字段名格式是 字段名,字段名  插入的内容格式是 ('123456','456789')多换后面带逗号跟换行"  # 传入字段跟内容示例 '字段1,字段2'    "(字段1值,字段2值)"
        self.__许可.acquire()
        if isinstance(表名, str) != True or isinstance(字段名, str) != True or isinstance(插入的内容, str) != True:
            print('数据库_增加记录：传入的参数有误')
            self.__许可.release()
            return -1
        Sql语句 = ""
        try:
            Sql语句 = "insert into " + 表名 + " " + "\n\n" + "( " + 字段名 + " )" + "\n\n" + "values" + "\n\n" + 插入的内容 + ";"
            结果 = self.__游标.execute(Sql语句)
            self.__数据库.commit()
            self.__许可.release()
            return 结果
        except Exception as error:
            # self.__数据库.rollback()
            print('数据库_增加记录：运行出错|' + str(error))
            self.__许可.release()
            return -1

    def 删除记录(self, 表名, 删除条件):
        '失败返回-1,成功返回删除数量'
        self.__许可.acquire()
        if isinstance(表名, str) != True or isinstance(删除条件, str) != True:
            print('数据库_删除记录：传入的参数有误')
            self.__许可.release()
            return -1
        try:
            sql语句 = "DELETE FROM " + 表名 + " WHERE " + 删除条件 + ";"
            结果 = self.__游标.execute(sql语句)
            self.__数据库.commit()
            self.__许可.release()
            return 结果
        except Exception as error:
            # self.__数据库.rollback()
            print('数据库_删除记录：运行出错|' + str(error))
            self.__许可.release()
            return -1


class 网页类型:
    def __init__(self):
        self.源码 = ''
        self.Cookie = ''
        self.协议头 = {}
        self.状态码 = 0


def 联众答题(账号, 密码, 图片字节集, 类型='', 最短识别='', 最长识别=''):
    data = {
        'user_name': 账号,
        'user_pw': 密码,
        'yzm_minlen': 最短识别,
        'yzm_maxlen': 最长识别,
        'yzmtype_mark': 类型,
        'zztool_token': ''
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
        # 'Content-Type': 'multipart/form-data; boundary=---------------------------227973204131376',
        'Connection': 'keep-alive',
        'Host': 'v1-http-api.jsdama.com',
        'Upgrade-Insecure-Requests': '1'
    }
    图片 = {'upload': ('code.png', 图片字节集, 'image/png')}
    return 网页_访问_对象('http://v1-http-api.jsdama.com/api.php?mod=php&act=upload', 1, data,提交的协议头=headers,上传文件=图片).源码


def reload():
    from importlib import reload
    while True:
        reload(b)
        from b import aaa
        aaa.abc()
        time.sleep(1)


#查询进程对应端口
#import psutil
#import os
def port(jingcheng):
    por_list=[]
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        #print('pid-%s,pname-%s' % (pid, p.name()))
        if p.name() == jingcheng:
            cmd = 'netstat -ano | findstr' + ' '+str(pid)
            #print(cmd)
            a = os.popen(cmd)
            # 此时打开的a是一个对象，如果直接打印的话是对象内存地址
            text = a.read()
            if text:
                #print('text',text)
                # 要用read（）方法读取后才是文本对象
                first_line = text.split(':')
                ab = first_line[1]
                cd = ab.split(' ')
                por = cd[0]
                por_list.append(por)
                # print(por) 
                # return por     
    print(por_list) 
    return por_list   

# import psutil
# import re## 标题
# import os
# def processinfo(x):
#   '''根据服务名找到PID'''
#   procs = list(psutil.process_iter()) # 获取所有服务列表
#   #print(procs)
#   for r in procs:
#     aa = str(r)
#     f = re.compile(x,re.I)
#     if f.search(aa):
#       print (aa.split('pid=')[1].split(',')[0])
#       print('----------')
#       return aa.split('pid=')[1].split(',')[0]
#       # print (aa.split('pid='))
# def port(x):
#   '''通过pid获取端口号'''
#   PID = processinfo(x)
#   cmd = 'netstat -ano | findstr' + ' '+str(PID)
#   print(cmd)
#   a = os.popen(cmd)
#   # 此时打开的a是一个对象，如果直接打印的话是对象内存地址
#   text = a.read()
#   # 要用read（）方法读取后才是文本对象
#   first_line = text.split(':')
#   ab = first_line[1]
#   cd = ab.split(' ')
#   por = cd[0]
#   print(por)
#   return por



if __name__ == '__main__':
    print('欢迎查看Python中文示例模块,模块可能存在使用,示范错误,仅做参考使用！有新建议或错误代码指正欢迎跟我反馈,一同进步。QQ:99396686')
