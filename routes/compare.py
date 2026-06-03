from flask import Blueprint, request, jsonify
from services.similarity import calculate_similarity
from utils.logger import logger

compare_bp = Blueprint('compare', __name__)

@compare_bp.route('/api/health', methods=['GET'])
def health_check():
    logger.info("Health check endpoint called")
    return jsonify({"status": "Server is running"}), 200

@compare_bp.route('/api/compare', methods=['POST'])
def compare_texts():
    logger.info("POST /api/compare request received")

    # Validate that request body is valid JSON
    data = request.get_json(silent=True)
    if data is None:
        logger.warning("Invalid or missing JSON body")
        return jsonify({"error": "Invalid or missing JSON body"}), 400

    # Validate that both fields exist
    if 'text1' not in data or 'text2' not in data:
        logger.warning("Missing text1 or text2 field in request")
        return jsonify({"error": "Both text1 and text2 fields are required"}), 400

    text1 = data['text1']
    text2 = data['text2']

    # Validate that both fields are non-empty strings
    if not isinstance(text1, str) or not isinstance(text2, str):
        logger.warning("text1 or text2 is not a string")
        return jsonify({"error": "text1 and text2 must be strings"}), 400

    if text1.strip() == '' or text2.strip() == '':
        logger.warning("text1 or text2 is empty")
        return jsonify({"error": "text1 and text2 must not be empty"}), 400

    logger.debug(f"text1 length: {len(text1)} | text2 length: {len(text2)}")

    result = calculate_similarity(text1, text2)

    score = result['similarity_score']
    if score >= 70:
        status = "High similarity detected"
    elif score >= 40:
        status = "Moderate similarity detected"
    else:
        status = "Low similarity detected"

    logger.info(f"Response sent | score: {score} | status: {status}")

    return jsonify({
        "similarity_score": score,
        "matched_segments": result['matched_segments'],
        "status": status
    }), 200