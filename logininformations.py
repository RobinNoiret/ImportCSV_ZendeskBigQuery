zendesk_crendentials = {
    'email' : 'your_email',
    'token' : 'your_token',
    'subdomain': 'your_subdomain'
}

# Other way to complete zendesk_credentials :
#
#   Methode 1 : An OAuth token
#       creds = {
#           "subdomain": "your_subdomain",
#           "oauth_token": "your_oathtoken"
#       }       
#
#   Methode 2 : a password
#       creds = {
#           'email' : 'your_email',
#           'password' : 'your_password',
#           'subdomain': 'your_subdomain'
#       }


gbq_credentials = 'From google-auth or pydata-google-auth library'
gbq_tableId = 'BigQuery table Id of the zendesk tickets table'
gbq_projectId = 'BigQuery project Id that the table is in'