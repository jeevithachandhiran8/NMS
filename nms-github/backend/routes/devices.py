from flask import Blueprint,request,jsonify
from database import fetch_all,fetch_one,execute
from services.monitoring_service import check_device
bp=Blueprint('devices',__name__,url_prefix='/api/devices')
@bp.get('')
def all():
 d=fetch_all('SELECT * FROM devices ORDER BY id DESC')
 for x in d:
  if x.get('last_checked'): x['last_checked']=x['last_checked'].isoformat()
 return jsonify(d)
@bp.post('')
def add():
 x=request.get_json() or {}
 if not all(x.get(k) for k in ('device_name','device_type','ip_address')): return jsonify(error='Name, type and IP are required'),400
 try:
  i=execute('INSERT INTO devices(device_name,device_type,ip_address,location,description) VALUES(%s,%s,%s,%s,%s)',(x['device_name'],x['device_type'],x['ip_address'],x.get('location'),x.get('description'))); return jsonify(id=i),201
 except Exception as e: return jsonify(error='Could not add device',detail=str(e)),400
@bp.delete('/<int:id>')
def delete(id): execute('DELETE FROM devices WHERE id=%s',(id,)); return jsonify(message='Deleted')
@bp.post('/<int:id>/check')
def check(id):
 try: return jsonify(check_device(id))
 except ValueError as e: return jsonify(error=str(e)),404
