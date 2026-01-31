import pytest

from api.endpoints.auth_endpoint import AuthEndpoints
from api.endpoints.booking_endpoint import BookingEndpoints
from utils.data_loader import DataLoader

@pytest.fixture(scope="session")
def auth_client():
    """Fixture for authentication client"""
    return AuthEndpoints()


@pytest.fixture(scope="session")
def auth_token(auth_client):
    """
    Fixture to get authentication token
    Returns a valid token for the session
    """
    token = auth_client.get_token()
    assert token is not None, "Failed to get authentication token"
    return token

@pytest.fixture(scope="session")
def booking_client():
    """Fixture for booking client"""
    return BookingEndpoints()

@pytest.fixture(scope="function")
def create_booking(booking_client):
    """
    Fixture to create a booking and return booking ID
    Automatically creates a booking before test and cleans up after
    """
    created_bookings = []
    
    def _create_booking(booking_data=None):
        if booking_data is None:
            booking_data = DataLoader.get_test_data("valid_booking")
        
        response = booking_client.create_booking(booking_data)
        assert response.status_code == 200, f"Failed to create booking: {response.text}"
        
        booking_id = response.json().get("bookingid")
        created_bookings.append(booking_id)
        
        return booking_id, response.json()
    
    yield _create_booking
    

@pytest.fixture(scope="function")
def test_data():
    """Fixture to provide test data"""
    return DataLoader.get_test_data()