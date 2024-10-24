from flask import Flask, jsonify
from migrations import migrate_data


app = Flask(__name__)

@app.route('/migrate', methods=['POST'])
def migrate():
    """
    Endpoint to trigger data migration from PostgreSQL to Azure Data Lake.
    """
    try:
        migrate_data()
        return jsonify({'message': 'Migration successful'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
