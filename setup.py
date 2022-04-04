from setuptools import find_packages, setup

setup(
        name='straight_ahead_hotline',
        version='1.0.0',
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            'straight_ahead_hotline',
            ],
        )

