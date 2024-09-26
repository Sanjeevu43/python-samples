import json, falcon
from sympy import content

class Person:
    def __init__(self) -> None:
        print("Initialising Person")

    def on_get(self, req, res):
        print("Initialising Person")
        content = {
            'name':'Sanjeevu',
            'age':45,
            'city':'Bangalore',
            'country':'India'
        }
        res.text = json.dumps(content)

    def on_post(self,req,res):
        post_body = req.stream.read().decode('utf-8')
        print(post_body)
        res.text = json.dumps(post_body)


api = falcon.App()
api.add_route('/test', Person())
