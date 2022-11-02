from flask import Flask
from housing.exception import HousingException
import sys
from housing.logger import logging

app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    try:
        raise Exception('hkasdassfa')
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
    return 'Manas Jaiswal'


if __name__=='__main__':
    app.run(debug=True)
