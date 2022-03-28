from flask import redirect, request
from . import application
import json
import hevyspacy



@application.route('/noop', methods=['GET', 'POST'])
def amf_schemes():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        ff = open(f.filename, 'r')
        content = json.load(ff)
        content.hevyspacy()
        print(content)
        
    return content
 
