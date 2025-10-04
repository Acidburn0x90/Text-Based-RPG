# Text-Based RPG

A Python-based text adventure role-playing game that provides an immersive command-line gaming experience.

## 📖 Description

This project is a text-based RPG built in Python where players can embark on adventures, battle monsters, level up their characters, and explore a rich fantasy world through text-based interactions. The game features character creation, inventory management, combat systems, and story progression.

## 🚀 Features

- Character creation and customization
- Turn-based combat system
- Inventory and item management
- Experience and leveling system
- Story-driven gameplay
- Save/load game functionality
- Multiple character classes and abilities

## 📋 Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8 or higher
- Git

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Acidburn0x90/Text-Based-RPG.git
cd Text-Based-RPG
```

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Game

```bash
python main.py
```

## 📁 Project Structure

```
Text-Based-RPG/
├── src/                    # Source code modules
│   ├── __init__.py
│   ├── core/              # Core game systems
│   │   ├── __init__.py
│   │   ├── game_engine.py      # Main game loop and state management
│   │   ├── database.py         # Database models and operations
│   │   └── events.py           # Event system for game actions
│   ├── entities/          # Game entities
│   │   ├── __init__.py
│   │   ├── player.py           # Player class and methods
│   │   ├── npc.py              # Non-player characters
│   │   ├── items.py            # Items and equipment
│   │   └── locations.py        # Game world locations
│   ├── systems/           # Game systems
│   │   ├── __init__.py
│   │   ├── combat.py           # Combat mechanics
│   │   ├── inventory.py        # Inventory management
│   │   ├── progression.py      # Level/XP system
│   │   └── dialogue.py         # NPC dialogue system
│   ├── ai/                # AI integration
│   │   ├── __init__.py
│   │   ├── core.py             # AI core functions (existing)
│   │   ├── model.py            # AI models (existing)
│   │   ├── game_master.py      # AI game master logic
│   │   └── content_generator.py # Dynamic content generation
│   ├── ui/                # User interface
│   │   ├── __init__.py
│   │   ├── terminal_ui.py      # Terminal-based UI
│   │   ├── menus.py            # Game menus
│   │   └── display.py          # Display utilities
│   └── utils/             # Utilities
│       ├── __init__.py
│       ├── config.py           # Configuration management
│       ├── save_load.py        # Save/load functionality
│       └── helpers.py          # General helper functions
├── data/                   # Game data files
│   ├── characters.json    # Character templates
│   ├── items.json         # Item definitions
│   ├── locations.json     # World locations
│   └── dialogue.json      # Dialogue trees
├── assets/                 # Game assets
│   └── ascii_art/         # ASCII art files
├── saves/                  # Save game files
├── tests/                  # Unit tests
│   ├── __init__.py
│   ├── test_core/         # Core system tests
│   │   └── __init__.py
│   ├── test_entities/     # Entity tests
│   │   └── __init__.py
│   ├── test_systems/      # System tests
│   │   └── __init__.py
│   └── fixtures/          # Test data
├── docs/                   # Documentation
│   ├── api.md             # API documentation
│   ├── game_design.md     # Game design document
│   └── development.md     # Development guide
├── scripts/                # Utility scripts
│   ├── setup_db.py        # Database setup
│   └── generate_content.py # Content generation tools
├── venv/                   # Virtual environment (ignored)
├── main.py                 # Main game entry point
├── UI.py                   # Legacy UI code (to be refactored)
├── game-loop.prompt.yml    # AI game master configuration
├── game.db                 # SQLite database file
├── requirements.txt        # Project dependencies
├── requirements-dev.txt    # Development dependencies
├── .env.example           # Environment variables example
├── .gitignore             # Git ignore file
├── .pre-commit-config.yaml # Pre-commit hooks
├── pyproject.toml         # Python project configuration
├── Dockerfile             # Docker configuration
├── Makefile               # Build and development commands
└── README.md              # This file
```

## 🎮 How to Play

1. Run the game with `python main.py`
2. Create a new character or load an existing save
3. Choose your character class (Warrior, Mage, Rogue, etc.)
4. Follow the on-screen prompts to navigate through the adventure
5. Use commands like:
   - `look` - Examine your surroundings
   - `inventory` - Check your items
   - `stats` - View character statistics
   - `save` - Save your progress
   - `help` - Display available commands

## 🧪 Running Tests

To run the unit tests:

```bash
# Using pytest
pytest

# Using make (if available)
make test
```

## 🔧 Development

### Code Formatting and Linting

This project uses several tools to maintain code quality:

```bash
# Format code with isort and black
make format

# Lint code with ruff
make lint

# Run all quality checks
make quality
```

### Pre-commit Hooks

Pre-commit hooks are set up to automatically format and lint code before commits:

```bash
# Install pre-commit hooks
pre-commit install

# Run pre-commit on all files
pre-commit run --all-files
```

### Docker Support

To run the game in a Docker container:

```bash
# Build the Docker image
docker build -t text-based-rpg .

# Run the container
docker run -it text-based-rpg
```

## 📦 Dependencies

Main dependencies include:
- Standard Python libraries for core functionality
- Additional packages as specified in `requirements.txt`

Development dependencies:
- `pytest` - Testing framework
- `black` - Code formatter
- `isort` - Import sorter
- `ruff` - Fast Python linter
- `pre-commit` - Git hooks framework

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and ensure code quality checks pass
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Roadmap

- [ ] Enhanced combat mechanics
- [ ] Multiple story paths and endings
- [ ] Multiplayer support
- [ ] Web-based interface
- [ ] Sound effects and music
- [ ] Advanced character progression
- [ ] Guild and faction systems

## 🐛 Known Issues

- Save files are currently stored locally only
- Limited error handling for invalid user input
- Performance optimization needed for large inventories

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/Acidburn0x90/Text-Based-RPG/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about the problem and your environment

## 🙏 Acknowledgments

- Inspired by classic text-based adventure games
- Built following Python project setup best practices from [Sam Borms' article](https://medium.com/@sborms/setting-up-a-python-project-964997f3cf40)
- Community feedback and contributions

---

**Happy Gaming! 🎮**

*Start your adventure today and become the hero of your own story!*