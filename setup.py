from setuptools import setup, find_packages

setup(
        name = "good_boids",
        version = "1.0.0",
        author = 'Gareth Jones',
        author_email = 'gareth.jones.16@ucl.ac.uk',
        license = 'The MIT License (MIT)',
        packages = find_packages(exclude=['*test']),
        scripts = ['scripts/good_boids'],
        install_requires = ['argparse', 'numpy', 'PyYaml', 'matplotlib']
)
