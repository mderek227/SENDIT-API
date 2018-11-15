"""MAKING CUSTOM ERROR"""
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

def error_response(status_code, message=None):
    """
    Defines the HTTP_STATUS_CODES
    It is put in the payload dictionary which appends
    message you defined and returns the new user friendly error
    """
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response

def bad_request(message):
    """Response for the 400 bad request"""
    return error_response(400, message)
