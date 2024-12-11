from flask import request, jsonify
from app.model import load_model
from .utils.preprocessing import preprocess_data
from .utils.validation import validate_input

model = load_model()

def init_routes(app):
    @app.route('/predict', methods=['POST'])
    def predict():
        data = request.json
        # Kiểm tra đầu vào
        if not validate_input(data):
            return jsonify({'error': 'Invalid input'}), 400

        # Tiền xử lý dữ liệu
        features = preprocess_data(data)
        prediction = model.predict([features])
        result = 'Fraud' if prediction[0] == 1 else 'Legitimate'
        return jsonify({'result': result})
