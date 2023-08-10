from setuptools import setup, find_packages

import certbot_dns_dynv6

with open("README.md") as f:
    long_description = f.read()

setup(
    name="certbot_dns_dynv6",
    version=certbot_dns_dynv6.__version__,
    author="Mat1RX",
    url="https://github.com/Mat1RX/certbot_dns_dynv6",
    description="Obtain certificates using a DNS TXT record for DynV6 domains",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPL-3.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities",
        "Topic :: System :: Systems Administration"
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "certbot>=1.18.0,<3.0",
        "requests>=2.20.0,<3.0"
    ],
    entry_points={
        "certbot.plugins": [
            "dns-dynv6 = certbot_dns_dynv6.cert.client:Authenticator",
        ]
    }
)
