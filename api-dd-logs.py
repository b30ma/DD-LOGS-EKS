from datadog import initialize, api

options = {
    'api_key': 'YOUR_DATADOG_API_KEY',
    'app_key': 'YOUR_DATADOG_APP_KEY'
}

initialize(**options)

# Example: Get list of logs
logs_list = api.Logs.list()
print(logs_list)
