class Location:
    def __init__(self, name: str, location_id: int, description: str, items: list = None, exits: list = None):
        self.name = name
        self.id = location_id
        self.description = description
        self.items = items if items is not None else []
        self.exits = exits if exits is not None else []
    
    def add_item(self, item: str):
        """Add an item to this location."""
        if item not in self.items:
            self.items.append(item)
    
    def remove_item(self, item: str):
        """Remove an item from this location."""
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def has_item(self, item: str) -> bool:
        """Check if location contains a specific item."""
        return item in self.items
    
    def add_exit(self, direction: str):
        """Add an exit direction to this location."""
        if direction not in self.exits:
            self.exits.append(direction)
    
    def remove_exit(self, direction: str):
        """Remove an exit direction from this location."""
        if direction in self.exits:
            self.exits.remove(direction)
    
    def has_exit(self, direction: str) -> bool:
        """Check if location has an exit in the specified direction."""
        return direction in self.exits
    
    def __str__(self) -> str:
        """String representation of the location."""
        return f"{self.name}\n{self.description}"
    
    def __repr__(self) -> str:
        """Developer representation of the location."""
        return f"Location(name='{self.name}', id={self.id}, items={self.items}, exits={self.exits})"
    
    def to_dict(self) -> dict:
        """Convert location to dictionary format."""
        return {
            "name": self.name,
            "ID": self.id,
            "description": self.description,
            "items": self.items,
            "exits": self.exits
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Create a Location instance from dictionary data."""
        return cls(
            name=data["name"],
            location_id=data["ID"],
            description=data["description"],
            items=data.get("items", []),
            exits=data.get("exits", [])
        )
