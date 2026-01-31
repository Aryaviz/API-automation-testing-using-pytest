
class Config:
   
    
    BASE_URL="https://restful-booker.herokuapp.com"
    USERNAME="admin"
    PASSWORD="password123"
    
    # Timeouts
    REQUEST_TIMEOUT = 30
    
    # Headers
    HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }


config = Config()