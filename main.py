from flask import Flask,request,jsonify
try:
    from aiModel import KnnModel 
except Exception as error:
    ERROR = str(error)
    pass

app=Flask(__name__)


try:
    MODEL = KnnModel()
except:
    pass

@app.route("/",methods=["GET"])
def index():
   
    meas1 = request.args.get("meas1")
    meas2 = request.args.get("meas2")

    try:
       predict = str(MODEL.model.predict([[meas1,meas2]]))
    except:
       predict = 2500

    #prediction = MODEL.model.predict([[meas1,meas2,meas3,meas4,meas5,dis1,dis2,dis3,dis4,dis5,dis6]])
    """ Return a friendly HTTP greeting"""
    try:
        return jsonify(harmful=predict)
    except:
        return json(harmful=predict)



if __name__ == "__main__":

    app.run(host="localhost", port=8080, debug=True)

