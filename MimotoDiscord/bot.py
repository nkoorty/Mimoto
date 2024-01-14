from discord.ext import commands
import aiohttp
import discord

API_ENDPOINT = 'http://127.0.0.1:5000/users/'
intents = discord.Intents.default()
intents.members = True
intents.message_content = True 
bot = commands.Bot(command_prefix='!', intents=intents)


async def get_user_data(username):
    async with aiohttp.ClientSession() as session:
        async with session.get(API_ENDPOINT + username) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None


@bot.command(name='paylinks')
async def paylinks(ctx):
    if not ctx.guild:
        await ctx.send("This command can only be used in a server.")
        return

    members = ctx.guild.members
    message = []
    for member in members:
        user_data = await get_user_data(member.name)
        if user_data:
            message.append(f"{member.display_name}: localhost:3000/pay/{user_data['username']}") # noqa
        else:
            message.append(f"{member.display_name} is not registered on Mimoto.") # noqa

    if message:
        await ctx.send("\n".join(message))
    else:
        await ctx.send("No payment links found for members in this server.")

bot.run('MTE5NjE0NTI4MTUyMDEwNzYzMQ.Gv58n1.xTjeaS4NJRyeVW_9nEp_ne36Tq9RoIyVhg7f04') # noqa
