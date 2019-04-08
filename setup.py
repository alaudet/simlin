from setuptools import setup

version = '0.0.1'

setup(name='SIR',
      version=version,
      description='Simple Image Resizer for Linux',
      long_description=open("./README.md", "r").read(),
      classifiers=[
          "Development Status :: 1 - Planning",
          "Environment :: Console",
          "Intended Audience :: End Users/Desktop",
          "Natural Language :: English",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python :: 3",
          "Topic :: Multimedia :: Graphics :: Graphics Conversion",
          "License :: OSI Approved :: MIT License",
          ],
      author='Al Audet',
      author_email='alaudet@linuxnorth.org',
      url='https://www.linuxnorth.org/sir/',
      download_url='https://github.com/alaudet/sir/releases',
      license='MIT License',
      packages=['sir'],
      scripts=['bin/sir.py'],
      install_requires=['PIL']
)
