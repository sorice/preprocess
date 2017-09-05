from distutils.core import setup
import setuptools
from setuptools import find_packages
from setuptools.command.build_ext import build_ext

#check if nltk is installed
NLTK_INSTALLED = True

try:
    import nltk
except ImportError:
    NLTK_INSTALLED = False
if not NLTK_INSTALLED:
    raise ImportError('nltk is not installed.')

# find external data and C libraries
def get_stanford_data():
    print('Please insert your full stanford postagger path!')
    stanford_pos_dir = input()
    eng_model_filename= stanford_pos_dir + 'models/english-left3words-distsim.tagger'
    my_path_to_jar= stanford_pos_dir + 'stanford-postagger.jar'
    print('The evaluation of your data could take some time. Wait please!')
    try:
        StanfordPOSTagger(model_filename=eng_model_filename, path_to_jar=my_path_to_jar)
    except LookupError:
        raise SkipTest('Package installation are stopped because one of the stanford parser or CoreNLP jars doesn\'t exist')

# find packages to be included. exclude benchmarks.
packages = setuptools.find_packages(exclude=['docs','notebooks'])

cmdclass = {"build_ext": build_ext}

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='textsim',
    version='0.1.0',
    description='Python library for text preprocessing and normalization.',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/sorice/preprocess',
    author='Abel Meneses-Abad',
    author_email='abelma1980@gmail.com',
    license='BSD',
    classifiers=[
        'Development Status :: 1 - Production',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Text Data Mining',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
    ],
    packages=packages,
    install_requires=[
        'numpy >= 1.7.0',
        'nltk >= 3.1',
    ],
    setup_requires=[
        'numpy >= 1.7.0'
    ],
    cmdclass=cmdclass,
    include_package_data=True,
    zip_safe=False
)

