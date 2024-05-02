from flask import request
from flask import (
    jsonify,
    make_response
)
from src.___init__ import app
# from src.utils.db_function import get_cursor,get_object
from src.utils import constant as settings



@app.route("/home",methods = ['GET'])
def home_detail():
    # cursor, connection = get_cursor()
    print("Inside fetch detail function.")
    try:
        if request.method == 'GET':
            # query = """ select * from api.api_user """
            # user_details = get_object(
            #     query=query,
            #     cursor=cursor
            # )
            home_page_data = settings.HOME_PAGE_DATA

            return make_response(jsonify(home_page_data))
    except Exception as e:
        print(e)

@app.route("/sports",methods = ['GET'])
def sport_detail():
    # cursor, connection = get_cursor()
    print("Inside sport detail function.")
    try:
        if request.method == 'GET':
            # query = """ select * from api.api_user """
            # user_details = get_object(
            #     query=query,
            #     cursor=cursor
            # )
            sport_page_data = settings.SPORT_PAGE_DATA

            return make_response(jsonify(sport_page_data))
    except Exception as e:
        print(e)
