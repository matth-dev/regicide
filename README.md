# Regicide - Kings and Robots

A Python implementation of Regicide with AI training capabilities using reinforcement learning.

## 🎯 Project Overview

This project implements a card game engine and trains an AI agent to play strategically using machine learning techniques. The goal is to create an AI that can learn optimal play strategies through self-play and human gameplay data.

## 🎮 Game Description

### Basic Rules
- **Players**: 2-4 players
- **Deck**: Standard 52-card deck
- **Objective**: [Describe the winning condition]
- **Gameplay**: [Brief description of core mechanics]

[Rules](https://www.regicidegame.com/site_files/33132/upload_files/RegicideRulesA4.pdf)

### Key Mechanics
- [ ] Card dealing and hand management
- [ ] Turn-based play system
- [ ] Scoring system
- [ ] Win/loss conditions
- [ ] Special rules or combinations

## 🚀 Features

### Core Game Engine
- [x] Card and deck classes
- [x] Player hand management with auto-sorting
- [x] Game state tracking
- [ ] Move validation system
- [ ] Scoring and win detection
- [ ] Game history logging

### AI Components
- [ ] Game state representation
- [ ] Action space definition
- [ ] Reward system design
- [ ] Neural network architecture
- [ ] Training pipeline
- [ ] Performance evaluation

### User Interface
- [ ] Command-line interface
- [ ] Game visualization
- [ ] Human vs AI gameplay
- [ ] Training progress monitoring

## 📁 Project Structure

```
card-game-ai/
├── src/
│   ├── game/
│   │   ├── __init__.py
│   │   ├── card.py              # Card and Deck classes
│   │   ├── player.py            # Player management
│   │   ├── game_engine.py       # Core game logic
│   │   └── rules.py             # Game rules and validation
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── agent.py             # AI agent implementation
│   │   ├── neural_network.py    # NN architecture
│   │   ├── training.py          # Training loops
│   │   └── evaluation.py        # Performance metrics
│   └── ui/
│       ├── __init__.py
│       ├── cli.py               # Command-line interface
│       └── visualizer.py        # Game state visualization
├── data/
│   ├── game_logs/               # Recorded gameplay
│   ├── models/                  # Trained AI models
│   └── training_data/           # Preprocessed training data
├── tests/
│   ├── test_game_engine.py
│   ├── test_ai_agent.py
│   └── test_integration.py
├── docs/
│   ├── game_rules.md
│   ├── ai_architecture.md
│   └── api_reference.md
├── requirements.txt
├── setup.py
└── README.md
```

## 🛠️ Installation

### Prerequisites
- Python 3.13+
- [UV](https://docs.astral.sh/uv/) package and project manager.

### Setup
```bash
# Clone the repository
git clone https://github.com/matth-dev/regicide.git
cd card-game-ai

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

## 🎯 Usage

### Playing the Game
```bash
# Human vs Human
python -m src.ui.cli --mode human

# Human vs AI
python -m src.ui.cli --mode vs-ai --ai-model models/best_model.pkl

# AI vs AI (for testing)
python -m src.ui.cli --mode ai-vs-ai
```

### Training the AI
```bash
# Start training from scratch
python -m src.ai.training --episodes 10000 --save-interval 1000

# Resume training from checkpoint
python -m src.ai.training --load-model models/checkpoint_5000.pkl --episodes 5000

# Evaluate trained model
python -m src.ai.evaluation --model models/best_model.pkl --games 1000
```

## 🧠 AI Architecture

### State Representation
- **Hand encoding**: [Describe how cards are represented]
- **Game state**: [Public information, turn phase, etc.]
- **History**: [Previous moves, if relevant]

### Action Space
- **Pass**: Skip turn (action 0)
- **Play cards**: Combinations of 1-4 cards (actions 1-N)
- **Total actions**: [Number based on hand size]

### Reward System
- **Immediate rewards**: [Points for successful plays]
- **Game completion**: [Win/loss bonuses]
- **Strategic bonuses**: [Penalties for poor play]

### Training Approach
- **Algorithm**: [PPO, DQN, A3C, etc.]
- **Self-play**: AI trains against previous versions
- **Curriculum learning**: Progressive difficulty increase
- **Experience replay**: Learning from past games

## 📊 Performance Metrics

### Training Metrics
- Win rate against random player
- Win rate against rule-based AI
- Average game length
- Training loss curves

### Evaluation Benchmarks
- [ ] Random baseline: [Target win rate]
- [ ] Rule-based AI: [Target win rate]
- [ ] Human players: [Target performance]
- [ ] Previous model versions: [Improvement tracking]

## 🔬 Experiments

### Completed
- [ ] Baseline random agent implementation
- [ ] Rule-based heuristic agent
- [ ] Basic neural network architecture

### In Progress
- [ ] Deep Q-Network (DQN) implementation
- [ ] Hyperparameter tuning
- [ ] Self-play training loop

### Planned
- [ ] Advanced architectures (Transformer, CNN)
- [ ] Multi-agent training environments
- [ ] Transfer learning experiments
- [ ] Human gameplay analysis

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation for API changes
- Use type hints where appropriate

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Relevant papers or resources]
- [Inspiration from other projects]
- [Special thanks to contributors]

## 📈 Roadmap

### Phase 1: Core Implementation (Weeks 1-4)
- [x] Basic game engine
- [ ] Complete rule implementation
- [ ] CLI interface
- [ ] Unit tests

### Phase 2: AI Foundation (Weeks 5-8)
- [ ] State representation design
- [ ] Basic AI agent
- [ ] Training infrastructure
- [ ] Evaluation framework

### Phase 3: Advanced AI (Weeks 9-12)
- [ ] Deep learning models
- [ ] Self-play training
- [ ] Performance optimization
- [ ] Comprehensive evaluation

### Phase 4: Polish & Analysis (Weeks 13-16)
- [ ] Advanced visualizations
- [ ] Strategy analysis tools
- [ ] Documentation completion
- [ ] Performance benchmarking

## 📞 Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/card-game-ai](https://github.com/yourusername/card-game-ai)

---

*Last updated: [Current Date]*