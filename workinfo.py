# coding:utf-8
"""
单张工单处理
"""

import xlrd
from logs import LogClass
import requests


class WorkInfoClass():
    """处理单张工单信息类"""
    serverCode = "dataWorkOrderImport2"
    workOrderCode = ""  # 工单单号*
    workOrderRepairType = ""  # 工单类别
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
    workOrderAllowanceCostMoney = "0"  # 总折扣金额
    workOrderPayableCostMoney = "0"  # 应付总金额
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
    workOrderCostPartMoney = ""  # 成本零件金额
    partArray = []  # 零件清单
    maintainArray = []  # 工时清单
    balanceArray = []  # 对表数据 可以传空

    carEngineCode = ""  # 车辆信息的车辆动机号
    getStatus = False  # 请求状态
    log = LogClass('workinfo.log', 'workinfo')

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.signCode = self.kwargs.get('signCode')
        self.apiUrl = self.kwargs.get('apiUrl')
        self.getWorks()

    def getWorks(self):

        def costPartMoney():
            """
            partArray列表,零件成本金额
            :return: 零件成功,partArray
            """
            partArrays = self.kwargs.get('partArray', "")
            if len(partArrays) > 0:
                itemOneCostMoneys = []  # 成本列表
                partArray = []  # 零件列表
                for part in partArrays:
                    try:
                        OneCostMoney = float(part.get('itemOneCostMoney', '0.0'))
                        itemOneCostMoneys.append(OneCostMoney)
                    except Exception as e:
                        itemOneCostMoneys.append(0.0)
                    part.pop('workOrderCode')
                    part.update({"itemPickingGroup": "", "itemType": "", "itemPayType": "", "itemWorkCategoryID": ""})
                    partArray.append(part)
                return sum(itemOneCostMoneys), partArray

            else:
                return 0, []

        def maintain():
            """
            工时处理
            :return:
            """
            maintainArrays = self.kwargs.get('maintainArray', "")
            if len(maintainArrays) > 0:
                maintainArray = []
                for maintain in maintainArrays:
                    maintain.pop('workOrderCode')
                    maintain.update({"itemWorkCategoryID": ""})
                    maintainArray.append(maintain)
                return maintainArray
            else:
                return []

        self.workOrderCode = self.kwargs.get('workOrderCode', "")
        self.workOrderRepairType = self.kwargs.get('workOrderRepairType', "")
        # self.workOrderCategoryCode = self.kwargs.get('workOrderCategoryCode',  "")
        # self.workOrderWorkCategoryID = self.kwargs.get('workOrderWorkCategoryID',  "")
        # self.workOrderSettlementOrder = self.kwargs.get('workOrderSettlementOrder',  "")
        self.workOrderCatetoryList = self.kwargs.get('workOrderCatetoryList', "")
        self.workOrderCarMileageKM = self.kwargs.get('workOrderCarMileageKM', "")
        self.workOrderRecordedDate = self.kwargs.get('workOrderRecordedDate', "")
        self.workOrderBeginFixDate = self.kwargs.get('workOrderBeginFixDate', "")
        self.workOrderDeliveryCarDate = self.kwargs.get('workOrderDeliveryCarDate', "")
        self.workOrderFinishOverDate = self.kwargs.get('workOrderFinishOverDate', "")
        self.workOrderPromiseOverDate = self.kwargs.get('workOrderPromiseOverDate', "")
        self.workOrderNextMaintenDate = self.kwargs.get('workOrderNextMaintenDate', "")
        self.workOrderAllowanceWorkTimeMoney = self.kwargs.get('workOrderAllowanceWorkTimeMoney', "")
        self.workOrderPayableWorkTimeMoney = self.kwargs.get('workOrderPayableWorkTimeMoney', "")
        self.workOrderTotalWorkTimeMoney = self.kwargs.get('workOrderTotalWorkTimeMoney', "")
        self.workOrderAllowancePartsMoney = self.kwargs.get('workOrderAllowancePartsMoney', "")
        self.workOrderPayablePartsMoney = self.kwargs.get('workOrderPayablePartsMoney', "")
        self.workOrderTotalPartsMoney = self.kwargs.get('workOrderTotalPartsMoney', "")
        self.workOrderCostPartsMoney, self.partArray = costPartMoney()  # 零件成本金額  零件列表
        self.workOrderAllowanceCostMoney = self.kwargs.get('workOrderAllowanceCostMoney', "")
        self.workOrderPayableCostMoney = self.kwargs.get('workOrderPayableCostMoney', "")
        self.workOrderTotalCostMoney = self.kwargs.get('workOrderTotalCostMoney', "")
        self.workOrderCostAllMoney = self.kwargs.get('workOrderCostAllMoney', "")
        self.workOrderHireEmployeeName = self.kwargs.get('workOrderHireEmployeeName', "")
        self.workOrderMaintenanceTechnician = self.kwargs.get('workOrderMaintenanceTechnician', "")
        self.msReasonMBreakdownWhy = self.kwargs.get('msReasonMBreakdownWhy', "")
        self.msReasonCheckResultWhy = self.kwargs.get('msReasonCheckResultWhy', "")
        self.msReasonNextTimeFixSuggest = self.kwargs.get('msReasonNextTimeFixSuggest', "")
        self.workOrderSendCarRepairMan = self.kwargs.get('workOrderSendCarRepairMan', "")
        self.workOrderSendCarRepairManTelephone = self.kwargs.get('workOrderSendCarRepairManTelephone', "")
        self.WorkOrderMemo = self.kwargs.get('WorkOrderMemo', "")
        self.customCarVIN = self.kwargs.get('customCarVIN', "")
        self.customCarCarLicence = self.kwargs.get('customCarCarLicence', "")
        self.customCustomName = self.kwargs.get('customCustomName', "")
        self.customActionPhone = self.workOrderSendCarRepairManTelephone  # 车主电话
        # self.workOrderWarrantyMoney = self.kwargs.get('workOrderWarrantyMoney',  "")
        # self.workOrderWarrantyPartMoney = self.kwargs.get('workOrderWarrantyPartMoney',  "")
        # self.workOrderWarrantyWorkTimeMoney = self.kwargs.get('workOrderWarrantyWorkTimeMoney',  "")
        self.workOrderCostPartMoney = self.workOrderCostPartsMoney  # 成本零件金额
        self.workOrderCostAllMoney = self.workOrderCostPartsMoney  # 成本总数金额
        self.maintainArray = maintain()  # 工时清单

    def uploadWork(self):

        workInfoJson = {
            "serverCode": self.serverCode,
            "signCode": self.signCode,
            "jsonData": str({
                "workOrderCode": self.workOrderCode,
                "workOrderRepairType": self.workOrderRepairType,
                "workOrderCategoryCode": self.workOrderCategoryCode,
                "workOrderWorkCategoryID": self.workOrderWorkCategoryID,
                "workOrderSettlementOrder": self.workOrderSettlementOrder,
                "workOrderCatetoryList": self.workOrderCatetoryList,
                "workOrderCarMileageKM": self.workOrderCarMileageKM,
                "workOrderRecordedDate": self.workOrderRecordedDate,
                "workOrderBeginFixDate": self.workOrderBeginFixDate,
                "workOrderDeliveryCarDate": self.workOrderDeliveryCarDate,
                "workOrderFinishOverDate": self.workOrderFinishOverDate,
                "workOrderPromiseOverDate": self.workOrderPromiseOverDate,
                "workOrderNextMaintenDate": self.workOrderNextMaintenDate,
                "workOrderAllowanceWorkTimeMoney": self.workOrderAllowanceWorkTimeMoney,
                "workOrderPayableWorkTimeMoney": self.workOrderPayableWorkTimeMoney,
                "workOrderTotalWorkTimeMoney": self.workOrderTotalWorkTimeMoney,
                "workOrderAllowancePartsMoney": self.workOrderAllowancePartsMoney,
                "workOrderPayablePartsMoney": self.workOrderPayablePartsMoney,
                "workOrderTotalPartsMoney": self.workOrderTotalPartsMoney,
                "workOrderCostPartsMoney": self.workOrderCostPartsMoney,
                "workOrderAllowanceCostMoney": self.workOrderAllowanceCostMoney,
                "workOrderPayableCostMoney": self.workOrderPayableCostMoney,
                "workOrderTotalCostMoney": self.workOrderTotalCostMoney,
                "workOrderCostAllMoney": self.workOrderCostAllMoney,
                "workOrderHireEmployeeName": self.workOrderHireEmployeeName,
                "workOrderMaintenanceTechnician": self.workOrderMaintenanceTechnician,
                "msReasonMBreakdownWhy": self.msReasonMBreakdownWhy,
                "msReasonCheckResultWhy": self.msReasonCheckResultWhy,
                "msReasonNextTimeFixSuggest": self.msReasonNextTimeFixSuggest,
                "workOrderSendCarRepairMan": self.workOrderSendCarRepairMan,
                "workOrderSendCarRepairManTelephone": self.workOrderSendCarRepairManTelephone,
                "WorkOrderMemo": self.WorkOrderMemo,
                "customCarVIN": self.customCarVIN,
                "customCarCarLicence": self.customCarCarLicence,
                "customCustomName": self.customCustomName,
                "customActionPhone": self.customActionPhone,
                "workOrderWarrantyMoney": self.workOrderWarrantyMoney,
                "workOrderWarrantyPartMoney": self.workOrderWarrantyPartMoney,
                "workOrderWarrantyWorkTimeMoney": self.workOrderWarrantyWorkTimeMoney,
                "workOrderCostPartMoney": self.workOrderCostPartMoney,
                "partArray": self.partArray,
                "maintainArray": self.maintainArray,
                "balanceArray": self.balanceArray
            })
        }
        # print(workInfoJson)
        # """

        if str(self.signCode) == '6451135' and self.workOrderRepairType in ['航班服务'] or float(self.workOrderTotalCostMoney) <= 0:
            self.log.logger.info('{0}:{1} not updata success...'.format(self.workOrderRecordedDate, self.workOrderCode, ))
            print('{0}:{1} not updata success...'.format(self.workOrderRecordedDate, self.workOrderCode, ))
        else:

            req = requests.post(self.apiUrl, data=workInfoJson)
            rep = req.json()
            if rep.get('showMsg') == '完成处理':
                self.log.logger.info('{0}:{1} updata success...'.format(self.workOrderRecordedDate,self.workOrderCode, ))
                print('{0}:{1} updata success...'.format(self.workOrderRecordedDate,self.workOrderCode, ))
            else:
                self.log.logger.info('{0}:{1} updata error...'.format(self.workOrderRecordedDate,self.workOrderCode, ))
                print('{0}:{1} updata error...'.format(self.workOrderRecordedDate,self.workOrderCode, ))
            # """
