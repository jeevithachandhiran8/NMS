import pymysql
from pymysql.cursors import DictCursor
from config import Config
def get_connection(): return pymysql.connect(host=Config.DB_HOST,port=Config.DB_PORT,user=Config.DB_USER,password=Config.DB_PASSWORD,database=Config.DB_NAME,cursorclass=DictCursor,autocommit=True)
def fetch_all(sql,params=()):
 c=get_connection()
 try:
  with c.cursor() as x: x.execute(sql,params); return x.fetchall()
 finally: c.close()
def fetch_one(sql,params=()):
 c=get_connection()
 try:
  with c.cursor() as x: x.execute(sql,params); return x.fetchone()
 finally: c.close()
def execute(sql,params=()):
 c=get_connection()
 try:
  with c.cursor() as x: x.execute(sql,params); return x.lastrowid
 finally: c.close()
