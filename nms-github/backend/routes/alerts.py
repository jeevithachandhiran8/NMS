from flask import Blueprint,jsonify
from database import fetch_all,execute
bp=Blueprint('alerts',__name__,url_prefix='/api/alerts')
@bp.get('')
def all():
 r=fetch_all('SELECT a.*,d.device_name FROM alerts a JOIN devices d ON d.id=a.device_id ORDER BY a.created_at DESC')
 for x in r:
  if x.get('created_at'): x['created_at']=x['created_at'].isoformat()
 return jsonify(r)
@bp.put('/<int:id>/resolve')
def resolve(id): execute('UPDATE alerts SET is_resolved=TRUE,resolved_at=NOW() WHERE id=%s',(id,)); return jsonify(message='Resolved')
