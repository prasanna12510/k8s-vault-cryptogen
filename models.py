from flask_sqlalchemy import SQLAlchemy
import json
import requests
import logging
import sys
from config import Config

# To be initialized with the Flask app object in app.py.
db = SQLAlchemy()

session = Config().create_session()


class Asset(db.Model):
    __tablename__ = 'assets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    asset_filename = db.Column(db.String(32))
    asset_data = db.Column(db.LargeBinary)

    def __repr__(self):
        return '<asset id={},name={}>'.format(self.id, self.name)


def get_asset(the_id):
    #return Image.query.filter(Image.id == the_id).first()
    return Asset.query.get_or_404(the_id)


def get_assets(params=None):
    if not params:
        return Asset.query.all()
    else:
        raise Exception('Filtering not implemented yet.')


def add_asset(asset_dict):
    print('inside add asset')
    errors=[]
    try:
        new_asset = Asset(name=asset_dict['name'], \
                            asset_filename=asset_dict['asset_filename'], \
                            asset_data=asset_dict['asset_data'])
        response=store_vault(asset_dict['name'],asset_dict['asset_data'])
        if response.status_code == 204:
            print('Inside commit session')
            session.add(new_asset)
            session.commit()
            print('session commited successfully')
    except Exception as e:
        logging.exception(sys.exc_info()[0])
        errors.append(e)
        return {"error": errors, "item": asset_dict, "vault_response":response.text}


def store_vault(asset_name,asset_data):

    print('inside store_vault', json.dumps(asset_data))
    VAULT_TOKEN="3e4a5ba1-kube-422b-d1db-844979cab098"
    headers = {'X-Vault-Token': VAULT_TOKEN}
    URL="http://104.43.240.36:8200/v1/cubbyhole"
    VAULT_URL="{0}/{1}".format(URL,asset_name)

    store_data={asset_name : asset_data}

    response = requests.post(VAULT_URL, data=json.dumps(store_data), headers=headers)
    print('asset added successfully to secret engine ',response.text)
    return response
