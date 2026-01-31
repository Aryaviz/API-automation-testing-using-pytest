from api.base_client import BaseClient
from typing import Dict, Optional


class BookingEndpoints(BaseClient):
    """Booking endpoints for Restful Booker API"""
    
    def __init__(self):
        super().__init__()
        self.booking_endpoint = "/booking"
    
    def get_booking_ids(self, params: Optional[Dict] = None):
        """
        Get all booking IDs
        
        Args:
            params: Optional query parameters (firstname, lastname, checkin, checkout)
        
        Returns:
            Response object
        """
        return self.get(self.booking_endpoint, params=params)
    def get_booking(self, booking_id: int):
        """
        Get booking by ID
        
        Args:
            booking_id: Booking ID to retrieve
        
        Returns:
            Response object
        """
        endpoint = f"{self.booking_endpoint}/{booking_id}"
        return self.get(endpoint)
    def create_booking(self, booking_data: Dict):
        """
        Create a new booking
        
        Args:
            booking_data: Booking details
        
        Returns:
            Response object
        """
        return self.post(self.booking_endpoint, payload=booking_data)
    def update_booking(self, booking_id: int, booking_data: Dict, token: str):
        """
        Update a booking (full update - PUT)
        
        Args:
            booking_id: Booking ID to update
            booking_data: Updated booking details
            token: Authentication token
        
        Returns:
            Response object
        """
        endpoint = f"{self.booking_endpoint}/{booking_id}"
        headers = {
            "Cookie": f"token={token}",
            "Accept": "application/json"
        }
        return self.put(endpoint, payload=booking_data, headers=headers)
    def update_booking(self, booking_id: int, booking_data: Dict, token: str):
        """
        Update a booking (full update - PUT)
        
        Args:
            booking_id: Booking ID to update
            booking_data: Updated booking details
            token: Authentication token
        
        Returns:
            Response object
        """
        endpoint = f"{self.booking_endpoint}/{booking_id}"
        headers = {
            "Cookie": f"token={token}",
            "Accept": "application/json"
        }
        return self.put(endpoint, payload=booking_data, headers=headers)