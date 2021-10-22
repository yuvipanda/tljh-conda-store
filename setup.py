from setuptools import setup, find_packages

setup(
    name="tljh-conda-store",
    author="YuviPanda",
    version="0.1",
    license="3-clause BSD",
    url='https://github.com/yuvipanda/tljh-conda-store',
    entry_points={"tljh": ["conda-store = tljh_conda_store"]},
    packages=find_packages()
)