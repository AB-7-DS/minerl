import gym
import minerl
import numpy as np
import time  # <--- Import the time library

print("--- Preparing to launch MineRLBasaltMakeWaterfall-v0 ---")
env = gym.make("MineRLBasaltMakeWaterfall-v0")

print("\n--- Environment created. Starting simulation. ---")
obs = env.reset()

for i in range(30):
    action = env.action_space.sample()
    action['camera'] = [0, 0]
    action['jump'] = 1 if i % 15 == 0 else 0
    action['attack'] = 1 if i % 25 == 0 else 0

    obs, reward, done, info = env.step(action)
    env.render()

    # =========================================================
    # THE FIX: Add a small sleep to release the main thread
    time.sleep(0.05)  # Sleep for 10 milliseconds
    # =========================================================

    if done:
        print("--- Episode finished. Resetting environment. ---")
        obs = env.reset()

print("\n--- Simulation finished. Closing environment and window. ---")
env.close()