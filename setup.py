from __future__ import print_function
import sys

from setuptools import setup, find_packages


def build_native(spec):
    cmd = ["cargo", "+nightly", "build", "--release"]

    build = spec.add_external_build(cmd=cmd, path="./rust")

    rtld_flags = ["NOW"]
    if sys.platform == "darwin":
        rtld_flags.append("NODELETE")
    spec.add_cffi_module(
        module_path="hypercore._lowlevel",
        dylib=lambda: build.find_dylib("hypercore", in_path="target/release"),
        header_filename=lambda: build.find_header("hypercore.h", in_path="include"),
        rtld_flags=rtld_flags,
    )


setup(
    name="hypercore",
    version="0.0.1",
    author="Luiz Irber",
    author_email="github@luizirber.org",
    license="BSD 3-clause",
    packages=find_packages(),
    zip_safe=False,
    platforms="any",
    install_requires=["milksnake"],
    setup_requires=["setuptools>=38.6.0", "milksnake"],
    include_package_data=True,
    milksnake_tasks=[build_native],
)
