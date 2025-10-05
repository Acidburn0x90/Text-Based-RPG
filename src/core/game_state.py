import json
import os
from src.entities.Player import Player
from src.entities.Location import Location

class GameState:
    def __init__(self):
        # Player
        self.player = Player()
        
        # Status
        self.location = 1
        
        
        # General game state attributes
        self.enemies = []
        self.locations = []
        
        
        # Load locations from JSON file
        self.load_locations()
        
    def load_locations(self):
        """Load locations from the JSON file and store them in the locations list."""
        locations_file = os.path.join(os.path.dirname(__file__), '..', 'Data', 'locations.json')
        
        try:
            with open(locations_file, 'r') as file:
                locations_data = json.load(file)
                
            self.locations = []
            for location_data in locations_data:
                location = Location.from_dict(location_data)
                self.locations.append(location)
                
        except FileNotFoundError:
            print(f"Error: Could not find locations file at {locations_file}")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {locations_file}")
        except Exception as e:
            print(f"Error loading locations: {e}")
    
    def get_current_location(self) -> Location:
        """Get a location by its ID."""
        for location in self.locations:
            if location.id == self.location:
                return location
        
    def move_player(self, new_location):
        self.player.location = new_location
        
        

global_game_state = GameState()