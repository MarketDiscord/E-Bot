import discord
from discord import app_commands, utils
from discord.app_commands import commands


class tiket_launcher(discord.ui.View):
    def __init__(self) -> None:
        super().__init(timeout = None)

    @discord.ui.button(label="Crée un tiket", custom_id="ticket_button", style=discord.ButtonStyle.blurple)

    async def ticket(self, interaction: discord.Interaction, button:discord.ui.Button):
        ticket = utils.get(interaction.guild.text_channels, name = f"ticket-for-{interaction.user.name}-{interaction.user.discrimanatior}")
        if ticket is not None: await interaction.response.send_message(f"You already have aticket open at {ticket.mention=}!", ephemeral = True )


class AClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=1046437841447686226))
            self.synced = True
        print(f"We have logged in as {self.user}.")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')

    async def on_member_join(self, member):
        print(member)


client = AClient()
tree = app_commands.CommandTree(client)


@tree.command(name="fact", description="Tells a TRUE fact", guild=discord.Object(id=1046437841447686226))
async def self(interaction: discord.Interaction, name: str, numb: int):
    await interaction.response.send_message(f"Suicidaul le pdddddddddd {name} {numb}")


@tree.command(name="clear", description="Clear messages", guild=discord.Object(id=1046437841447686226))
async def self(ctx, amount: int = None):  # Set default value as None
    await ctx.response.defer(ephemeral=True)
    if amount is None:
        await ctx.channel.purge(limit=1000000)
    else:
        try:
            int(amount)
        except Exception:  # Error handler
            await ctx.send('Please enter a valid integer as amount.')
        else:
            await ctx.followup.send(f"Cleared {amount} messages.", ephemeral=True)
            await ctx.channel.purge(limit=amount)


client.run("MTA1MTIwMjUxMDI5MzA1NzY0Nw.GviMZU.SRCECZQ8H5ezfW7LVOMszIpM4gQ48GPlka8H0w")