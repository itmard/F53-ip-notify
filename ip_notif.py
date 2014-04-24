from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def get_ip():
	if len(request.access_route) > 1:
		return request.access_route[-1]
	else:
		return request.access_route[0]
