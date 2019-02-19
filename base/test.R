dx<-c();
dy<-c()

##轮廓点
outline<- function(star, end, step){
    a<- seq(from=star,to = end, by =step);pi<-3.14156;
    for( t in a ) {
    x<-c((t^10+1)*cos(pi/6-2*pi*(15*t/16 + 1/16)));
    y<-c((t**10+1)*sin(pi/6-2*pi*(15*t/16 + 1/16)));
    dx<- c(dx, x);
    dy<- c(dy, y)
  }
  print(dx,dy);
};

##鼻子点
nose<- function(star, end, step){
    a<- seq(from=star,to = end, by =step);pi<-3.14156;
    for( t in a){
    x<-c(cos(2*pi*t)/4+ 25/40);
    ###dx<-c(dx, x);
    y<-c(sin(2*pi*t)/3+ 7/10);
    ###dy<- c(dy, y);
    x1<-c(cos(2 * pi * t) / 16 + 59 / 40);
    y1<-c(sin(2 * pi * t) / 16 + 7 / 10);

    x2<-c(cos(2 * pi * t) / 16 + 69 / 40);
    y2<-c(sin(2 * pi * t) / 16 + 7 / 10);

    dx<-c(dx, x, x1, x2);
    dy<-c(dy, y, y1, y2)
    }
};

##眼睛点
eye<- function(star, end, step){
    a<- seq(from=star,to = end, by =step);pi<-3.14156;
    for( t in a){
    x<-c(0.15*cos(2 * pi * t));
    y<-c(0.15*(sin(2 * pi * t)+5.3333));

    x1<-c(0.15 * (cos(2 * pi * t)+4));
    y1<-c(0.15 * (sin(2 * pi * t) + 6));

    x2<-c(0.05 * cos(2 * pi * t));
    y2<-c(0.05 * (sin(2 * pi * t) + 16));

    x3<-c(0.05 * (cos(2 * pi * t)+12));
    y3<-c(0.05 * (sin(2 * pi * t) + 18));

    dx<-c(dx, x, x1, x2, x3);
    dy<-c(dy, y, y1, y2, y3);
    }

};

##嘴巴点
mouth<- function(star, end, step){
    a<- seq(from=star,to = end, by =step);pi<-3.14156;
    for( t in a){
    x<-c(t-1/3);
    y<-c((t-2/5)^2);

    dx<-c(dx, x);
    dy<-c(dy, y);
    }

};

##耳朵点
ear<- function(star, end, step){
    a<- seq(from=star,to = end, by =step);pi<-3.14156;
    for( t in a){
    x<-c((2*t**2-2*t-1) * sin((2*t+pi)/6));
    y<-c(-(2*t**2-2*t-1) * cos((2*t+pi)/6));

    x1<-c((2 * t ** 2 - 2 * t - 1) * sin(t/3));
    y1<-c((2 * t ** 2 - 2 * t - 1) * cos(t/3));

    dx<-c(dx, x, x1);
    dy<-c(dy, y, y1);
    }

};


main_painting <- function(){
   outline(0,1, 0.01);
   nose(0,1, 0.05);
   eye(0,1, 0.05);
   mouth(0,1, 0.05);
   ear(0,1, 0.05);

   #描点
   plot(dx,dy);
};

main_painting()
##source("C:\\Workcode\\PL\\base\\test.R")


Titanic    #泰坦尼克乘员统计
crimtab    #3000个男性罪犯左手中指长度和身高关系
chickwts   #不同饮食种类对小鸡生长速度的影响
Freeny     #每季度收入和其他四因素的记录
sleep      #两药物的催眠效果
Nile       #1871-1970尼罗河流量
