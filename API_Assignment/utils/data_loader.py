import json
import os


class DataLoader:
    """Utility class to load test data from JSON files"""
    
    @staticmethod
    def load_json(file_name: str) -> dict:
        """
        Load JSON data from file
        
        Args:
            file_name: Name of the JSON file
        
        Returns:
            dict: Loaded JSON data
        """
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_path, "data", file_name)
        
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        return data
    
    @staticmethod
    def get_test_data(key: str = None):
        """
        Get test data from test_data.json
        
        Args:
            key: Optional key to get specific data
        
        Returns:
            Test data
        """
        data = DataLoader.load_json("test_data.json")
        
        if key:
            return data.get(key)
        return data
