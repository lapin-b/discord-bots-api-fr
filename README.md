# Discord Bot FR API
Une package en Python pour interagir avec l'API de DiscordBots-FR.

## Utilisation

### Installation

```bash
pip install discord-bot-fr-api
```

### Utilisation

#### Exemple d'utilisation sans shards et dans un event
```python
import DiscordBotsAPI

# bot est une instance de discord.ext.commands.Bot

@bot.event
async def on_server_join(server: discord.Server):
    DiscordBotsAPI.update_counter('Clef API', bot.user.id, len(bot.servers))
```

## Licence
Voir le fichier LICENSE