# 获取项目路径
import os

import yaml
import json

# 获得项目根路径
def get_object_path():
    return os.path.abspath(os.getcwd().split('common')[0])  # 绝对路径


# 读取config.yml文件

def read_config_file(one_node, two_node):  # 如果想要得到其中的一个基础路径，如得到测试路径，需要加上第一个节点的值base，和第二个结点的值ceshi_url
    with open(get_object_path() + '/config.yml', encoding='utf-8') as f:
        # '/config.yml' 在此处py没加/调试通过，但是在all.py里面找不到文件，因为这是相对路径所以需要加 /
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[one_node][two_node]  # 通过键引出他的值


# 读取extract.yml文件
def read_extract_file(node_name):  # 读写的时候只需要一个节点的名称就可以了，通过节点的名称提取
    with open(get_object_path() + '/extract.yml', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[node_name]


# 读取YAML文件 测试用例
def read_testcase_file(yaml_path):
    with open(get_object_path() + yaml_path, encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


# 写入extract.yml文件
def write_extract_file(data):
    with open(get_object_path() + '/extract.yml', encoding='utf-8', mode='a') as f:
    #with open(get_object_path() + '/extract.yml', encoding='utf-8', mode='w+') as f:
        # 写入要加入方式，w表示每次写入会把原来的清空；追加’a‘
        yaml.dump(data, stream=f, allow_unicode=True)



# 清空extract.yml文件
def clean_extract_file():
    with open(get_object_path() + '/extract.yml', encoding='utf-8', mode='a') as f:
        f.truncate(0)


# if __name__ == '__main__':
#     print(get_object_path())   # 获取当前py的路径


if __name__ == '__main__':
    print(read_config_file('base', 'ceshi_url'))  # 获取read_config_file 的值
    print(read_config_file('base', 'xian_url'))  # 获取线上的基础路径
