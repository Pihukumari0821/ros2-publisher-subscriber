from setuptools import find_packages, setup

package_name = 'pub_sub_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pihu-kumari',
    maintainer_email='kpihu0821@gmail.com',
    description='ROS 2 Publisher and Subscriber communication using Python',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        'publisher = pub_sub_demo.publisher:main',
        'subscriber = pub_sub_demo.subscriber:main',
    ],
          
    },
)
