#!/usr/bin/env python3

import sys

if int(sys.argv[1]) < 0:
  print("Energy must be positive")
  sys.exit(59)
else:
  sys.exit(0)
