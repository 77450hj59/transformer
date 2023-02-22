import random
import re
import numpy as np
import json

def data_prepare(filename, path):  #临时的
    file = open(filename, 'r', encoding='utf-8')
    r = file.readlines()
    len1 = len(r)
    with open(path, 'w', encoding='utf-8') as f:
        for i in range(0, len1, 4): 
            f.write(r[i])



def ex_data(filename, path1, path2):
    file = open(filename, 'r', encoding='utf-8')
    r = file.readlines()
    len1 = len(r)
    if r[-4].strip() == ";;":
        r = r[1: len1 - 4]
        print('Removing redundant data...')
    # valid_set, train_set = data_split(r, ratio=0.2, shuffle=True)
    # data_seper(valid_set, path2)
    data_seper(r, path1) 
    

def data_split(full_list, ratio, shuffle=False):
    """
    :param full_list: 数据列表
    :param ratio:     子列表1
    :param shuffle:   子列表2
    :return:
    """
    n_total = len(full_list)
    offset = int(n_total * ratio)
    if n_total == 0 or offset < 1:
        return [], full_list
    if shuffle:
        random.shuffle(full_list)
    sublist_1 = full_list[:offset]
    sublist_2 = full_list[offset:]
    return sublist_1, sublist_2  

def data_seper(file, path):
    ch = {}
    for i in file:
        i = re.sub('=', ' ', i)
        list1 = re.sub('->', '/', i)
        list1 = list1.split('/', 1)
        if list1[0] not in ch:
            ch[list1[0]] = list1[1]
        else:
            t = ch[list1[0]]
            t = re.sub('\n', '', t)
            t = t + ',' + list1[1]
            ch[list1[0]] = t
    
    with open(path, 'w', encoding='utf-8') as f:
        for i, j in ch.items():
            f.write(i + '/' + j)
        

if __name__ == '__main__':
    filename1 = '/user_data/huaj/Paper_code/CL/transformer/dataset/dependency_result4.txt'
    path1 = "/user_data/huaj/Paper_code/CL/Transformer-main/data/mtrain.txt"
    path2 = "/user_data/huaj/Paper_code/CL/Transformer-main/data/mtest.txt"
    path = "/user_data/huaj/Paper_code/CL/Transformer-main/data/train_s.txt"
    ex_data(filename1, path1, path2)
    # print(len(valid_set)
    
    