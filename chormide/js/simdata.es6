function diffdata(n) {
  
  datas = [];

  for( var i=0; i<n; i++) {
    
    c1 = Math.round( (Math.random()+0.2)*20 );
    c2 = c1+Math.round( (Math.random()-0.5)*3 );

    cd = c1 - c2;

    r1 = Math.round( c1*(Math.random()+0.4)*100 );
    r2 = Math.round( c2*(Math.random()+0.2)*100 );

    rd = r1 - r2;

    p1 = Math.round( r1*(Math.random()+0.6)*4000 );
    p2 = Math.round( r2*(Math.random()+0.2)*4000 );

    pd = p1 - p2;

    datas.push( {
      'moviecode': '001100582017',
      'movie': '疯岳撬佳人',
      'chain': '太平洋',
      'cinemacode': '51020802',
      'cinema': '安县安州影剧院',
      'device': '自购',
      'c1': c1,
      'c2': c2,
      'cd': cd,
      'r1': r1,
      'r2': r2,
      'rd': rd,
      'p1': p1,
      'p2': p2,
      'pd': pd,
    } )
  }
  
  return datas;
}


diffcols =  [
    {'display':"排次号", "key":"moviecode", 'w':100, 'align':'center', 'type':'str'},
    {'display':"影片", "key":"movie", 'w':80, 'align':'left', 'type':'str' },
    {'display':"院线", "key":"chain", 'w':80, 'align':'center', 'type':'str' },
    {'display':"影院\n编码", "key":"cinemacode", 'w':80, 'align':'center', 'type':'str' },
    {'display':"影院\n名称", "key":"cinema", 'w':120, 'align':'left', 'type':'str' },
    {'display':"设备", "key":"device", 'w':50, 'align':'center', 'type':'str' },
    {'display':"月报\n场数", "key":"c1", 'w':60, 'align':'right', 'type':'int' },
    {'display':"日报\n场数", "key":"c2", 'w':60, 'align':'right', 'type':'int' },
    {'display':"差额", "key":"cd", 'w':60, 'align':'right', 'type':'int', 'watch':i=>(i<0) },
    {'display':"月报\n人数", "key":"r1", 'w':60, 'align':'right', 'type':'int' },
    {'display':"日报\n人数", "key":"r2", 'w':60, 'align':'right', 'type':'int' },
    {'display':"差额", "key":"rd", 'w':60, 'align':'right', 'type':'int', 'watch':i=>(i<0) },
    {'display':"月报\n票房", "key":"p1", 'w':80, 'align':'right', 'type':'money' },
    {'display':"日报\n票房", "key":"p2", 'w':80, 'align':'right', 'type':'money' },
    {'display':"差额", "key":"pd", 'w':80, 'align':'right', 'type':'money', 'watch':i=>(i<0) },
];


function bodata(n) {
  
  datas = [];

  for( let i=43832; i<=43880; i++ ){
    
    p1 = Math.round( (Math.random()+10)*40000 );
    p2 = Math.round( (Math.random()+10)*40000 );
    p3 = Math.round( (Math.random()+10)*80000 );
    p4 = Math.round( (Math.random()+10)*80000 );
    p5 = Math.round( (Math.random()+10)*40000 );
    p6 = Math.round( (Math.random()+10)*40000 );
    p7 = Math.round( (Math.random()+10)*40000 );
    p8 = Math.round( (Math.random()+10)*40000 );

    pA = Math.round( (Math.random()+10)*40000 );
    pB = Math.round( (Math.random()+10)*40000 );

    pd12 = p1 - p2;
    pd34 = p3 - p4;
    pd56 = p5 - p6;
    pd78 = p7 - p8;
    
    pdAB = pA - pB;
    
    datas.push( {
      'p1': p1,
      'p2': p2,
      'p3': p3,
      'p4': p4,
      'p5': p5,
      'p6': p6,
      'p7': p7,
      'p8': p8,
      'pd12': pd12,
      'pd34': pd34,
      'pd56': pd56,
      'pd78': pd78,
      'pA': pA,
      'pB': pB,
      'pdAB': pdAB,
      'chainid' : i,
    } )
  }
  
  return datas;
}

bocols = [
    {'display':"累计月报\n自购票房", "key":"p1", 'w':80, 'align':'right', 'type':'money' },
    {'display':"累计日报\n自购票房", "key":"p2", 'w':80, 'align':'right', 'type':'money' },
    {'display':"差额", "key":"pd12", 'w':80, 'align':'right', 'type':'money' },
    {'display':"累计月报\n租赁票房", "key":"pA", 'w':80, 'align':'right', 'type':'money' },
    {'display':"累计日报\n租赁票房", "key":"pB", 'w':80, 'align':'right', 'type':'money' },
    {'display':"差额", "key":"pdAB", 'w':80, 'align':'right', 'type':'money' },
    {'display':"累计月报\n全部票房", "key":"p3", 'w':80, 'align':'right', 'type':'money' },
    {'display':"累计专资\n全部票房", "key":"p4", 'w':80, 'align':'right', 'type':'money' },
    {'display':"差额", "key":"pd34", 'w':80, 'align':'right', 'type':'money' },
    {'display':"累计月度\n结算票房", "key":"p4", 'w':80, 'align':'right', 'type':'money' },
    {'display':"差额", "key":"pd34", 'w':80, 'align':'right', 'type':'money', 'line':'#ffaacc' },
    {'display':"当月月报\n上报票房", "key":"p5", 'w':80, 'align':'right', 'type':'money' },
    {'display':"当月日报\n上报票房", "key":"p6", 'w':80, 'align':'right', 'type':'money' },
    {'display':"差额", "key":"pd56", 'w':80, 'align':'right', 'type':'money' },
    {'display':"当月月度\n结算票房", "key":"p7", 'w':80, 'align':'right', 'type':'money' },
    {'display':"差额", "key":"pd78", 'w':80, 'align':'right', 'type':'money' },
];

scheduleformat = {
     'chain_day': [
       {'key':'upload','show':'circle'},
       {'key':'diff','show':'triangle'},
       {'key':'publish','show':'square'},
     ],
     'chain_month': [
       {'key':'upload','show':'circle'},
       {'key':'diff','show':'triangle'},
       {'key':'diff2','show':'triangle'},
       {'key':'publish','show':'square'},
     ],
     'zhongying_day': [
       {'key':'upload','show':'circle'},
       {'key':'publish','show':'square'},
     ],
     'zhongying_month': [
       {'key':'upload','show':'circle'},
       {'key':'diff','show':'triangle'},
       {'key':'publish','show':'square'},
     ],
      
    };

function gettaskinfo( ft, d, ms ) {
  
  var r = {}
  
  if ( ft == 'zhongying_month' || ft == 'zhongying_day' ) {
    r = {'upload':0, 'diff':0, 'publish':0};
    if ( Math.random() < 0.99 ) {
      r['upload'] = ( Math.random() < 0.99 )?1:2;
      if ( Math.random() < 0.99 ) {
        r['diff'] = ( Math.random() < 0.99 )?1:2;
        r['diff2'] = ( Math.random() < 0.99 )?1:2;
        if ( Math.random() < 0.95 ) {
          r['publish'] = ( Math.random() < 0.95 )?1:2;
        }
      }
    }
    
    return r;
  }
  
  for( let i=43832; i<=43880; i++ ){
    r[i] = {'upload':0, 'diff':0, 'publish':0};
    if ( Math.random() < 0.99 ) {
      r[i]['upload'] = ( Math.random() < 0.99 )?1:2;
      if ( Math.random() < 0.99 ) {
        r[i]['diff'] = ( Math.random() < 0.99 )?1:2;
        r[i]['diff2'] = ( Math.random() < 0.99 )?1:2;
        if ( Math.random() < 0.95 ) {
          r[i]['publish'] = ( Math.random() < 0.95 )?1:2;
        }
      }
    }
  }
  console.log('gettaskinfo', d, r);
  return new Promise((resolve, reject) => {
    setTimeout(()=>resolve(r), ms, 'done');
  });
}


chainrows = [{'chain': '万达', 'chainid': 43832, 'star': false, 'zone': 1},
 {'chain': '上海大光明', 'chainid': 43833, 'star': false, 'zone': 2},
 {'chain': '上海弘歌', 'chainid': 43834, 'star': false, 'zone': 1},
 {'chain': '上海联和', 'chainid': 43835, 'star': false, 'zone': 2},
 {'chain': '世纪环球', 'chainid': 43836, 'star': false, 'zone': 1},
 {'chain': '中广国际', 'chainid': 43837, 'star': false, 'zone': 2},
 {'chain': '中影数字', 'chainid': 43838, 'star': true, 'zone': 1},
 {'chain': '中影星美', 'chainid': 43839, 'star': false, 'zone': 2},
 {'chain': '九州中原', 'chainid': 43840, 'star': false, 'zone': 1},
 {'chain': '内蒙民族', 'chainid': 43841, 'star': false, 'zone': 2},
 {'chain': '北京世茂', 'chainid': 43842, 'star': false, 'zone': 1},
 {'chain': '北京新影联', 'chainid': 43843, 'star': false, 'zone': 2},
 {'chain': '北京红鲤鱼', 'chainid': 43844, 'star': false, 'zone': 1},
 {'chain': '华夏大地', 'chainid': 43845, 'star': true, 'zone': 2},
 {'chain': '华夏星火', 'chainid': 43846, 'star': false, 'zone': 1},
 {'chain': '华夏联合', 'chainid': 43847, 'star': false, 'zone': 2},
 {'chain': '吉林吉影', 'chainid': 43848, 'star': false, 'zone': 1},
 {'chain': '四川太平洋', 'chainid': 43849, 'star': false, 'zone': 2},
 {'chain': '四川峨眉', 'chainid': 43850, 'star': false, 'zone': 1},
 {'chain': '天津银光', 'chainid': 43851, 'star': false, 'zone': 2},
 {'chain': '山东奥卡新世纪', 'chainid': 43852, 'star': true, 'zone': 1},
 {'chain': '山东鲁信', 'chainid': 43853, 'star': false, 'zone': 2},
 {'chain': '广东大地', 'chainid': 43854, 'star': false, 'zone': 1},
 {'chain': '广州金逸珠江', 'chainid': 43855, 'star': false, 'zone': 2},
 {'chain': '新干线', 'chainid': 43856, 'star': false, 'zone': 1},
 {'chain': '新疆公司', 'chainid': 43857, 'star': false, 'zone': 2},
 {'chain': '新疆华夏天山', 'chainid': 43858, 'star': false, 'zone': 1},
 {'chain': '时代华夏今典', 'chainid': 43859, 'star': true, 'zone': 2},
 {'chain': '武汉天河', 'chainid': 43860, 'star': false, 'zone': 1},
 {'chain': '江苏东方', 'chainid': 43861, 'star': false, 'zone': 2},
 {'chain': '江苏幸福蓝海', 'chainid': 43862, 'star': false, 'zone': 1},
 {'chain': '江西星河', 'chainid': 43863, 'star': false, 'zone': 2},
 {'chain': '河北中联', 'chainid': 43864, 'star': false, 'zone': 1},
 {'chain': '河南奥斯卡', 'chainid': 43865, 'star': false, 'zone': 2},
 {'chain': '浙江时代', 'chainid': 43866, 'star': true, 'zone': 1},
 {'chain': '浙江星光', 'chainid': 43867, 'star': false, 'zone': 2},
 {'chain': '浙江横店', 'chainid': 43868, 'star': false, 'zone': 1},
 {'chain': '深圳深影', 'chainid': 43869, 'star': false, 'zone': 2},
 {'chain': '温州雁荡', 'chainid': 43870, 'star': false, 'zone': 1},
 {'chain': '湖北银兴', 'chainid': 43871, 'star': false, 'zone': 2},
 {'chain': '湖南楚湘', 'chainid': 43872, 'star': false, 'zone': 1},
 {'chain': '湖南潇湘', 'chainid': 43873, 'star': true, 'zone': 2},
 {'chain': '福建中兴', 'chainid': 43874, 'star': false, 'zone': 1},
 {'chain': '西安长安', 'chainid': 43875, 'star': false, 'zone': 2},
 {'chain': '辽宁北方', 'chainid': 43876, 'star': false, 'zone': 1},
 {'chain': '重庆保利万和', 'chainid': 43877, 'star': false, 'zone': 2},
 {'chain': '长城沃美', 'chainid': 43878, 'star': false, 'zone': 1},
 {'chain': '安徽中安', 'chainid': 43879, 'star': false, 'zone': 2},
 {'chain': '贵州星空', 'chainid': 43880, 'star': true, 'zone': 1}];

