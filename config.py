class Configuration(object):
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False 
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1@127.0.0.1/test'
	SECRET_KEY = 'something very secret'
	
	### Flask Secutity
	
	SECURITY_PASSWORD_SALT = 'salt'
	SECURITY_PASSWORD_HASH = 'sha256_crypt'