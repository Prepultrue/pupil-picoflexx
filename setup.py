from Cython.Build import cythonize
from Cython.Distutils import Extension
from distutils.core import setup

extensions = [
    Extension(
        'roypy_backend', ['roypycy.pyx'],
        library_dirs=['.'],
        libraries=['royale'],
        include_dirs=['include'],
        language='c++',
    )
]

setup(
    name="Pico Flexx",
    ext_modules=cythonize(extensions),
)
