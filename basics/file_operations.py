#!/usr/bin/env python

filename = "/tmp/test.txt"

f = open(filename, "a")

f.write("Hello this is a test file\n")

f.write("Take it easy")
f.write("open(\"text.txt\")")

f.close()

with open(filename, "r") as f:
    content = f.readlines()

f.close()
print("closed=", f.closed)

for c in content:
    print(c)
