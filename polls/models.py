from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
"""
以下命令，在Pycharm IDE中的Terminal中运行，运行manage命令，要在包含manage.py文件的目录下才能运行
***改变模型需要这三步:***
1 编辑 models.py 文件，改变模型(数据库结构设计和附加的其它元数据)。
2 运行 python manage.py makemigrations +应用名称（如polls） 为模型的改变生成迁移文件。
3 运行 python manage.py migrate 来应用数据库迁移,即在数据库里创建新定义的模型的数据表。

常用命令：
--sqlmigrate 命令接收一个迁移的名称，然后返回对应的 SQL--

python manage.py sqlmigrate polls 0001

--交互式命令行：python manage.py shell
--启动服务器：python manage.py runserver   
  修改端口号：python manage.py runserver 9000
  让其它电脑可以连接到开发服务器：python manage.py runserver 0.0.0.0:8000
  停止服务器：CTRL + C =shutdown server 
--使用命令行创建project：
   django-admin startproject HelloWorld（project 名称），
   此工程创建命令在Pycharm安装目录下运行即可
   
***我的应用发布地址：***
http://127.0.0.1:8000/polls/
http://127.0.0.1:8000/admin/

***DateField() and DateTimeField() 日期与时间字段***

一般建议设置默认日期default date.

For DateField: default=date.today - 先要from datetime import date

For DateTimeField: default=timezone.now - 先要from django.utils import timezone

对于上一次修改日期(last_modified date)，可以设置: auto_now=True

***class Meta类的常用参数***
class Meta:
    # 按Priority降序, order_date升序排列.
    get_latest_by = ['-priority', 'order_date']
    # 自定义数据库里表格的名字
    db_table = 'music_album'
    # 按什么排序
    ordering = ['pub_date']
    # 定义APP的标签
    app_label = 'myapp'
    # 声明此类是否为抽象,如果为抽象类，则不会生成后台库表
    abstract = True
    # 添加授权
    permissions = (("can_deliver_pizzas", "Can deliver pizzas"),)

"""
"""
   此应用已上传Github, https://github.com/lijiliang123/mysite/
   1) make amendment;
   2) Git工具栏：commit;
   3) 鼠标右健project名称，Git--Repository--push
   4) Github查看
   从Github下载， https://github.com/lijiliang123/mysite/
   1) 鼠标右健project名称，Git--Repository--pull
   2) 或者菜单VCS--Git--pull
   从github上下载程序更新
"""


class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    question_author = models.CharField(max_length=20)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Student(models.Model):
    name = models.CharField(max_length=20)
    add = models.CharField(max_length=200)
    birthday = models.DateField(default=date.today)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name



