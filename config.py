import os
 
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'ENTER_STORAGE_ACCOUNT_NAME'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'ENTER_BLOB_STORAGE_KEY'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'ENTER_IMAGES_CONTAINER_NAME'

    import os
 
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'ENTER_STORAGE_ACCOUNT_NAME'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'ENTER_BLOB_STORAGE_KEY'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'ENTER_IMAGES_CONTAINER_NAME'

    SQL_SERVER = 'cmsshazia92173.database.windows.net'
    SQL_DATABASE = 'free-sql-db-4925829 '
    SQL_USER_NAME = 'azureadmin'
    SQL_PASSWORD = 'Shafreen0205@'

    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False





    ### Info for MS Authentication ###
    CLIENT_ID = os.environ.get('CLIENT_ID') or 'ENTER_CLIENT_ID_HERE'
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'ENTER_CLIENT_SECRET_HERE'
    AUTHORITY = os.environ.get('AUTHORITY') or 'https://login.microsoftonline.com/b3641256-9fb9-4fa6-b862-670627210539'
    REDIRECT_PATH = os.environ.get('REDIRECT_PATH') or '/getAToken'

    SCOPE = []
    SESSION_TYPE = "filesystem"

    ### Info for MS Authentication ###
    CLIENT_ID = os.environ.get('CLIENT_ID') or 'ENTER_CLIENT_ID_HERE'
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'ENTER_CLIENT_SECRET_HERE'
    AUTHORITY = os.environ.get('AUTHORITY') or 'https://login.microsoftonline.com/b3641256-9fb9-4fa6-b862-670627210539'
    REDIRECT_PATH = os.environ.get('REDIRECT_PATH') or '/getAToken'

    SCOPE = []
    SESSION_TYPE = "filesystem"
