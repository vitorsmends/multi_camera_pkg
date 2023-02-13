from setuptools import setup
import os
from glob import glob

package_name = 'multi_camera_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vitor',
    maintainer_email='joao.mendes@fbter.org.br',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'camera_1 = multi_camera_pkg.camera_pub_1:main',
            'camera_2 = multi_camera_pkg.camera_pub_2:main',
            'camera_3 = multi_camera_pkg.camera_pub_3:main',
        ],
    },
)
