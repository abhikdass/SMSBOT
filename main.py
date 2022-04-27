import requests,json
from pyrogram import Client, filters 
from pykeyboard import InlineKeyboard
from pyrogram.types import InlineKeyboardButton
from datetime import datetime

app = Client("ConfigDec",api_id=675749   ,api_hash="d7e93f550b87515f22bc51f44acfede5"  ,bot_token="1943454168:AAFoXkMw_QMCT44up0jzy4XiwTpqi9QyF9Y"  )

@app.on_message(filters.command(["list","list@DECRYPTOR_ROBOT"]))
async def listhandler(client,message):
  
    await message.reply_text("1688\n1xbet\n23red\n32red\n888casino\n99app\nace2three\nadidas\nagroinform\nairbnb\nairtel\naitu\nakelni\nalfa\nalgida\nalibaba\naliexpress\nalipay\namasia\namazon\naol\napple\nastropay\nauchan\navito\navon\nazino\nb4ucabs\nbaidu\nbanqi\nbigolive\nbillmill\nbisu\nbitaqaty\nbitclout\nbittube\nblablacar\nblizzard\nblockchain\nblued\nbolt\nbrand20ua\nburgerking\nbykea\ncafebazaar\ncaixa\ncareem\ncarousell\ncdkeys\ncekkazan\ncitaprevia\ncitymobil\nclickentregas\ncliqq\nclubhouse\ncmtcuzdan\ncoinbase\ncoinfield\ncraigslist\ncryptocom\ndbrua\ndeliveroo\ndelivery\ndent\ndhani\ndidi\ndigikala\ndiscord\ndisneyhotstar\ndivar\ndixy\ndodopizza\ndomdara\ndominospizza\ndostavista\ndouyu\ndream11\ndrom\ndrugvokrug\ndukascopy\neasypay\nebay\nebikegewinnspiel\nedgeless\nelectroneum\neneba\nezbuy\nfaberlic\nfacebook\nfiqsy\nfiverr\nfoodpanda\nfoody\nforwarding\nfreecharge\ngalaxy\ngamearena\ngameflip\ngamekit\ngamer\ngcash\nget\ngetir\ngett\ngg\ngittigidiyor\nglobal24\nglobaltel\nglobus\nglovo\ngoogle\ngrabtaxi\ngreen\ngrindr\nhamrahaval\nhappn\nharaj\nhepsiburadacom\nhezzl\nhily\nhopi\nhqtrivia\nhumblebundle\nhumta\nhuya\nicard\nicq\nicrypex\nifood\nimmowelt\nimo\ninboxlv\nindriver\nininal\ninstagram\niost\niqos\nirancell\nivi\niyc\njd\njkf\njustdating\njustdial\nkakaotalk\nkarusel\nkeybase\nkomandacard\nkotak811\nkucoinplay\nkufarby\nkvartplata\nkwai\nlazada\nlbry\nlenta\nlianxin\nline\nlinkedin\nlivescore\nmagnit\nmagnolia\nmailru\nmamba\nmcdonalds\nmeetme\nmega\nmercado\nmichat\nmicrosoft\nmiloan\nmiratorg\nmobile01\nmomo\nmonese\nmonobank\nmosru\nmrgreen\nmtscashback\nmyfishka\nmyglo\nmylove\nmymusictaste\nmzadqatar\nnana\nnaver\nncsoft\nnetflix\nnhseven\nnifty\nnike\nnimses\nnrjmusicawards\nnttgame\nodnoklassniki\nofferup\noffgamers\nokcupid\nokey\nokta\nolacabs\nolx\nonlinerby\nopenpoint\noraclecloud\noriflame\nother\nozon\npaddypower\npairs\npapara\npaxful\npayberry\npaycell\npaymaya\npaypal\npaysend\npaytm\npeoplecom\nperekrestok\npgbonus\npicpay\npof\npokec\npokermaster\npotato\npowerkredite\nprajmeriz2020\npremiumone\nprom\nproton\nprotonmail\nprotp\npubg\npureplatfrom\npyaterochka\npyromusic\nq12trivia\nqiwiwallet\nquipp\nrakuten\nrambler\nrediffmail\nreuse\nripkord\nrosakhutor\nrsa\nrutube\nsamokat\nseosprint\nsheerid\nshopee\nsignal\nsikayetvar\nskout\nsnapchat\nsnappfood\nsneakersnstuff\nsocios\nsportmaster\nspothit\nssoidnet\nsteam\nsurveytime\nswvl\ntaksheel\ntango\ntantan\ntaobao\ntelegram\ntencentqq\nticketmaster\ntiktok\ntinder\ntosla\ntotalcoin\ntouchance\ntrendyol\ntruecaller\ntwitch\ntwitter\nuber\nukrnet\nuploaded\nvernyi\nvernyj\nviber\nvitajekspress\nvkontakte\nvoopee\nwechat\nweibo\nweku\nweststein\nwhatsapp\nwildberries\nwingmoney\nwinston\nwish\nwmaraci\nwolt\nyaay\nyahoo\nyalla\nyandex\nyemeksepeti\nyoudo\nyoula\nyoustar\nzalo\nzoho\nzomato\n\n\nother for other sites\n**SEND /otp sitename**")

@app.on_message(filters.command(["otp","otp@DECRYPTOR_ROBOT"]))
async def otphandler(client,message):
    product=" ".join(message.command[1:])
    keyboard = InlineKeyboard()
    keyboard.row(InlineKeyboardButton('INDIA', "country,india,"+product))
    keyboard.row(InlineKeyboardButton('USA',  "country,usa,"+product))
    keyboard.row(InlineKeyboardButton('RUSSIA',  "country,russia,"+product)) 
    await message.reply_text("Select The Country Name",reply_markup=keyboard)

@app.on_callback_query()
async def callbackupdates(client,query):
    ii = query["data"]
    if "country" in ii:
     c = ii.split(',')
     i =await country(c[1],c[2])
     y = json.loads(i)
     id = y["id"]
     status = y["status"]
     pro =y["product"]
     phone = y["phone"]
     await query.message.reply_text("You have successfully got a number\n**Number:**"+phone+"\n**ID:**"+str(id)+"\n**PRODUCT:**"+pro+"\n**STATUS:**"+status+"")
     await query.message.delete()
    elif "refresh" in ii:
     id=query["data"].split(":")[1]
     idchek = await idcheck(id)
     idche = json.loads(idchek)
     sms = idche["sms"]
     phone = idche["phone"]
     status = idche["status"]
     pro =idche["product"]
     now = datetime.now()
     current_time = now.strftime("%H:%M:%S")
     h = InlineKeyboard()
     h.row(InlineKeyboardButton('Refresh',"refresh:"+str(id)))
     await query.message.reply_text("Your Id details "+current_time+":\nNumber:"+phone+"\nPRODUCT:"+pro+"\nID:"+str(id)+"\nSTATUS:"+status+"\nSMS:"+str(sms),reply_markup=h)
     await query.message.delete()
@app.on_message(filters.command(["id","id@DECRYPTOR_ROBOT"]))
async def idhandler(client,message):
    id=" ".join(message.command[1:])
    idchek = await idcheck(id)
    idche = json.loads(idchek)
    sms = idche["sms"]
    phone = idche["phone"]
    status = idche["status"]
    pro =idche["product"]
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    h = InlineKeyboard()
    h.row(InlineKeyboardButton('Refresh',"refresh:"+str(id)))
    await message.reply_text("Your Id details "+current_time+":\n**Number:**"+phone+"\n**PRODUCT:**"+pro+"\n**ID:**"+str(id)+"\n**STATUS:**"+status+"\n**SMS:**"+str(sms),reply_markup=h)
     
async def country(country,product):
     headers = {'Content-Type': 'application/json','Authorization':'Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTQ3ODYyNjIsImlhdCI6MTYyMzI1MDI2MiwicmF5IjoiNmI3NzAyZTQ4MjljMjU0MjljNTA0YzE3MjkzNjliZmYiLCJzdWIiOjY0NjQ4M30.P-rqeoAFqCrRP3rDqeIMXUBE88jkX5iCS2sK0KhQXNyhAUVYe2ATo9zUAinKYGV_x3NgLgeAAFDdP_15-SO4UUyqIp-diZZEghir1QuBR_O0xhGL85c-Y71WO4IKszNy77C8S3oELl2iyW0pRkHjq975p1DfF-9hEjtUFDZO9YGdm15-I5eyBLAug3b2Sbdw20TTm18cqwkxOZQo_F5iemoYRNO3EL5M6ytkab24aUfhDlC-9neItLP6NogYr1_6VpI_lceGH0f8BMCbwiuDQAMUtgaD9HX63USjAb_3LQsIIzhQ9VTfVPhdBw_pQ3m90C4gWXGl5w_meJbDNZKt9A'}
     resp = requests.get("https://5sim.net/v1/user/buy/activation/"+country+"/any/"+product, headers=headers)
     response=resp.text
     print(response)
     return response

async def idcheck(id):
     headers = {'Content-Type': 'application/json','Authorization':'Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTQ3ODYyNjIsImlhdCI6MTYyMzI1MDI2MiwicmF5IjoiNmI3NzAyZTQ4MjljMjU0MjljNTA0YzE3MjkzNjliZmYiLCJzdWIiOjY0NjQ4M30.P-rqeoAFqCrRP3rDqeIMXUBE88jkX5iCS2sK0KhQXNyhAUVYe2ATo9zUAinKYGV_x3NgLgeAAFDdP_15-SO4UUyqIp-diZZEghir1QuBR_O0xhGL85c-Y71WO4IKszNy77C8S3oELl2iyW0pRkHjq975p1DfF-9hEjtUFDZO9YGdm15-I5eyBLAug3b2Sbdw20TTm18cqwkxOZQo_F5iemoYRNO3EL5M6ytkab24aUfhDlC-9neItLP6NogYr1_6VpI_lceGH0f8BMCbwiuDQAMUtgaD9HX63USjAb_3LQsIIzhQ9VTfVPhdBw_pQ3m90C4gWXGl5w_meJbDNZKt9A'}
     resp = requests.get("https://5sim.net/v1/user/check/"+id, headers=headers)
     response=resp.text
     return response
app.run()