import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.voice_states = True
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds)
    existing_channel = discord.utils.get(guild.voice_channels, name="Create Room")

    if not existing_channel:
        await guild.create_voice_channel("Create Room")

    print(f"Bot is online and ready in guild: {guild.name}")

@bot.event
async def on_voice_state_update(member, before, after):
    guild = member.guild

    if after.channel and after.channel.name == "Create Room":
        new_channel_name = f"{member.name}'s Room"
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            member: discord.PermissionOverwrite(view_channel=True, manage_channels=True, connect=True),
        }
        new_channel = await guild.create_voice_channel(new_channel_name, overwrites=overwrites)
        await member.move_to(new_channel)

    # Automatically mute the next user who joins the new room
    if after.channel and after.channel != before.channel:
        for user in after.channel.members:
            if user != member:
                await user.edit(mute=True)

    # Delete the created channel when the creator leaves
    if before.channel and before.channel.name == f"{member.name}'s Room" and len(before.channel.members) == 0:
        await before.channel.delete()

@bot.tree.command(name="private", description="Make your current voice channel private.")
async def private(interaction: discord.Interaction):
    if interaction.user.voice:
        channel = interaction.user.voice.channel
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(connect=False),
            interaction.user: discord.PermissionOverwrite(connect=True, manage_channels=True),
        }
        await channel.edit(overwrites=overwrites)

        embed = discord.Embed(
            title="Room Updated",
            description=f"The channel **{channel.name}** is now private.",
            color=0x800080
        )
        embed.set_footer(text="Private room enabled.")
        await interaction.response.send_message(embed=embed)

@bot.tree.command(name="public", description="Make your current voice channel public.")
async def public(interaction: discord.Interaction):
    if interaction.user.voice:
        channel = interaction.user.voice.channel
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(connect=True),
        }
        await channel.edit(overwrites=overwrites)

        embed = discord.Embed(
            title="Room Updated",
            description=f"The channel **{channel.name}** is now public.",
            color=0x800080
        )
        embed.set_footer(text="Public room enabled.")
        await interaction.response.send_message(embed=embed)

@bot.tree.command(name="change_room_name", description="Change the name of your voice channel.")
@app_commands.describe(new_name="The new name for your voice channel.")
async def change_room_name(interaction: discord.Interaction, new_name: str):
    if interaction.user.voice:
        channel = interaction.user.voice.channel
        await channel.edit(name=new_name)

        embed = discord.Embed(
            title="Room Renamed",
            description=f"The channel name is now **{new_name}**.",
            color=0x800080
        )
        embed.set_footer(text="Room name updated.")
        await interaction.response.send_message(embed=embed)

@bot.tree.command(name="force_mute", description="Force mute the next user who joins your voice channel.")
async def force_mute(interaction: discord.Interaction):
    if interaction.user.voice:
        channel = interaction.user.voice.channel
        await interaction.response.send_message(f"Next user to join **{channel.name}** will be muted automatically.")

        @bot.event
        async def on_voice_state_update(member, before, after):
            if after.channel == channel and len(channel.members) == 1:
                await member.edit(mute=True)

@bot.tree.command(name="help_embed", description="Shows help information for voice room commands.")
async def help_embed(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Room Management Commands",
        description="Manage your custom voice rooms with these commands:",
        color=0x800080
    )
    embed.add_field(name="/private", value="Make your room private.", inline=False)
    embed.add_field(name="/public", value="Make your room public.", inline=False)
    embed.add_field(name="/change_room_name <name>", value="Change your room's name.", inline=False)
    embed.add_field(name="/force_mute", value="Force mute the next user who joins.", inline=False)
    embed.set_footer(text="Enjoy managing your voice channels!", icon_url=interaction.user.avatar.url)

    await interaction.response.send_message(embed=embed)

bot.run("Bot_token")
