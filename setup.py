from setuptools import setup

with open("README.md", "r") as f:
    text = f.read()

setup(
    name='keyslide',
    version='0.7',
    entry_points={
        "console_scripts": [
            "keyslide.encrypt = keyslide:cli_encrypt",
            "keyslide.decrypt = keyslide:cli_decrypt"
        ],
    },
    long_description=text,
    description="Encrypt text by shifting keys on the QWERTY keyboard.",
    long_description_content_type="text/markdown"
)