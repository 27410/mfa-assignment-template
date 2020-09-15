
###### Ignore this
import pytest
import hashlib
_ = 123456789  # just a wrong number, please ignore
###### Stop ignoring

import numpy as np

# Metabolic Flux Analysis

# 1. Write down the stoichiometry matrix S for the model as a numpy array.

# replace [[]] with the stoichiometric matrix.
S = np.array([[]])

###### Don't touch
def test_stoichiometry_matrix():
    assert hashlib.md5(S).digest() == b'\xe2Q(\xd6\xf1\x8f.7F\xfbB(\xabY\xf8\xcc'
###### this


# 2. Calculate how many fluxes need to be measured (degrees of freedom).

# Assign your solution to the following variable (replace _ with your solution;
# cannot be just a number; should be a computation based on S)

degrees_of_freedom = _

###### Don't touch
def test_degrees_of_freedom():
    assert degrees_of_freedom == 3
###### this


# 3. Based on measured fluxes v4 = 2, v5 = 10, and v6 = 0.5, calculate v1-v3.

# Put you're intermediate steps here ...


# Assign the final solution here (replace _ with your final step)
# v_c needs to be a numpy.array containing the three calculated fluxes v1-v3
# Ideally you should get to v_c through a computation involving S and the
# measured fluxes v4-v6 as covered in the lecture.

v_c = _

###### Don't touch
def test_mfa_calculation():
    assert v_c.sum() == 15.5
###### this
