from flask import Blueprint,request,jsonify,session
from werkzeug.security import check_password_hash
from database import fetch_one
bp=Blueprint('auth',__name__,url_prefix='/api/auth')
@bp.post('/login')
def login():
 x=request.get_json() or {}; u=fetch_one('SELECT * FROM users WHERE email=%s',(x.get('email',''),))
 if not u or not check_password_hash(u['password_hash'],x.get('password','')): return jsonify(error='Invalid email or password'),401
 session['user_id']=u['id']; session['user_name']=u['name']; return jsonify(message='Login successful')
@bp.post('/logout')
def logout(): session.clear(); return jsonify(message='Logged out')
