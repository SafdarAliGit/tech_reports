from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tech_reports/__init__.py
from tech_reports import __version__ as version

setup(
	name="tech_reports",
	version=version,
	description="this is tech reports",
	author="safdar211@gmail.com",
	author_email="safdar211@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
