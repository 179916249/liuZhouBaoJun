#coding:utf-8
"""处理单张工单信息"""


from bs4 import BeautifulSoup
from logg import LogClass
import logging

workInfoLog = LogClass('workInfo.log', 'workInfo')
workInfoLog.logger.setLevel(logging.ERROR)
workInfoLog.fh.setLevel(logging.ERROR)

class WorkInfoClass():
    """处理单张工单信息类"""
    workOrderCode = ""                      #工单单号*
    workOrderCategoryCode = ""              #主要工单分类代码
    workOrderWorkCategoryID = "1"           #主要工单分类ID   默认值1
    workOrderSettlementOrder = ""           #预约单号
    workOrderCatetoryList = []              #自定工单分类名称（数组）*
    workOrderCarMileageKM = ""              #进厂里程*
    workOrderRecordedDate = ""              #结算时间*
    workOrderBeginFixDate = ""              #来厂时间*
    workOrderDeliveryCarDate = ""           #交车时间
    workOrderFinishOverDate = ""            #竣工时间
    workOrderPromiseOverDate = ""           #预计交车时间
    workOrderNextMaintenDate = ""           #下次保养时间
    workOrderAllowanceWorkTimeMoney = "0"    #工时折扣金額
    workOrderPayableWorkTimeMoney = "0"      #工時應付金額
    workOrderTotalWorkTimeMoney = "0"        #工时合计金額
    workOrderAllowancePartsMoney = "0"       #零件折扣金額
    workOrderPayablePartsMoney = "0"         #零件應付金額
    workOrderTotalPartsMoney = "0"           #零件合计金額
    workOrderCostPartsMoney = "0"            #零件成本金額
    workOrderAllowanceCostMoney = "0"        #总折扣金额
    workOrderPayableCostMoney = "0"          #应付总金额
    workOrderTotalCostMoney = "0"            #总金額
    workOrderCostAllMoney = "0"              #成本总数金额
    workOrderHireEmployeeName = ""          #服务顾问
    workOrderMaintenanceTechnician = ""     #维修技师
    msReasonMBreakdownWhy = ""              #故障描述
    msReasonCheckResultWhy = ""             #檢測結果
    msReasonNextTimeFixSuggest = ""         #下次維修建議
    workOrderSendCarRepairMan = ""          #送修人
    workOrderSendCarRepairManTelephone = "" #送修人电话
    WorkOrderMemo = ""                      #维修备注
    customCarVIN = ""                       #车辆VIN*
    customCarCarLicence = ""                #车辆牌号
    customCustomName = ""                   #车主
    customActionPhone = ""                  #车主电话
    workOrderWarrantyMoney = "0"             #索赔金額
    workOrderWarrantyPartMoney = "0"         #索赔零件金額
    workOrderWarrantyWorkTimeMoney = "0"     #索赔工时金額
    workOrderCostPartMoney = ""             #成本零件金额
    partArray = []                          #零件清单
    maintainArray = []                      #工时清单
    balanceArray = []                       #对表数据 可以传空



    def __init__(self):
        """
        """


        self.start()

    def start(self):
        pass



    @property
    def getworkOrderCode(self):
        """
        获取工单号
        :return:
        """
        return self.workOrderCode

    @property
    def getworkOrderCategoryCode(self):
        """
        主要工单分类代码
        :return:
        """
        return ''

    @property
    def getworkOrderWorkCategoryID(self):
        """
        主要工单分类ID 默认值1
        :return:
        """
        return self.workOrderWorkCategoryID

    @property
    def getworkOrderSettlementOrder(self):
        """
        预约单号
        :return:
        """
        return ''

    @property
    def getworkOrderCatetoryList(self):
        """
        自定工单分类名称 数组
        :return:
        """
        return [self.workOrderCatetoryList]

    @property
    def getworkOrderCarMileageKM(self):
        """
        进厂里程
        :return:
        """
        return self.workOrderCarMileageKM

    @property
    def getworkOrderRecordedDate(self):
        """
        结算时间
        :return:
        """
        return self.workOrderRecordedDate

    @property
    def getworkOrderBeginFixDate(self):
        """
        来厂时间
        :return:
        """
        return self.workOrderBeginFixDate

    @property
    def getworkOrderDeliveryCarDate(self):
        """
        交车时间
        :return:
        """
        return self.workOrderDeliveryCarDate

    @property
    def getworkOrderFinishOverDate(self):
        """
        竣工时间
        :return:
        """
        return self.workOrderPromiseOverDate

    @property
    def getworkOrderPromiseOverDate(self):
        """
        预计交车时间
        :return:
        """
        return ''

    @property
    def getworkOrderNextMaintenDate(self):
        """
        下次保养时间
        :return:
        """
        return ''

    @property
    def getworkOrderAllowanceWorkTimeMoney(self):
        """
        工时折扣金額
        :return:
        """
        return self.workOrderAllowanceWorkTimeMoney

    @property
    def getworkOrderPayableWorkTimeMoney(self):
        """
        工時應付金額
        :return:
        """
        return self.workOrderPayableWorkTimeMoney

    @property
    def getworkOrderTotalWorkTimeMoney(self):
        """
        工时合计金額
        :return:
        """
        return self.workOrderTotalWorkTimeMoney
    @property
    def getworkOrderAllowancePartsMoney(self):
        """
        零件折扣金額
        :return:
        """
        return self.workOrderAllowancePartsMoney
    @property
    def getworkOrderPayablePartsMoney(self):
        """
        零件應付金額
        :return:
        """
        return self.workOrderPayablePartsMoney
    @property
    def getworkOrderTotalPartsMoney(self):
        """
        零件合计金額
        :return:
        """
        return self.workOrderTotalPartsMoney

    @property
    def getworkOrderCostPartsMoney(self):
        """
        零件成本金額
        :return:
        """
        return ''
    @property
    def getworkOrderAllowanceCostMoney(self):
        """
        总折扣金额
        :return:
        """
        workOrderAllowanceCostMoney = str(
            float(self.workOrderAllowancePartsMoney) + float(self.workOrderAllowanceWorkTimeMoney))  # 总折扣金额
        return workOrderAllowanceCostMoney
    @property
    def getworkOrderPayableCostMoney(self):
        """
        应付总金额
        :return:
        """
        workOrderPayableCostMoney = str(
            float(self.workOrderPayablePartsMoney) + float(self.workOrderPayableWorkTimeMoney))  # 应付总金额
        return workOrderPayableCostMoney
    @property
    def getworkOrderTotalCostMoney(self):
        """
        总金額
        :return:
        """
        workOrderTotalCostMoney = str(
            float(self.workOrderTotalPartsMoney) + float(self.workOrderTotalWorkTimeMoney))  # 总金額
        return workOrderTotalCostMoney

    @property
    def getworkOrderCostAllMoney(self):
        """
        成本总数金额
        :return:
        """
        return ''

    @property
    def getworkOrderHireEmployeeName(self):
        """
        服务顾问
        :return:
        """
        return self.workOrderHireEmployeeName

    @property
    def getworkOrderMaintenanceTechnician(self):
        """
        维修技师
        :return:
        """
        return self.workOrderMaintenanceTechnician

    @property
    def getmsReasonMBreakdownWhy(self):
        """
        故障描述
        :return:
        """
        try:
            td = self.maintenance2.findAll(name='td', text='进厂原因')[0]
            msReasonMBreakdownWhy = str(td.parent.select('td')[1].text)  # 故障描述
            return msReasonMBreakdownWhy
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 故障描述获取失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getmsReasonCheckResultWhy(self):
        """
        檢測結果
        :return:
        """
        return ''

    @property
    def getmsReasonNextTimeFixSuggest(self):
        """
        下次維修建議
        :return:
        """
        return ''

    @property
    def getworkOrderSendCarRepairMan(self):
        """
        送修人
        :return:
        """
        try:
            td = self.maintenance2.findAll(name='td', text='电访对象')[0]
            workOrderSendCarRepairMan = str(td.parent.select('td')[5].text)  # 送修人
            return workOrderSendCarRepairMan
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 送修人获取失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getworkOrderSendCarRepairManTelephone(self):
        """
        送修人电话
        :return:
        """
        try:
            td = self.maintenance2.findAll(name='td', text='电访手机')[0]
            workOrderSendCarRepairManTelephone = str(td.parent.select('td')[5].text)  # 送修人电话
            return workOrderSendCarRepairManTelephone
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 送修人电话获取失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getWorkOrderMemo(self):
        """
        维修备注
        :return:
        """
        try:
            td = self.maintenance2.findAll(name='td', text='工单备注')[0]
            WorkOrderMemo = str(td.parent.select('td')[1].text)  # 维修备注
            return WorkOrderMemo
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 维修备注获取失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getcustomCarVIN(self):
        """
        车辆VIN
        :return:
        """
        return self.vin

    @property
    def getcustomCarCarLicence(self):
        """
        车辆牌号
        :return:
        """
        return self.customCarCarLicence

    @property
    def getcustomCustomName(self):
        """
        车主
        :return:
        """
        try:
            td = self.maintenance2.findAll(name='td', text='委修客户名称')[0]
            customCustomName = str(td.parent.select('td')[1].text).strip().split()[1]  # 车主
            return customCustomName
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 车主获取失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getcustomActionPhone(self):
        """
        车主电话
        :return:
        """
        try:
            td = self.maintenance2.findAll(name='td', text='移动电话一')[0]
            customActionPhone = str(td.parent.select('td')[5].text)  # 车主电话
            return customActionPhone
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 车主电话获取失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getworkOrderWarrantyMoney(self):
        """
        索赔金額
        :return:
        """
        return ''

    @property
    def getworkOrderWarrantyPartMoney(self):
        """
        索赔零件金額
        :return:
        """
        return ''

    @property
    def getworkOrderWarrantyWorkTimeMoney(self):
        """
        索赔工时金額
        :return:
        """
        return ''

    @property
    def getworkOrderCostPartMoney(self):
        """
        成本零件金额
        :return:
        """
        return ''
    @property
    def getpartArray(self):
        """
        零件清单 (数组)
        :return:
        """
        partArray = []
        workOrderAllowancePartsMoneyList = []  # 零件折扣金額s
        workOrderPayablePartsMoneyList = []  # 零件應付金額s
        workOrderTotalPartsMoneyList = []  # 零件合计金額s
        try:
            workParts = self.HoursProject.select('table[id="MRP009_3_TP2"]')[0]
            workPartsList = workParts.select('tr')
            for i in workPartsList[1::]:
                try:
                    span = i.select('span')
                    itemCodeitemName = span[2].select('input')
                except Exception as e:
                    self.log.logger.error((e,'{0} {1} 零件清单获取失败...'.format(self.stime,self.workId)))
                    continue
                try:
                    itemCode = str(itemCodeitemName[0].get('value'))
                except Exception as e:
                    itemCode = ""
                    self.log.logger.error((e,'{0} {1} 零件代号获取失败...'.format(self.stime,self.workId)))
                try:
                    itemName = str(itemCodeitemName[1].get('value'))
                except Exception as e:
                    itemName = ""
                    self.log.logger.error((e,'{0} {1} 零件名称获取失败...'.format(self.stime,self.workId)))
                try:
                    itemAmount = str(span[4].text)
                    s = span[2:4]
                except Exception as e:
                    itemAmount = ""
                    self.log.logger.error((e,'{0} {1} 零件数量获取失败...'.format(self.stime,self.workId)))
                try:
                    itemMoney = str(span[11].text)
                except Exception as e:
                    itemMoney = ""
                    self.log.logger.error((e,'{0} {1} 零件金额获取失败...'.format(self.stime,self.workId)))
                try:
                    itemOneMoney = str(span[6].text)
                except Exception as e:
                    itemOneMoney = ""
                    self.log.logger.error((e,'{0} {1} 零件单价获取失败...'.format(self.stime,self.workId)))
                try:
                    workOrderAllowancePartsMoneyList.append(float(span[10].text))  # 零件折扣金額
                except Exception as e:
                    workOrderAllowancePartsMoneyList.append(0)  # 零件折扣金額
                    self.log.logger.error((e,'{0} {1} 零件折扣金額获取失败...'.format(self.stime,self.workId)))
                try:
                    workOrderPayablePartsMoneyList.append(float(span[11].text))  # 零件應付金額
                except Exception as e:
                    workOrderPayablePartsMoneyList.append(0)  # 零件應付金額
                    self.log.logger.error((e,'{0} {1} 零件應付金額获取失败...'.format(self.stime,self.workId)))
                try:
                    workOrderTotalPartsMoneyList.append(float(span[7].text))  # 零件合计金額
                except Exception as e:
                    workOrderTotalPartsMoneyList.append(0)  # 零件應付金額
                    self.log.logger.error((e,'{0} {1} 零件合计金額获取失败...'.format(self.stime,self.workId)))

                parts = {
                    "itemCode": itemCode,  # 零件代码
                    "itemName": itemName,  # 零件名称
                    "itemAmount": itemAmount,  # 零件数量
                    "itemMoney": itemMoney,  # 零件金额
                    "itemOneMoney": itemOneMoney,  # 零件单价
                    "itemOneCostMoney": "",  # 零件成本金额(icare)
                    "itemType": "",  # 零件维修分类
                    "itemPayType": "",  # 零件付款分类
                    "itemWorkCategoryID": ""  # GBOX维修分类ID
                }
                partArray.append(parts)
            self.workOrderAllowancePartsMoney = str(sum(workOrderAllowancePartsMoneyList))  # 零件折扣金額
            if not self.workOrderAllowancePartsMoney:
                self.workOrderAllowancePartsMoney = 0
            self.workOrderPayablePartsMoney = str(sum(workOrderPayablePartsMoneyList))  # 零件應付金額
            if not self.workOrderPayablePartsMoney:
                self.workOrderPayablePartsMoney = 0
            self.workOrderTotalPartsMoney = str(sum(workOrderTotalPartsMoneyList))  # 零件合计金額
            if not self.workOrderTotalPartsMoney:
                self.workOrderTotalPartsMoney = 0

            return partArray
        except Exception as e:
            self.log.logger.error((e,'{0} {1} 工时代码跟名字获取失败...'.format(self.stime,self.workId)))
            return False

    @property
    def getmaintainArray(self):
        """
        工时清单（数组）
        :return:
        """
        maintainArray = []
        workOrderPayableWorkTimeMoneyList = []
        workOrderAllowanceWorkTimeMoneyList = []
        workOrderTotalWorkTimeMoneyList = []
        try:
            workHours = self.HoursProject.select('table[id="MRP009_3_TP1"]')[0]
            workHoursList = workHours.select('tr')
            for i in workHoursList[1::]:
                span = i.select('span')
                try:
                    itemCodeitemName = span[3].select('input')
                except Exception as e:
                    itemCodeitemName = ""
                    self.log.logger.error((e,'{0} {1} 工时代码跟名字获取失败...'.format(self.stime,self.workId)))
                try:
                    itemCode = str(itemCodeitemName[0].get('value'))
                except Exception as e:
                    itemCode = ""
                    self.log.logger.error((e,'{0} {1} 工时代码获取失败...'.format(self.stime,self.workId)))
                try:
                    itemName = str(itemCodeitemName[1].get('value'))
                except Exception as e:
                    itemName = ""
                    self.log.logger.error((e,'{0} {1} 工时名字获取失败...'.format(self.stime,self.workId)))
                try:
                    itemMoney = str(span[11].text)
                except Exception as e:
                    itemMoney = 0
                    self.log.logger.error((e,'{0} {1} 工时金额获取失败...'.format(self.stime,self.workId)))
                try:
                    itemType = str(span[1].text)

                except Exception as e:
                    itemType = ""
                    self.log.logger.error((e,'{0} {1} 工时维修分类获取失败...'.format(self.stime,self.workId)))
                try:
                    itemAmount = span[4].font.text
                except Exception as e:
                    itemAmount = ""
                    self.log.logger.error((e, '{0} {1} 工时数量获取失败...'.format(self.stime, self.workId)))
                try:
                    itemTechnician = str(span[12].text).split()[1]
                except Exception as e:
                    itemTechnician = ""
                    self.log.logger.error((e,'{0} {1} 维修技师获取失败...'.format(self.stime,self.workId)))
                try:
                    itemDiscountRate = str(span[8].text)
                except Exception as e:
                    itemDiscountRate = ""
                    self.log.logger.error((e,'{0} {1} 工时折扣比率获取失败...'.format(self.stime,self.workId)))
                hours = {
                    "itemCode": itemCode,  # 工时代码
                    "itemName": itemName,  # 工时名称
                    'itemAmount': itemAmount,  # 工时使用时数
                    "itemMoney": itemMoney,  # 工时金额
                    "itemType": itemType,  # 工时维修分类
                    "itemPayType": "",  # 工时付款分类
                    "itemWorkCategoryID": "",  # GBOX维修分类ID
                    "itemTechnician": itemTechnician,  # 维修技师
                    "itemDiscountRate": itemDiscountRate,  # 折扣比率
                    "itemDiscountMoney": "",  # 折扣金額
                }
                maintainArray.append(hours)
                try:
                    workOrderPayableWorkTimeMoneyList.append(float(span[11].text))
                except Exception as e:
                    workOrderPayableWorkTimeMoneyList.append(0)
                    self.log.logger.error((e,'{0} {1} 工時應付金額获取失败...'.format(self.stime,self.workId)))
                try:
                    workOrderAllowanceWorkTimeMoneyList.append(float(span[10].text))
                except Exception as e:
                    workOrderAllowanceWorkTimeMoneyList.append(0)
                    self.log.logger.error((e,'{0} {1} 工时折扣金額获取失败...'.format(self.stime,self.workId)))
                try:
                    workOrderTotalWorkTimeMoneyList.append(float(span[7].text))
                except Exception as e:
                    workOrderTotalWorkTimeMoneyList.append(0)
                    self.log.logger.error((e,'{0} {1} 工时合计金額获取失败...'.format(self.stime,self.workId)))
            self.workOrderPayableWorkTimeMoney = str(sum(workOrderPayableWorkTimeMoneyList))    #工時應付金額
            if not self.workOrderPayableWorkTimeMoney:
                self.workOrderPayableWorkTimeMoney = 0
            self.workOrderAllowanceWorkTimeMoney = str(sum(workOrderAllowanceWorkTimeMoneyList))        #工时折扣金額
            if not self.workOrderAllowanceWorkTimeMoney:
                self.workOrderAllowanceWorkTimeMoney = 0
            self.workOrderTotalWorkTimeMoney = str(sum(workOrderTotalWorkTimeMoneyList))            #工时合计金額
            if not self.workOrderTotalWorkTimeMoney:
                self.workOrderTotalWorkTimeMoney = 0
            return maintainArray
        except Exception as e:
            self.log.logger.error((e,'{0} {1} 没有工时清单...'.format(self.stime,self.workId)))
            return maintainArray

    @property
    def getbalanceArray(self):
        """
        对表数据 可以传空
        :return:
        """
        return ''
    @property
    def getcarEngineCode(self):
        """
        车辆动机号
        :return:
        """
        try:
            td = self.maintenance2.findAll(name='td', text='发动机号码')[0]
            carEngineCode = str(td.parent.select('td')[5].text)  # 车辆动机号
            return carEngineCode
        except Exception as e:
            self.log.logger.error((e,'{0} {1} 发动机号码获取失败...'.format(self.stime,self.workId)))
            return ''



