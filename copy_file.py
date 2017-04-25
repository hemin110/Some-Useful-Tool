# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 17:56:23 2017

@author: APAC
"""
import os, shutil
#src 原始目录， des 目标目录
def sourcecpy(src, des):
    src = os.path.normpath(src)
    des = os.path.normpath(des)
    if not os.path.exists(src) or not os.path.exists(src):
        print("folder is not found")
        sys.exit(1)
    os.chdir(src)
    src_file = [os.path.join(src, file) for file in os.listdir()]
    for source in src_file:
        if os.path.isfile(source):
            shutil.copy(source, des)   
        else:
            pass
        
        '''
        if os.path.isdir(source):
            p, src_name = os.path.split(source)
            des = os.path.join(des, src_name)
            shutil.copytree(source, des)
            
            
        '''
if __name__ == '__main__':
    src = ''
    des = ''
    
    sourcecpy(src  , des)