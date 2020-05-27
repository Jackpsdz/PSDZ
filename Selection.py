import pandas as pd

def readfile(file_name): #读取candidate名单
    file = open(file_name,'r')
    candidate = file.readlines()
    file.close()
    return candidate

# def selection():
readfile()