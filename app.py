# app.py
from flask import Flask, render_template
from pymongo import MongoClient
app = Flask(__name__)

# A welcome message to test our server
@app.route('/')
def index():
    cluster = MongoClient("mongodb+srv://admin:root@cluster0.ffidn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["myFirstDatabase"]
    collection = db['users']
    passed = collection.count_documents({"answers":{"$ne":' '}, "accountType": False})
    not_passed = collection.count_documents({"answers":' ', "accountType": False})
    return render_template("statistics.html",passed = passed,not_passed = not_passed)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run()