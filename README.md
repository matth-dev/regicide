# Regicide - Regents and Robots

A Python implementation of the card game [Regicide](https://www.regicidegame.com) 

## 🎯 Project Overview

This project is the implementation of an existing card game called Regicide in python. 
The goal of this project is to then train AI agents to play this game with machine learning and/or deep-learning (Most probably with the [Gymnasium](https://gymnasium.farama.org/index.html#) API).

This repo is the first part of an on-going project but can be launched independently

## 🎮 Game Description

### Basic Rules
- **Players**: 2-4 players (Can be played as one player but it's very hard since I decided to not implement the Jester mechanics for solo play)
- **Deck**: Standard 52-card deck
- **Objective**: Kill all Regents (Face Cards)
- **Gameplay**: There are a total of 12 face cards to defeat (4 Jacks, Queens and Kings), each with their own health and attacks. Each turn a player choose a combination of cards to attack the current regent (or skip his/her turn) and then discard cards to mitigate the current regent' attack. The game is over if a player cannot discard enough card or when all regents are defeated (This is called a Regicide).

Find all the (better explained) [Rules](https://www.regicidegame.com/site_files/33132/upload_files/RegicideRulesA4.pdf).

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
uv sync
```

## 🎯 Usage

### Playing the Game

Do the following commands to play the game (You'll play as Alice)

```bash
cd regicide
uv run -m src.regicide.game.game
```

## 🤖 AI & Gymnasium Integration

This project is designed to be extended with AI agents using the [Gymnasium](https://gymnasium.farama.org/) API. Stay tuned for updates!