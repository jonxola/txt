import setuptools

setuptools.setup(
    name = 'txt',
    description = 'Turn an image into text art!',
    packages = setuptools.find_packages(),
    install_requires = [
        'Pillow==8.1.2'
    ],
    entry_points = {
        'console_scripts': [
            'txt = txt.core:txt'
        ]
    }
)