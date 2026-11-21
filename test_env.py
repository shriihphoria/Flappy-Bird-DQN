
import gymnasium as gym
import flappy_bird_gymnasium

env = gym.make("FlappyBird-v0")

try:
    state, info = env.reset()

    for step in range(10000):
        action = env.action_space.sample()

        state, reward, terminated, truncated, info = env.step(action)

        if step % 100 == 0:
            print(f"Step: {step}, Reward: {reward}")

        if terminated or truncated:
            state, info = env.reset()

finally:
    env.close()
