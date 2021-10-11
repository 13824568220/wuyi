# -*- coding:utf-8 -*-
import yaml

def test_yaml():
    """
     # 把字典写进yml文件
    :return:
    """
    env={
        "default": "test",
        "aa":
            {
                "test": "0.0.0.0",
                "dev": "0.0.0.1"
            }
    }
    with open("../data/data_yaml.yml", "w") as f:
        yaml.dump(data=env,stream=f)