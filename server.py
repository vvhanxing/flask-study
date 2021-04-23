from flask import Flask, request,jsonify
import json
import numpy as np
app = Flask(__name__)
1,2
@app.route('/')
def test():
    return 'hello xyz'

@app.route('/sum', methods=['POST'])
def register():
    get_data = request.get_json()
    array = np.array(list(map(lambda x:float(x),get_data["array"])))
    result = {"result":array.sum()}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)