import os
import random
import discord
from discord.ext import commands
import aux
import continue_ping

my_secret = os.environ['TOKEN']
bot = commands.Bot(command_prefix='/', description="Este es el bot de los Illuminatis")

@bot.command()
async def on_ready():
  await print(f'We have logged as {bot}')

@bot.command()
async def illuminati(ctx):
  illuminati_level = random.randint(1,999)
  embed = discord.Embed(title="NIVEL ILLUMINATI",color=discord.Color.red())
  embed.set_thumbnail(url="https://w0.peakpx.com/wallpaper/701/275/HD-wallpaper-anuel-aa-anuel-aa-illuminati-iluminai-karol-g.jpg")
  embed.add_field(name=f"{ctx.author.name} tu nivel de Illuminati es:", value=f"{illuminati_level}")
  if illuminati_level < 333:
    embed.add_field(name="flow",value=f"no eres illuminati gang, millo gang.")
    embed.set_image(url="https://lomasrankiao.net/wp-content/uploads/2020/04/anuel-aa-illuminati-video-photo-2020-lomasrankiao.jpg")
  elif illuminati_level < 666:
    embed.add_field(name="flow",value=f"Illuminati promedio.")
    embed.set_image(url="https://laverdadnoticias.com/__export/1589128322995/sites/laverdad/img/2020/05/10/anuel_aa_acusado_de_plagio_musical.jpg_478486366.jpg")
  else:
    embed.add_field(name="flow",value=f"Eres una :ram: Illuminati.")
    embed.set_image(url="https://i.ytimg.com/vi/XZCxvlxZKRc/maxresdefault.jpg")
    
  await ctx.send(embed=embed)

@bot.command()
async def reyes(ctx):
  embed = discord.Embed(title="Probervio", description=" ",color=discord.Color.red())
  embed.add_field(name="Los reyes con:", value="Los reyes.")
  embed.add_field(name="Los dioses con:", value="Los Dioses.")
  await ctx.send(embed=embed)

@bot.command()
async def tiros(ctx):
  num_tiros = random.randint(1,999)
  embed = discord.Embed(title=f"Tiroteo con Anuel", description=f"Anuel te metio {num_tiros} tiros.",color=discord.Color.red())
  embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/238/238547.png")
  if num_tiros < 333:
    #anuel contento
    embed.set_image(url="https://www.elnuevodia.com/resizer/aqwN7yVbPWWMaibkvj1hWNNEmCo=/1200x717/filters:quality(75):format(jpeg):focal(505x505:515x495)/cloudfront-us-east-1.images.arcpublishing.com/gfrmedia/TCNCOFMQMBDWPFV432JF6VUKI4.jpg")
  elif num_tiros < 666:
    #anuel intermedio
    embed.set_image(url="https://tn.com.ar/resizer/mNOBlDVa-uDB9vjtadPcocbMwiw=/767x0/smart/filters:quality(60)/cloudfront-us-east-1.images.arcpublishing.com/artear/ALJHUDBF7JBHPDI2FMNKMXODCY.jpg")
  else:
    #anuel diablo
    embed.set_image(url="https://i.imgur.com/paSU9Mg.png")
    
  await ctx.send(embed=embed)

@bot.command()
async def sabiduria(ctx):
  value = aux.get_quote()
  if value != False:
    foto = random.randint(1,3)
    embed = discord.Embed(title="Sabiduria de Anuel",color=discord.Color.red())
    embed.add_field(name=f"Cancion: {value[1]}", value=f'"{value[0]}"')

    if foto == 1:
      embed.set_image(url="https://i.ytimg.com/vi/DHlh-xE4g5s/maxresdefault.jpg")
    elif foto == 2:
      embed.set_image(url="https://sss.moda.pe/imagen/apaisado/anuel-aa-presume-su-tecnica-para-el-canto-6cdc9.jpg")
    else:
      embed.set_image(url="https://www.hola.com/us/images/0263-10ee84952e62-9682164bb90f-1000/square-480/anuel-aa-in-concert-brooklyn-ny.jpg")
    
    await ctx.send(embed=embed)
  else:
    await ctx.send(f"No soy illuminati :'(")

@bot.command()
async def karolg(ctx):
  rand = random.randint(1,3)
  embed = discord.Embed(title="Anuel y KarolG",color=discord.Color.red())
  embed.add_field(name="El rey Illuminati y KarolG terminaron hace:", value=f"{aux.calc_breakup()} días.")
  embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1473/1473881.png")
  if rand == 1:
    embed.set_image(url="https://c.tenor.com/qJfhRIE6OhIAAAAd/bailar-anuel-aa.gif")
  elif rand == 2:
    embed.set_image(url="https://c.tenor.com/VtoxIyJ5-6kAAAAC/anuelaa-karolg.gif")
  else:
    embed.set_image(url="https://c.tenor.com/oeYRl8cm_qoAAAAC/limpiar-dientes-anuel-aa.gif")
  await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
  embed = discord.Embed(title="Commands bot illuminati",color=discord.Color.red())
  embed.set_thumbnail(url="https://i1.sndcdn.com/artworks-000158485461-y0vdm8-t500x500.jpg")
  embed.add_field(name='"/sabiduria"', value="Para ver una frase inspiracional de Anuel.", inline=True)
  embed.add_field(name='"/tiros"', value="Para entrar a un tiroteo con Anuel.", inline=True)
  embed.add_field(name='"/karolg"', value="Para saber hace cuantos dias Anuel y la bebecita terminaron.", inline=True)
  embed.add_field(name='"/reyes"', value="Para averiguar con quien estan los reyes.", inline=True)
  embed.add_field(name='"/illuminati"', value="Para averiguar que nivel de illuminati tienes.", inline=True)
  await ctx.send(embed=embed)

continue_ping.keep_alive()
bot.run(my_secret)