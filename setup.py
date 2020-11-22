import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name = 'flask_uio',
    packages = ['flask_uio'],
    version = '0.1.0',
    license='MIT',
    description = 'Build user interface by implementing object',
    author = 'Men Sopheak',
    author_email = 'sopheakmen1970@gmail.com',
    long_description=README,
    long_description_content_type="text/markdown",
    url = 'https://github.com/mensopheak/flask_uio',
    keywords = ['html', 'element', 'ui', 'semantic-ui', 'fomantic-ui'],
    install_requires=['flask', 'Flask-WTF', 'requests', 'cryptography', 'Flask-SQLAlchemy'],
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',   
        'Programming Language :: Python :: 3.7',
    ],
)