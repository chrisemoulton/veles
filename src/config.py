"""
Created on May 28, 2013

Global configuration variables.

@author: Kazantsev Alexey <a.kazantsev@samsung.com>
"""
import numpy


# Supported number types as OpenCL => numpy dictionary.
dtypes = {"float": numpy.float32, "double": numpy.float64}

# Current number type
dtype = "float"
#dtype = "double"

# CL defines
cl_defines = {"float": "#define dtype float",
              "double": "#pragma OPENCL EXTENSION cl_khr_fp64: enable\n"
                        "#define dtype double"}

# inline.py argument types
inline_types = {"float": "f", "double": "d"}
