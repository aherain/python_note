def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]


# uwsgi --http :9090 --wsgi-file uwsggi.py --master --processes 4 --threads 2



# [uwsgi]
# socket = 127.0.0.1:9090
# master = true         //主进程
# vhost = true          //多站模式
# no-site = true        //多站模式时不设置入口模块和文件
# workers = 2           //子进程数
# reload-mercy = 10
# vacuum = true         //退出、重启时清理文件
# max-requests = 1000
# limit-as = 512
# buffer-size = 30000
# pidfile = /var/run/uwsgi9090.pid    //pid文件，用于下面的脚本启动、停止该进程
# daemonize = /website/uwsgi9090.log


# server
# {
#     listen 80;
#     server_name localhost;
#
# location / {
#     include uwsgi_params;
#     uwsgi_pass 127.0.0.1: 9090; // 必须和uwsgi中的设置一致
#     uwsgi_param UWSGI_SCRIPT demosite.wsgi; // 入口文件，即wsgi.py相对于项目根目录的位置，“.”相当于一层目录
#     uwsgi_param UWSGI_CHDIR / demosite; // 项目根目录
#     index index.html index.htm;
#     client_max_body_size 35m;
#   }
# }

