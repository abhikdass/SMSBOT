import requests
import json
from pyrogram import Client, filters
from pykeyboard import InlineKeyboard
from pyrogram.types import InlineKeyboardButton
from datetime import datetime
import os

# Load sensitive information from environment variables
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
auth_token = os.getenv("AUTH_TOKEN")

app = Client("SMSBOT", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command(["list", "list@SMSBOT"]))
async def listhandler(client, message):
    await message.reply_text(
        "1688\n1xbet\n23red\n32red\n888casino\n99app\nace2three\nadidas\nagroinform\nairbnb\nairtel\naitu\nakelni\nalfa\nalgida\nalibaba\naliexpress\nalipay\namasia\namazon\naol\napple\nastropay\nauchan\navito\navon\nazino\nb4ucabs\nbaidu\nbanqi\nbigolive\nbillmill\nbisu\nbitaqaty\nbitclout\nbittube\nblablacar\nblizzard\nblockchain\nblued\nbolt\nbrand20ua\nburgerking\nbykea\ncafebazaar\ncaixa\ncareem\ncarousell\ncdkeys\ncekkazan\ncitaprevia\ncitymobil\nclickentregas\ncliqq\nclubhouse\ncmtcuzdan\ncoinbase\ncoinfield\ncraigslist\ncryptocom\ndbrua\ndeliveroo\ndelivery\ndent\ndhani\ndidi\ndigikala\ndiscord\ndisneyhotstar\ndivar\ndixy\ndodopizza\ndomdara\ndominospizza\ndostavista\ndouyu\ndream11\ndrom\ndrugvokrug\ndukascopy\neasypay\nebay\nebikegewinnspiel\nedgeless\nelectroneum\neneba\nezbuy\nfaberlic\nfacebook\nfiqsy\nfiverr\nfoodpanda\nfoody\nforwarding\nfreecharge\ngalaxy\ngamearena\ngameflip\ngamekit\ngamer\ngcash\nget\ngetir\ngett\ngg\ngittigidiyor\nglobal24\nglobaltel\nglobus\nglovo\ngoogle\ngrabtaxi\ngreen\ngrindr\nhamrahaval\nhappn\nharaj\nhepsiburadacom\nhezzl\nhily\nhopi\nhqtrivia\nhumblebundle\nhumta\nhuya\nicard\nicq\nicrypex\nifood\nimmowelt\nimo\ninboxlv\nindriver\nininal\ninstagram\niost\niqos\nirancell\nivi\niyc\njd\njkf\njustdating\njustdial\nkakaotalk\nkarusel\nkeybase\nkomandacard\nkotak811\nkucoinplay\nkufarby\nkvartplata\nkwai\nlazada\nlbry\nlenta\nlianxin\nline\nlinkedin\nlivescore\nmagnit\nmagnolia\nmailru\nmamba\nmcdonalds\nmeetme\nmega\nmercado\nmichat\nmicrosoft\nmiloan\nmiratorg\nmobile01\nmomo\nmonese\nmonobank\nmosru\nmrgreen\nmtscashback\nmyfishka\nmyglo\nmylove\nmymusictaste\nmzadqatar\nnana\nnaver\nncsoft\nnetflix\nnhseven\nnifty\nnike\nnimses\nnrjmusicawards\nnttgame\nodnoklassniki\nofferup\noffgamers\nokcupid\nokey\nokta\nolacabs\nolx\nonlinerby\nopenpoint\noraclecloud\noriflame\nother\nozon\npaddypower\npairs\npapara\npaxful\npayberry\npaycell\npaymaya\npaypal\npaysend\npaytm\npeoplecom\nperekrestok\npgbonus\npicpay\npof\npokec\npokermaster\npotato\npowerkredite\nprajmeriz2020\npremiumone\nprom\nproton\nprotonmail\nprotp\npubg\npureplatfrom\npyaterochka\npyromusic\nq12trivia\nqiwiwallet\nquipp\nrakuten\nrambler\nrediffmail\nreuse\nripkord\nrosakhutor\nrsa\nrutube\nsamokat\nseosprint\nsheerid\nshopee\nsignal\nsikayetvar\nskout\nsnapchat\nsnappfood\nsneakersnstuff\nsocios\nsportmaster\nspothit\nssoidnet\nsteam\nsurveytime\nswvl\ntaksheel\ntango\ntantan\ntaobao\ntelegram\ntencentqq\nticketmaster\ntiktok\ntinder\ntosla\ntotalcoin\ntouchance\ntrendyol\ntruecaller\ntwitch\ntwitter\nuber\nukrnet\nuploaded\nvernyi\nvernyj\nviber\nvitajekspress\nvkontakte\nvoopee\nwechat\nweibo\nweku\nweststein\nwhatsapp\nwildberries\nwingmoney\nwinston\nwish\nwmaraci\nwolt\nyaay\nyahoo\nyalla\nyandex\nyemeksepeti\nyoudo\nyoula\nyoustar\nzalo\nzoho\nzomato\n\n\nother for other sites\n**SEND /otp sitename**"
    )

@app.on_message(filters.command(["otp", "otp@SMSBOT"]))
async def otphandler(client, message):
    product = " ".join(message.command[1:])
    keyboard = InlineKeyboard()
    keyboard.row(InlineKeyboardButton('INDIA', f"country,india,{product}"))
    keyboard.row(InlineKeyboardButton('USA', f"country,usa,{product}"))
    keyboard.row(InlineKeyboardButton('RUSSIA', f"country,russia,{product}"))
    await message.reply_text("Select The Country Name", reply_markup=keyboard)

@app.on_callback_query()
async def callbackupdates(client, query):
    if "country" in query.data:
        c = query.data.split(',')
        i = await country(c[1], c[2])
        y = json.loads(i)
        await query.message.reply_text(
            f"You have successfully got a number\n**Number:** {y['phone']}\n**ID:** {y['id']}\n**PRODUCT:** {y['product']}\n**STATUS:** {y['status']}"
        )
        await query.message.delete()
    elif "refresh" in query.data:
        id = query.data.split(":")[1]
        idchek = await idcheck(id)
        idche = json.loads(idchek)
        now = datetime.now().strftime("%H:%M:%S")
        h = InlineKeyboard()
        h.row(InlineKeyboardButton('Refresh', f"refresh:{id}"))
        await query.message.reply_text(
            f"Your Id details {now}:\n**Number:** {idche['phone']}\n**PRODUCT:** {idche['product']}\n**ID:** {id}\n**STATUS:** {idche['status']}\n**SMS:** {idche['sms']}",
            reply_markup=h
        )
        await query.message.delete()

@app.on_message(filters.command(["id", "id@SMSBOT"]))
async def idhandler(client, message):
    id = " ".join(message.command[1:])
    idchek = await idcheck(id)
    idche = json.loads(idchek)
    now = datetime.now().strftime("%H:%M:%S")
    h = InlineKeyboard()
    h.row(InlineKeyboardButton('Refresh', f"refresh:{id}"))
    await message.reply_text(
        f"Your Id details {now}:\n**Number:** {idche['phone']}\n**PRODUCT:** {idche['product']}\n**ID:** {id}\n**STATUS:** {idche['status']}\n**SMS:** {idche['sms']}",
        reply_markup=h
    )

@app.on_message(filters.command(["split", "split@SMSBOT"]))
async def split(client, message):
    if not message.reply_to_message:
        await message.reply("Please use this command while replying to the file to split.")
        return

    path = message.reply_to_message.document.file_name
    await message.reply_to_message.download("./")
    lines_per_file = int(" ".join(message.command[1:]))
    allfiles = []

    with open(path) as bigfile:
        for lineno, line in enumerate(bigfile):
            if lineno % lines_per_file == 0:
                if smallfile:
                    smallfile.close()
                small_filename = f'{path}_{lineno + lines_per_file}.csv'
                allfiles.append(small_filename)
                smallfile = open(small_filename, "w")
            smallfile.write(line)
        if smallfile:
            smallfile.close()

    if allfiles:
        for file in allfiles:
            await message.reply_document(file)

async def country(country, product):
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {auth_token}'}
    resp = requests.get(f"https://5sim.net/v1/user/buy/activation/{country}/any/{product}", headers=headers)
    return resp.text

async def idcheck(id):
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {auth_token}'}
    resp = requests.get(f"https://5sim.net/v1/user/check/{id}", headers=headers)
    return resp.text

app.run()
