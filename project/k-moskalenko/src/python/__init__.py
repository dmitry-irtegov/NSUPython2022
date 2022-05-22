import os
import sys

current_dir = os.path.dirname(__file__)
project_dir = os.path.join(current_dir, os.pardir, os.pardir)
build_dir = os.path.abspath(os.path.join(project_dir, 'build'))

sys.path.append(build_dir)
