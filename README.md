# Regicide - Regents and Robots

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
- [x] Card, Regents(Enemies) and deck classes
- [x] Player hand management with auto-sorting
- [] Game state tracking
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
wip
```

## 🛠️ Installation

### Prerequisites
- Python 3.13+
- [UV](https://docs.astral.sh/uv/) package and project manager.

### Setup
```bash
# Clone the repository
git clone https://github.com/matth-dev/regicide.git
cd regicide

wip
```

## 🎯 Usage

### Playing the Game

### Training the AI

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

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Relevant papers or resources]
- [Inspiration from other projects]

## 📈 Roadmap

### Phase 1: Core Implementation (Weeks 1-4)
- [x] Basic game engine
- [ ] Complete rule implementation
- [x] CLI interface
- [ ] Solo-play
- [ ] Tests

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