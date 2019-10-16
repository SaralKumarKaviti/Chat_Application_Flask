from flask import Flask,render_template,request,jsonify,json
from flask_cors import CORS
from pusher import pusher
import simplejson

app=Flask(__name__)
cors=CORS(app)
app.config['CORSHEADERS']='Content-Type'

pusher = pusher.Pusher(
    app_id='880565',
    key='5b11297234df431aeca4',
    secret='2119845d9a5739d99d0f',
    cluster='mt1',
    ssl=True)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/admin')
def admin():
	return render_template('admin.html')

@app.route('/new/guest',methods=['POST'])
def guestUser():
	data=request.json
	pusher.trigger(u'general-channel',u'new-guest-details',{
		'name':data['name'],
		'email':data['email']
		})
	return json.dumps(data)

@app.route("/pusher/auth",methods=['POST'])
def pusher_authentication():
	auth=pusher.authenticate(channel=request.form['channel_name'],socket_id=request.form['socket_id'])
	return json.dumps(auth)

if __name__=='__main__':
	app.run(port=5000,debug=True)
