import requests

post_url = "http://localhost:8002/score_image"

results = []

for id in range(1,11):
    payload = '''
    {
    "data": [
        {
            "id": "1",
            "bank": "Malaysia",
            "batchId": "1",
            "dateRef": "2021",
            "model_size": "base",
            "payeeName": "TS FORCE SDN. BHD.",
            "actions": [
                "PAYEE_NAME_SCORING",
                "LARCAR_SCORING",
                "DATE_VALIDATION"
            ],
            "mimeTypeImageFront": "image/tiff",
            "imageFront": "SUkqAPAnAAAKbXr9//////r+///5XMr1frV1x/ot8ErldZBp"
		}]
    }
    '''
    # post_res = requests.post(post_url, data=payload)
    # if post_res.status_code == 200:
    #     results.append(post_res.text)

#print(results)

wash_clothes = 'tuesdays'
clean_dishes = 'never'

mystring =f""" I like to wash clothes on {wash_clothes}
I like to clean dishes {clean_dishes}
"""

print(mystring)

for i in range(1,3):
    print(type(i))
    id = str(i)
    print(type(id))