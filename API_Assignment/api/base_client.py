import requests
from typing import Dict, Any, Optional
from config.parameters import config



class BaseClient:
    """Base API client for making HTTP requests"""
    
    def __init__(self):
        self.base_url = config.BASE_URL
        self.session = requests.Session()
        self.session.headers.update(config.HEADERS)
        self.timeout = config.REQUEST_TIMEOUT
    
    def get(self, endpoint: str, params: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        """Make GET request"""
        url = f"{self.base_url}{endpoint}"
        print(f"GET Request: {url}")
        
        if headers:
            self.session.headers.update(headers)
        
        response = self.session.get(url, params=params, timeout=self.timeout)
        print(f"Response Status: {response.status_code}")
        print(f"Response Body: {response.text}")
        
        return response
    
    def post(self, endpoint: str, payload: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        """Make POST request"""
        url = f"{self.base_url}{endpoint}"
        print(f"POST Request: {url}")
        print(f"Payload: {payload}")
        
        if headers:
            self.session.headers.update(headers)
        
        response = self.session.post(url, json=payload, timeout=self.timeout)
        print(f"Response Status: {response.status_code}")
        print(f"Response Body: {response.text}")
        
        return response
    
    def put(self, endpoint: str, payload: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        """Make PUT request"""
        url = f"{self.base_url}{endpoint}"
        print(f"PUT Request: {url}")
        print(f"Payload: {payload}")
        
        if headers:
            self.session.headers.update(headers)
        
        response = self.session.put(url, json=payload, timeout=self.timeout)
        print(f"Response Status: {response.status_code}")
        print(f"Response Body: {response.text}")
        
        return response
    

