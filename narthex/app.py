from flask import Flask
from flask import render_template,jsonify,request
import os
app = Flask(__name__)


from get_aws_prayers import download_prayers ## s3


import json
try:
	with open('prayers.json','r') as f:
		prayers = json.load(f)
except: ## need to redownload, may occur when heroku restarts
	download_prayers(); 
	with open('prayers.json','r') as f:
		prayers = json.load(f)


@app.route('/')
def main_page():
    return render_template('narthex.html')


@app.route('/get_prayers', methods=['GET'])
def get_prayers():
	hour = request.args.get('hour')
	return jsonify(prayers[hour])


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)