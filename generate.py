#!/usr/bin/python3
import subprocess

size_config = {
    "small": 1000,
    "medium": 200,
    "large": 5
}

generate_config = {
    "small": True,
    "medium": True,
    "large": True
}

def generate(size):
    print(f"generating {size} input with {size_config[size]} sets")
    subprocess.run(f"python3 input_generator.py -s {size_config[size]} -as {size}", shell=True)

if generate_config["small"]:
    generate("small")

if generate_config["medium"]:
    generate("medium")

if generate_config["large"]:
    generate("large")