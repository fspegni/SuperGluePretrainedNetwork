from setuptools import setup, find_packages

setup(
    name="SuperGluePretrainedNetwork",
    version="1.0",
    packages=find_packages(),
    py_modules=["SuperGluePretrainedNetwork"], 
    install_requires=[
        "torch",
        "opencv-python",
        "numpy",
        "matplotlib",
    ],
)
