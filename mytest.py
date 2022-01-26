# -*- coding: utf-8 -*-


from sxtwl import Lunar
from datetime import datetime,timedelta





# ----------五运---------
class WuyunHuafeng:
    # ---------基本属性-------------
    wuyun_cx=['木', '火', '土', '金', '水']
    wuyin_cx=['角', '征', '宫', '商', '羽']
    wuse_cx=['青', '赤', '黄', '白', '黑']
    wuwei_cx=['酸', '苦', '甘', '辛', '咸']
    wuzang_cx=['肝', '心', '脾', '肺', '肾']
    dganhua={'甲': '土', '己': '土', '乙': '金', '庚': '金', '丙': '水', '辛': '水', '丁': '木', '人': '木', '戊': '火', '癸': '火'}
    ri_cx=['东', '南', '中', '西', '北']

    Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    ShX = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
    numCn = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
    jqmc = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑","白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"]
    ymc = ["十一", "十二", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十" ]
    rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]

    t=['01:00','03:00','05:00','07:00','09:00','11:00','13:00','15:00','17:00','19:00','21:00','23:00']
    drsqs={'甲': '甲', '己': '甲', '乙': '丙', '庚': '丙', '丙': '戊', '辛': '戊', '丁': '庚', '壬': '庚', '戊': '壬', '癸': '壬'}
    # 初运二运初始时辰
    djs_ce={'寅':['申', '子', '辰'],'巳':['巳', '酉', '丑'],'申':['寅', '午', '戌'],'亥':['亥', '卯', '未']}
    # 三运四运初始时辰
    djs_ss={'卯':['申', '子', '辰'],'午':['巳', '酉', '丑'],'酉':['寅', '午', '戌'],'子':['亥', '卯', '未']}
    # 终运初始时辰
    djs_z={'辰':['申', '子', '辰'],'未':['巳', '酉', '丑'],'戌':['寅', '午', '戌'],'丑':['亥', '卯', '未']}
    # 设置类变量
    Gz_y=''        # 岁干岁支
    ZhongYun=''

    # 节点日的公历年月日 
    gongli_y=''
    gongli_m=''
    gongli_d=''

    DAHAN=() 
    CHUNFENG=()
    MANGZHONG=()
    CHUSHU=()
    LIDONG=()

    # ===========季节节点=================   

    def huafeng(self,nian):
        day=Lunar().getDayBySolar(nian,9,9)
        year=int(day.Lyear0+1984)
        
        gz_y=self.Gan[day.Lyear2.tg]+self.Zhi[day.Lyear2.dz]
        self.Gz_y=gz_y

        # 大寒
        xuanzhe=[20,21,22]
        for dh in xuanzhe:
            day=Lunar().getDayBySolar(nian,1,dh)
            
            if (day.qk>=0):
                dahan= self.Gan[day.Lday2.tg]+self.Zhi[day.Lday2.dz]
                jieqi=self.jqmc[day.jqmc]
                jieqi_time=day.jqsj

                

                dt=jieqi_time.split(':')
                date=datetime(nian,1,dh,int(dt[0]),int(dt[1]),int(dt[2]))

                # print(str(date.time()),type(date.time()))
                print('节气: %s'%jieqi,'干支: %s'%dahan,'日期: %s'%date)
                self.DAHAN=(jieqi,dahan,date)

        # 春分
        xuanzhe=[20,21,22]
        for dh in xuanzhe:
            day=Lunar().getDayBySolar(nian,3,dh)
            
            if (day.qk>=0):
                dahan= self.Gan[day.Lday2.tg]+self.Zhi[day.Lday2.dz]
                jieqi=self.jqmc[day.jqmc]
                jieqi_time=day.jqsj

                
                dt=jieqi_time.split(':')
                date=datetime(nian,3,dh,int(dt[0]),int(dt[1]),int(dt[2]))

                # print(str(date.time()),type(date.time()))
                print('节气: %s'%jieqi,'干支: %s'%dahan,'日期: %s'%date)
                self.CHUNFENG=(jieqi,dahan,date) 

        # 芒种
        xuanzhe=[5,6,7]
        for dh in xuanzhe:
            day=Lunar().getDayBySolar(nian,6,dh)
            
            if (day.qk>=0):
                dahan= self.Gan[day.Lday2.tg]+self.Zhi[day.Lday2.dz]
                jieqi=self.jqmc[day.jqmc]
                jieqi_time=day.jqsj

                

                dt=jieqi_time.split(':')
                date=datetime(nian,6,dh,int(dt[0]),int(dt[1]),int(dt[2]))
                
                # print(str(date.time()),type(date.time()))
                print('节气: %s'%jieqi,'干支: %s'%dahan,'日期: %s'%date)
                self.MANGZHONG=(jieqi,dahan,date)

        # 处暑
        xuanzhe=[22,23,24]
        for dh in xuanzhe:
            day=Lunar().getDayBySolar(nian,8,dh)
            
            if (day.qk>=0):
                dahan= self.Gan[day.Lday2.tg]+self.Zhi[day.Lday2.dz]
                jieqi=self.jqmc[day.jqmc]
                jieqi_time=day.jqsj

                

                dt=jieqi_time.split(':')
                date=datetime(nian,8,dh,int(dt[0]),int(dt[1]),int(dt[2]))

                # print(str(date.time()),type(date.time()))
                print('节气: %s'%jieqi,'干支: %s'%dahan,'日期: %s'%date)
                self.CHUSHU=(jieqi,dahan,date)

        # 立冬
        xuanzhe=[7,8]
        for dh in xuanzhe:
            day=Lunar().getDayBySolar(nian,11,dh)
            
            if (day.qk>=0):
                dahan= self.Gan[day.Lday2.tg]+self.Zhi[day.Lday2.dz]
                jieqi=self.jqmc[day.jqmc]
                jieqi_time=day.jqsj

                
                dt=jieqi_time.split(':')
                date=datetime(nian,11,dh,int(dt[0]),int(dt[1]),int(dt[2]))

                # print(str(date.time()),type(date.time()))
                print('节气: %s'%jieqi,'干支: %s'%dahan,'日期: %s'%date)
                self.LIDONG= (jieqi,dahan,date)   

    def shiershichen(self,tt):   # 十二时辰序数定位
        for i in range(len(self.t)):
            try:
                tk1=datetime.strptime(self.t[i],'%H:%M')
                tk2=datetime.strptime(self.t[i+1],'%H:%M')
                sj=datetime.strptime(tt,'%H:%M:%S')

                if tk1<=sj<tk2:
                    return self.Zhi[i+1],i+1
            except IndexError:
                return '亥',11

    def shiGan(self,rgan):
        for k,v in enumerate(self.Gan):
            if v==self.drsqs[rgan]:
                return k

    # ------------五运交司-----------

    def wyjiaosi(self,jiedian):      #jiedian:tuple,节气名称,干支,日期和时间。
        jqmc=jiedian[0];jqgz=jiedian[1];jqrs=jiedian[2]
        if (jqmc=='大寒'):
            theZhi=[v for k,v in enumerate(self.djs_ce) if self.Gz_y[1] in self.djs_ce[v]][0]
            theZhixs=[k for k,v in enumerate(self.Zhi) if theZhi==self.Zhi[k]][0]
            # print(theZhi,theZhixs)
            first=self.drsqs[jqgz[0]]
            firstxs=[k for k,v in enumerate(self.Gan) if first==self.Gan[k]][0]
            # print(first,firstxs)
            theGan=self.Gan[(theZhixs+firstxs)%10]

            # 计算交司时间和时刻
            esssj=self._jiaosisj(jqrs,theZhixs)
            
            return theGan+theZhi,esssj              #datetime.strftime(jqrs,'%Y-%m-%d')

        elif (jqmc=='春分'):
            # 二运交司在春分后13天
            jqrs=jqrs+timedelta(days=13)
            # 计算这天的相关干支
            day=Lunar().getDayBySolar(jqrs.year,jqrs.month,jqrs.day)
            year=int(day.Lyear0+1984)
            
            gz_y=self.Gan[day.Lyear2.tg]+self.Zhi[day.Lyear2.dz]
            self.Gz_y=gz_y
            gz_m=self.Gan[day.Lmonth2.tg]+self.Zhi[day.Lmonth2.dz]
            gz_d=self.Gan[day.Lday2.tg]+self.Zhi[day.Lday2.dz]

            print(gz_y,gz_m,gz_d)
            # 计算这天的交司时辰,二运与初运时辰相同。
            theZhi=[v for k,v in enumerate(self.djs_ce) if self.Gz_y[1] in self.djs_ce[v]][0]
            theZhixs=[k for k,v in enumerate(self.Zhi) if theZhi==self.Zhi[k]][0]

            first=self.drsqs[gz_d[0]]
            firstxs=[k for k,v in enumerate(self.Gan) if first==self.Gan[k]][0]

            theGan=self.Gan[(theZhixs+firstxs)%10]

            esssj=self._jiaosisj(jqrs,theZhixs,2)

            return theGan+theZhi,esssj # datetime.strftime(jqrs,'%Y-%m-%d')
        
        elif (jqmc=='芒种'):
            # 三运在芒种后13天
            jqrs=jqrs+timedelta(days=10)
            # 计算这天的相关干支
            day=Lunar().getDayBySolar(jqrs.year,jqrs.month,jqrs.day)
            year=int(day.Lyear0+1984)
            
            gz_y=self.Gan[day.Lyear2.tg]+self.Zhi[day.Lyear2.dz]
            self.Gz_y=gz_y
            gz_m=self.Gan[day.Lmonth2.tg]+self.Zhi[day.Lmonth2.dz]
            gz_d=self.Gan[day.Lday2.tg]+self.Zhi[day.Lday2.dz]

            print(gz_y,gz_m,gz_d)
            # 计算这天的交司时辰，三运比初运二运推迟一个时辰。
            theZhi=[v for k,v in enumerate(self.djs_ss) if self.Gz_y[1] in self.djs_ss[v]][0]
            theZhixs=[k for k,v in enumerate(self.Zhi) if theZhi==self.Zhi[k]][0]

            first=self.drsqs[gz_d[0]]
            firstxs=[k for k,v in enumerate(self.Gan) if first==self.Gan[k]][0]

            theGan=self.Gan[(theZhixs+firstxs)%10]

            esssj=self._jiaosisj(jqrs,theZhixs,3)

            return theGan+theZhi,esssj  #datetime.strftime(jqrs,'%Y-%m-%d')
        
        elif (jqmc=='处暑'):
            # 四运在处暑后7天
            jqrs=jqrs+timedelta(days=7)
            # 计算这天的相关干支
            day=Lunar().getDayBySolar(jqrs.year,jqrs.month,jqrs.day)
            year=int(day.Lyear0+1984)
            
            gz_y=self.Gan[day.Lyear2.tg]+self.Zhi[day.Lyear2.dz]
            self.Gz_y=gz_y
            gz_m=self.Gan[day.Lmonth2.tg]+self.Zhi[day.Lmonth2.dz]
            gz_d=self.Gan[day.Lday2.tg]+self.Zhi[day.Lday2.dz]

            print(gz_y,gz_m,gz_d)
            # 计算这天的交司时辰，四运与三运同。
            theZhi=[v for k,v in enumerate(self.djs_ss) if self.Gz_y[1] in self.djs_ss[v]][0]
            theZhixs=[k for k,v in enumerate(self.Zhi) if theZhi==self.Zhi[k]][0]

            first=self.drsqs[gz_d[0]]
            firstxs=[k for k,v in enumerate(self.Gan) if first==self.Gan[k]][0]

            theGan=self.Gan[(theZhixs+firstxs)%10]

            esssj=self._jiaosisj(jqrs,theZhixs,4)

            return theGan+theZhi,esssj #datetime.strftime(jqrs,'%Y-%m-%d')

        elif (jqmc=='立冬'):
            # 终运在立冬后4天
            jqrs=jqrs+timedelta(days=4)
            # 计算这天的相关干支
            day=Lunar().getDayBySolar(jqrs.year,jqrs.month,jqrs.day)
            year=int(day.Lyear0+1984)
            
            gz_y=self.Gan[day.Lyear2.tg]+self.Zhi[day.Lyear2.dz]
            self.Gz_y=gz_y
            gz_m=self.Gan[day.Lmonth2.tg]+self.Zhi[day.Lmonth2.dz]
            gz_d=self.Gan[day.Lday2.tg]+self.Zhi[day.Lday2.dz]

            print(gz_y,gz_m,gz_d)
            # 计算这天的交司时辰，三运比初运二运推迟一个时辰。
            theZhi=[v for k,v in enumerate(self.djs_z) if self.Gz_y[1] in self.djs_z[v]][0]
            theZhixs=[k for k,v in enumerate(self.Zhi) if theZhi==self.Zhi[k]][0]

            first=self.drsqs[gz_d[0]]
            firstxs=[k for k,v in enumerate(self.Gan) if first==self.Gan[k]][0]

            theGan=self.Gan[(theZhixs+firstxs)%10]

            esssj=self._jiaosisj(jqrs,theZhixs,5)

            return theGan+theZhi,esssj #datetime.strftime(jqrs,'%Y-%m-%d')
    
    # 计算交司日的二十四小时制
    def _jiaosisj(self,Year,z_xs,yun=1):
        z_xs=z_xs-1
        if (z_xs)<0: z_xs=z_xs+12
        sk=self.t[z_xs]

        if (yun==1) : kd=0
        elif (yun==2) : kd= 1+2.4/60
        elif (yun==3) : kd= (2.4+14.4)/60
        elif (yun==4) : kd = 1+(2.4+14.4+14.4)/60
        elif (yun==5) : kd = (2.4+14.4*3)/60

        shike=datetime.strptime(sk,'%H:%M')+timedelta(hours=kd)
        shike=datetime(Year.year,Year.month,Year.day,shike.hour,shike.minute,shike.second)

        return shike

            

# 五音建运
class WuyinJianyun(WuyunHuafeng):
    '''要了解主运和客运，还须先弄清楚五音建运、太少相生和五步推运等问题。'''
    zhuyun=['木运','火运','土运','金运','水运']
    wuyin=['角', '徵', '宫', '商', '羽']    #  3,5,1,2,6
    wy_nitui=['角','羽','商','宫','徵']
    dOnOff={'太':'少','少':'太'}

    def zhongyun(self,gz_y):
        '''中运（又称大运、岁运），主运和客运'''
        suiyun=self.dganhua[gz_y[0]]      # 岁运或大运
        self.ZhongYun=suiyun
        
        # print(self.ZhongYun)
        if [k for k,v in enumerate(self.Gan) if gz_y[0]==v][0] % 2==0:
            return suiyun+'运太过'
        else:
            return suiyun+'运不及'

    def taishaoinwy(self,gz_y):
        suiyun=self.zhongyun(gz_y)
        
        zyxs=[k for k,v in enumerate(self.zhuyun) if suiyun[:2]==v][0] # 序数
        
        if suiyun[-2:]=='太过':temp='太'  
        else:temp='少'
        keyun=[]
        for i in range(5):    # 推断客运
            wy_ts=temp+self.wuyin[(zyxs+i)%5]
            keyun.append(wy_ts)
            temp=self.dOnOff[temp]
            # print(wy_ts)

        # 从岁运推主运(逆推)
        if suiyun[-2:]=='太过':temp='太'  
        else:temp='少'

        for i in range(5):
            xs=zyxs-i
            if xs<0:xs=xs+5
            wy_ts=temp+self.wuyin[xs]
            temp=self.dOnOff[temp]
            if self.wuyin[xs]=='角':break
        
        temp=wy_ts[0];zhuyun=[]
        for i in range(len(self.wuyin)):
            zhuyun.append(temp+self.wuyin[i])
            temp=self.dOnOff[temp]
        # 返回主运和客运
        return zhuyun,keyun

    """ 初运至终运"""
    def chuyunzhizhongyun(self,nian):
        self.huafeng(nian)
        print(self.Gz_y,'年','大寒: ',self.DAHAN)
        
        chuyun=self.wyjiaosi(self.DAHAN)
        eryun=self.wyjiaosi(self.CHUNFENG)
        sanyun=self.wyjiaosi(self.MANGZHONG)
        siyun=self.wyjiaosi(self.CHUSHU)
        zhongyun=self.wyjiaosi(self.LIDONG)

        nextdahan=self._get_next_dahan(nian)

        wuyun=[chuyun,eryun,sanyun,siyun,zhongyun,nextdahan]

        wuyin=self.taishaoinwy(self.Gz_y)
        
        return wuyun,wuyin[0],wuyin[1]

    def _get_next_dahan(self,nian):
        nian=nian+1
        day=Lunar().getDayBySolar(nian,5,3)
        gz_y=self.Gan[day.Lyear2.tg]+self.Zhi[day.Lyear2.dz]

        xuanzhe=[20,21,22]
        for dh in xuanzhe:
            day=Lunar().getDayBySolar(nian,1,dh)
            
            if (day.qk>=0):
                dahan= self.Gan[day.Lday2.tg]+self.Zhi[day.Lday2.dz]
                jieqi=self.jqmc[day.jqmc]
                jieqi_time=day.jqsj

                

                dt=jieqi_time.split(':')
                date=datetime(nian,1,dh,int(dt[0]),int(dt[1]),int(dt[2]))

                # print(str(date.time()),type(date.time()))
                # print('节气: %s'%jieqi,'干支: %s'%dahan,'日期: %s'%date)
                # self.DAHAN=(jieqi,dahan,date)
                return dahan,date



# ---------六气----------
class LiuQi(WuyunHuafeng):
    dzhihuaqi={'子': '少阴君火', '午': '少阴君火', '丑': '太阴湿土', '未': '太阴湿土', '寅': '少阳相火', '申': '少阳相火', '卯': '阳明燥金', '酉': '阳明燥金', '辰': '太阳寒水', '戌': '太阳寒水', '巳': '厥阴风木', '亥': '厥阴风木'}
    lzhuqicx=['厥阴风木', '少阴君火', '少阳相火', '太阴湿土', '阳明燥金', '太阳寒水']
    # 客气列表,先找司天,再找在泉...
    lkeqi=['厥阴风木', '少阴君火', '太阴湿土', '少阳相火', '阳明燥金', '太阳寒水']
    # 司天在泉对子
    dzkduizi={'厥阴风木':'少阳相火','少阳相火':'厥阴风木','少阴君火':'阳明燥金','阳明燥金':'少阴君火','太阴湿土':'太阳寒水','太阳寒水':'太阴湿土'}
    XIAOMAN=''
    def jieqiforzhuqi(self,nian):
        day=Lunar().getDayBySolar(nian,9,9)
        year=int(day.Lyear0+1984)
        
        gz_y=self.Gan[day.Lyear2.tg]+self.Zhi[day.Lyear2.dz]
        self.Gz_y=gz_y

        xuanzhe=[20,21,22]
        for dh in xuanzhe:
            day=Lunar().getDayBySolar(nian,1,dh)
            
            if (day.qk>=0):
                dahan= self.Gan[day.Lday2.tg]+self.Zhi[day.Lday2.dz]
                jieqi=self.jqmc[day.jqmc]
                jieqi_time=day.jqsj

                dt=jieqi_time.split(':')
                date=datetime(nian,1,dh,int(dt[0]),int(dt[1]),int(dt[2]))

                # print(str(date.time()),type(date.time()))
                print('节气: %s'%jieqi,'干支: %s'%dahan,'日期: %s'%date)
                self.DAHAN=(jieqi,dahan,date)

        # 春分
        xuanzhe=[20,21,22]
        for dh in xuanzhe:
            day=Lunar().getDayBySolar(nian,3,dh)
            
            if (day.qk>=0):
                dahan= self.Gan[day.Lday2.tg]+self.Zhi[day.Lday2.dz]
                jieqi=self.jqmc[day.jqmc]
                jieqi_time=day.jqsj

                
                dt=jieqi_time.split(':')
                date=datetime(nian,3,dh,int(dt[0]),int(dt[1]),int(dt[2]))

                # print(str(date.time()),type(date.time()))
                print('节气: %s'%jieqi,'干支: %s'%dahan,'日期: %s'%date)
                self.CHUNFENG=(jieqi,dahan,date)
        # 小满
        xuanzhe=[20,21,22]
        for dh in xuanzhe:
            day=Lunar().getDayBySolar(nian,5,dh)
            
            if (day.qk>=0):
                dahan= self.Gan[day.Lday2.tg]+self.Zhi[day.Lday2.dz]
                jieqi=self.jqmc[day.jqmc]
                jieqi_time=day.jqsj

                
                dt=jieqi_time.split(':')
                date=datetime(nian,5,dh,int(dt[0]),int(dt[1]),int(dt[2]))

                # print(str(date.time()),type(date.time()))
                print('节气: %s'%jieqi,'干支: %s'%dahan,'日期: %s'%date)
                self.XIAOMAN=(jieqi,dahan,date)

        # 大暑
        xuanzhe=[22,23,24]
        for dh in xuanzhe:
            day=Lunar().getDayBySolar(nian,7,dh)
            
            if (day.qk>=0):
                dahan= self.Gan[day.Lday2.tg]+self.Zhi[day.Lday2.dz]
                jieqi=self.jqmc[day.jqmc]
                jieqi_time=day.jqsj

                
                dt=jieqi_time.split(':')
                date=datetime(nian,7,dh,int(dt[0]),int(dt[1]),int(dt[2]))

                # print(str(date.time()),type(date.time()))
                print('节气: %s'%jieqi,'干支: %s'%dahan,'日期: %s'%date)
                self.DASHU=(jieqi,dahan,date)

        # 秋分
        xuanzhe=[22,23,24]
        for dh in xuanzhe:
            day=Lunar().getDayBySolar(nian,9,dh)
            
            if (day.qk>=0):
                dahan= self.Gan[day.Lday2.tg]+self.Zhi[day.Lday2.dz]
                jieqi=self.jqmc[day.jqmc]
                jieqi_time=day.jqsj

                
                dt=jieqi_time.split(':')
                date=datetime(nian,9,dh,int(dt[0]),int(dt[1]),int(dt[2]))

                # print(str(date.time()),type(date.time()))
                print('节气: %s'%jieqi,'干支: %s'%dahan,'日期: %s'%date)
                self.QIUFEN=(jieqi,dahan,date)

        # 小雪
        xuanzhe=[22,23]
        for dh in xuanzhe:
            day=Lunar().getDayBySolar(nian,11,dh)
            
            if (day.qk>=0):
                dahan= self.Gan[day.Lday2.tg]+self.Zhi[day.Lday2.dz]
                jieqi=self.jqmc[day.jqmc]
                jieqi_time=day.jqsj

                
                dt=jieqi_time.split(':')
                date=datetime(nian,11,dh,int(dt[0]),int(dt[1]),int(dt[2]))

                # print(str(date.time()),type(date.time()))
                print('节气: %s'%jieqi,'干支: %s'%dahan,'日期: %s'%date)
                self.XIAOXUE=(jieqi,dahan,date)
    # 六气列表--以大寒日为气之起点
    def start_dahan_lq(self,nian):
        # 六十花甲
        LSHJ=[self.Gan[i%10]+self.Zhi[i%12] for i in range(60)]
        # 本年年干支
        day=Lunar().getDayBySolar(nian,5,3)
        gz_y=self.Gan[day.Lyear2.tg]+self.Zhi[day.Lyear2.dz]
        
        xunzhe=[20,21]
        for dh in xunzhe:
            day=Lunar().getDayBySolar(nian,1,dh)

            if (day.qk>=0):
                dahan=self.Gan[day.Lday2.tg]+self.Zhi[day.Lday2.dz]
                jieqi=self.jqmc[day.jqmc]
                jieqi_time=day.jqsj

                dt=jieqi_time.split(':')
                date=datetime(nian,1,dh)

                # 本年日干支在六十花甲的序数
                theXS=[k for k,v in enumerate(LSHJ) if gz_y==v ][0]
                print('%s年'%gz_y, theXS,dahan) 

                if theXS % 4==0:    # 申子辰日
                    start=date+timedelta(hours=6)
                if theXS % 4==1:
                    start=date+timedelta(hours=6+25*14.4/60)
                if theXS % 4 ==2:
                    start=date+timedelta(hours=6+25*14.4/60*2)
                if theXS % 4 ==3:
                    start=date+timedelta(hours=6+25*14.4/60*3)

                

                chuzhiqi=start
                erzhiqi=start+timedelta(days=60.875)
                sanzhiqi=start+timedelta(days=60.875*2)
                sizhiqi=start+timedelta(days=60.875*3)
                wuzhiqi=start+timedelta(days=60.875*4)
                zhongzhiqi=start+timedelta(days=60.875*5)

                new=start+timedelta(days=60.875*6)

                return chuzhiqi,erzhiqi,sanzhiqi,sizhiqi,wuzhiqi,zhongzhiqi,new

    # 以正月塑日为气之始,既是大年初一,这才是内经的本旨
    def zq_suri(self,nian):
        ymc = ["十一", "十二", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十" ]
        rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]
        
        yues=[1,2]
        for yue in yues:
            for ri in range(1,32):
                day=Lunar().getDayBySolar(nian,yue,ri)
                # year=int(day.Lyear0 + 1984)

                if (day.Lleap):
                    nl_m='润'+ymc[day.Lmc]
                    nl_d='润'+rmc[day.Ldi]
                else:
                    nl_m=ymc[day.Lmc]
                    nl_d=rmc[day.Ldi]  

                if nl_m=='正' and nl_d=='初一':
                    print(nian,yue,ri, nl_m,nl_d)
                    return nian,yue,ri 

    # 以立春推六气：甲子年立春卯正时为起点
    def list_liuqi_neijing(self,nian):
        # 六十花甲
        LSHJ=[self.Gan[i%10]+self.Zhi[i%12] for i in range(60)]
        
        xunzhe=[3,4,5]
        for lc in xunzhe:
            day=Lunar().getDayBySolar(nian,2,lc)
            gz_y=self.Gan[day.Lyear2.tg]+self.Zhi[day.Lyear2.dz]

            if (day.qk>=0):
                lichun=self.Gan[day.Lday2.tg]+self.Zhi[day.Lday2.dz]
                jieqi=self.jqmc[day.jqmc]
                jieqi_time=day.jqsj

                dt=jieqi_time.split(':')
                date=datetime(nian,2,lc)

                # 此年立春干支在六十花甲里的序数
                theXS=[k for k,v in enumerate(LSHJ) if lichun==v ][0]
                print('%s年'%gz_y, theXS,lichun)
                if theXS % 4==0:    # 申子辰日
                    start=date+timedelta(hours=6)
                if theXS % 4==1:
                    start=date+timedelta(hours=6+25*14.4/60)
                if theXS % 4 ==2:
                    start=date+timedelta(hours=6+25*14.4/60*2)
                if theXS % 4 ==3:
                    start=date+timedelta(hours=6+25*14.4/60*3)

                chuzhiqi=start
                erzhiqi=start+timedelta(days=60.875)
                sanzhiqi=start+timedelta(days=60.875*2)
                sizhiqi=start+timedelta(days=60.875*3)
                wuzhiqi=start+timedelta(days=60.875*4)
                zhongzhiqi=start+timedelta(hours=24*60.875*5)

                new=start+timedelta(days=60.875*6)
                print(chuzhiqi)

    def zhuhekeqi(self,nian):
        # 主气和客气时间段
        zk_time=self.start_dahan_lq(nian) 
        day=Lunar().getDayBySolar(nian,5,3)
        gz_y=self.Gan[day.Lyear2.tg]+self.Zhi[day.Lyear2.dz]
        
        # 主气
        zhuqi=self.lzhuqicx
        
        # 下面是客气，复杂一些
        sitian=self.dzhihuaqi[gz_y[1]]
        zaiquan=self.dzkduizi[sitian]
        # print(sitian,zaiquan)
        # 司天在泉序数
        stxs=[i for i,v in enumerate(self.lkeqi) if sitian==v][0]
        zqxs=[i for i,v in enumerate(self.lkeqi) if zaiquan==v][0]        
        # zqxs=(stxs+3)%6

        # 在泉的左间气
        xs=(zqxs+1)%6
        left_zq=self.lkeqi[xs]
        # 司天右间气
        xs=(stxs-1)
        if xs<0:xs=xs+6
        right_st=self.lkeqi[xs]
        # 司天的左间气
        xs=(stxs+1)%6
        left_st=self.lkeqi[xs]
        # 在泉的右间气
        xs=zqxs-1
        if xs<0:xs=xs+6
        right_zq=self.lkeqi[xs]

        # 客气
        keqi=[left_zq,right_st,sitian,left_st,right_zq,zaiquan]
        for i in range(6):
            print('主气',zhuqi[i],'时间',zk_time[i],'至',zk_time[i+1])
            print('客气',keqi[i],'时间',zk_time[i],'至',zk_time[i+1])

        return left_zq,right_st,sitian,left_st,right_zq,zaiquan
        

异化平气=['丙寅', '丙申', '丙午', '丙子', '乙巳', '乙亥', '丁丑', '丁未', '癸酉', '癸卯', '甲辰', '甲戌']
天刑=['戊辰', '戊戌', '己巳', '己亥', '庚寅', '庚申', '庚子', '庚午', '丁酉', '丁卯', '辛丑', '辛未']
顺化=['癸巳', '癸亥', '甲子', '甲午', '甲寅', '甲申', '乙丑', '乙未', '辛卯', '辛酉', '壬辰', '壬戌']
兼化平气之年=['已巳，己亥', '辛丑', '辛未', '丁卯', '丁酉']
得政平气之年=['乙巳', '乙亥', '丁丑', '丁未', '癸酉', '癸卯']


if __name__=='__main__':
    nian=2021
    r=WuyinJianyun()   # 五音建运
    
    wuyun=r.chuyunzhizhongyun(nian)
    for i in range(5):
        print('%s运'%(i+1),'时间',wuyun[0][i][1],'至',wuyun[0][i+1][1])
        print('主运',wuyun[1][i])
        print('客运',wuyun[2][i])


    q=LiuQi()
    print(q.zhuhekeqi(nian))
    suiyun=r.zhongyun(r.Gz_y)
    print(suiyun)