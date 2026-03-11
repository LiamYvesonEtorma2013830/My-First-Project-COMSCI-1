import time
import os

frames = [
"""
   🤑
  /|\\
  / \\
""",
"""
  \\🤑/
   |
  / \\
""",
"""
   🤑
  \\|/
  / \\
""",
"""
  /🤑\\
   |
  / \\
"""
]

while True:
    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        print(frame)
        print("I love dancing!🕺🕺💃💃")
        print("Press Ctrl+C to stop the dance.")
        time.sleep(0.25)