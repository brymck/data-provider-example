from setuptools import setup

setup(
    name='dataproviderexample',
    license='MIT',
    author='Bryan Lee McKelvey',
    author_email='bryan.mckelvey@gmail.com',
    url='https://github.com/brymck/data-provider-example',
    install_requires=[
        'boto3==1.9.210',
        'Flask==1.1.1.',
        'psycopg2==2.8.3',
    ],
)
