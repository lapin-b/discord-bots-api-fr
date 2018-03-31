from setuptools import setup, find_packages

setup(
    name="discord-bot-fr-api",
    version='1.0.0',
    description="Permet d'interagir avec l'API de DiscordBots-FR",
    url="https://github.com/lapin-b/discord-bots-api-fr",
    license="LGPL-3.0",

    author="l4p1n",
    author_email="contact@l4p1n.met-hardware.fr",

    keywords="discord bot api fr",

    packages=["DiscordBotsAPI"],

    project_urls={
        'Bug reports': "https://github.com/lapin-b/discord-bots-api-fr/issues",
        'Source': 'https://github.com/lapin-b/discord-bots-api-fr'
    }
)