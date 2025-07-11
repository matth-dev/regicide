# Regicide - Regents and Robots

A Python implementation of the card game [Regicide](https://www.regicidegame.com) 

## 🎯 Project Overview

This project is the implementation of an existing card game called Regicide in python.

The goal of this project is to sharpen my Python skills by adapting a card game into a Python script, my data pipelines skills by generating and using game data and my Machine Learning (and/or Deep-Learning) skills by training AI agents to play this game. (Most probably with help from the [Gymnasium](https://gymnasium.farama.org/index.html#) API).

## 🎮 Game Description

### Basic Rules
- **Players**: 2-4 players (Can be played as one player, but it's very hard since I decided to not implement the Jester mechanics for solo play)
- **Deck**: Standard 52-card deck
- **Objective**: Kill all Regents (Face Cards)
- **Gameplay**: There are a total of 12 face cards to defeat (4 Jacks, Queens and Kings), each with their own health and attack value. Each turn a player choose a combination of cards to attack the current regent (or skip his/her turn) and then discard cards to mitigate the current regent attack. The game is over when a player cannot discard enough card (loss) or when all regents are defeated (win).

Find all the (better explained) [Rules](https://www.regicidegame.com/site_files/33132/upload_files/RegicideRulesA4.pdf).

## 📚 Stack

- Python (Game)
- JSON / CSV / Pandas (Game data)
- Pytorch / TensorFlow / Scikit-learn (AI models training)
- Gymnasium (AI Training)
- Pickle (AI models saving)

> May change and is not accurate, especially for AI training and game data management

## 📁 Project Structure

```
wip
```

## 🛠️ Installation

### Prerequisites
- Python 3.13+
- [UV](https://docs.astral.sh/uv/) package and dependencies manager.

### Setup
```bash
# Clone the repository
git clone https://github.com/matth-dev/regicide.git
cd regicide
uv sync
```

## 🎯 Usage

### Playing the Game

Run the following commands to play the game (You'll play as Alice)

```bash
cd regicide
uv run -m src.regicide.game.game
```

> As of right now, the game runs entirely in the console, making it challenging to track the actions, especially if you're unfamiliar with the game mechanics. Given that the main focus is on AI agent training, investing in a polished UI isn't imperative.

## 🤖 AI & Gymnasium Integration

This project is designed to be extended with AI agents using the [Gymnasium](https://gymnasium.farama.org/) API. Stay tuned for updates!

## 📅 Roadmap

- [x] Regicide game python Implementation
- [ ] Game state representation
- [ ] Game data generation
- [ ] Gymnasium implementation
- [ ] AI agents training
- [ ] AI agents evaluation
- [ ] Game can be play with very smart bots

## 💡 Inspirations / Acknowledgement

- [This video](https://youtu.be/DcYLT37ImBY) (Youtube) - [Link](https://github.com/PWhiddy/PokemonRedExperiments) to the project (Github)