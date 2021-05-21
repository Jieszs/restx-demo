## FLASK RESTX 样板工程

### 执行创建表信息
    Make sure to run the initial migration commands to update the database.
    
    > python manage.py db init

    > python manage.py db migrate --message 'initial database migration'

    > python manage.py db upgrade


### Swagger地址 ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/

### 实现功能
1. 基础的CRUD
2. 跨域设置
3. 分页设置
4. 原生sql查询与修改更新
5. 异常统一处理（不够优雅）
6. 查询条件的筛选
7. 简单jwt接口权限
8. swagger  


### 软件运行环境
```
Python 3.9

MySql 8.0
```

### 参考资料

```
https://github.com/cosmic-byte/flask-restplus-boilerplate.git  样板项目
https://marshmallow.readthedocs.io/en/stable/extending.html#schemavalidation  Schemas进行参数校验
https://github.com/python-restx/flask-restx  restx框架地址
https://dormousehole.readthedocs.io/en/latest/index.html flask 中文文档地址
```
