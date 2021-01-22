# Every time a new file is created in the endpoint folder it must be added here
# this is because the main function calls "from endpoint import *" which pulls this list of modules
#__all__ = ["hello-world-endpoint"]

# insert wizardry here
from os.path import dirname, basename, isfile, join
import glob
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]