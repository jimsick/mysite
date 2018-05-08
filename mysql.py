# alter table gl_fineItem add orgId varchar(50) comment '机构id'
#
#
#
#
# -- 大项表（有或者无细项）
# ALTER TABLE gl_bigItem ADD (
#     `orgId` varchar(50)  COMMENT '机构id',
#     `bigItemId` varchar(50)  COMMENT '套餐id',
#     `bigItemName` varchar(50)  COMMENT '大项名称',
#     `bigItemUnit` varchar(50)  COMMENT '大项单位',
#     `fineItemCode` varchar(50)  COMMENT '关联的细项编码',
#     `bigItemspec` varchar(50)  COMMENT '大项规格',
#     `bigItemBelongDep` varchar(50)  COMMENT '大项所属部门id',
#     `bigItemExamRoom` varchar(50)  COMMENT '大项执行诊间id',
#     `bigItemSex` varchar(50)  COMMENT '大项针对性别',
#     `bigItemPrice` varchar(50)  COMMENT '大项价格',
#     `bigItemDisconut` varchar(50)  COMMENT '大项折扣',
#     `bigItemCost` varchar(50)  COMMENT '大项成本',
#     `salesStartTime` varchar(50)  COMMENT '销售开始时间',
#     `salesEndTime` varchar(50)  COMMENT '销售结束时间',
#     `isSaleAlone` varchar(50)  COMMENT '是否单独销售',
#     `defaultNum` varchar(50)  COMMENT '大项默认数量',
#     `lastupdatetime` varchar(20)  COMMENT '数据最后更新时间'
# );
#
# -- 套餐表(大项的组合)
# ALTER TABLE gl_package ADD (
#     `orgId` varchar(50)  COMMENT '机构id',
#     `packageId` varchar(50)  COMMENT '套餐编号',
#     `packageName` varchar(50)  COMMENT '套餐名称',
#     `packageCost` varchar(50)  COMMENT '套餐成本',
#     `packagePrice` varchar(50)  COMMENT '套餐价格',
#     `packageGroup` varchar(50)  COMMENT '套餐类别',
#     `packageStartDate` varchar(50)  COMMENT '套餐销售开始时间',
#     `packageEndDate` varchar(50)  COMMENT '套餐销售结束时间',
#     `disableState` varchar(50)  COMMENT '上下架状态',
#     `creator` varchar(50)  COMMENT '创建人',
#     `packageBelongDep` varchar(50)  COMMENT '套餐所属部门',
#     `packageMessage` varchar(50)  COMMENT '套餐信息模板',
#     `lastupdatetime` varchar(20)  COMMENT '数据最后更新时间'
# );
#
# -- 诊间管理表
# ALTER TABLE gl_examRomm ADD (
#     `orgId` varchar(50)  COMMENT '机构id',
#     `roomId` varchar(50)  COMMENT '诊间id',
#     `roomShortName` varchar(50)  COMMENT '诊间简称',
#     `roomAllName` varchar(50)  COMMENT '诊间全称',
#     `roomIp` varchar(50)  COMMENT '诊间ip',
#     `lastupdatetime` varchar(20)  COMMENT '数据最后更新时间'
# );
#
# -- 销售政策表
# ALTER TABLE gl_salesPolicy ADD (
#     `orgId` varchar(50)  COMMENT '机构id',
#     `policyId` varchar(50)  COMMENT '政策id',
#     `policyType` varchar(50)  COMMENT '政策类型',
#     `PolicyStartTime` varchar(20)  COMMENT '政策生效时间',
#     `PolicyEndTime` varchar(20)  COMMENT '政策结束时间',
#     `PolicyTitle` varchar(100)  COMMENT '政策标题',
#     `PolicyContent` varchar(500)  COMMENT '政策内容',
#     `PolicyPrice` varchar(20)  COMMENT '政策价格',
#     `hisPrice` varchar(20)  COMMENT '原价格',
#     `coOperatorRes` varchar(500)  COMMENT '合作商业绩核算',
#     `salerRes` varchar(500)  COMMENT '销售人员业绩核算',
#     `otherReward` varchar(500)  COMMENT '其他奖励',
#     `salesAim` varchar(100)  COMMENT '销售目标',
#     `fineItem` varchar(500)  COMMENT '选择曾策所含细项',
#     `otherRemark` varchar(500)  COMMENT '其他备注',
#     `attachmentAddress` varchar(500)  COMMENT '附件地址'
# );
#
# -- 新增产品流程申请表
# ALTER TABLE gl_addProFlow ADD (
#     `orgId` varchar(50)  COMMENT '机构id',
#     `appId` varchar(50)  COMMENT '申请id',
#     `appManId` varchar(50)  COMMENT '申请人id',
#     `appManName` varchar(50)  COMMENT '申请人名称',
#     `appName` varchar(200)  COMMENT '申请名称',
#     `appDate` varchar(100)  COMMENT '申请日期',
#     `appDepId` varchar(100)  COMMENT '申请部门ID',
#     `depManager` varchar(50)  COMMENT '申请部门负责人',
#     `appContent` varchar(500)  COMMENT '申请内容',
#     `proId` varchar(200)  COMMENT '产品id',
#     `proBelongDep` varchar(50)  COMMENT '产品归属部门',
#     `proDes` varchar(500)  COMMENT '产品描述',
#     `proAdvantage` varchar(500)  COMMENT '产品优势',
#     `proSource` varchar(100)  COMMENT '产品来源',
#     `functionDes` varchar(500)  COMMENT '产品功能描述',
#     `salesTarget` varchar(100)  COMMENT '销售目标',
#     `remark` varchar(500)  COMMENT '申请备注',
#     `attachmentAddress` varchar(500)  COMMENT '申请附件地址',
#     `curState` varchar(50)  COMMENT '当前申请流程状态',
#     `curRole` varchar(100)  COMMENT '当前申请流程处在什么角色',
#     `curManager` varchar(100)  COMMENT '当前流程负责处理人',
#     `lastupdatetime` varchar(20)  COMMENT '数据最后更新时间'
# );
#
# -- 新增销售政策流程表
# ALTER TABLE gl_addSalePolicyFlow ADD (
#     `orgId` varchar(50)  COMMENT '机构id',
#     `appId` varchar(100)  COMMENT '申请id',
#     `appManId` varchar(100)  COMMENT '申请人id',
#     `appManName` varchar(100)  COMMENT '申请人名称',
#     `appDepId` varchar(100)  COMMENT '申请部门',
#     `appDate` varchar(20)  COMMENT '申请日期',
#     `depManagerId` varchar(50)  COMMENT '部门负责人ID',
#     `policyId` varchar(50)  COMMENT '政策id',
#     `policyType` varchar(50)  COMMENT '政策类型',
#     `PolicyStartTime` varchar(20)  COMMENT '政策生效时间',
#     `PolicyEndTime` varchar(20)  COMMENT '政策结束时间',
#     `PolicyTitle` varchar(100)  COMMENT '政策标题',
#     `PolicyContent` varchar(500)  COMMENT '政策内容',
#     `PolicyPrice` varchar(20)  COMMENT '政策价格',
#     `hisPrice` varchar(20)  COMMENT '原价格',
#     `coOperatorRes` varchar(500)  COMMENT '合作商业绩核算',
#     `salerRes` varchar(500)  COMMENT '销售人员业绩核算',
#     `otherReward` varchar(500)  COMMENT '其他奖励',
#     `salesAim` varchar(100)  COMMENT '销售目标',
#     `fineItem` varchar(500)  COMMENT '选择曾策所含细项',
#     `otherRemark` varchar(500)  COMMENT '其他备注',
#     `attachmentAddress` varchar(500)  COMMENT '附件地址',
#     `curState` varchar(50)  COMMENT '当前申请流程状态',
#     `curRole` varchar(100)  COMMENT '当前申请流程处在什么角色',
#     `curManager` varchar(100)  COMMENT '当前流程负责处理人',
#     `lastupdatetime` varchar(20)  COMMENT '数据最后更新时间'
# );
#
# -- 新增客户申请流程表
# ALTER TABLE gl_addCusFlow ADD (
#     `orgId` varchar(100)  COMMENT '机构id',
#     `cusCardId` varchar(100)  COMMENT '客户/id 会员卡号',
#     `cusName` varchar(100)  COMMENT '客户姓名',
#     `cusSex` varchar(10)  COMMENT '性别',
#     `cusAge` varchar(10)  COMMENT '年龄',
#     `cusBirthDate` varchar(20)  COMMENT '出生年月',
#     `cusidCard` varchar(20)  COMMENT '身份证号码',
#     `cusMobile` varchar(11)  COMMENT '手机号码',
#     `cusqqCode` varchar(50)  COMMENT 'QQ号',
#     `cusweixinCode` varchar(100)  COMMENT '微信号',
#     `cusWeight` varchar(10)  COMMENT '体重',
#     `cusHeight` varchar(10)  COMMENT '身高',
#     `cusEmail` varchar(100)  COMMENT '电子邮箱',
#     `cusPosition` varchar(100)  COMMENT '职业',
#     `cusAddress` varchar(300)  COMMENT '家庭住址',
#     `cusEmerContact` varchar(11)  COMMENT '紧急联系人/联系方式',
#     `cusBelongStore` varchar(100)  COMMENT '所属店家',
#     `cusBelongTeacher` varchar(100)  COMMENT '所属导师',
#     `cusStoreAddress` varchar(300)  COMMENT '店家地址',
#     `cusCusSource` varchar(50)  COMMENT '客户来源',
#     `cusMariStatus` varchar(10)  COMMENT '婚姻状况',
#     `cusMarRelationship` varchar(20)  COMMENT '夫妻关系',
#     `cusEduDegree` varchar(20)  COMMENT '文化程度',
#     `cusMedicalHistory` varchar(500)  COMMENT '既往病史或家族病史、症状',
#     `cusMedicalTreatment` varchar(500)  COMMENT '既往就诊情况/有无禁用的药物',
#     `cusConSumerPrefer` varchar(50)  COMMENT '消费喜好',
#     `cusSuitableConsumer` varchar(50)  COMMENT '适合哪种消费方式',
#     `cusPurchaseFactor` varchar(50)  COMMENT '产生购买的因素',
#     `cusLivConditions` varchar(50)  COMMENT '居住条件及产业',
#     `cusCarInformation` varchar(50)  COMMENT '车辆信息',
#     `cusWorkUnit` varchar(300)  COMMENT '工作单位',
#     `cusTopConsumption` varchar(300)  COMMENT '最高消费及项目',
#     `cusConsumerType` varchar(100)  COMMENT '消费类型',
#     `cusConsumHabit` varchar(100)  COMMENT '消费习惯',
#     `cusMemberActivities` varchar(100)  COMMENT '会员活动',
#     `cusCapitalType` varchar(100)  COMMENT '资金类型',
#     `cusOwnLuxury` varchar(100)  COMMENT '拥有的奢侈品',
#     `cusExpAnnualIncome` varchar(50)  COMMENT '预计年收入',
#     `cusExpAnnualConsumption` varchar(50)  COMMENT '预计年消费',
#     `cusConsumpAmount` varchar(50)  COMMENT '累计消费金额',
#     `cusAccountBalance` varchar(50)  COMMENT '账户余额',
#     `cusHisConsumption` varchar(500)  COMMENT '历史消费记录',
#     `cusRemainderItem` varchar(500)  COMMENT '剩余操作项目',
#     `cusCustomerKinship` varchar(300)  COMMENT '客户亲属关系',
#     `curState` varchar(50)  COMMENT '当前申请流程状态',
#     `curRole` varchar(100)  COMMENT '当前申请流程处在什么角色',
#     `curManager` varchar(100)  COMMENT '当前流程负责处理人',
#     `lastupdatetime` varchar(20)  COMMENT '数据最后更新时间'
# );