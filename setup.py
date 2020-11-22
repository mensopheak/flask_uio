from setuptools import setup

setup(
    name = 'flask_uio',
    packages = ['flask_uio'],
    version = '1.0.0',
    license='MIT',
    description = 'Build user interface by implementing object',
    author = 'Men Sopheak',
    author_email = 'sopheakmen1970@gmail.com',
    url = 'https://github.com/mensopheak/html_elementor',
    keywords = ['html', 'element', 'ui'],
    install_requires=['flask', 'flask-wtf', 'requests', 'cryptography', 'flask-sqlalchemy'],
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',   
        'Programming Language :: Python :: 3.7',
    ],
)