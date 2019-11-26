##############���������������ͼ
ClaimData<-read.table(file="��������.txt",header=TRUE)
boxplot(nclaims~vehiclegroup,data=ClaimData,horizontal=FALSE,main="��ͬ���ͳ��������������ͼ",xlab="����",ylab="�������")

##############pch��ȡֵ���ţ�0~25��
h<-c(rep(1.25,5),rep(1.20,5),rep(1.15,5),rep(1.10,5),rep(1.05,5))
l<-rep(seq(from=1,to=1.2,by=0.05),5)
c<-0:24
plot(x=l,y=h,pch=c,xlim=c(1,2),ylim=c(1,2))
points(x=1.25,y=1.05,pch=25)

################lty��ȡֵ��1~6��
i<-1.8
l<-c(1,1.2)
k<-1
while(i>=1.5){ 
h<-rep(i,2)
i<-i-0.05
lines(x=l,y=h,lty=k)
k<-k+1
}

###############type��ȡֵ
t<-c("p","l","b")
k<-0
a<-1.2
for(i in 1:3){
  l<-c(1.4,1.6,1.8)
  a<-a+k
  h<-c(a,a,a)
  k<-k+0.05
  lines(x=l,y=h,type=t[i])
}

#####################ͼ�β���
MyLayout<-matrix(c(1,1,0,2),nrow=2,ncol=2,byrow=TRUE)
DrawLayout<-layout(MyLayout,widths=c(1,1),heights=c(1,2),respect=TRUE)
layout.show(DrawLayout)

####ֱ��ͼ�ʹ���̬�ֲ����ߵ�ֱ��ͼ�����ܶ�ͼ
ClaimData<-read.table(file="��������.txt",header=TRUE)
DrawL<-par()
par(mfrow=c(2,1),mar=c(4,6,4,4))
hist(ClaimData$nclaims,xlab="�������",ylab="Ƶ��",main="�����������ֱ��ͼ",cex.lab=0.7,freq=FALSE,ylim=c(0,0.1))
MeanTmp=mean(ClaimData$nclaims,rm.na=TRUE)
SdTmp=sd(ClaimData$nclaims)
d=seq(from=min(ClaimData$nclaims),to=max(ClaimData$nclaims),by=0.1)
lines(x=d,y=dnorm(d,MeanTmp,SdTmp),lty=2,col=2)
###���Ӻ��ܶ�����
lines(density(ClaimData$nclaims),lty=4,col=4)
plot(density(ClaimData$nclaims),type="l",main="��������������ܶ�ͼ",xlab="�������",ylab="�ܶ�",cex.lab=0.7)
rug(jitter(ClaimData$nclaims),side=1,col=2) 
par(DrawL)

############С����ͼ
install.packages("vioplot")
library("vioplot")
ClaimData<-read.table(file="��������.txt",header=TRUE)
DrawL<-par()
par(mfrow=c(2,1),mar=c(4,6,4,4))
vioplot(ClaimData$nclaims,horizontal=TRUE)   ##����ȫ���۲��С����ͼ
####����ͼ�����
title(main="�������������С����ͼ",cex.main=0.8,xlab="�������",ylab="ȫ���۲�",cex.lab=0.7)
###���Ƹ����͵�С����ͼ
TmpD1<-ClaimData$nclaims[ClaimData$vehiclegroup=="A"]
TmpD2<-ClaimData$nclaims[ClaimData$vehiclegroup=="B"]
TmpD3<-ClaimData$nclaims[ClaimData$vehiclegroup=="C"]
TmpD4<-ClaimData$nclaims[ClaimData$vehiclegroup=="D"]
LabX<-c("A","B","C","D")
Lo<-vioplot(TmpD1,TmpD2,TmpD3,TmpD4,names=LabX)  #��ͼͬʱ�õ��ؼ�λ������
text(x=1:4,y=Lo$upper,labels=c(length(TmpD1),length(TmpD2),length(TmpD3),length(TmpD4)),
  srt=90)    #��ָ��λ������������Ϣ
title(main="�����ͳ������������С����ͼ",cex.main=0.8,xlab="����",ylab="�������",cex.lab=0.7)
par(DrawL)


###########����������ͼ
DrawL<-par()
ClaimData<-read.table(file="��������.txt",header=TRUE)
par(mfrow=c(2,1),mar=c(4,6,4,4))
dotchart(ClaimData$nclaims,main="������������Ŀ�������ͼ",cex.main=0.8,xlab="�������",ylab="�۲���",cex.lab=0.8)
AvN<-tapply(ClaimData$nclaims,INDEX=ClaimData$vehiclegroup,FUN=mean)  #������������������ƽ��ֵ
dotchart(ClaimData$nclaims[order(ClaimData$vehiclegroup)],main="�����ͳ�����������Ŀ�������ͼ",cex.main=0.8,xlab="�������",cex.lab=0.8,groups=ClaimData$vehiclegroup,gdata=AvN,gpch=17)
legend("bottomright",title="����˵��",c("�۲�ֵ","��ֵ"),pch=c(1,17),bg="white",cex=0.5)
par(DrawL)

##############��Ԫ��̬�ֲ��ܶ�ͼ
mu1<-0
mu2<-0
ss1<-10 
ss2<-10 
rho<-0.7
MyDen<-function(x,y) 
{
 t1<-1/(2*pi*sqrt(ss1*ss2*(1-rho^2)))
 t2<--1/(2*(1-rho^2))
 t3<-(x-mu1)^2/ss1
 t4<-(y-mu2)^2/ss2
 t5<--2*rho*((x-mu1)*(y-mu2))/(sqrt(ss1)*sqrt(ss2))
 return(t1*exp(t2*(t3+t4-t5)))
}
x<-seq(-10,10,length=50) 
y<-x                     
z<-outer(x,y,FUN=MyDen)   
par(mfrow=c(2,2),mar=c(6,4,4,1))
persp(x,y,z,main="��Ԫ��̬�ֲ��ܶ�����ͼ",theta=30,phi=20,expand=0.5,shade = 0.5,xlab="X",ylab="Y",zlab="f(x,y)")
contour(x,y,z,main="��Ԫ��̬�ֲ��ܶȵȸ���ͼ")     

###########��������ͼ
Myf<-function(x,y) {
  r<-sqrt(x^2+y^2)
  r<-10*sin(r)/r
  return(r)
}
x<-seq(-10,10,length=30)
y<-x
z<-outer(x,y,Myf)
z[is.na(z)]<-1   
persp(x,y,z,main="����ͼ",theta=30,phi=30,expand=0.5) 
contour(x,y,z,nlevels=10,main="�ȸ���ͼ")    

#########################  
library(MASS)  
mu1<-0  
mu2<-0  
ss1<-10 
ss2<-10   
s12<-3  
sigma<-matrix(c(ss1,s12,s12,ss2),nrow=2,ncol=2)  
Data<-mvrnorm(n=1000,mu=c(mu1,mu2),Sigma=sigma,empirical = TRUE) 
library(mclust)
DataDens<-densityMclust(data=Data)      
par(mfrow=c(2,2),mar=c(6,4,4,1))
plot(x=DataDens,type ="persp",col=grey(level=0.8))    
plot(x=DataDens,type ="contour",col=grey(level=0))   

#########################
ClaimData<-read.table(file="��������.txt",header=TRUE)
library(mclust)
ClaimDens=densityMclust(data=ClaimData[,c(1,5)])       
plot(x=ClaimDens,type = "persp",col = grey(0.8))      
plot(x=ClaimDens,data=ClaimData[,c(1,5)],type ="contour",col=grey(0.8),nlevels=20)     

##############�״�ͼ
install.packages("fmsb")
library("fmsb")
Forest<-read.table(file="ɭ������.txt",header=TRUE,sep="	")
head(Forest)
AvY<-aggregate(Forest[,5:9],by=list(Forest[,2]),FUN=mean)   
AvY
radarchart(df=AvY[,2:6],axistype=0,seg=5,maxmin=FALSE,
  vlabels=c("�¶�","ʪ��","����","����","�������"),title="��ͬγ�ȵ�������ƽ��ֵ���״�ͼ")


#################������ͼ
library("vcd")
ClaimData<-read.table(file="��������.txt",header=TRUE)
mosaic(~vehiclegroup+vehicleage,data=ClaimData,shade=TRUE,legend=TRUE) 
with(ClaimData,{table(vehiclegroup,vehicleage)}) 

##############ɢ��ͼ
Forest<-read.table(file="ɭ������.txt",header=TRUE,sep="	")
DrawL<-par()
par(mfrow=c(1,2),mar=c(6,4,4,1))
###############ɢ��ͼ
plot(Forest$temp,Forest$RH,main="�¶Ⱥ����ʪ�ȵ�ɢ��ͼ",xlab="�¶�",ylab="���ʪ��",cex.main=0.8,cex.lab=0.8)
M0<-lm(RH~temp,data=Forest)    
abline(M0$coefficients)
M.Loess<-loess(RH~temp,data=Forest)
Ord<-order(Forest$temp) 
lines(Forest$temp[Ord],M.Loess$fitted[Ord],lwd=1,lty=1,col=2)
smoothScatter(x=Forest$temp,y=Forest$RH,main="ɭ�ֵ����¶Ⱥ����ʪ�ȵĸ��ܶȴ���ɢ��ͼ",xlab="�¶�",ylab="���ʪ��",cex.main=0.8,cex.lab=0.8)
par(DrawL)

###############���ܶ�ɢ��ͼ�Ĵ���
install.packages("hexbin")
library("hexbin")
bin<-hexbin(Forest$temp,Forest$RH,xbins=30)
plot(bin,main="ɭ�ֵ����¶Ⱥ����ʪ�ȵĸ��ܶȴ���ɢ��ͼ",xlab="�¶�",ylab="���ʪ��")

####��άɢ��ͼ������ͼ
install.packages("scatterplot3d")
library("scatterplot3d")
DrawL<-par()
MyLayout<-matrix(c(1,2,3,3),nrow=2,ncol=2,byrow=TRUE)
DrawLayout<-layout(MyLayout,widths=c(1,1),height=c(1,1),respect=FALSE)
layout.show(DrawLayout)
s3d<-with(Forest,scatterplot3d(temp,RH,wind,main="ɭ�ֵ����¶ȡ����ʪ�Ⱥͷ�������άɢ��ͼ",xlab="�¶�",ylab="���ʪ��",zlab="����",cex.main=0.7,cex.lab=0.7,cex.axis=0.7))
fit<-lm(wind~temp+RH,data=Forest) 
s3d$plane3d(fit,col="blue")  
with(Forest,symbols(temp,RH,circle=wind,inches=0.1,main="ɭ�ֵ����¶ȡ����ʪ�Ⱥͷ���������ͼ",xlab="�¶�",ylab="���ʪ��",cex.main=0.7,cex.lab=0.7,cex.axis=0.7))
with(Forest,symbols(temp,RH,circle=wind,inches=0.1,main="ɭ�ֵ����¶ȡ����ʪ�Ⱥͷ���������ͼ",xlab="�¶�",ylab="���ʪ��",
     cex.main=0.7,cex.lab=0.7,cex.axis=0.7,fg="white",bg="lightblue"))
par(DrawL)

######����ɢ��ͼ
pairs(~temp+RH+wind,data=Forest,main="ɭ�ֵ����¶ȡ����ʪ�Ⱥͷ����ľ���ɢ��ͼ")
install.packages("car")
library("car")
scatterplotMatrix(~temp+RH+wind,data=Forest,main="ɭ�ֵ����¶ȡ����ʪ�Ⱥͷ����ľ���ɢ��ͼ",lty.smooth=2,spread=FALSE)


##############���������ͬ�����µ�ɢ��ͼ
Forest<-read.table(file="ɭ������.txt",header=TRUE,sep="	")
Forest$month<-factor(Forest$month,levels=c("jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"))

coplot(RH~temp|month,pch=9,data=Forest,xlab="�¶�",ylab="���ʪ��")
coplot(RH~temp|wind,number=6,pch=1,data=Forest,xlab="�¶�",ylab="���ʪ��")
coplot(RH~temp|as.factor(X)*as.factor(Y),pch=1,data=Forest,xlab="�¶�",ylab="���ʪ��")

Mypanel.lm<-function(x,y,...){
 Tmp<-lm(y~x)
 abline(Tmp$coefficients)
 points(x,y,pch=1)}
coplot(RH~temp|wind,number=6,panel=Mypanel.lm,data=Forest,pch=1,xlab="�¶�",ylab="���ʪ��")

###############���ϵ��ͼ
TaoBaoData<-read.table(file="�Ա��ɽ�ָ��.txt",header=TRUE,sep="	")
cor(TaoBaoData[,2:8])
install.packages("corrgram")
library("corrgram")
corrgram(TaoBaoData[,2:8],lower.panel=panel.shade,upper.panel=panel.pie,text.panel=panel.txt,main="��ҵ��Ʒ�ɽ�ָ�������ϵ��ͼ")
corrgram(TaoBaoData[,2:8],lower.panel=panel.ellipse,upper.panel=panel.pts,diag.panel=panel.minmax,main="��ҵ��Ʒ�ɽ�ָ�������ϵ��ͼ")

################���������ͼ��������ͼ
install.packages("maps")      
library("maps") 
data(state)

map(database="world",fill=TRUE,col=rainbow(n=200),ylim=c(-60,90),mar=c(0,0,2,0)) 
title("�����ͼ",cex=0.7)
par(mfrow=c(2,1),mar=c(2,2,6,2))
map(database="state",fill=TRUE,col=rainbow(n=209),mar=c(2, 0, 1, 0))
title("�����ݵ�ͼ",cex=0.7)
map.text(database="state",region=c("California","Florida","Texas","Wisconsin","Utah"),cex=0.6,add=TRUE)  #���ݵ�ͼ������ָ���ݵ�����
map(database="county",region="Michigan",fill=TRUE,col=grey(level=0.9),mar=c(2, 0, 1, 0)) 
title("������Ъ���ݿ��ص�ͼ",cex=0.7)
map.text(database="state",region="Michigan",cex=0.75,add=TRUE,col=2) 

############�����й�����������ͼ

install.packages("maptools")  
library("maptools")
chinaMap<-readShapeSpatial(fn="ʡ��������.shp")  #��ȡ�й�����������shape��ʽ����
plot(chinaMap,panel.first = grid(),col=grey(level=0.7))
slot(object=chinaMap,name="data")  
slot(object=chinaMap,name="polygons") 
sapply(slot(objec=chinaMap,name="polygons"),FUN=function(x) slot(x,"ID"))
sapply(slot(objec=chinaMap,name="polygons"),FUN=function(x) slot(x,"area")) 
xy<-sapply(slot(objec=chinaMap,name="polygons"),FUN=function(x) slot(x,"labpt"))  
xy<-t(xy)
pointLabel(xy[,1],xy[,2],labels=chinaMap$NAME,cex=0.6,col=rgb(red=1,green=0,blue=0),doPlot=TRUE)


##############��������ͼ
library("maptools")
chinaMap<-readShapeSpatial("ʡ��������.shp")  
xy<-sapply(slot(chinaMap, "polygons"),FUN=function(x) slot(x, "labpt")) 
xy<-t(xy)
MapFun<-function(Indices,provName,titleName){
 colT<-(max(Indices)-Indices[])/(max(Indices)-min(Indices))*100  #���ݱ���ȡֵ������ɫ
 Name<-as.vector(chinaMap$NAME)
 MapIndex<-sapply(Name,FUN=function(x) grep(x,provName)) #�������������ƽ���ƥ��
 colPanel<-sapply(MapIndex,FUN=function(x){
  if(length(x)!=0) return(rgb(red=colT[x],green=colT[x],blue=colT[x],maxColorValue=100))
   else return(grey(1))
 })
 plot(chinaMap,panel.first = grid(),col=colPanel)
 pointLabel(xy[,1],xy[,2],labels=chinaMap$NAME,cex=0.6,col=rgb(1,0,0),doPlot=TRUE)
 title(main=titleName)  #��ͼ��ָ������
}

Data<-read.table(file="�Ա��ɽ�ָ��.txt",header=TRUE,sep="	")
indices<-Data[[2]]   #Ůװ�ɽ�ָ��
provname<-as.vector(Data[[1]])
MapFun(indices,provname,"�Ա�Ůװ�ɽ�ָ������ͼ")

Data<-read.table(file="���¼�����������.txt",header=TRUE,sep="	")
indices<-Data[[5]]
provname<-as.vector(Data[[2]])
MapFun(indices,provname,"���¼���������������ͼ")

##############����ͼ
install.packages("wordcloud")
library("wordcloud")
wordFreq<-read.table(file="��Ƶʾ��.txt",header=TRUE,sep=" ")   #����Ƶ����
head(wordFreq[order(wordFreq$Freq,decreasing=TRUE),])   #�����Ƶ��ߵ�ǰ6����
set.seed(123)    #�������������
wordcloud(words=wordFreq$Word,freq=wordFreq$Freq,random.order=FALSE,min.freq=20)  #���ƴ���ͼ

