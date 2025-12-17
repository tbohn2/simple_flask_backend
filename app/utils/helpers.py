"""Utility functions and helpers"""

def validate_email(email):
    """Validate email format"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def format_response(data, status='success', message=None):
    """Format API response"""
    response = {
        'status': status,
        'data': data
    }
    if message:
        response['message'] = message
    return response

