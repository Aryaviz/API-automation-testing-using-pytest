
from config.parameters import config
from api.base_client import BaseClient


class AuthEndpoints(BaseClient):
    
    
    def __init__(self):
        super().__init__()
        self.auth_endpoint = "/auth"
    #  Create authentication token 
    def create_token(self, username: str = None, password: str = None) -> dict:
     
        payload = {
            "username": username or config.USERNAME,
            "password": password or config.PASSWORD
        }
        
        response = self.post(self.auth_endpoint, payload=payload)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Authentication failed: {response.status_code} - {response.text}")
        
      # Get authentication token string  
    
    def get_token(self, username: str = None, password: str = None) -> str:
       
        token_response = self.create_token(username, password)
        return token_response.get("token")
