#coding:utf-8
import xlrd
from carinfo import CarInfoClass
from workinfo import WorkInfoClass
from acGui import CarsExportClass
import os
import datetime
from configparser import ConfigParser
from logs import LogClass
import time
from threading import Thread

class importAllEx:
    """导入所有Ex"""

    def __init__(self,carRepairExfile, carSettleExfile, carOutboundExfile, carHousExfile, carsUserExfile):
        self.__carRepairExfile = carRepairExfile
        self.__carSettleExfile = carSettleExfile
        self.__carOutboundExfile = carOutboundExfile
        self.__carHousExfile = carHousExfile
        self.__carsUserExfile = carsUserExfile

        self.__importCarRepair()
        self.__importCarSettle()
        self.__importOutbound()
        self.__importHous()
        self.__importCarsUser()


    def dateFormat(self,sdate):
        """
        日期格式化
        :param sdate:
        :return:
        """
        year = sdate[0:4]
        mon = sdate[4:6]
        day = sdate[6:8]
        ymd = '-'.join([year,mon,day])
        return ymd

    def __importCarRepair(self):
        # 维修查询/委托号为主keys
        carRepairExfile = xlrd.open_workbook(self.__carRepairExfile)
        sheets = carRepairExfile.sheets()
        self.carRepairDict = {}
        n = 0
        for rows in sheets[0].get_rows():
            n += 1
            if n > 1:
                # 分厂[0]
                workOrderCode = str(rows[1].value).split('.')[0]  # 工单单号*
                # 新客户[2]
                customCustomName = rows[3].value  # 车主
                workOrderSendCarRepairMan = rows[4].value  # 送修人
                workOrderSendCarRepairManTelephone = rows[5].value  # 送修人电话
                customCarCarLicence = rows[6].value  # 车辆牌号
                # 车型[7]
                # 车型平台[8]
                customCarVIN = rows[9].value  # 车辆VIN*
                # 车辆本店销售[10]
                workOrderBeginFixDate = self.dateFormat(rows[11].value)  # 进厂日期
                # 进厂时间 [12]
                # 开票日期[13]
                workOrderHireEmployeeName = rows[14].value  # 服务顾问
                workOrderMaintenanceTechnician = rows[15].value # 服务技师
                # 状态[16]
                # 厂牌[17]
                workOrderRecordedDate = self.dateFormat(rows[18].value)  # 结算时间
                # 结算时间[19]
                workOrderTotalCostMoney = rows[20].value  # 总金額
                workOrderAllowanceCostMoney = rows[21].value # 总折扣金额
                # 优惠模式[22]
                workOrderPayableCostMoney = rows[23].value  # 应付总金额*
                workOrderTotalWorkTimeMoney = rows[24].value  # 工时合计金額
                workOrderTotalPartsMoney = rows[25].value  # 零件合计金額
                # 积分换钱[26]
                # 欠账清帐[27]
                # 抹掉金额[28]
                # 款项[29]
                workOrderDeliveryCarDate = self.dateFormat(rows[30].value)   # 交车日期
                # 交车时间[31]
                workOrderPromiseOverDate = self.dateFormat(rows[32].value)   # 预计交车日期
                # 预计交车时间[33]
                # 开单人[34]
                # 审查人[35]
                workOrderCarMileageKM = rows[36].value  # 进厂里程
                # 客户编号[37]
                workOrderCatetoryList = [rows[38].value]  # 自定工单分类名称
                # 回访日期[39]
                # 回访人[40]
                WorkOrderMemo = rows[41].value  # 维修备注
                # 地址[42]
                # 责任人[43]
                msReasonCheckResultWhy = rows[44].value  # 檢測結果
                # 服务站建议[45]
                # 发票号[46]
                # 航班救援[47]
                # 重新开单[48]
                # 索赔坚定[49]
                # 预检单号[50]
                msReasonMBreakdownWhy = rows[51].value  # 故障描述
                # 保险公司[52]
                # 促销关怀活动[53]
                # 索赔类型[54]
                # App状态[55]
                # 救援航班[26
                try:
                    workOrderTotalCostMoney = float(workOrderTotalWorkTimeMoney)+float(workOrderTotalPartsMoney)    # 总金額
                except Exception as e:
                    workOrderTotalCostMoney = 0
                self.carRepairDict.update(
                    {str(workOrderCode): {"workOrderCode": workOrderCode, "customCustomName": customCustomName,
                                          "customCarCarLicence": customCarCarLicence,
                                          "workOrderHireEmployeeName": workOrderHireEmployeeName,
                                          "customCarVIN": customCarVIN, "workOrderBeginFixDate": workOrderBeginFixDate,
                                          "workOrderCatetoryList": workOrderCatetoryList,
                                          "workOrderSendCarRepairMan": workOrderSendCarRepairMan,
                                          "workOrderSendCarRepairManTelephone": workOrderSendCarRepairManTelephone,
                                          "workOrderTotalCostMoney": workOrderTotalCostMoney,
                                          "workOrderRecordedDate": workOrderRecordedDate,
                                          "workOrderCarMileageKM": workOrderCarMileageKM,
                                          "WorkOrderMemo": WorkOrderMemo,"workOrderMaintenanceTechnician": workOrderMaintenanceTechnician,
                                          "workOrderDeliveryCarDate": workOrderDeliveryCarDate, "workOrderPromiseOverDate": workOrderPromiseOverDate,
                                          "msReasonCheckResultWhy": msReasonCheckResultWhy, "msReasonMBreakdownWhy": msReasonMBreakdownWhy}})

    def __importCarSettle(self):
        # 车辆结算明细/对应车辆维修的委托编号
        carSettleExfile = xlrd.open_workbook(self.__carSettleExfile)
        sheets = carSettleExfile.sheets()
        self.carSettleDict = {}
        n = 0
        for rows in sheets[0].get_rows():
            n += 1
            if n > 1:
                workOrderCode = str(rows[0].value).split('.')[0]  # 工单单号*
                #customCustomName = rows[1].value  # 车主
                #customCarCarLicence = rows[2].value  # 车辆牌号
                # 车型[3]
                # 开单日期[4]
                # -workOrderFinishOverDate = self.dateFormat(rows[5].value) #竣工时间
                # 状态[6]
                # 结算方式[7]
                # workOrderTotalCostMoney = rows[8].value  # 总金額
                workOrderPayablePartsMoney = rows[9].value  # 零件應付金額        # 合计-折扣
                # -workOrderTotalPartsMoney = rows[10].value  # 零件合计金額
                workOrderAllowancePartsMoney = rows[11].value  # 零件折扣金額     # 零件列表计算
                workOrderPayableWorkTimeMoney = rows[12].value  # 工時應付金額    # 合计-折扣
                # -workOrderTotalWorkTimeMoney = rows[13].value  # 工时合计金額
                workOrderAllowanceWorkTimeMoney = rows[14].value # 工时折扣金額   # 工时列表计算
                # 救援费[15]
                # 结算日期[16]
                # 结算人[17]
                # 付款方式[18]
                # -workOrderPayableCostMoney = rows[19].value  # 应付总金额*
                # 预付[20]
                # 发票号[21]
                # 厂牌[22]
                # 送修人[23]
                # 手机号[24]
                # 服务顾问[25]
                # 完工审查人[26]
                # 结算工单已打印[27]
                workOrderRepairType = rows[28].value    #维修类别
                # 付款备注[29]
                # 分厂[30]
                # 备注[31]
                try:
                    # -workOrderAllowanceCostMoney = float(workOrderAllowancePartsMoney)+float(workOrderAllowanceWorkTimeMoney)    #总折扣金额
                except Exception as e:
                    workOrderAllowanceCostMoney = 0
                self.carSettleDict.update({workOrderCode:{"workOrderFinishOverDate":workOrderFinishOverDate,
                                                          "workOrderTotalCostMoney":workOrderTotalCostMoney,"workOrderPayablePartsMoney":workOrderPayablePartsMoney,
                                                          "workOrderTotalPartsMoney":workOrderTotalPartsMoney,"workOrderAllowancePartsMoney":workOrderAllowancePartsMoney,
                                                          "workOrderPayableWorkTimeMoney":workOrderPayableWorkTimeMoney,"workOrderTotalWorkTimeMoney":workOrderTotalWorkTimeMoney,
                                                          "workOrderAllowanceWorkTimeMoney":workOrderAllowanceWorkTimeMoney,"workOrderPayableCostMoney":workOrderPayableCostMoney,
                                                          "workOrderRepairType":workOrderRepairType,"workOrderAllowanceCostMoney":workOrderAllowanceCostMoney}})

    def __importOutbound(self):
        # 出库明细/对应车辆维修的委托编号
        carOutboundExfile = xlrd.open_workbook(self.__carOutboundExfile)
        sheets = carOutboundExfile.sheets()
        self.carOutboundList = []
        n = 0
        for rows in sheets[0].get_rows():
            n += 1
            if n > 1:
                workOrderCode = str(rows[0].value).split('.')[0]  # 工单单号*
                # 仓库[1]
                # 车型平台[2]
                itemCode = rows[3].value    #零件代码
                itemName = rows[4].value    #零件名称
                # 单位[5]
                try:
                    itemAmount = int(float(rows[6].value))  #零件数量
                except Exception as e:
                    itemAmount = 0
                itemOneMoney = rows[7].value   #零件单价
                itemMoney = rows[8].value   #零件金额
                #itemDiscountMoney = rows[9].value   #折扣金额
                sepitemMoney = rows[10].value   # 优惠后金额[10]
                itemPickingDate = self.dateFormat(rows[11].value)    #領料日期
                # 结算日期[12]
                # 付清日期[13]
                # 优惠模式[14]
                # 车牌号码[15]
                # 底盘号[16]
                # 批次号[17]
                # 配件自编码[18]
                # 剩余库存[19]
                # 入库价[20]
                itemOneCostMoney = rows[21].value   #零件成本金额
                # 保修价[22]
                # 客户名称[23]
                # 领料员部门[24]
                # 内部领料部门[25]
                # 货位号[26]
                # 供应商[27]
                itemPickingTechnician = rows[28].value  #領料技師
                # 发料员[29]
                # 操作员[30]
                # 服务顾问[31]
                # 收费方式[32]
                # 保修单号[33]
                # 出库类别[34]
                # 备注[35]
                # 退料[36]
                # 常用件[37]
                itemPickingOrder = str(rows[38].value).split('.')[0] if len(str(rows[38].value).split('.'))>0 else "" #領料單號
                # 分厂[39]
                itemOneSellMoney = rows[40].value   #销售单价-指导价
                # 调价比率[41]
                # 车型[42]
                # 批次入库价[43]
                # 安装工时[44]
                # 修理类别[45]
                # 最近供货单位[46]
                # 车主手机[47]
                # 销售合同号[48]
                # 配件大类[49]
                # 适用车型[50]
                # 配件型号[51]
                # 发票号[52]
                # 进站日期[53]
                # 增料[54]
                # 最近入库日期[55]
                # 最近出库日期[56]
                # 周转率[57]
                try:
                    itemDiscountMoney = float(itemMoney)-float(sepitemMoney)     #折扣金额
                except Exception as e:
                    itemDiscountMoney = 0
                try:
                    itemDiscountRate = 1-(float(itemDiscountMoney)/float(itemMoney))
                except Exception as e:
                    itemDiscountRate = 1

                self.carOutboundList.append({"workOrderCode":workOrderCode,"itemCode":itemCode,"itemName":itemName,"itemAmount":itemAmount,"itemOneMoney":itemOneMoney,
                                                       "itemMoney":itemMoney,"itemDiscountMoney":itemDiscountMoney,"itemPickingDate":itemPickingDate,
                                                       "itemOneCostMoney":itemOneCostMoney,"itemPickingTechnician":itemPickingTechnician,
                                                       "itemPickingOrder":itemPickingOrder,"itemDiscountRate":itemDiscountRate,"itemOneSellMoney":itemOneSellMoney})

    def __importHous(self):
        # 项目查询/对应车辆维修的委托编号
        carHousExfile = xlrd.open_workbook(self.__carHousExfile)
        sheets = carHousExfile.sheets()
        self.carHousList = []
        n = 0
        for rows in sheets[0].get_rows():
            n += 1
            if n > 1:
                workOrderCode = str(rows[0].value).split('.')[0]  # 工单单号*
                # 车牌号码[1]
                itemCode = rows[2].value    # 工时代码
                itemName = rows[3].value    # 工时名称
                # 是否增项[4]
                itemStandardWorkTime = rows[5].value    # 標準工時
                # 标准工费[6]
                itemMoney = rows[7].value if rows[7].value else 0  # 工时金额
                speitemMoney = rows[8].value if rows[8].value else 0  # 实收工费[8]
                # 派工工费[9]
                # 附加工费[10]
                itemPayType = rows[11].value    # 工时付款分类
                # 状态[12]
                itemTechnician = rows[13].value # 维修技师
                # 车型[14]
                # 服务顾问[15]
                # 派工日期[16]
                # 派工人[17]
                # 完工日期[18]
                # 审查人[19]
                # 结算日期[20]
                itemOneMoney = rows[21].value if rows[21].value else 0  # 工时单价[21]
                # 备注[22]
                # 车主[23]
                # 手机[24]
                # 地址[25]
                itemType = rows[26].value   #工时维修分类
                # 班组[27]
                # 分厂[28]

                try:
                    itemAmount = float(itemMoney)//float(itemOneMoney)  #工时使用时数
                    itemDiscountMoney = float(itemMoney) - float(speitemMoney)  #折扣金額
                    itemDiscountRate = 1-(itemDiscountMoney/float(itemMoney))  #折扣比率
                except Exception as e:
                    itemAmount = 0
                    itemDiscountMoney = 0
                    itemDiscountRate = 1
                self.carHousList.append({"workOrderCode":workOrderCode,"itemCode":itemCode,"itemName":itemName,"itemStandardWorkTime":itemStandardWorkTime,
                                                         "itemMoney":itemMoney,"itemPayType":itemPayType,"itemTechnician":itemTechnician,
                                                         "itemType":itemType,"itemAmount":itemAmount,"itemDiscountMoney":itemDiscountMoney,
                                                         "itemDiscountRate":itemDiscountRate})

    def __importCarsUser(self):
        # 车辆信息-VIN为唯一/关联车辆维修表
        carsUserExfile = xlrd.open_workbook(self.__carsUserExfile)
        sheets = carsUserExfile.sheets()
        self.carsUserDict = {}
        n = 0
        for rows in sheets[0].get_rows():
            n += 1
            if n > 1:
                # print(rows)
                # 分厂[0]
                # 客户档案号[1]
                customPersonName = rows[2].value    # 客户名称*
                customLicence = rows[3].value       # 客户身份证号
                # 购车单位[4]
                # 客户级别[5]
                carLicence = rows[6].value      # 车辆牌号*
                carSerial = rows[7].value   # 车型平台[7]
                carModel = rows[8].value # 车型[8]
                carVIN = rows[9].value      # 车辆VIN*
                # VSN[10]
                carEngineCode = rows[11].value  # 车辆动机号
                delivererPersonName = rows[12].value    # 使用人名称*
                delivererBaSexID = rows[13].value       # 性别ID

                if delivererBaSexID=='男':
                    delivererBaSexID = 1
                elif delivererBaSexID=='女':
                    delivererBaSexID = 0
                else:
                    delivererBaSexID = 3

                delivererPhone = rows[14].value     # 使用人电话*
                #delivererAddress1 = rows[15].value   # 省
                #delivererAddress2 = rows[16].value   # 市
                #delivererAddress3 = rows[17].value   # 显区
                delivererAddress = rows[18].value   # 使用人地址
                carSaleInvoiceDate = self.dateFormat(rows[19].value) # 发票日销售日
                # 行驶里程[20]
                # 最近来厂日期[21]
                carBrand = rows[22].value  # 厂牌[22]
                carWarrantyDate = self.dateFormat(rows[23].value)    # 车辆保修到期
                # 累计积分[24]
                # 积分余额[25]
                # 内部车[26]
                # 车辆状态[27]
                carSaleManName = rows[28].value     # 销售人员
                # 服务顾问[29]
                carInsuranceCompany = rows[30].value    # 保險公司
                # 险种[31]
                # 上次保养日期[32]
                # 上次保养里程[33]
                carPeriodicMaintenanceDate = self.dateFormat(rows[34].value) # 车辆定保到期
                # 下次保养里程[35]
                # 自动建档日期[36]
                memo = rows[37].value   # 备注
                # 客户爱好[39]
                # 过户车[40]

                customAddress = delivererAddress    #客户地址
                customPhone = delivererPhone # 客户电话
                self.carsUserDict.update({carVIN:{"customPersonName":customPersonName,"customLicence":customLicence,"carLicence":carLicence,
                                             "carVIN":carVIN,"carEngineCode":carEngineCode,"delivererPersonName":delivererPersonName,
                                             "delivererBaSexID":delivererBaSexID,"delivererPhone":delivererPhone,"delivererAddress":delivererAddress,
                                             "carSaleInvoiceDate":carSaleInvoiceDate,"carWarrantyDate":carWarrantyDate,"carSaleManName":carSaleManName,
                                             "carInsuranceCompany":carInsuranceCompany,"carPeriodicMaintenanceDate":carPeriodicMaintenanceDate,"memo":memo,
                                             "customAddress":customAddress,"customPhone":customPhone, "carBrand": carBrand, "carSerial": carSerial,
                                                  "carModel": carModel}})


class GetWorksCarsClass:

    def __init__(self, signCode, apiUrl, carRepairExfile, carSettleExfile,
                 carOutboundExfile, carHousExfile, carsUserExfile):
        self.__signCode = signCode
        self.__apiUrl = apiUrl
        self.__exDb = importAllEx(carRepairExfile=carRepairExfile,
                           carSettleExfile=carSettleExfile,
                           carOutboundExfile=carOutboundExfile,
                           carHousExfile=carHousExfile,
                           carsUserExfile=carsUserExfile)

    def getCarsList(self):
        """
        获取车主列表
        :return:
        """
        cars = self.__exDb.carsUserDict.items()
        # print(cars)
        for k,carsUsers in cars:
            carsUsers.update({'signCode': self.__signCode}) # 增加GBOX门店代码
            carsUsers.update({'apiUrl': self.__apiUrl}) # GBOX 上传URL
            carinfo = CarInfoClass(**carsUsers)
            carinfo.uploadCar()


    def getWorkList(self):
        """
        处理工单列表组合
        :return:
        """
        works = self.__exDb.carRepairDict  # 维修车辆列表，主工单列表
        settles = self.__exDb.carSettleDict  # 车辆结算列表，
        parts = self.__exDb.carOutboundList  # 维修零件列表，
        hours = self.__exDb.carHousList  # 维修项目列表，

        workList = {}       # 工单列表

        for work,workinfo in works.items():
            settle = settles.get(work,None)
            partList = []
            hourList = []
            for part in parts:
                if part.get('workOrderCode') == work:
                    partList.append(part)
            for hour in hours:
                # print("hour:", hour)
                if hour.get('workOrderCode') == work:
                    hourList.append(hour)
            if settle:
                workinfo.update(settle)
            workinfo.update({"partArray":partList,"maintainArray":hourList})
            workinfo.update({'signCode': self.__signCode})  # 增加GBOX门店代码
            workinfo.update({'apiUrl': self.__apiUrl})  # GBOX 上传URL
            workList.update({work:workinfo})
        for keys,works in workList.items():
            workinfoclass = WorkInfoClass(**works)
            workinfoclass.uploadWork()

if __name__ == "__main__":
    signCode = '6451135'
    apiUrl = 'http://121.40.67.196:9090/GBOXData10/action'
    carRepairExfile = ''
    carSettleExfile = ''
    carOutboundExfile = ''
    carHousExfile = ''
    carsUserExfile = ''