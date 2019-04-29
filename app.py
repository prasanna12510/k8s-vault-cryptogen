from flask import Flask, render_template, abort, request,\
                    redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

from flaskext.mysql import MySQL

import random
import string
import datetime
import jsonify

from rq import Queue
from rq.job import Job
from worker import conn
from models import db, Asset, add_asset, get_asset, get_assets

ERR_NO_FILE_SPECIFIED = 'error: no file specified'

def create_app():
    app = Flask("app",instance_relative_config=False)
    app.config.from_object('config.DevelopmentConfig')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


app = create_app()
print("application name",app.name)
q = Queue(connection=conn)

def randstr():
    '''Creates a random string of alphanumeric characters.'''
    return ''.join(random.choice(string.ascii_uppercase + string.digits) \
                for _ in range(8))


@app.route('/')
def home():
    return redirect(url_for('show_form'))


@app.route('/assets/', methods=['GET'])
def show_form():
    return render_template('form.html')



@app.route('/assets/', methods=['POST'])
def upload_asset():

    if 'file' not in request.files:
        return ERR_NO_FILE_SPECIFIED

    inputfile = request.files['file']

    if inputfile.filename == '':
        return ERR_NO_FILE_SPECIFIED

    safefilename = secure_filename(randstr() + '-' + inputfile.filename)
    target = request.form['target']

    input_args={
        'name': request.form['name'],
        'asset_filename':safefilename,
        'asset_data' : inputfile.read() if target == 'db' else None,
    }

    job = q.enqueue_call(
        func=add_asset, args=(input_args,), result_ttl=5000
    )
    print(job.get_id())

    flash('New crytoasset "{0}" created with jobID: {1}'.format(request.form['name'],job.get_id()))

    return redirect(url_for('show_form'))


@app.route('/assets/db/', methods=['GET'])
def get_assets_from_db():
    assets = get_assets()
    assets = list(filter(lambda asset: asset.asset_data != None, assets))
    return render_template('show_assets.html', assets=assets, target='db')


@app.route('/assets/db/<int:the_id>', methods=['GET'])
def get_asset_from_db(the_id):
    asset = get_asset(the_id)
    return app.response_class(asset.asset_data, mimetype='application/octet-stream')

@app.route("/tasks/<job_key>", methods=['GET'])
def get_results(job_key):

    job = Job.fetch(job_key, connection=conn)

    if job.is_finished:
        #result = Asset.query.filter_by(id=job.result).first()
        #results = sorted(
        #    result.name.items(),
        #    key=operator.itemgetter(1),
        #    reverse=True
        #)[:10]
        response= "Job finish successfully... !!! {}".format(str(job.result))
        return response, 200

    else:
        return "Request In Progress...!", 202



if __name__ == "__main__":
    app.run(debug=True, threaded=True)
