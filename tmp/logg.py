#coding:utf-8
import logging

class LogClass():
    """
    日志处理
    """
    def __init__(self,file,name):
        self.file = 'log/'+file
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.logfile = self.file
        self.fh = logging.FileHandler(self.logfile, mode='a')
        self.fh.setLevel(logging.INFO)  # 输出到file的log等级的开关
        self.formatter = logging.Formatter(
            "%(asctime)s - %(filename)s[line:%(lineno)d] - %(funcName)s -%(levelname)s: %(message)s")
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)


