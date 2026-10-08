import platform,subprocess,time
def ping_device(ip):
 cmd=['ping','-n','1','-w','2000',ip] if platform.system().lower()=='windows' else ['ping','-c','1','-W','2',ip]
 start=time.perf_counter()
 try:
  r=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=5); ms=(time.perf_counter()-start)*1000
  return {'status':'ONLINE' if r.returncode==0 else 'OFFLINE','response_time':round(ms,2) if r.returncode==0 else 0,'packet_loss':0.0 if r.returncode==0 else 100.0}
 except Exception: return {'status':'OFFLINE','response_time':0.0,'packet_loss':100.0}
