import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="game"
    version="0.0.1",
    author="Cody",
    author_email="",
    url="https://github.com/yourusername/game",
    description="what does game do?",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
