from setuptools import setup

package_name = 'combined_launch'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your.email@example.com',
    description='Launch file for combined usb_cam and web_video_server',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
