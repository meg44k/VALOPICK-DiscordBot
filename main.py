import discord
import discord.app_commands
import random
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

#discord
token = os.getenv('DISCORD_BOT_SECRET')
client = discord.Client(intents=discord.Intents.default())
tree = discord.app_commands.CommandTree(client)


@tree.command(
    name="valopic",
    description="ランダムでキャラを選びます。"
)
async def pick(ctx:discord.Integration):
    charactor_list = ["KAY-O","アストラ","ヴァイパー","オーメン","キルジョイ","サイファー","ジェット","スカイ","セージ","チェンバー","ネオン","ハーバー","フェイド","フェニックス","ブリーチ","ブリムストーン","ヨル","レイズ","レイナ","ソーヴァ","ゲッコー","デッドロック","アイソ","クローヴ"]
    charactor_length = len(charactor_list)
    random_charactor = random.randint(0,charactor_length - 1)
    await ctx.response.send_message("あなたが使うキャラクターは**【"+charactor_list[random_charactor]+"】**です。\n",file=discord.File("/discord-bot/MegaakBot/image/"+str(random_charactor)+".png"))

@tree.command(
    name="mappic",
    description="ランダムでマップを選びます。"
)
async def map(ctx:discord.Integration):
    map_list = ["アセント","ブリーズ","アイスボックス","バインド","スプリット","ロータス","サンセット"]
    map_length = len(map_list)
    random_map = random.radiant(0,map_length -1 )
    await ctx.response.send_message(f"{random_map}です")

@client.event
async def on_ready():
    await tree.sync()
    print("ready")
client.run(token)