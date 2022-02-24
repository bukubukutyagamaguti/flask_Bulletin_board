import os

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
      'user': os.getenv('DB_USER', 'flask'),
      'password': os.getenv('DB_PASSWORD', 'flask'),
      'host': os.getenv('DB_HOST', 'db'),
      'database': os.getenv('DB_DATABASE', 'flask')
  })
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
SECRET_KEY = 'secret key'
USERNAME = 'toritani'
PASSWORD = 'test1234'
