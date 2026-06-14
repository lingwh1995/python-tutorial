# -*- coding: utf-8 -*-
"""
@author think
@desc python 中的数据序列化类库
@date 2026/6/8 17:50
"""

import json


def json_lib_test() :
    user_dict = {"name":"小明", "age":18}
    print(user_dict)
    # 字典转json字符串
    user_json = json.dumps(user_dict)
    print(user_json)
    # 字符串转回字典
    user_dict = json.loads(user_json)
    print(user_dict)


if __name__ == "__main__":
    json_lib_test()
