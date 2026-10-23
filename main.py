
import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"PAK RW MLBB online sebagai {bot.user}")
    try:
        await bot.tree.sync()
        print("Slash commands berhasil disinkronkan")
    except Exception as e:
        print(f"Sync error: {e}")

@bot.tree.command(name="ktp", description="Lihat identitas anggota")
async def ktp(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🪪 KTP Warga PAK RW MLBB",
        color=discord.Color.dark_grey()
    )
    embed.add_field(name="Nama Discord", value=interaction.user.display_name)
    embed.add_field(name="ID Discord", value=str(interaction.user.id))
    embed.set_footer(text="Warga server .syntxrr")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="curhat", description="Mulai curhat dengan PAK RW")
async def curhat(interaction: discord.Interaction, pesan: str):
    await interaction.response.send_message(
        f"🏡 **PAK RW MLBB:** Terima kasih sudah cerita, {interaction.user.mention}.\n"
        f"Pak RW mendengarkan: *{pesan}*\n"
        "Semoga masalahmu segera membaik, ya!"
    )

@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! Latensi: {round(bot.latency * 1000)} ms")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN belum diatur di Render")

bot.run(TOKEN)
