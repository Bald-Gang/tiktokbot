import os
import sys

def main():
    if len(sys.argv) == 2:
        print("video: " + sys.argv[1])
    else:
        print("please input a video link")

main()