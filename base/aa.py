
b = [{'name': '专资总票房', 'en_name': 'zz_revenue', 'source': '流程中填写'},
    {'name': '统计总票房', 'en_name': 'ss_revenue', 'source': '流程中填写'},
    {'name': '净票房', 'en_name': 'net_revenue', 'source': '票房*0.91737864（票房=专资票房？统计票房）'},
    {'name': '非中数净票房', 'en_name': 'chain_revenue', 'source': ''},
    {'name': '中数净票房', 'en_name': 'zy_revenue', 'source': ''},
    {'name': '应到账发行收入', 'en_name': 'act_money', 'source': ''},
    {'name': '实际到账发行收入', 'en_name': 'received_rev/pub_rev', 'source': ''},
    {'name': '未到账发行收入', 'en_name': 'unget_money', 'source': '4-5'},
    {'name': '数字制作费', 'en_name': 'digital_fee', 'source': '业务填写'},
    {'name': '硬盘赔付', 'en_name': 'hardDisk_fee', 'source': '发行平台获取'},
    {'name': '华影代支付费用', 'en_name': 'huaxia_pox_pay', 'source': '汇总子收支项'},
    {'name': '华影所得', 'en_name': 'huaxiaService', 'source': '即发行服务费（华夏提取费用）'},
    {'name': '华影所得1', 'en_name': 'huaxiaService_1', 'source': '即发行服务费（华夏提取费用）'},
    {'name': '华影所得2', 'en_name': 'huaxiaService_2', 'source': '即发行服务费（华夏提取费用）'},
    {'name': '华影所得3', 'en_name': 'huaxiaService_3', 'source': '即发行服务费（华夏提取费用）'},
    {'name': '华影所得4', 'en_name': 'huaxiaService_4', 'source': '即发行服务费（华夏提取费用）'},
    {'name': '华影提取代理费', 'en_name': 'huaxiaAgent', 'source': '即发行服务费（华夏提取费用）'},
    {'name': '应支付协推分账款', 'en_name': 'must_alloc_fund', 'source': ''},
    {'name': '本次应支付协助推广公司分账款', 'en_name': 'allocFund_this', 'source': '13-14'},
    {'name': '本次实际支付协助推广公司分账款', 'en_name': 'allocFund_pay', 'source': '手动输入'},
    {'name': '待下次结算金额', 'en_name': 'allocFund_next', 'source': '15-16'}]


aa = [{'name': '专资总票房', 'en_name': 'zz_revenue', 'source': '流程中填写', 'amount': '117269312678', 'num': 1},
      {'name': '统计总票房', 'en_name': 'stt_revenue', 'source': '流程中填写', 'amount': '115709468666', 'num': 2},
      {'name': '统计总票房','en_name': 'ss_revenue', 'source': '流程中填写', 'amount': '0', 'num': 3},
      {'name': '净票房', 'en_name': 'net_revenue', 'source': '票房*0.91737864（票房=专资票房？统计票房）', 'amount': '107580362578', 'num': 4},
      {'name': '非中数净票房', 'en_name': 'chain_revenue', 'source': '', 'amount': '0', 'num': 5},
      {'name': '中数净票房', 'en_name': 'zy_revenue', 'source': '', 'amount': '107580362578', 'num': 6},
      {'name': '应到账发行收入', 'en_name': 'act_money', 'source': '', 'amount': '0', 'num': 7},
      {'name': '实际到账发行收入', 'en_name': 'received_rev/pub_rev', 'source': '', 'amount': '40686735175', 'num': 8},
      {'name': '未到账发行收入', 'en_name': 'unget_money', 'source': '4-5', 'amount': '0', 'num': 9},
      {'name': '数字制作费', 'en_name': 'digital_fee', 'source': '业务填写', 'amount': '46140000', 'num': 10},
      {'name': '硬盘赔付', 'en_name': 'hardDisk_fee', 'source': '发行平台获取', 'amount': '0', 'num': 11},
      {'name': '数字制作费收入', 'en_name': 'digital_zz_exp_rev', 'source': '收支表', 'amount': '0', 'num': 12},
      {'name': '数字制作费', 'en_name': 'digital_fee', 'source': '汇总收支表', 'amount': '46140000', 'num': 13},
      {'name': '华影代支付费用', 'en_name': 'huaxia_pox_pay', 'source': '汇总子收支项', 'amount': '63084000', 'num': 14},
      {'name': '华影所得', 'en_name': 'huaxiaService', 'source': '即发行服务费（华夏提取费用）', 'amount': '0', 'num': 15},
      {'name': '华影所得1', 'en_name': 'huaxiaService_1', 'source': '即发行服务费（华夏提取费用）', 'amount': '0', 'num': 16},
      {'name': '华影所得2', 'en_name': 'huaxiaService_2', 'source': '即发行服务费（华夏提取费用）', 'amount': '0','num': 17},
      {'name': '华影所得3', 'en_name': 'huaxiaService_3', 'source': '即发行服务费（华夏提取费用）', 'amount': '0', 'num': 18},
      {'name': '华影所得4', 'en_name': 'huaxiaService_4', 'source': '即发行服务费（华夏提取费用）', 'amount': '0', 'num': 19},
      {'name': '华影提取代理费', 'en_name': 'huaxiaAgent', 'source': '即发行服务费（华夏提取费用）', 'amount': '0', 'num': 20},
      {'name': '应支付协推分账款', 'en_name': 'must_alloc_fund', 'source': '', 'amount': '0', 'num': 21},
      {'name': '本次应支付协助推广公司分账款', 'en_name': 'allocFund_this', 'source': '13-14', 'amount': '0', 'num': 22},
      {'name': '本次实际支付协助推广公司分账款', 'en_name': 'allocFund_pay', 'source': '手动输入', 'amount': '0', 'num': 23},
      {'name': '待下次结算金额', 'en_name': 'allocFund_next', 'source': '15-16', 'amount': '0', 'num': 24},
      {'name': '发行收入', 'en_name': 'received_rev/pub_rev', 'source': '收支表', 'amount': '40686735175', 'num': 25},
      {'name': '预收款', 'en_name': 'dep_fund', 'source': '收支表', 'amount': '46140000', 'num': 26},
      {'name': '宣传费', 'en_name': 'hydf/propagate_exp', 'source': '收支表', 'amount': '594067390', 'num': 27},
      {'name': '数字制作费（中国巨幕）', 'en_name': 'szzz_exp/zgjm', 'source': '收支表', 'amount': '16944000', 'num': 28},
      {'name': '差旅费', 'en_name': 'hydf/travel_exp','source': '收支表', 'amount': '3452093', 'num': 29},
      {'name': '业务招待费', 'en_name': 'business_hospitality', 'source': '收支表', 'amount': '158200', 'num': 30},
      {'name': '第一次分账款（已支付）', 'en_name': 'alloc_fund_1', 'source': '收支表', 'amount': '1200000000', 'num': 31},
      {'name': '第二次分账款（已支付）', 'en_name': 'alloc_fund_2', 'source': '收支表', 'amount': '28150000000', 'num': 32}]