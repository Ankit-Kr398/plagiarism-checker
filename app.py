from flask import Flask, jsonify
from routes.compare import compare_bp
from utils.logger import logger

app = Flask(__name__)

app.register_blueprint(compare_bp)

@app.errorhandler(404)
def not_found(error):
    logger.warning(f"404 error: {error}")
    return jsonify({"error": "Route not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"500 error: {error}")
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    logger.info("Starting Plagiarism Checker server")
    app.run(host='0.0.0.0', port=5000, debug=True)