# Flappy Bird AI using Deep Q-Network (DQN)

An autonomous Flappy Bird agent built using **Deep Q-Learning (DQN)**, PyTorch, and Gymnasium. The agent learns to play through trial and error by interacting with the game environment and maximizing cumulative rewards.

## Gameplay Demo

[▶ Watch Gameplay Demo](https://github.com/user-attachments/assets/7b010e71-9b5b-46d5-a06e-3323d564fbc2)

## Tech Stack

- Python
- PyTorch
- Gymnasium
- Flappy Bird Gymnasium
- Pygame
- NumPy
- PyYAML

## Key Features

- Deep Q-Network for action-value prediction.
- Experience Replay for learning from past experiences.
- Target Network for stable Q-learning.
- Epsilon-Greedy strategy for exploration and exploitation.
- Model checkpoint saving and evaluation.
- Pygame gameplay visualization.

## DQN Architecture

| Layer | Configuration |
|---|---|
| Input | 12 state features |
| Hidden | 256 neurons, ReLU |
| Output | 2 action values |

## Project Structure

```text
Flappy_Bird/
├── agent.py
├── dqn.py
├── experience_replay.py
├── game_flappy_bird.py
├── parameters.yaml
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Flappy_Bird
```

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

**Train the agent:**

```bash
python agent.py flappybirdv0 --train
```

**Evaluate the trained agent:**

```bash
python agent.py flappybirdv0
```

**Play manually:**

```bash
python game_flappy_bird.py
```

Use the **SPACEBAR** to flap.

## Future Improvements

- Improve agent performance and consistency.
- Tune DQN hyperparameters.
- Visualize training progress.
- Compare against a random-action baseline.

---

**Author:** Shreeya Chakraborty

**GitHub:** [shriihphoria](https://github.com/shriihphoria)