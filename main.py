import discord
from discord.ext import commands
import requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
h_d_k={
    "Clouds":"Bulutlu",
    "Snow" : "Karlı",
    "Rain" :"Yağmurlu",
    "Mist" : "Sisli",
    "Clear" : "Açık hava" ,
    "Drizzle" : "Hafif yağmur",
    "Thunderstorm" : "Gökgürültülü fırtına"
}
api_key = "ff4d0f71153fc14f03f0ef1410af08a9" 
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
    

def hava(sehir):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data["weather"][0]["main"] in h_d_k:
        return h_d_k[data["weather"][0]["main"]]
    else:
        return data["weather"][0]["main"]

def derece(sehir):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data["main"]["temp"]

def r_h(sehir):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data["wind"]["speed"]

def nem(sehir):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data["main"]["humidity"]

def basınc(sehir):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data["main"]["pressure"]

def b_s(sehir):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data["clouds"]["all"]

def hava_f(sehir):
    if hava(sehir)=="Bulutlu":
        with open('h_d_r\\6.png', 'rb') as f:
            picture = discord.File(f)
            return picture

    elif hava(sehir)=="Karlı":
        with open('h_d_r\\4.png', 'rb') as f:
            picture = discord.File(f)
            return picture  

    elif hava(sehir)=="Sisli":
        with open('h_d_r\\3.png', 'rb') as f:
            picture = discord.File(f)
            return picture
        
    elif hava(sehir)=="Açık hava":
        with open('h_d_r\\2.png', 'rb') as f:
            picture = discord.File(f)
            return picture 
            
    elif hava(sehir)=="Yağmurlu":
        with open('h_d_r\\5.png', 'rb') as f:
            picture = discord.File(f)
            return picture
        
    elif hava(sehir)=="Hafif yağmur":
        with open('h_d_r\\7.png', 'rb') as f:
            picture = discord.File(f)
            return picture
        
    elif hava(sehir)=="Gökgürültülü fırtına":
        with open('h_d_r\\1.png', 'rb') as f:
            picture = discord.File(f)
            return picture
        
@bot.command()
async def hava_d(ctx,sehir):
    await ctx.send(hava(sehir))
    if hava(sehir) in h_d_k.values():
        await ctx.send(file=hava_f(sehir)) 
    
@bot.command()
async def derece_g(ctx,sehir):
    await ctx.send(derece(sehir))

@bot.command()
async def r_h_g(ctx,sehir):
    await ctx.send(r_h(sehir))

@bot.command()
async def b_s_g(ctx,sehir):
    await ctx.send(b_s(sehir))

@bot.command()
async def nem_g(ctx,sehir):
    await ctx.send(nem(sehir))

@bot.command()
async def basınc_g(ctx,sehir):
    await ctx.send(basınc(sehir))
                   
@bot.command()
async def h_r_g(ctx,sehir):
    embed=discord.Embed(title="Hava durumu",color=discord.Color.red())
    embed.add_field(name=f"{sehir} hava durumu:",value=f"Hava:{hava(sehir)} , Derece:{derece(sehir)} , Nem:{nem(sehir)} , Bulut sayısı:{b_s(sehir)} , Basınç:{basınc(sehir)} , Rüzgar hızı:{r_h(sehir)}")
    await ctx.send(embed=embed)
    if hava(sehir) in h_d_k.values():
        await ctx.send(file=hava_f(sehir))


bot.run("Lütfen tokeninizi buraya giriniz.)
