# environments
flask_env_dev = "development"
flask_env_testing = "testing"
flask_env_production = "production"

# Logging
log_file_name = "logs/backend_api.log"
log_level_critical = 50
log_level_error = 40
log_level_warning = 30
log_level_info = 20
log_level_debug = 10
log_level_notset = 0

# response message key
response_message_key = "message"
response_status_key = "status"

# Http response statuses codes

# successful responses - 2xx
status_ok_200 = 200
status_created_201 = 201

# client side errors - 4xx
status_badrequest_400 = 400
status_unauthorized_401 = 401
status_already_exists_403 = 403
status_notfound_404 = 404

# server side errors
status_internal_server_error_500 = 500