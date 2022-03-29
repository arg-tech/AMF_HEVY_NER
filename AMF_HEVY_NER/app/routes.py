from flask import redirect, request
from . import application
import json
import en_core_web_sm
from app.hevyspacy import getjson_aif

@application.route('/noop', methods=['GET', 'POST'])
def amf_schemes():
	if request.method == 'POST':
		f = request.files['file']
		f.save(f.filename)
		ff = open(f.filename, 'r')
		readcontent = f.read()
		content = json.load(readcontent)
		example = getjson_aif(content)
	return example
