import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
print __file__
print sys.path[0]
from bayesnet import bn


