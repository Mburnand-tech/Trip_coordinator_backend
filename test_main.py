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



## POST ##
class TestAddUser:
    def test_return_200(self):
        response = requests.post('https://http://127.0.0.1:8000//createuser', )
        print(response, "this is matts response")
        #assert response.status_code == 200


