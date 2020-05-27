import os

class Config:
    DEBUG = True
    ENV = "development"
    # 配置数据库自动更新
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 配置数据库文件位置
    file_path = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(file_path, 'my.db')
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+db_path