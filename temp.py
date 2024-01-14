from pdf2image import convert_from_path
from collections import deque

A, B, C = "1층 4층", "2층 5층", "3층 6층"
floor = deque([A, B, C])

def lotate_order(floor):
    last = floor.pop() 
    floor.appendleft(last)
    return floor
