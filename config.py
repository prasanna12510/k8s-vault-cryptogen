import os
basedir = os.path.abspath(os.path.dirname(__file__))
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

MYSQL_DATABASE_HOST=os.getenv("MYSQL_DATABASE_HOST", "vaultstore.mysql.database.azure.com")
MYSQL_DATABASE_DB=os.getenv("MYSQL_DATABASE_DB", "k8svault")
MYSQL_DATABASE_USER=os.getenv("MYSQL_DATABASE_USER","dbadmin@vaultstore")
MYSQL_DATABASE_PASSWORD=os.getenv("MYSQL_DATABASE_PASSWORD","Pa$$w0rd")
SSL_PATH="ssl/BaltimoreCyberTrustRoot.crt.pem"


DATABASE_URL="mysql://{0}:{1}@{2}/{3}?ssl_ca={4}".format(MYSQL_DATABASE_USER,MYSQL_DATABASE_PASSWORD,MYSQL_DATABASE_HOST,MYSQL_DATABASE_DB,SSL_PATH)

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'secret-key'
    SQLALCHEMY_DATABASE_URI = DATABASE_URL

    @staticmethod
    def create_session():
        mysql_engine = create_engine(DATABASE_URL)
        Session = sessionmaker(bind=mysql_engine)
        session = Session()
        return session

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
