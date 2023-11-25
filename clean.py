#!/usr/bin/python3
import subprocess

if __name__ == "__main__":
    subprocess.run('rm *.out *.in', shell=True)
    subprocess.run('rm -r test_cases', shell=True)