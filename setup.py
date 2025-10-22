from setuptools import setup

setup(
    name='gopu',
    version='1.0.0',
    py_modules=['gopu'],
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'gopu = gopu:main',
        ],
    },
    author='Ceose',
    description='GopuOS CLI — Agent terminal pour introspection, IA, tokens et cloud agentique',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.6',
)
