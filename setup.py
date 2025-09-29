from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np
import sys
import os

# Thử bật OpenMP nếu compiler hỗ trợ
def get_openmp_args():
    if os.name == "nt":
        # MSVC
        return (["/openmp"], [])
    else:
        # gcc/clang
        return (["-fopenmp"], ["-fopenmp"])

extra_compile_args, extra_link_args = get_openmp_args()

ext = Extension(
    name="color_based_ga",
    sources=["color_based_ga.pyx"],
    include_dirs=[np.get_include()],
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args,
)

setup(
    name="color_based_ga",
    ext_modules=cythonize(
        [ext],
        compiler_directives={
            "language_level": 3,
            "boundscheck": False,
            "wraparound": False,
            "nonecheck": False,
            "cdivision": True,
            "initializedcheck": False,
            # enable OpenMP in prange code-gen
            "linetrace": False,
        },
    ),
    zip_safe=False,
)
