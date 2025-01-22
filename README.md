# D-Study-App

Here’s a fancy-looking README for your GitHub repository that explains the features and usage of your bot. You can copy this into the `README.md` file of your repository.

```markdown
# 🎤 Discord Voice Room Manager Bot 🎤

A powerful and easy-to-use Discord bot that allows users to manage their voice channels with ease. This bot offers several features like creating private rooms, force muting users, changing room names, and even setting your nickname as "AFK" when you need to step away.

## Features ✨

- **Create Custom Voice Rooms**: Create a custom voice channel whenever you join the "Create Room" channel.
- **Force Mute**: Force mute the next user who joins your voice channel.
- **Private & Public Rooms**: Make your voice channel private or public with just one command.
- **Change Room Name**: Change the name of your voice channel to whatever you'd like.
- **AFK Mode**: Mark yourself as "AFK" by changing your nickname and automatically revert it when you send a message.
- **Unmute**: Undo the force mute and allow everyone to speak again.

## Commands 📜

### `/private`
Make your current voice channel **private** so only you can connect to it.

### `/public`
Make your current voice channel **public**, allowing anyone to join.

### `/force_mute`
Force mute all members in your voice channel and automatically mute anyone who joins next.

### `/unmute`
Allow everyone in the voice channel to speak again.

### `/afk`
Set your nickname to "[AFK] YourName" to indicate you’re away. Your nickname will revert back to normal when you send a message.

### `/change_room_name <new_name>`
Change the name of your current voice channel to **new_name**.

### `/help_embed`
Displays a helpful guide of all available commands.

## Installation 🛠️

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/discord-voice-room-manager.git
   cd discord-voice-room-manager
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your bot:
   - Create a bot on the [Discord Developer Portal](https://discord.com/developers/applications).
   - Get your bot token and replace the `YOUR_BOT_TOKEN` placeholder in the script with your token.

4. Run the bot:
   ```bash
   python bot.py
   ```

## Requirements 🧰

- Python 3.8 or higher
- `discord.py` library
  - Install it by running `pip install discord.py`
  
## Permissions ⚙️

For this bot to function correctly, make sure the bot has the following permissions in the server:
- **Manage Nicknames**: To change users' display names when they use the `/afk` command.
- **Manage Channels**: To create, delete, and edit voice channels.
- **Mute Members**: To mute members when using `/force_mute`.
- **View Channels**: To view and manage channels in the server.

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support 💬

If you encounter any issues or need help, feel free to open an issue on the [GitHub repository](https://github.com/yourusername/discord-voice-room-manager/issues).

---

Enjoy managing your voice channels with ease! 😎🎧
```
