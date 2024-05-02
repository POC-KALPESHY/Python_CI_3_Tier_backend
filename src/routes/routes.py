from flask import request
from flask import (
    jsonify,
    make_response
)
from src.___init__ import app
# from src.utils.db_function import get_cursor,get_object



@app.route("/user",methods = ['GET'])
def fetch_detail():
    # cursor, connection = get_cursor()
    print("Inside fetch detail function.")
    try:
        if request.method == 'GET':
            # query = """ select * from api.api_user """
            # user_details = get_object(
            #     query=query,
            #     cursor=cursor
            # )
            user_details = {
  "articles": [
    {
      "id": 1,
      "title": "Breaking News: Scientists Discover New Species of Bird",
      "content": "Moon Holds More Water Ice Than Expected, Especially at North Pole."
    },
    {
      "id": 2,
      "title": "Sports: IPL match between.",
      "content": "Punjab Kings defeats Chennai Super Kings by seven wickets."
    },
    {
      "id": 3,
      "title": "Political: Powell talks about the interest rate.",
      "content": "BackBack US Fed policy: Political stability to outweigh higher interest rate concerns for Indian investors."
    }
  ]
}

            return make_response(jsonify(user_details))
    except Exception as e:
        print(e)
