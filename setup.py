from __future__ import print_function
import os
import sys

from setuptools import setup, find_packages


def build_native(spec):
    cmd = ["cargo", "+nightly", "build"]

    if os.environ.get("RUST_BACKTRACE", "false") in ("true", "1", "full"):
        dylib_folder = "target/debug"
    else:
        dylib_folder = "target/release"
        cmd.append("--release")

    build = spec.add_external_build(cmd=cmd, path="./rust")

    spec.add_cffi_module(
        module_path="hypercore._native",
        dylib=lambda: build.find_dylib("hypercore", in_path=dylib_folder),
        header_filename="rust/include/hypercore.h",
        rtld_flags=["NOW", "NODELETE"],
    )


setup(
    name="hypercore",
    author="Luiz Irber",
    author_email="github@luizirber.org",
    license="BSD 3-clause",
    packages=find_packages("src"),
    package_dir={"": "src"},
    zip_safe=False,
    platforms="any",
    install_requires=["milksnake"],
    setup_requires=["setuptools>=38.6.0", "setuptools_scm != 1.12.0", "milksnake"],
    include_package_data=True,
    use_scm_version={"write_to": "src/hypercore/version.py"},
    milksnake_tasks=[build_native],
)
