from setuptools import setup, find_packages

def get_long_description():
    with open('/workspace/README.md', 'r') as f:
        long_description = f.read()
    return long_description

setup(
    name='wwstatviz-webapp',
    version='0.1a0',
    license='License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    description='A web app package for world wide statistics visualization',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires = [
        'flask==1.1.2',
    ]
    classifiers=[
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/SophieManuel/Worldwide_statistics',
    author='Anas Zakroum, Sophie Manuel, Ravahere Paint-Koui, Seydou Sane',
    author_email='anaszkrm@protonmail.com',
    keywords='country map visualization statistics data web'
)
