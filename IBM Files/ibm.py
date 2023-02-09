import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "slh8-ruOG1-dzPa_sS9bv9xOmneEQRwlIDm_touyMEDj"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["AI","V","AP","RH"]], "values": [[1,5,3,4]]}]}
response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/620c82e1-3b17-4d11-88d8-5dc3bdabe710/predictions?version=2023-02-08', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
predictions=response_scoring.json()
print("The Prediction is ")
print(predictions['predictions'][0]['values'][0][0])