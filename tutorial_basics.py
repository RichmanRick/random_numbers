import pyopencl as cl
import numpy as np

ocl_platforms = (platform.name
	for platform in cl.get_platforms())
print("\n".join(ocl_platforms)) # three platforms: Portable Computing Language, Apple, Oclgrind

apple_platform = [platform
	for platform in cl.get_platforms()
		if platform.name == "Apple"][0]

apple_devices = apple_platform.get_devices() # selecting devices of Apple platform
apple_context = cl.Context(devices=apple_devices) # create context, which "holds" the (apple) devices
# kernel/function source code to do vector sum
program_source = """
	kernel void sum(global float *a,
					global float *b,
					global float *c)
	{
		int gid = get_global_id(0);
		c[gid] = a[gid] + b[gid];
	}
	"""
apple_program_source = cl.Program(apple_context, program_source) # program made for context, using written kernel
apple_program = apple_program_source.build() # build the program
# next step is to 















