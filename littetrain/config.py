import os

INPUT_PIN = int(os.environ.get('INPUT', 0))

OUTPUT_PIN = int(os.environ('OUTPUT', 0))

TIMER = int(os.environ('TIMER', 10))

BOUNCE_TIME = float(os.environ('BOUNCE_TIME'), 0.05)