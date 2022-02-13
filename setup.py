#Describes the metadata about your package#
import setuptools
setuptools.setup(
    name="cryptoCompare",
    version="1.0.0",
    description="Further learning project",
    packages=setuptools.find_packages("src"),
    package_dir={'':"src"})