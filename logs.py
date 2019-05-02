# coding:utf-8
import logging

class LogClass:
    """
    日志处理
    """
    def __init__(self,file,name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.fh = logging.FileHandler('log/'+file,mode='a',encoding='utf-8')
        self.fh.setLevel(logging.INFO)
        self.formatter = logging.Formatter( "%(asctime)s - %(filename)s[line:%(lineno)d] - %(funcName)s -%(levelname)s: %(message)s")
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)