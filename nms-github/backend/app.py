import os
from flask import Flask,send_from_directory
from flask_cors import CORS
from config import Config
from routes.auth import bp as auth
from routes.devices import bp as devices
from routes.monitoring import bp as monitoring
from routes.alerts import bp as alerts
from routes.dashboard import bp as dashboard
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); FRONT=os.path.join(BASE,'frontend')
app=Flask(__name__,static_folder=FRONT,static_url_path=''); app.config['SECRET_KEY']=Config.SECRET_KEY; CORS(app,supports_credentials=True)
for b in (auth,devices,monitoring,alerts,dashboard): app.register_blueprint(b)
@app.route('/',defaults={'path':'login.html'})
@app.route('/<path:path>')
def page(path):
 f=os.path.join(FRONT,path); return send_from_directory(FRONT,path) if os.path.isfile(f) else send_from_directory(FRONT,'login.html')
if __name__=='__main__': app.run(host='127.0.0.1',port=5000,debug=True)
