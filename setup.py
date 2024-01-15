from setuptools import setup, find_packages

def load_requirements(filename='requirements.txt'):
    with open(filename, 'r') as file:
        return file.read().splitlines()


setup(
    name='YOLOv7Detector',
    version='0.1',
    packages=find_packages(),
    description='A simple Wrapper for YOLOv7',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Stefan Saoulis',
    author_email='stefan.sooley@gmail.com',
    url='https://github.com/yourusername/your_package_name',
    install_requires=load_requirements(),
    python_requires='>=3.6',
)
