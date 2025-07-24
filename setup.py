from setuptools import setup

setup(
    name='keyslide',
    version='0.3',
    entry_points={
        "console_scripts": [
            "keyslide.encrypt = keyslide:cli_encrypt",
            "keyslide.decrypt = keyslide:cli_decrypt"
        ],
    }
)