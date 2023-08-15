import requests
from main import read_root, addUser

# def double(num):
#         return num * 2

# class TestDummy:
#     def test_one(self):
#         assert read_root() == {"Ping":"Pongy"}


#     def test_two(self):
#         assert double(2) == 4


        
#     def test_three(self):
#         assert double(3) == 5


##  GET ## 
class TestRoot:
    def test_one(self):
        assert read_root() == {"Ping":"Pongy"}
    
    def test_two(self):
        response = requests.get('http://127.0.0.1:8000')
        assert response.json() == {"Ping":"Pongy"}
        

class TestGroupData:
    def test_one(self):
        response = requests.get('http://127.0.0.1:8000/groupresults/mattsfirstgroup')
        assert response.text == {}


## POST ##
#class TestAddUser:
    # def test_return_200(self):
    #     data = {
    #         'group_id': 'montydog',
    #         'username' : 'mattyb'
    #     }
    #     response = requests.post('http://127.0.0.1:8000/createuser', data=data)
    #     print(response.text, "this is matts response")
    #     #assert response.status_code == 200
    #     assert response.json() == {"msg": "matts building endpoint to add mattyb to montydog"}

    # def test_queries(self):
    #     response = requests.post('http://127.0.0.1:8000/createuser', data=data)

