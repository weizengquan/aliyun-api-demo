# aliyun-api-demo

## 安装 ##
1. git clone https://github.com/weizengquan/aliyun-api-demo.git
2. cd aliyun-api-demo
3. virtualenv env
4. source env/bin/activate
5. pip install Flask
6. cp config.py.template config.py
7. modify the config.py file with your aliyun app_id and app_secret string, save it.
8. python run.py

## Docker 安装 ##
1. git clone https://github.com/weizengquan/aliyun-api-demo.git
2. cd aliyun-api-demo
3. docker build -t aliyun-api-demo .
4. after built, use "docker images" to check if there is a docker image called "aliyun-api-demo"
5. docker run -it -p 5000:5000 aliyun-api-demo
