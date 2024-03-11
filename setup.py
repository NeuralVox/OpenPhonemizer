from setuptools import setup, find_packages

setup(
    name='openphonemizer',
    version='0.1.0',
    packages=find_packages(),
    author='mrfakename',
    author_email='me@mrfake.name',
    description='Permissively licensed, open sourced, local IPA Phonemizer (G2P) powered by deep learning.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/NeuralVox/OpenPhonemizer',
    license='BSD-3-Clause',
	classifiers=[
		'License :: OSI Approved :: BSD License',
	],
)
