from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'my_first_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
        glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='derrick',
    maintainer_email='derrick@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'hello_node = my_first_package.hello_node:main',
        'inspection_camera_node = my_first_package.inspection_camera_node:main',
        'inspection_node = my_first_package.inspection_node:main',
        'inspection_service = my_first_package.inspection_service:main',
        'inspection_parameter_node = my_first_package.inspection_parameter_node:main',
    ],
  },
)
