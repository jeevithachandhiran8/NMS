from flask import Blueprint,jsonify
from database import fetch_all
bp=Blueprint('monitoring',__name__,url_prefix='/api/monitoring')
@bp.get('/<int:id>')
def history(id):
 r=fetch_all('SELECT * FROM monitoring_logs WHERE device_id=%s ORDER BY checked_at DESC LIMIT 50',(id,))
 for x in r:
  if x.get('checked_at'): x['checked_at']=x['checked_at'].isoformat()
 return jsonify(r)
