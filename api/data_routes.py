from flask import Blueprint, jsonify 
 
data_bp = Blueprint('data', __name__) 
 
@data_bp.route('/data', methods=['GET']) 
def get_data(): 
    sample_data = {"message": "This is a sample API response", "status": "success"} 
    return jsonify(sample_data) 
