import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=[POST])
def predict():
    data = request.get json(force=True)
    prediction = model.predict([[np.array(data['exp'])]])
    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)