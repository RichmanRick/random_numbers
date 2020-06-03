# The 5 Essential Data Structures
1. Device
2. Program
3. Command Queue
4. Kernel
5. Context

# Summary of Findings
## Find platforms and devices on host that support OpenCl:
_p = pyopencl.get_platforms()_ 
then for a particular platform 
_d = p.get_devices()_

## Create context made of devices:
_pyopencl.Context(devices=d)_

# Other things:
-NumPy library is pretty necessary for many of OpenCl operations

© 2020 GitHub, Inc.
