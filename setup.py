setup(
    name="do-cli",
    version="1.0.0",
    description="A custom CLI for managing DigitalOcean resources",
    author="Connor O'Dea",
    author_email="cpodea5@gmail.com",
    url="https://github.com/connorodea/do-cli",
    packages=find_packages(),
    install_requires=["pydo", "click", "python-dotenv"],
    entry_points={
        "console_scripts": [
            "do-cli=do_cli:cli",
        ],
    },
)
