from flask import  Flask, request, jsonify

sample = Flask(__name__)

heart_record = [
    {
    "heart_id": "01",
    "date": "13-11-2023",
    "heart_rate":"80",
    },
    {
    "heart_id": "02",
    "date": "12-11-2023",
    "heart_rate":"79",
    },
    {
    "heart_id": "03",
    "date": "11-11-2023",
    "heart_rate":"78",
    },

]

@sample.route('/',methods=['GET'])
def read_information():
    return jsonify(heart_record)

@sample.route('/<int:index>',methods=['DELETE'])
def specific_information(index)
    heart_record.index(index)
    return jsonify(heart_record)

@sample.route('/',methods=['POST'])
def create_information():
    info = request.get_json()
    heart_record.append(info)
    return jsonify(heart_record)

@sample.route('/<int:index>',methods=['DELETE'])
def delete_information(index):
    heart_record.pop(index)
    return jsonify(heart_record)


if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)


