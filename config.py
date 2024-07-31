import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmspythonapp'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'VuPHCusl8bcw1kNSFamGrBFRcV0SPaEtWJyrEyvsuGFlfgoUtdu1RFBjE0U4X41+El53b8JSdWs8+AStVtxfAw==/ikuabfYs1ojGw+AStQgR0Ew=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'image'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cmspyhtonapp.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cmspythonapp'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'adminn'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Aa123456'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+18+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "Pry8Q~4hvf7-2kwG-_su1ixmewPB10VYbVUkDdk0"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/c9438db9-196a-42d9-bf5e-3206c5334a57"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "c63c4391-3851-4997-b936-c372e1809bf3"

    REDIRECT_PATH = "https://cmspythonapp-caewfqguapb9g3g0.southeastasia-01.azurewebsites.net/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session