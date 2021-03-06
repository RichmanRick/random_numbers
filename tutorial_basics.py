# Credit: Parallel Programming with (Py)OpenCL for Fun and Profit, via Youtube
	
import pyopencl as cl
import numpy as np

# code to run a kernel
def run_kernel(queue, kernel, global_size, input_tuples, output_tuples, local_size = (32,)):

	#copying data onto the device
	for (array, buffer) in input_tuples:
		cl.enqueue_copy(queue, src=array, dest=buffer)

	#running program on the device
	kernel_arguments = [buffer for (_,buffer) in input_tuples]
	kernel_arguments += [buffer for (_,buffer) in output_tuples] 
	kernel(queue, global_size, local_size, *kernel_arguments)

	#copying data off device
	for (arr, buffer) in output_tuples:
		cl.enqueue_copy(queue, src=buffer, dest=arr)
		
	#waiting for process to finish
	queue.finish()


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

# Creating data
N = int(2**20) # 2^20
a = np.random.rand(N).astype(int) # array of 2^20 random integers
b = np.random.rand(N).astype(int) 
c = np.empty_like(a) # destination array

# Device Memory setup
a_apple_buffer = cl.Buffer(apple_context, flags=cl.mem_flags.READ_ONLY, size=a.nbytes)
b_apple_buffer = cl.Buffer(apple_context, flags=cl.mem_flags.READ_ONLY, size=b.nbytes)
c_apple_buffer = cl.Buffer(apple_context, flags=cl.mem_flags.WRITE_ONLY, size=c.nbytes)

apple_queue = cl.CommandQueue(apple_context) # Create command queue associated with context












