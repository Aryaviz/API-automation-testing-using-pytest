import pytest


class TestAuthentication:
    """Test cases for authentication endpoint"""
    
    def test_create_token_with_valid_credentials(self, auth_client):
        """Test creating token with valid credentials"""
        response_data = auth_client.create_token()
        
        assert "token" in response_data, "Response should contain token"
        assert response_data["token"] is not None, "Token should not be None"
        assert len(response_data["token"]) > 0, "Token should not be empty"
        
        print(f"Successfully created token: {response_data['token'][:10]}...")

    def test_create_token_with_invalid_credentials(self, auth_client):
        """Test creating token with invalid credentials"""
        with pytest.raises(Exception) as exc_info:
            auth_client.create_token(username="invalid_user", password="invalid_pass")
        
        assert "Authentication failed" in str(exc_info.value)
        
        print("Correctly failed authentication with invalid credentials")


class TestGetBooking:
    """Test cases for GET /booking endpoint"""
    
    def test_get_all_booking_ids(self, booking_client):
        """Test getting all booking IDs"""
        response = booking_client.get_booking_ids()
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert isinstance(response.json(), list), "Response should be a list"
        assert len(response.json()) > 0, "Booking list should not be empty"
        
        # Verify structure of first booking ID
        first_booking = response.json()[0]
        assert "bookingid" in first_booking, "Each item should have bookingid"
        
        print(f"Retrieved {len(response.json())} booking IDs")   

        print("booking id arya " , first_booking)

    def test_get_specific_booking(self, booking_client, create_booking):
        """Test getting a specific booking by ID"""
        # Create a booking first
        booking_id, created_booking = create_booking()
        
        # Get the booking
        response = booking_client.get_booking(booking_id)
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        booking_data = response.json()
        assert booking_data["firstname"] == created_booking["booking"]["firstname"]
        assert booking_data["lastname"] == created_booking["booking"]["lastname"]
        assert booking_data["totalprice"] == created_booking["booking"]["totalprice"]
        
        print(f"Successfully retrieved booking ID: {booking_id}")    

class TestPutBooking:
    """Test cases for PUT /booking endpoint (requires authentication)"""
    
    def test_update_booking_with_valid_token(self, booking_client, auth_token, create_booking, test_data):
        """Test updating a booking with valid authentication token"""
        # Create a booking first
        booking_id, created_booking = create_booking()
        
        # Prepare updated data
        updated_data = test_data["updated_booking"]
        
        # Update the booking
        response = booking_client.update_booking(booking_id, updated_data, auth_token)
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        # Verify the update
        updated_booking = response.json()
        assert updated_booking["firstname"] == updated_data["firstname"]
        assert updated_booking["lastname"] == updated_data["lastname"]
        assert updated_booking["totalprice"] == updated_data["totalprice"]
        assert updated_booking["depositpaid"] == updated_data["depositpaid"]
        
        print(f"Successfully updated booking ID: {booking_id}")
    