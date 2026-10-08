from flask import Blueprint,jsonify
from database import fetch_one,fetch_all
bp=Blueprint('dashboard',__name__,url_prefix='/api/dashboard')
@bp.get('/summary')
def summary():
 q=lambda s:fetch_one(s)['n']; return jsonify(total=q('SELECT COUNT(*) n FROM devices'),online=q("SELECT COUNT(*) n FROM devices WHERE status='ONLINE'"),offline=q("SELECT COUNT(*) n FROM devices WHERE status='OFFLINE'"),active_alerts=q('SELECT COUNT(*) n FROM alerts WHERE is_resolved=FALSE'))
@bp.get('/chart')
def chart(): return jsonify(fetch_all("SELECT DATE_FORMAT(checked_at,'%%H:%%i') label,ROUND(AVG(response_time),2) response_time FROM monitoring_logs WHERE checked_at>=NOW()-INTERVAL 24 HOUR GROUP BY DATE_FORMAT(checked_at,'%%Y-%%m-%%d %%H:%%i') ORDER BY MIN(checked_at)"))
