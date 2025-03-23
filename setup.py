from setuptools import setup, find_packages
import os
import sys
import subprocess

def post_install():
    """
    Post-installation script to run vibe start --global
    """
    print("\nInitializing vibe-coding-init-kit global settings...")
    try:
        # Try to import and run directly (more reliable)
        from vibe_coding_init_kit.cli.commands import start_command
        start_command(is_global=True)
    except Exception as e:
        print(f"Direct import failed: {e}")
        try:
            # Fallback: try running the command externally
            subprocess.run([sys.executable, "-m", "vibe_coding_init_kit.cli.main", "start", "--global"])
        except Exception as e2:
            print(f"Failed to initialize global settings: {e2}")
            print("Please run 'vibe start --global' manually to complete setup.")

# Run post-install script if installing in development mode
if len(sys.argv) > 1 and sys.argv[1] in ['develop', 'install']:
    # Register post-install hook to be run after setup
    from setuptools.command.develop import develop
    from setuptools.command.install import install

    class PostDevelopCommand(develop):
        def run(self):
            develop.run(self)
            self.execute(post_install, (), msg="Running post-installation script...")

    class PostInstallCommand(install):
        def run(self):
            install.run(self)
            self.execute(post_install, (), msg="Running post-installation script...")

    cmdclass = {
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    }
else:
    cmdclass = {}

setup(
    name="vibe-coding-init-kit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "vibe=vibe_coding_init_kit.cli.main:main",
        ],
    },
    python_requires=">=3.6",
    author="Vibe Coding Team",
    author_email="example@example.com",
    description="A toolkit for enhancing code maintainability through Windsurf/Cursor rules",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/vibe-coding-init-kit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    cmdclass=cmdclass,
)
