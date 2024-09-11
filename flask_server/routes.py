from flask import request
from services import add_summary

summaries = {}

def init_routes(app):
    @app.route('/summarize', methods=['POST'])
    def summarize():
        data = request.get_json()
        return add_summary(data)
