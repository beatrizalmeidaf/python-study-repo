import subprocess
import sys

result = subprocess.run([sys.executable, "-c", "raise ValueError('oops')"], check=True)

test = subprocess.run([sys.executable, "-c", "raise ValueError('oops')"])
test.check_returncode()