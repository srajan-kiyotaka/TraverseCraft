from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='TraverseCraft',
    version='0.4.5',
    author='Srajan Chourasia, Varun Patrikar',
    author_email='srajanstark.ash@gmail.com, patrikarvarun@gmail.com',
    maintainer='Srajan Chourasia, Varun Patrikar',
    maintainer_email='srajanstark.ash@gmail.com, patrikarvarun@gmail.com',
    description='TraverseCraft: Cross-Platform Real-Time Algorithm Simulation Tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://official-website.com',  # Official website
    project_urls={
        'Documentation': 'https://docs.traverseCraft.com',
        'Source': 'https://github.com/srajan-kiyotaka/TraverseCraft/tree/main',
        'Tracker': 'https://github.com/srajan-kiyotaka/TraverseCraft/tree/main/issues',
        'Reference': 'https://reference.traverseCraft.com',
    },
    package_dir={'': 'traverseCraft'},
    packages=find_packages(where='traverseCraft'),
    python_requires='>=3.6',
    install_requires=[
        'prettytable',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Education',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    keywords='algorithms, simulation, real-time, tkinter, education, research, visualization, machine learning, reinforcement learning, artificial intelligence, agent-based modeling, cross-platform, dynamic heatmap, world generation, customizable, interactive, framework, algorithm visualization, graph traversal, tree traversal, grid world',
)