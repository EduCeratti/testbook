from flask import Flask, render_template, request


from lib.connector import Basedb
from models.model import Testplan

import yaml

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

from flask import Blueprint

app = Flask(__name__)

Base = declarative_base()

testplan = Blueprint('testplan',__name__,url_prefix="/testplan")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        testplanDetails = request.form
        title = testplanDetails['title']

        testplan = Testplan()
        testplan.title = title
        db_object = Basedb()
        db_object.insert_row(testplan)

        return render_template('index.html')

    else:
        return render_template('index.html')



@app.route('/list', methods=['GET', 'POST'])
def list():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']

        cur = mysql.connection.cursor()
    else:

        # engine = create_engine('mysql://root:root@localhost/testbook') # connect to server
        # Base.metadata.create_all(bind=engine)
        # Session = sessionmaker(bind=engine)
        # session = Session()

        db_object = Basedb()
        testbooks = db_object.select_all_rows(Testplan)
        print (testbooks)
        #session.query(Testplan).all()

        # all = []
        # for testbook in testbooks:
        #     return (testbook.title)

        return render_template('list_testbook.html', testbooks= testbooks)


if __name__ == '__main__':
    app.run(debug=True)
