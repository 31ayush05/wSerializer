from distutils.core import setup

setup(
    name='wSerializer',  # How you named your package folder (MyLib)
    packages=['wSerializer'],  # Chose the same as "name"
    version='0.7',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Library for saving data to text files which can then be retrieved afterwards',
    # Give a short description about your library
    author='Ayush Yadav',  # Type in your name
    author_email='ayush3105yadav@gmail.com',  # Type in your E-Mail
    url='https://github.com/31ayush05/wSerializer',  # Provide either the link to your github or to your website
    download_url='https://github.com/31ayush05/wSerializer/archive/refs/tags/v0.7.tar.gz',  # I explain this later on
    keywords=['wSerializer', 'save', 'load', 'Serialize', 'Deserialize'],  # Keywords that define your package best
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Specify which python versions that you want to support
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
