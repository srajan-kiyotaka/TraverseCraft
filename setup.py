from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='TraverseCraft',
    version='1.2.1',
    author='Srajan Chourasia, Varun Patrikar',
    author_email='srajanstark.ash@gmail.com, patrikarvarun@gmail.com',
    maintainer='Varun Patrikar, Srajan Chourasia',
    maintainer_email='patrikarvarun@gmail.com, srajanstark.ash@gmail.com',
    description='A Cross-Platform Real-Time Algorithm Simulation Tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://harrionparrix.github.io/traversecraft/',  # Official website
    project_urls={
        'Documentation': 'https://harrionparrix.github.io/traversecraft/user-guide/index.html',
        'Source': 'https://github.com/srajan-kiyotaka/TraverseCraft/tree/main',
        'Tracker': 'https://github.com/srajan-kiyotaka/TraverseCraft/issues',
        'Reference': 'https://harrionparrix.github.io/traversecraft/references/world/World.html',
    },
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'prettytable',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Education',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    keywords='algorithms, simulation, real-time, tkinter, education, research, visualization, machine learning, reinforcement learning, artificial intelligence, agent-based modeling, cross-platform, dynamic heatmap, world generation, customizable, interactive, framework, algorithm visualization, graph traversal, tree traversal, grid world',
)
