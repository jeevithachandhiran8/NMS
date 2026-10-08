from database import execute,fetch_one
def create_alert_if_needed(device_id,status,response_time):
 if status=='OFFLINE':
  if not fetch_one("SELECT id FROM alerts WHERE device_id=%s AND alert_type='DEVICE_DOWN' AND is_resolved=FALSE LIMIT 1",(device_id,)): execute("INSERT INTO alerts(device_id,alert_type,severity,message) VALUES(%s,%s,%s,%s)",(device_id,'DEVICE_DOWN','CRITICAL','Device is unreachable.'))
 elif response_time>500:
  if not fetch_one("SELECT id FROM alerts WHERE device_id=%s AND alert_type='HIGH_LATENCY' AND is_resolved=FALSE LIMIT 1",(device_id,)):
   sev='CRITICAL' if response_time>1000 else 'WARNING'; execute("INSERT INTO alerts(device_id,alert_type,severity,message) VALUES(%s,%s,%s,%s)",(device_id,'HIGH_LATENCY',sev,f'High response time: {response_time} ms.'))
