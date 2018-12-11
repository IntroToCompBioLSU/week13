#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

rng = np.arange(50)
rnd = np.random.randint(0, 10, size=(3, rng.size))
yrs = 1950 + rng