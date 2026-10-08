from datetime import datetime
from database import fetch_one,execute
from services.ping_service import ping_device
from services.alert_service import create_alert_if_needed
def check_device(device_id):
 d=fetch_one('SELECT * FROM devices WHERE id=%s',(device_id,))
 if not d: raise ValueError('Device not found')
 r=ping_device(d['ip_address']); now=datetime.now()
 execute('INSERT INTO monitoring_logs(device_id,status,response_time,packet_loss,checked_at) VALUES(%s,%s,%s,%s,%s)',(device_id,r['status'],r['response_time'],r['packet_loss'],now))
 execute('UPDATE devices SET status=%s,last_checked=%s WHERE id=%s',(r['status'],now,device_id)); create_alert_if_needed(device_id,r['status'],r['response_time']); d.update(r); d['last_checked']=now.isoformat(); return d
