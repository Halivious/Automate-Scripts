from pathlib import Path
import glob


image_dir= Path("/home/Halivious/Desktop/Labeled/")
count = len(list(image_dir.glob('*.txt')))
print(count)
