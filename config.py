from dotenv import load_dotenv
load_dotenv()
import os

DEBUG=True
SQLALCHEMY_DATABASE_URI="sqlite:///Ticketz.db"
SECRET_KEY=os.environ.get('SECRET_KEY')