import requests
import json
url = "https://fhtei84br6.execute-api.us-east-1.amazonaws.com/v1/design"
geneid=input('GeneID: ')
payload = '{\"#\":null,\"genome\":\"homo_sapiens_gencode_26_primary\",\"nuclease\":\"cas9\",\"gene_id\":\"\",\"symbol\":\"'+geneid+'\"}'
headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)
your_json = response.text
parsed = json.loads(your_json)
print(json.dumps(parsed, indent=4, sort_keys=True))
