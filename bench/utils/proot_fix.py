import sys
import warnings

# Disable hiredis to avoid ENOSYS errors on PRoot/Termux
# This forces redis-py to use the pure Python parser which works fine in PRoot
sys.modules["hiredis"] = None

# Suppress fork warnings from rq which are noisy and not helpful in this context
# The warning is: DeprecationWarning: This process (pid=...) is multi-threaded, use of fork() may lead to deadlocks in the child.
warnings.filterwarnings("ignore", message=".*multi-threaded.*fork.*", category=DeprecationWarning)
