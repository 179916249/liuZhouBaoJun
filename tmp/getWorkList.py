#coding:utf-8
"""获取批量工单号码  2019.03.27 v1.0"""
import requests
from logg import LogClass
import logging
from loginM.login import LoginClass


class GetWorkListClass():
    """获取单日的工单列表"""
    pages = False              #当前日期页码数
    workOrderCode = ""  # 工单单号*
    workOrderCategoryCode = ""  # 主要工单分类代码
    workOrderWorkCategoryID = "1"  # 主要工单分类ID   默认值1
    workOrderSettlementOrder = ""  # 预约单号
    workOrderCatetoryList = []  # 自定工单分类名称（数组）*
    workOrderCarMileageKM = ""  # 进厂里程*
    workOrderRecordedDate = ""  # 结算时间*
    workOrderBeginFixDate = ""  # 来厂时间*
    workOrderDeliveryCarDate = ""  # 交车时间
    workOrderFinishOverDate = ""  # 竣工时间
    workOrderPromiseOverDate = ""  # 预计交车时间
    workOrderNextMaintenDate = ""  # 下次保养时间
    workOrderAllowanceWorkTimeMoney = "0"  # 工时折扣金額
    workOrderPayableWorkTimeMoney = "0"  # 工時應付金額
    workOrderTotalWorkTimeMoney = "0"  # 工时合计金額
    workOrderAllowancePartsMoney = "0"  # 零件折扣金額
    workOrderPayablePartsMoney = "0"  # 零件應付金額
    workOrderTotalPartsMoney = "0"  # 零件合计金額
    workOrderCostPartsMoney = "0"  # 零件成本金額
    workOrderAllowanceCostMoney = ""  # 总折扣金额
    workOrderPayableCostMoney = ""  # 应付总金额
    workOrderTotalCostMoney = "0"  # 总金額
    workOrderCostAllMoney = "0"  # 成本总数金额
    workOrderHireEmployeeName = ""  # 服务顾问
    workOrderMaintenanceTechnician = ""  # 维修技师
    msReasonMBreakdownWhy = ""  # 故障描述
    msReasonCheckResultWhy = ""  # 檢測結果
    msReasonNextTimeFixSuggest = ""  # 下次維修建議
    workOrderSendCarRepairMan = ""  # 送修人
    workOrderSendCarRepairManTelephone = ""  # 送修人电话
    WorkOrderMemo = ""  # 维修备注
    customCarVIN = ""  # 车辆VIN*
    customCarCarLicence = ""  # 车辆牌号
    customCustomName = ""  # 车主
    customActionPhone = ""  # 车主电话
    workOrderWarrantyMoney = "0"  # 索赔金額
    workOrderWarrantyPartMoney = "0"  # 索赔零件金額
    workOrderWarrantyWorkTimeMoney = "0"  # 索赔工时金額
    workOrderCostPartMoney = "0"  # 成本零件金额
    partArray = []  # 零件清单
    maintainArray = []  # 工时清单
    balanceArray = []  # 对表数据 可以传空

    httpCode = [404,504]        #http错误状态码
    getStatus = False           #请求状态
    workCount = 0               #获取页码
    log = LogClass('getWorkList.log','getWorkList')
    log.logger.setLevel(logging.ERROR)
    log.fh.setLevel(logging.ERROR)

    def __init__(self,session,stime):
        pass


    def start(self):
        pass



    def getWorkHtml(self, page, msg):
        pass

    def getPages(self,html):
        pass
    @property
    def getWorkList(self):
        pass

class UpdataCarInfo():
    """上传车辆"""
    # 'http://gt7.com.cn:9090/GBOXData10/action'
    def __init__(self,url):
        self.url = url

    def uploadWorkOrderImport(self,data):
        try:
            res = requests.post(self.url, data=data)
            res = res.json()
            # print(res)
            if res.get('showMsg') == '完成处理':
                return True
            else:
                return False
        except Exception as e:
            return False

    def uploadCarImport(self,data):
        try:
            res = requests.post(self.url, data=data)
            res = res.json()
            if res.get('showMsg') == '完成处理':
                return True
            else:
                return False
        except Exception as e:
            return False





def getWorkInfo(stime,signCode,url):
    """
    获取工单信息
    :param stime: 日期
    :param signCode: 门店代号
    :return:
    """

    pass

if __name__ == "__main__":
    login = LoginClass()
