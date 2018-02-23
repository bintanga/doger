# -*- coding: utf-8 -*-

import LINETCR
import requests
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
#import time,random,sys,json,codecs,threading,glob,urllib,urllib2
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,subprocess
import goslate
import wikipedia
from gtts import gTTS
import ast
from enum import Enum 
import os

cl = LINETCR.LINE()
cl.login(token="")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token="")
kk.loginResult()

kc = LINETCR.LINE()
kc.login(token="")
kc.loginResult()

kb = LINETCR.LINE()
kb.login(token="")
kb.loginResult()

kd = LINETCR.LINE()
kd.login(token="")
kd.loginResult()

ke = LINETCR.LINE()
ke.login(token="")
ke.loginResult()

kg = LINETCR.LINE()
kg.login(token="")
kg.loginResult()

kh = LINETCR.LINE()
kh.login(token="")
kh.loginResult()

sw = LINETCR.LINE()
sw.login(token="")
sw.loginResult()

print u"login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""

_________________________________

Bot Protect   ̵̧̧̢̠̗̱̗̲̝̪͇͇̐̓̓̀̀͢͞͞ͅͅǍ̜̖̼̤͔̤̝̲̗̣͍̮̽͝҉̡̡̨̧̕͢͜͠͡͡҉͞ḁ̴̸̴̡̧̢̧̜̟̥̣̩͎̼̟ͦ͗̾̿̇ͨ̍̎̉̉ͥ̋́̀͞͞͡͠͏̸̛͞͝n̦̞̭̘̯̺̗͔̲͓̖̭̤̱̖̦̑͘҉҉̛͏̡̨̛͡҉̡̡͘ ̷̗͙̫̠̹̹̙̳͚͉̦͈͖̺̤̆͑ͯ̈́͝J̞̟̫̮̜̬̘̫̗͈͚̗͔͕̻̝ͩ̋ͤͩͣ̋ͣ̐ͯ͗̈́̿̊̓͐̾͌͛ữ̴̴̸̢͈͕̙̮̭͍͔͖̪̣̘͙̬̺͐̾͒̃̀͆͐͆̀̇̕̕͘͜҉̷̴̴̛͡t̸̴̨̧̧̨̡͙͔̬̭̱̪̪͈͎̺̣̰̱̥͖̘͈̰̻̹ͦͯ̋̏͊̇̇ͩ̈́̆͊̌͋̿͟͜͟͟͜͡͡͝ȁ̷̺̭͎̙̩̝̝̻͖̮̼͍͈͈͓̻͕̻͇͍̉͒ͫͦ̃ͯ̎̃̿ͧ̈̾̊̏̄̄̍͟҉w̠̘͍̘̱͙̺͙̮̟͖̻̙̹͍̻̑̏͛̋͐̔ͥ̆ͧ̎ͪͫͨͣ͋ͦ̍̎̀ͅͅͅ͏̶̕͘͢͜҉̵̢͘҉̸͘̕͝ḁ̵̶̡̛͎͔̺̘͍ͫ̉̅̈́͑ͦ̊̚̕͏҉͢n̥̯̫̘͋̂̀́́͘҉̵̧̢͘͢͟͝͡͞
========Menu Bot=========
☞Help
☞Me
☞Invite
☞Tikunganku
☞Doraemon
☞Cancel/..
☞Qr on/Qr off
☞Aan on/ Aan off
☞Responkick on/off
☞Alwaysread on/off
☞Welcome on/off
☞lurk on/off
☞cyduk
☞Restart
☞Ginfo
☞Gc
☞Name: Memgubah semua nama bot
☞Mybio: Buat Bio akun induk
☞Allbio: Buat ubah semua bio bot
☞Setvideo
☞Pap video
☞megs
☞Reject
☞.google
☞.fb
==========BotCreator==========

A̩̥͎̫ͪ̕͜ͅa̟̙̦̘̺̍ͤͦ͌̅ͮn̻͕̳͎̾͋̄ͥ̊̾ͭ̓̓҉̶́͜͜ ̴̸͈̫̯̲̹̤̾̐ͨͦͤͦͅ͏j̷̶̢̱̱̱̪̬̱̊ͧ̎̆̈́͘͝u̟̬͈̪͈͖̘͓̿ͬͪ̂́̕͜͡͠ͅt̴̴̛̤ͧͩͮ̄͒̔̑̀͟͏̶ȧ̴̴̢̨̳̼̬̯̼̘͖̒ͧ̓̄͗͊́͝w̸̢̦̹̺͈̾͆ͣ́̔́̚͢͠ą̵̴̸̻͙ͯ̎͊̒̅̓͜n̸͍͇̙͔̼̗͑̎͊ͣ̅̅͆̑̕͢
==>Aan jutawan: https://line.me/R/ti/p/%40iyv1920f<==
_________________________________
_________________________________

Bot Protect   ̵̧̧̢̠̗̱̗̲̝̪͇͇̐̓̓̀̀͢͞͞ͅͅǍ̜̖̼̤͔̤̝̲̗̣͍̮̽͝҉̡̡̨̧̕͢͜͠͡͡҉͞ḁ̴̸̴̡̧̢̧̜̟̥̣̩͎̼̟ͦ͗̾̿̇ͨ̍̎̉̉ͥ̋́̀͞͞͡͠͏̸̛͞͝n̦̞̭̘̯̺̗͔̲͓̖̭̤̱̖̦̑͘҉҉̛͏̡̨̛͡҉̡̡͘ ̷̗͙̫̠̹̹̙̳͚͉̦͈͖̺̤̆͑ͯ̈́͝J̞̟̫̮̜̬̘̫̗͈͚̗͔͕̻̝ͩ̋ͤͩͣ̋ͣ̐ͯ͗̈́̿̊̓͐̾͌͛ữ̴̴̸̢͈͕̙̮̭͍͔͖̪̣̘͙̬̺͐̾͒̃̀͆͐͆̀̇̕̕͘͜҉̷̴̴̛͡t̸̴̨̧̧̨̡͙͔̬̭̱̪̪͈͎̺̣̰̱̥͖̘͈̰̻̹ͦͯ̋̏͊̇̇ͩ̈́̆͊̌͋̿͟͜͟͟͜͡͡͝ȁ̷̺̭͎̙̩̝̝̻͖̮̼͍͈͈͓̻͕̻͇͍̉͒ͫͦ̃ͯ̎̃̿ͧ̈̾̊̏̄̄̍͟҉w̠̘͍̘̱͙̺͙̮̟͖̻̙̹͍̻̑̏͛̋͐̔ͥ̆ͧ̎ͪͫͨͣ͋ͦ̍̎̀ͅͅͅ͏̶̕͘͢͜҉̵̢͘҉̸͘̕͝ḁ̵̶̡̛͎͔̺̘͍ͫ̉̅̈́͑ͦ̊̚̕͏҉͢n̥̯̫̘͋̂̀́́͘҉̵̧̢͘͢͟͝͡͞
========Menu Bot=========
☞Bc:
☞Cbc:
☞Ban:on
☞Unban:on
☞TD ban
☞TD del
☞Ban @
☞Respon
_________________________________

Bot Protect   ̵̧̧̢̠̗̱̗̲̝̪͇͇̐̓̓̀̀͢͞͞ͅͅǍ̜̖̼̤͔̤̝̲̗̣͍̮̽͝҉̡̡̨̧̕͢͜͠͡͡҉͞ḁ̴̸̴̡̧̢̧̜̟̥̣̩͎̼̟ͦ͗̾̿̇ͨ̍̎̉̉ͥ̋́̀͞͞͡͠͏̸̛͞͝n̦̞̭̘̯̺̗͔̲͓̖̭̤̱̖̦̑͘҉҉̛͏̡̨̛͡҉̡̡͘ ̷̗͙̫̠̹̹̙̳͚͉̦͈͖̺̤̆͑ͯ̈́͝J̞̟̫̮̜̬̘̫̗͈͚̗͔͕̻̝ͩ̋ͤͩͣ̋ͣ̐ͯ͗̈́̿̊̓͐̾͌͛ữ̴̴̸̢͈͕̙̮̭͍͔͖̪̣̘͙̬̺͐̾͒̃̀͆͐͆̀̇̕̕͘͜҉̷̴̴̛͡t̸̴̨̧̧̨̡͙͔̬̭̱̪̪͈͎̺̣̰̱̥͖̘͈̰̻̹ͦͯ̋̏͊̇̇ͩ̈́̆͊̌͋̿͟͜͟͟͜͡͡͝ȁ̷̺̭͎̙̩̝̝̻͖̮̼͍͈͈͓̻͕̻͇͍̉͒ͫͦ̃ͯ̎̃̿ͧ̈̾̊̏̄̄̍͟҉w̠̘͍̘̱͙̺͙̮̟͖̻̙̹͍̻̑̏͛̋͐̔ͥ̆ͧ̎ͪͫͨͣ͋ͦ̍̎̀ͅͅͅ͏̶̕͘͢͜҉̵̢͘҉̸͘̕͝ḁ̵̶̡̛͎͔̺̘͍ͫ̉̅̈́͑ͦ̊̚̕͏҉͢n̥̯̫̘͋̂̀́́͘҉̵̧̢͘͢͟͝͡͞
========Menu Bot=========
☞Admin on/off
☞Admin list
☞Staff on/off
☞Staff list
☞Mimic:on/off
☞Mimic list
☞Mimic add @
☞TD in
☞TD out
☞Bye
☞Leave
☞Cipok @/Sayang @
☞Nk
☞.
☞Mentions
☞TD:Bc
☞InviteMeTo:
☞TD play

==========BotCreator==========

A̩̥͎̫ͪ̕͜ͅa̟̙̦̘̺̍ͤͦ͌̅ͮn̻͕̳͎̾͋̄ͥ̊̾ͭ̓̓҉̶́͜͜ ̴̸͈̫̯̲̹̤̾̐ͨͦͤͦͅ͏j̷̶̢̱̱̱̪̬̱̊ͧ̎̆̈́͘͝u̟̬͈̪͈͖̘͓̿ͬͪ̂́̕͜͡͠ͅt̴̴̛̤ͧͩͮ̄͒̔̑̀͟͏̶ȧ̴̴̢̨̳̼̬̯̼̘͖̒ͧ̓̄͗͊́͝w̸̢̦̹̺͈̾͆ͣ́̔́̚͢͠ą̵̴̸̻͙ͯ̎͊̒̅̓͜n̸͍͇̙͔̼̗͑̎͊ͣ̅̅͆̑̕͢
==>Aan jutawan: https://line.me/R/ti/p/%40iyv1920f<==
_________________________________
"""

translateMessage ="""
║Aan ṭȏɞʏ║ɞȏṭ ṭȏɞʏ║Translate
════════════════
║> тr-ιd = ιndoneѕιa
║> тr-мy = мyanмar
║> тr-en = englιѕн
║> тr-тн = тнaιland
║> тr-ja = japaneѕe
║> тr-мѕ = мalayѕιa
║> тr-ιт = ιтalιan
║> тr-тr = тυrĸιѕн
║> тr-aғ = aғrιĸaanѕ
║> тr-ѕq = alвanιan
║> тr-aм = aмнarιc
║> тr-ar = araвιc
║> тr-нy = arмenιan
╠════════════"""

stealMessage ="""
★ STEALING ★
● Steal Bio     @[name]
● Steal mid     @[name]
● Steal contact @[name]
● Steal cover   @[name]
● Steal pict    @[name]"""

kantongajaibMessage ="""
_________________________________

Bot Protect   ̵̧̧̢̠̗̱̗̲̝̪͇͇̐̓̓̀̀͢͞͞ͅͅǍ̜̖̼̤͔̤̝̲̗̣͍̮̽͝҉̡̡̨̧̕͢͜͠͡͡҉͞ḁ̴̸̴̡̧̢̧̜̟̥̣̩͎̼̟ͦ͗̾̿̇ͨ̍̎̉̉ͥ̋́̀͞͞͡͠͏̸̛͞͝n̦̞̭̘̯̺̗͔̲͓̖̭̤̱̖̦̑͘҉҉̛͏̡̨̛͡҉̡̡͘ ̷̗͙̫̠̹̹̙̳͚͉̦͈͖̺̤̆͑ͯ̈́͝J̞̟̫̮̜̬̘̫̗͈͚̗͔͕̻̝ͩ̋ͤͩͣ̋ͣ̐ͯ͗̈́̿̊̓͐̾͌͛ữ̴̴̸̢͈͕̙̮̭͍͔͖̪̣̘͙̬̺͐̾͒̃̀͆͐͆̀̇̕̕͘͜҉̷̴̴̛͡t̸̴̨̧̧̨̡͙͔̬̭̱̪̪͈͎̺̣̰̱̥͖̘͈̰̻̹ͦͯ̋̏͊̇̇ͩ̈́̆͊̌͋̿͟͜͟͟͜͡͡͝ȁ̷̺̭͎̙̩̝̝̻͖̮̼͍͈͈͓̻͕̻͇͍̉͒ͫͦ̃ͯ̎̃̿ͧ̈̾̊̏̄̄̍͟҉w̠̘͍̘̱͙̺͙̮̟͖̻̙̹͍̻̑̏͛̋͐̔ͥ̆ͧ̎ͪͫͨͣ͋ͦ̍̎̀ͅͅͅ͏̶̕͘͢͜҉̵̢͘҉̸͘̕͝ḁ̵̶̡̛͎͔̺̘͍ͫ̉̅̈́͑ͦ̊̚̕͏҉͢n̥̯̫̘͋̂̀́́͘҉̵̧̢͘͢͟͝͡͞
========Menu Bot=========
☞Getgrup image
☞Getname @
☞Urlgrup image
☞Getvid @
☞Mypict
☞Myvid
☞Spam:
☞Simisimi on/off
☞Coverurl @
☞Runtime
☞Papset:
☞Pap
☞Searchid:
☞Mymid
☞Memlist
☞zodiak 05-03-2003
☞wiki contoh: wiki ayam
☞Checkig
☞Music 
☞s.stream
☞.instagram
☞.lyric
☞/youtube 
_________________________________
_________________________________

Bot Protect   ̵̧̧̢̠̗̱̗̲̝̪͇͇̐̓̓̀̀͢͞͞ͅͅǍ̜̖̼̤͔̤̝̲̗̣͍̮̽͝҉̡̡̨̧̕͢͜͠͡͡҉͞ḁ̴̸̴̡̧̢̧̜̟̥̣̩͎̼̟ͦ͗̾̿̇ͨ̍̎̉̉ͥ̋́̀͞͞͡͠͏̸̛͞͝n̦̞̭̘̯̺̗͔̲͓̖̭̤̱̖̦̑͘҉҉̛͏̡̨̛͡҉̡̡͘ ̷̗͙̫̠̹̹̙̳͚͉̦͈͖̺̤̆͑ͯ̈́͝J̞̟̫̮̜̬̘̫̗͈͚̗͔͕̻̝ͩ̋ͤͩͣ̋ͣ̐ͯ͗̈́̿̊̓͐̾͌͛ữ̴̴̸̢͈͕̙̮̭͍͔͖̪̣̘͙̬̺͐̾͒̃̀͆͐͆̀̇̕̕͘͜҉̷̴̴̛͡t̸̴̨̧̧̨̡͙͔̬̭̱̪̪͈͎̺̣̰̱̥͖̘͈̰̻̹ͦͯ̋̏͊̇̇ͩ̈́̆͊̌͋̿͟͜͟͟͜͡͡͝ȁ̷̺̭͎̙̩̝̝̻͖̮̼͍͈͈͓̻͕̻͇͍̉͒ͫͦ̃ͯ̎̃̿ͧ̈̾̊̏̄̄̍͟҉w̠̘͍̘̱͙̺͙̮̟͖̻̙̹͍̻̑̏͛̋͐̔ͥ̆ͧ̎ͪͫͨͣ͋ͦ̍̎̀ͅͅͅ͏̶̕͘͢͜҉̵̢͘҉̸͘̕͝ḁ̵̶̡̛͎͔̺̘͍ͫ̉̅̈́͑ͦ̊̚̕͏҉͢n̥̯̫̘͋̂̀́́͘҉̵̧̢͘͢͟͝͡͞
========Menu Bot=========
☞Steal bio
☞Steal contact
☞Steal home
☞Steal mid
☞Mc:
☞Steal cover @
☞Steal pict
☞Info @
☞Conban
☞Banlist
☞Midban
☞Fuck
☞Blocklist
☞Set view
☞Friendlist
☞Friendlistmid
☞Friendinfo:
☞Friendpict:
☞Spam to @
==========BotCreator==========

A̩̥͎̫ͪ̕͜ͅa̟̙̦̘̺̍ͤͦ͌̅ͮn̻͕̳͎̾͋̄ͥ̊̾ͭ̓̓҉̶́͜͜ ̴̸͈̫̯̲̹̤̾̐ͨͦͤͦͅ͏j̷̶̢̱̱̱̪̬̱̊ͧ̎̆̈́͘͝u̟̬͈̪͈͖̘͓̿ͬͪ̂́̕͜͡͠ͅt̴̴̛̤ͧͩͮ̄͒̔̑̀͟͏̶ȧ̴̴̢̨̳̼̬̯̼̘͖̒ͧ̓̄͗͊́͝w̸̢̦̹̺͈̾͆ͣ́̔́̚͢͠ą̵̴̸̻͙ͯ̎͊̒̅̓͜n̸͍͇̙͔̼̗͑̎͊ͣ̅̅͆̑̕͢
==>Aan jutawan: https://line.me/R/ti/p/%40iyv1920f<==
_________________________________
"""

helpMessage1 ="""  *** Set Group ***

╔════════════
╠🔐 Auto cancel 「on / off」
╠🔐 Contact 「on / off」
╠🔐 Allprotect 「on / off」
╠🔐 Auto like 「on / off」
╠🔐 Auto leave 「on / off」
╠🔐 Backup 「on / off」
╠🔐 Welcome 「on / off」
╚════════════

  *** Set Group ***"""

KAC=[cl,ki,kk,kc,kb,kd,ke,kh,kg,sw] 
mid = cl.getProfile().mid 
Amid = ki.getProfile().mid 
Bmid = kk.getProfile().mid 
Cmid = kc.getProfile().mid 
Dmid = kb.getProfile().mid 
Emid = kd.getProfile().mid 
Fmid = ke.getProfile().mid 
Gmid = kg.getProfile().mid 
Hmid = kh.getProfile().mid 
Imid = sw.getProfile().mid 
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,"u0f3b4d62ba8de5b4cb83f71613c75be2","ue3bacabd0bd2e6b35de4f4ddb7a685cd","u5b7f49f8d7b07344ffba5ef934894c42","u28dd35e855947e7b05b093235c51cd1c","uf4ff19c51147465307d7be273b0ea981","u6acc6cbc260a82144fb50c89cc1d0bda","udc7bc6e719fa2f3ee25f5160ce203a17","u3fa50dfca9536210e7c454e8adc2db9c","ue0778c5c6c7da7a090a809a3ab7d2f4a","u2bcba79790a78db95ee18afd0142e9c9","ud010d283f3fb4157ec43ad4e53fe6d3c","uc61b399ed6e9006f52268713a227abae","u0ea1b9a2868e04292d9fd7db9925edb5"]
admin = ["ub76a0153a283da9a1443dfb043181335","u092d27cb60830dd2ba6e691cbe563b5d","ube597dd17603406a6b278bc62cc5fdcf","u092d27cb60830dd2ba6e691cbe563b5d","u3fa50dfca9536210e7c454e8adc2db9c","ue0778c5c6c7da7a090a809a3ab7d2f4a","u2bcba79790a78db95ee18afd0142e9c9","ud010d283f3fb4157ec43ad4e53fe6d3c","uc61b399ed6e9006f52268713a227abae","u0ea1b9a2868e04292d9fd7db9925edb5"]
staff = ["ub76a0153a283da9a1443dfb043181335","u092d27cb60830dd2ba6e691cbe563b5d","ube597dd17603406a6b278bc62cc5fdcf","u092d27cb60830dd2ba6e691cbe563b5d","u3fa50dfca9536210e7c454e8adc2db9c","ue0778c5c6c7da7a090a809a3ab7d2f4a","u2bcba79790a78db95ee18afd0142e9c9","ud010d283f3fb4157ec43ad4e53fe6d3c","uc61b399ed6e9006f52268713a227abae","u0ea1b9a2868e04292d9fd7db9925edb5"]
owner = ["ub76a0153a283da9a1443dfb043181335","u092d27cb60830dd2ba6e691cbe563b5d","ube597dd17603406a6b278bc62cc5fdcf","u092d27cb60830dd2ba6e691cbe563b5d","u3fa50dfca9536210e7c454e8adc2db9c","ue0778c5c6c7da7a090a809a3ab7d2f4a","u2bcba79790a78db95ee18afd0142e9c9","ud010d283f3fb4157ec43ad4e53fe6d3c","uc61b399ed6e9006f52268713a227abae","u0ea1b9a2868e04292d9fd7db9925edb5"]
adminMID = 'ub76a0153a283da9a1443dfb043181335','u092d27cb60830dd2ba6e691cbe563b5d','ube597dd17603406a6b278bc62cc5fdcf','u092d27cb60830dd2ba6e691cbe563b5d','u3fa50dfca9536210e7c454e8adc2db9c','ue0778c5c6c7da7a090a809a3ab7d2f4a','u2bcba79790a78db95ee18afd0142e9c9','ud010d283f3fb4157ec43ad4e53fe6d3c','uc61b399ed6e9006f52268713a227abae','u0ea1b9a2868e04292d9fd7db9925edb5'
wait ={ 
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':False,
    'timeline':False,
    'autoAdd':False,
    'message':"Thanks for add Created by : https://line.me/R/ti/p/%40iyv1920f",
    "lang":"JP",
    "comment":" Auto like \n\n ʙʏ:\n[☆] A̷̶̶̧̬̝̤̟͖͗̾̕͘͢͜͞a̵̵̷̛̝̲͖̜͈͓͕ͫ̉̅̆ͯ͐̄̽͘̕͝n̨̛̛͒̀̀́ ̹̐͌̒̅̈͑̏̀̿͢͜j̧̹̹̍ͦ̓ͯ́ͯ͂̿ͩ҉̸̢́҉u̇̋ͧ̅̇͂͏͞͏̷̨̡͜͢t̨̛̏ͮ̀a̸̷̴̛̿ͩ̀w̴̡̫͍͖͓̑̓̐̒̑́ą͎̯͇̩͓̥̤̉̈́ͬ̔̿͗́́̆́n̛̛͉̘̯̝̪͙͕͖̝̞ͭ̈́ͦ̔ͭͧ̾̿̌͟͠͞͞ [☆]\n[✯] https://line.me/R/ti/p/%40iyv1920f ",
    "likeOn":True,
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":" ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "Protectgroupname":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "protectJoin":False,
    "Backup":True,
    "welcome":False,
    "goodbye":False,
    "TDinvite":False,
    'pap':{},
    'detectMention':True,
    'kickMention':False,
    "alwaysRead":True,
    "Simi":{},
    'sticker':False,
    
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{},
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{},
    }
    
settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
}

setTime = {}
setTime = wait2['setTime']
blacklistFile='blacklist.txt'
pendinglistFile='pendinglist.txt'

setTime = {}
setTime = wait2["setTime"]
contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus



def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
mulai = time.time()

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)         
 
def translate(to_translate, to_language="auto", language="auto"):
    bahasa_awal = "auto"
    bahasa_tujuan = to_language
    kata = to_translate
    url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
    agent = {'User-Agent':'Mozilla/5.0'}
    cari_hasil = 'class="t0">'
    request = urllib2.Request(url, headers=agent)
    page = urllib2.urlopen(request).read()
    result = page[page.find(cari_hasil)+len(cari_hasil):]
    result = result.split("<")[0]
    return result

def mention(to,name):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = name
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x98\xbb @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.from_ = cl.getProfile.mid
    msg.text = "[MENTION]\n"+bb
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       cl.sendMessage(msg)
    except Exception as error:
        print error

def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        cl.sendText(op.param1, cl.getContact(op.param3).displayName + " Jangan kick sembarangan ")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_KICKOUT_FROM_GROUP\n\n")
        return

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass
#------------------------Auto Join-------------------------------
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
			    G.preventJoinByTicket = False
			    cl.updateGroup(G)
			    Ticket = cl.reissueGroupTicket(op.param1)
			    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
			    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
			    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
			    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
			    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
			    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
			    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
			    G.preventJoinByTicket = True
			    cl.updateGroup(G)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
	if op.type == 13:
	    if Bmid in op.param3:
                G = kk.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            kk.rejectGroupInvitation(op.param1)
                        else:
                            kk.acceptGroupInvitation(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        kk.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kk.cancelGroupInvitation(op.param1, matched_list)
                    
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in Bmid:
                if op.param2 in Amid:
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                
            if op.param3 in Dmid:
                if op.param2 in Cmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                
            if op.param3 in Emid:
                if op.param2 in Dmid:
                    X = kb.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kd.updateGroup(X)
                    Ti = kd.reissueGroupTicket(op.param1)
                
            if op.param3 in Fmid:
                if op.param2 in Emid:
                    X = kd.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kd.updateGroup(X)
                    Ti = kd.reissueGroupTicket(op.param1)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                
            if op.param3 in Gmid:
                if op.param2 in Fmid:
                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kg.updateGroup(X)
                    Ti = kg.reissueGroupTicket(op.param1)
                
            if op.param3 in Hmid:
                if op.param2 in Gmid:
                    X = kg.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kg.updateGroup(X)
                    Ti = kg.reissueGroupTicket(op.param1)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kh.updateGroup(X)
                    Ti = kh.reissueGroupTicket(op.param1)
                    
            if op.param3 in Imid:
                if op.param2 in mid:
                    X = sw.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    sw.updateGroup(X)
                    Ti = sw.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)        

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

#_____________
                    
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
  #_____________________________                  
#-------------------------------------------------------------------
	if op.type == 11:
            if not op.param2 in Bots:
                try:
                    gs = ki.getGroup(op.param1)
                    targets = [op.param2]
                    for target in targets:
                       try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                       except:
                        pass

                except Exception, e:
                    print e
                    
#--------------------------------------------------------------------------------------------
        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = cl.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                    except Exception, e:
                        print e

                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        klist=[ki,kk,kc,kd,kb,ke,kg,kh,cl]
                        kicker = random.choice(klist)
                        kicker.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e

		if not op.param2 in Bots:
		 if op.param2 not in Bots:
                  if wait["protect"] == True:
                   try:
                       klist=[cl,ki,kk,kc,kb,kd,ke,kg,kh]
                       kicker=random.choice(klist)
                       G = kicker.getGroup(op.param1)
                       G.preventJoinByTicket = False
                       kicker.updateGroup(G)
                       invsend = 0
                       Ticket = kicker.reissueGroupTicket(op.param1)
                       sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                       X = kicker.getGroup(op.param1)
                       X.preventJoinByTicket = True
                       sw.kickoutFromGroup(op.param1,[op.param2])
		       kicker.kickoutFromGroup(op.param1,[op.param2])
                       sw.leaveGroup(op.param1)
                       kicker.updateGroup(X)
                   except Exception, e:
                            print e
#--------------------------------------------------------------------------------------------
	if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nI could not kick.\nAdd it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kc.updateGroup(G)
                    Ti = kc.reissueGroupTicket(op.param1)
		    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                   # kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                   # kl.acceptGroupInvitationByTicket(op.param1,Ti)
                   # km.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  kn.acceptGroupInvitationByTicket(op.param1,Ti)
                   # ko.acceptGroupInvitationByTicket(op.param1,Ti)
                 #   kp.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because there is no kick regulation or group,\n["+op.param1+"]\nof\n["+op.param2+"]\nI could not kick.\nAdd it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
   	            cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  kj.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  kl.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  km.acceptGroupInvitationByTicket(op.param1,Ti)
                   # kn.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  ko.acceptGroupInvitationByTicket(op.param1,Ti) 
                   # kp.acceptGroupInvitationByTicket(op.param1,Ti)
                   # kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because there is no kick regulation or group,\n["+op.param1+"]\nof\n["+op.param2+"]\nI could not kick.\nAdd it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
	            cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                   # kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  kj.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  kl.acceptGroupInvitationByTicket(op.param1,Ti)
                   # km.acceptGroupInvitationByTicket(op.param1,Ti)
                    #kn.acceptGroupInvitationByTicket(op.param1,Ti)                   
                  #  ko.acceptGroupInvitationByTicket(op.param1,Ti) 
                  #  kp.acceptGroupInvitationByTicket(op.param1,Ti)
                 #   kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because there is no kick regulation or group,\n["+op.param1+"]\nof\n["+op.param2+"]\nI could not kick.\nAdd it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kb.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
		    cl.acceptGroupInvitationByTicket(op.param1,Ti) 
		    ki.acceptGroupInvitationByTicket(op.param1,Ti) 
		    kk.acceptGroupInvitationByTicket(op.param1,Ti) 
		    kc.acceptGroupInvitationByTicket(op.param1,Ti) 
		    kb.acceptGroupInvitationByTicket(op.param1,Ti) 
		    kd.acceptGroupInvitationByTicket(op.param1,Ti) 
		    ke.acceptGroupInvitationByTicket(op.param1,Ti) 
		  #  kf.acceptGroupInvitationByTicket(op.param1,Ti)
		    kg.acceptGroupInvitationByTicket(op.param1,Ti) 
		    kh.acceptGroupInvitationByTicket(op.param1,Ti) 
		  #  kj.acceptGroupInvitationByTicket(op.param1,Ti)
                 #   kl.acceptGroupInvitationByTicket(op.param1,Ti)
                 #   km.acceptGroupInvitationByTicket(op.param1,Ti)
                 #   kn.acceptGroupInvitationByTicket(op.param1,Ti)                   
                  #  ko.acceptGroupInvitationByTicket(op.param1,Ti) 
                #    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                 #   kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kb.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kb.updateGroup(G)
                    Ticket = kb.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because there is no kick regulation or group,\n["+op.param1+"]\nof\n["+op.param2+"]\nI could not kick.\nAdd it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kd.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kd.updateGroup(X)
                    Ti = kd.reissueGroupTicket(op.param1)
		    cl.acceptGroupInvitationByTicket(op.param1,Ti) 
		    ki.acceptGroupInvitationByTicket(op.param1,Ti) 
		    kk.acceptGroupInvitationByTicket(op.param1,Ti) 
		    kc.acceptGroupInvitationByTicket(op.param1,Ti) 
		    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  kf.acceptGroupInvitationByTicket(op.param1,Ti)
		    kg.acceptGroupInvitationByTicket(op.param1,Ti)              
		    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                 #   kl.acceptGroupInvitationByTicket(op.param1,Ti)
                 #   km.acceptGroupInvitationByTicket(op.param1,Ti)
                 #   kn.acceptGroupInvitationByTicket(op.param1,Ti)                   
                 #   ko.acceptGroupInvitationByTicket(op.param1,Ti) 
                 #   kj.acceptGroupInvitationByTicket(op.param1,Ti)
                   # kp.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kd.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kd.updateGroup(G)
                    Ticket = kd.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because there is no kick regulation or group,\n["+op.param1+"]\nof\n["+op.param2+"]\nI could not kick.\nAdd it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
		    cl.acceptGroupInvitationByTicket(op.param1,Ti) 
		    ki.acceptGroupInvitationByTicket(op.param1,Ti) 
	 	    kk.acceptGroupInvitationByTicket(op.param1,Ti) 
		    kc.acceptGroupInvitationByTicket(op.param1,Ti) 
		    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)        
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)            
		  #  kf.acceptGroupInvitationByTicket(op.param1,Ti)           
		    kg.acceptGroupInvitationByTicket(op.param1,Ti)       
		    kh.acceptGroupInvitationByTicket(op.param1,Ti)
              #      kl.acceptGroupInvitationByTicket(op.param1,Ti)
               #     km.acceptGroupInvitationByTicket(op.param1,Ti)
              #      kn.acceptGroupInvitationByTicket(op.param1,Ti)     
              #      ko.acceptGroupInvitationByTicket(op.param1,Ti) 
               #     kj.acceptGroupInvitationByTicket(op.param1,Ti)
                #    kp.acceptGroupInvitationByTicket(op.param1,Ti)
               #     kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ke.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kg.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because there is no kick regulation or group,\n["+op.param1+"]\nof\n["+op.param2+"]\nI could not kick.\nAdd it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kg.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kg.updateGroup(X)
                    Ti = kg.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                 #   kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)                                       
		   # kj.acceptGroupInvitationByTicket(op.param1,Ti)
                 #   kl.acceptGroupInvitationByTicket(op.param1,Ti)
               #     km.acceptGroupInvitationByTicket(op.param1,Ti)
               #     kn.acceptGroupInvitationByTicket(op.param1,Ti)                  
               #     ko.acceptGroupInvitationByTicket(op.param1,Ti) 
                #    kp.acceptGroupInvitationByTicket(op.param1,Ti)
               #     kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kg.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kg.updateGroup(G)
                    Ticket = kg.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

		if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kh.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nI could not kick.\nAdd it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    G = kh.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kh.updateGroup(G)
                    Ti = kh.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
		    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  kj.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  kf.acceptGroupInvitationByTicket(op.param1,Ti)
                   # kl.acceptGroupInvitationByTicket(op.param1,Ti)
                   # km.acceptGroupInvitationByTicket(op.param1,Ti)
                 #   kn.acceptGroupInvitationByTicket(op.param1,Ti)                 
                 #   ko.acceptGroupInvitationByTicket(op.param1,Ti) 
                  #  kp.acceptGroupInvitationByTicket(op.param1,Ti)
                   # kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kh.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kh.updateGroup(X)
                    Ti = kh.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

		if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).KickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
      #              kj.acceptGroupInvitationByTicket(op.param1,Ti)
       #             kf.acceptGroupInvitationByTicket(op.param1,Ti)
        #            kl.acceptGroupInvitationByTicket(op.param1,Ti)
         #           km.acceptGroupInvitationByTicket(op.param1,Ti)
          #          kn.acceptGroupInvitationByTicket(op.param1,Ti)                
           #         ko.acceptGroupInvitationByTicket(op.param1,Ti)
            #        kp.acceptGroupInvitationByTicket(op.param1,Ti)
             #       kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
#____________~_~~~~_~___~~~~~~~~~~~~___~~~~~~
        if op.type == 19:
          if op.param2 not in Bots:
            if op.param3 in admin:
                 random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                 random.choice(KAC).inviteIntoGroup(op.param1,admin)
            else:
                pass

        if op.type == 19:
          if op.param2 not in Bots:
            if op.param2 not in admin:
                 random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                 wait["blacklist"][op.param2] = True
                 print "kicker kicked"
            else:
                pass

        if op.type == 19:
            if op.param2 not in Bots:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group¡¢\n["+op.param1+"]\n¤Î\n["+op.param2+"]\n¤òõí¤ëÊÂ¤¬¤Ç¤­¤Þ¤»¤ó¤Ç¤·¤¿¡£\n¥Ö¥é¥Ã¥¯¥ê¥¹¥È¤Ë×·¼Ó¤·¤Þ¤¹¡£")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client¤¬õí¤êÒŽÖÆor¥°¥ë©`¥×¤Ë´æÔÚ¤·¤Ê¤¤žé¡¢\n["+op.param1+"]\n¤Î\n["+op.param2+"]\n¤òõí¤ëÊÂ¤¬¤Ç¤­¤Þ¤»¤ó¤Ç¤·¤¿¡£\n¥Ö¥��¥Ã¥¯¥ê¥¹¥È¤Ë×·¼Ó¤·¤Þ¤¹¡£")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client¤¬õí¤êÒŽÖÆor¥°¥ë©`¥×¤Ë´æÔÚ¤·¤Ê¤¤žé¡¢\n["+op.param1+"]\n¤Î\n["+op.param2+"]\n¤òõí¤ëÊÂ¤¬¤Ç¤­¤Þ¤»¤ó¤Ç¤·¤¿¡£\n¥Ö¥é¥Ã¥¯¥ê¥¹¥È¤Ë×·¼Ó¤·¤Þ¤¹¡£")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client¤¬õí��êÒŽÖÆor¥°¥ë©`¥×¤Ë´æÔÚ¤·¤Ê¤¤žé¡¢\n["+op.param1+"]\n¤Î\n["+op.param2+"]\n¤ò��í¤ëÊÂ¤¬¤Ç¤­¤Þ¤»¤ó¤Ç¤·¤¿¡£\n¥Ö¥é¥Ã¥¯¥ê¥¹¥È¤Ë×·¼Ó¤·¤Þ¤¹¡£")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
#~~~~~~~__~____~~~__________~~___
#----------------Welcome---------------------------------------------
        if op.type == 15:
          if wait["goodbye"] == True:
            cl.sendText(op.param1, "Yaahh ada yg leave 😢")
            print op.param3 + "has left the group"
            
          if op.type == 11:
            if op.param2 not in Bots:
                return
            cl.sendText(op.param1,cl.getContact(op.param2).displayName + "Please don't play qr")
            print "Update group"

        if op.type == 17:
          if wait["welcome"] == True:
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendText(op.param1,"Hallo " + cl.getContact(op.param2).displayName + "\nWelcome To ☞ " + str(ginfo.name) + " ☜" + "\nBudayakan Cek Note\nDan Semoga Betah Disini ^_^")
            cl.sendImageWithURL(op.param1,image)
            print "MEMBER JOIN TO GROUP"

#-----------------------------------------------------------------
        if op.type == 13:
            if mid in op.param3:
                klist=[cl,ki,kk,kc,kb,kd,ke,kg,kh]
                kicker = random.choice(klist)
                G = kicker.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            kicker.rejectGroupInvitation(op.param1)
                        else:
                            kicker.acceptGroupInvitation(op.param1)
                    else:
                        kicker.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        kicker.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kicker.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == admin: 
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
    
        if op.type == 32:
            if op.param2 not in Bots:
                if op.param2 not in admin:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
            	if wait["TDinvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invite
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"[×]" + _name + " Sudah di grup ini😉")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry 😉 " + _name + " Ada di daftar Blacklist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Succes : \n➡" + _name)
                                     wait["TDinvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait["TDinvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Sorry i can't invite this contact")
                                         wait["TDinvite"] = False
                                         break
                if wait["akaInvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 ki.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 ki.sendText(msg.to,"Call my daddy to use command !, \n➡ Unban: " + invite)
                                 break
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     ki.findAndAddContactsByMid(target)
                                     ki.inviteIntoGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"✍⎯ٴ☬⟿Admin kece☬ Invited: \n➡ " + _name)
                                     wait["akaInvite"] = False
                                     break
                                 except:
                                          cl.sendText(msg.to,"Negative, Err0r Detected")
                                          wait["akaInvite"] = False
                                          break


            if op.type == 26:
                msg = op.message
                if msg.to in settings["simiSimi"]:
                   if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to,data['result']['response'].encode('utf-8'))
                if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Aku Bilang Jangan Ngetag Lagi " + cName + "\nAku Kick Kamu! Sorry, Byee!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break                              
                              
                if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag!! Lagi Sibuk",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","-_-","Dia Lagi Off", cName + " Kenapa Tag Saya?","Dia Lagi Tidur\nJangan Di Tag " + cName, "Jangan Suka Tag Gua " + cName, "Kamu Siapa " + cName + "?", "Ada Perlu Apa " + cName + "?","Woii " + cName + " Jangan Ngetag, Riibut!"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break 

                if wait["alwaysRead"] == True:
                    if msg.toType == 0:
                       cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
                #if wait['sticker'] == True:
                    #stk_id = msg.contentMetadata['STKID']
                    #stk_ver = msg.contentMetadata['STKVER']
                    #pkg_id = msg.contentMetadata['STKPKGID']
                    #filler = "『 Sticker Check 』\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n『 Link 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    #cl.sendText(msg.to, filler)
                #else:
                    #pass
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"Telah ditambahkan ke daftar hitam")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")
               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False
                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Telah ditambahkan di daftar hitam")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Succes")
               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False
                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"🔹Name 》\n" + msg.contentMetadata["displayName"] + "\n🔹Mid 》\n" + msg.contentMetadata["mid"] + "\n🔹Status 》\n" + contact.statusMessage + "\n🔹Picture status 》\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n🔹CoverURL:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"🔹[NAME]:\n" + msg.contentMetadata["displayName"] + "\n🔹[MID]:\n" + msg.contentMetadata["mid"] + "\n🔹[STATUS]:\n" + contact.statusMessage + "\n🔹[PICTURE STATUS]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n🔹[CoverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Help","Sw help","Menu","Key","menu"]:
	      if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {"mid": msg.from_}
                  cl.sendMessage(msg)
                  cl.sendText(msg.to, "Bot only admin & staff 😆\nKetik 「Creator」 for contact admin")
                  print "COMMENT DENIED"
            elif msg.text in ["Set view"]:
	      if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage1)
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "TD kick " in msg.text:
	      if msg.from_ in admin:
                midd = msg.text.replace("TD kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {"mid": msg.from_}
                  cl.sendMessage(msg)
                  cl.sendText(msg.to, "Acces denied for you 😆\nKetik 「Creator」 for contact admin")
                  print "COMMENT DENIED"
            elif "Kick " in msg.text:
	      if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {"mid": msg.from_}
                  cl.sendMessage(msg)
                  cl.sendText(msg.to, "Acces denied for you 😆\nKetik 「Creator」 for contact admin")
                  print "COMMENT DENIED"
	    elif msg.text in ["Invite on"]:
            	if msg.from_ in admin:
                 wait["TD invite"] = True
                 cl.sendText(msg.to,"send contact to invite")
            elif "TD invite " in msg.text: 
	      if msg.from_ in admin:
                midd = msg.text.replace("TD invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "TD invite " in msg.text:
	      if msg.from_ in admin:
                midd = msg.text.replace("TD invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {"mid": msg.from_}
                  cl.sendMessage(msg)
                  cl.sendText(msg.to, "Acces denied for you 😆\nKetik 「Creator」 for contact admin")
                  print "COMMENT DENIED"
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
                
            elif msg.text.lower() == 'invite':
                if msg.from_ in admin:
                  if msg.toType == 2:
                    wait["akaInvite"] = True
                    ki.sendText(msg.to,"send contact 😉")
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
                
	    elif msg.text in ["Doraemon"]:
	      if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Imid}
                cl.sendMessage(msg)
                
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ã��—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text in ["Cancel"]:
	      if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {"mid": msg.from_}
                  cl.sendMessage(msg)
                  cl.sendText(msg.to, "Acces denied for you 😆\nKetik 「Creator」 for contact admin")
                  print "COMMENT DENIED"
            elif msg.text in ["Canc"]:
                if msg.toType == 2:
                    G = kk.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kk.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            kk.sendText(msg.to,"No one is inviting")
                        else:
                            kk.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")            
            elif msg.text in ["Qr on","TD link on"]:
	      if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["R1 ourl","R1 link on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done ")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["R2 ourl","R2 link on"]:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done ")
                    else:
                        kk.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Qr off","Sw link off"]:
	      if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["R1 curl","R1 link off"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done ")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["R2 curl","R2 link off"]:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done ")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
	    elif msg.text in ["Ginfo"]:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': ginfo.creator.mid}
                    cl.sendText(msg.to,"➰ NAME GROUP ➰\n" + str(ginfo.name) + "\n\n🔹 Group Id \n" + msg.to + "\n\n🔹Creator \n" + gCreator + "\n\n🔹Status profile \nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\n~  Anggota :: " + str(len(ginfo.members)) + " Members\n~  Pending :: " + sinvitee + " People\n~  URL  :: ")
	 	    cl.sendMessage(msg)
	 	    cl.sendImageWithURL(msg.to, "http://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
	           
        #    elif "Music" in msg.text.lower():
	     #       songname = msg.text.lower().replace("Music","")
	      #      params = {"songname":" songname"}
	       #     r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
	          #  data = r.text
	         #   data = json.loads(data)
	        #    for song in data:
	       #cl.sendMessage(msg.to,song[4])

       # elif "jointicket " in msg.text.lower():
	       #  rplace=msg.text.lower().replace("jointicket ")
	     # if rplace == "on":
		   # 	wait["atjointicket"]=True
	  #  elif rplace == "off":
	#	    	wait["atjointicket"]=False
       # cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
      #  elif '/ti/g/' in msg.text.lower():
	   # link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
	   # links = link_re.findall(msg.text)
	   # n_links=[]
	   #	for l in links:
		#	if l not in n_links:
		#		n_links.append(l)
		#for ticket_id in n_links:
			#if wait["atjointicket"] == True:
			#	group=cl.findGroupByTicket(ticket_id)
			#	cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
			#	cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif "Gc" == msg.text:
	      if msg.from_ in admin:
                try:
                    group = cl.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    cl.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    cl.sendMessage(M)
                    cl.sendText(msg.to,"old user")
	    elif msg.text in ["kantong ajaib"]:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,kantongajaibMessage)
					else:
						cl.sendText(msg.to,helpt)
	    elif "Me @" in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("Me @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                         pass

	    elif "Name: " in msg.text:
	      if msg.from_ in admin:
                string = msg.text.replace("Name: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kc.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kb.getProfile()
                    profile.displayName = string
                    kb.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kd.getProfile()
                    profile.displayName = string
                    kd.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ke.getProfile()
                    profile.displayName = string
                    ke.updateProfile(profile)
		if len(string.decode('utf-8')) <= 20:
                    profile = kf.getProfile()
                    profile.displayName = string
                    kf.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kg.getProfile()
                    profile.displayName = string
                    kg.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kh.getProfile()
                    profile.displayName = string
                    kh.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kj.getProfile()
                    profile.displayName = string
                    kj.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kl.getProfile()
                    profile.displayName = string
                    kl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = km.getProfile()
                    profile.displayName = string
                    km.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kn.getProfile()
                    profile.displayName = string
                    kn.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ko.getProfile()
                    profile.displayName = string
                    ko.updateProfile(profile)
                    cl.sendText(msg.to,"Update Name all bot succes")

            elif "Mybio: " in msg.text:
               if msg.from_ in admin:
                string = msg.text.replace("Mybio: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio👉 " + string + " 👈Succes")

            elif "Allbio: " in msg.text:
	      if msg.from_ in admin:
                string = msg.text.replace("Allbio: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kb.getProfile()
                    profile.statusMessage = string
                    kb.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kd.getProfile()
                    profile.statusMessage = string
                    kd.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ke.getProfile()
                    profile.statusMessage = string
                    ke.updateProfile(profile)
		if len(string.decode('utf-8')) <= 500:
                    profile = kf.getProfile()
                    profile.statusMessage = string
                    kf.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kg.getProfile()
                    profile.statusMessage = string
                    kg.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kh.getProfile()
                    profile.statusMessage = string
                    kh.updateProfile(profile)

            elif "Rename: " in msg.text:
	      if msg.from_ in admin:
                string = msg.text.replace("Rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"[●] Update Name👉 " + string + "👈")
            elif 'searchimage' in msg.text.lower():
                  try:
                      shi = msg.text.lower().replace("searchimage ","")
                      kha = random.choice(items)
                      url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + shi
                      raw_html = (download_page(url))
                      items = items + (_images_get_all_items(raw_html))
                      items = []
                  except:
                      try:
                          start = timeit.timeit()
                          cl.sendImageWithURL(msg.to,random.choice(items))
                          cl.sendText(msg.to,"Total Image Links ="+str(len(items)))
                      except Exception as e:
                          cl.sendText(msg.to,str(e))
            elif msg.text in ["Aan on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"Auto Respon Sudah Aktif")
		else:
		    cl.sendText(msg.to,"Khusus Aan")

            elif msg.text in ["Aan off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    cl.sendText(msg.to,"Auto Respon Sudah Off")
		else:
		    cl.sendText(msg.to,"Khusus Nadya")	
		    
		    
 
            elif msg.text in ["Responkick on"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    cl.sendText(msg.to,"Auto Respon Kick Sudah Aktif")
		else:
		    cl.sendText(msg.to,"Khusus Aan")

            elif msg.text in ["Responkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    cl.sendText(msg.to,"Auto Respon Kick Sudah Off")
		else:
		    cl.sendText(msg.to,"Khusus Aan")			  
            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                cl.sendText(msg.to,"Always Read Sudah Aktif")

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                cl.sendText(msg.to,"Always Read Sudah Di Nonaktifkan")                

            elif msg.text in ["Kick on","Kickall"]:
                    try:
                        cl.sendText(msg.to,"Bahasa di jaga ya bangsat")
                        cl.kickoutFromGroup(msg.to,[msg.from_])
                    except:
                        pass
            elif 'crash' in msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u092d27cb60830dd2ba6e691cbe563b5d,'"}
                cl.sendMessage(msg)                   
#----------------------------------------
            elif "say-ar" in msg.text.lower():
                say = msg.text.lower().replace("say-ar","")
                lang = 'ar'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
            elif "say-ja" in msg.text.lower():
                say = msg.text.lower().replace("say-ja","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
            elif "Setvideo " in msg.text:
                wait["Vid"] = msg.text.replace("Setvideo ","")
                cl.sendText(msg.to,"Video Has Ben Set To")

            elif msg.text in ["Papvideo","/Papvid"]:
                cl.sendVideoWithURL(msg.to,wait["Vid"])
            elif "Wl " in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del wait["blacklist"][target]
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Done Unbanned")
                            print "[CMD]  Unbannad"
                        except:
                            pass
            elif "Ambil QR: " in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("Ambil QR: ","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Not for use less than group")
            elif '#dy ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('#dy ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ght = ('https://www.youtube.com' + results['href'])
                    cl.sendVideoWithURL(msg.to, ght)
                except:
                    cl.sendText(msg.to,"ไม่พบข้อมูล (｀・ω・´)")            
            elif 'mp4 ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('mp4 ',"").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class':'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        cl.sendVideoWithURL(msg.to, ght)
                    except:
                        cl.sendText(msg.to, "ไม่พบข้อมูล (｀・ω・´)")
            
            elif "siri " in msg.text.lower():
                    query = msg.text.lower().replace("siri ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'DESKTOPMAC 10.10.2-YOSEMITE-x64    MAC 4.5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            elif "siri:" in msg.text.lower():
                    query = msg.text.lower().replace("siri:","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'DESKTOPMAC 10.10.2-YOSEMITE-x64    MAC 4.5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            elif "siri-en " in msg.text.lower():
                    query = msg.text.lower().replace("siri-en ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'DESKTOPMAC 10.10.2-YOSEMITE-x64    MAC 4.5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'en', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            elif "Talk " in msg.text.lower():
                    query = msg.text.lower().replace("Talk ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'DESKTOPMAC 10.10.2-YOSEMITE-x64    MAC 4.5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithURL(msg.to, mp3)     
            elif msg.text in ["Remove all chat"]:
		cl.removeAllMessages(op.param2)
		ki.removeAllMessages(op.param2)
		kk.removeAllMessages(op.param2)
		kc.removeAllMessages(op.param2)
		cl.sendText(msg.to,"Removed all chat")

            elif "/botadd @" in msg.text:
              if msg.toType == 2:
                if msg.from_ in admin:
                  print "[Command]Add executing"
                  _name = msg.text.replace("/botadd @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  gs = ki.getGroup(msg.to)
                  gs = kk.getGroup(msg.to)
                  gs = kc.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        ki.findAndAddContactsByMid(target)
                        kk.findAndAddContactsByMid(target)
                        kc.findAndAddContactsByMid(target)
                        cl.senText(msg.to, "Berhasil Menambah Kan Teman")
                      except:
                        cl.sendText(msg.to,"Error")
              else:
                cl.sendText(msg.to,"Perintah Ditolak")
                cl.sendText(msg.to,"Perintah ini Hanya Untuk Admin")
            elif msg.text in ["Restart"]:
              if msg.from_ in admin:
                    cl.sendText(msg.to, "Bot has been restarted")
                    restart_program()
                    print "@Restart"
            elif "megs " in msg.text:
              if msg.from_ in owner:
                  gName = msg.text.replace("megs ","")
                  ap = random.choice(KAC).getGroups([msg.to])
                  semua = [contact.mid for contact in ap[0].members]
                  nya = ap[0].members
                  for a in nya:
                      Mi_d = str(a.mid)
                      random.choice(KAC).createGroup(gName, semua)
                #cl.leaveRoom(op.param1)
                #cl.leaveGroup([msg.to])
            elif "Anime" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						strnum = msg.text.replace("Anime","")
						si=["1","2","3","4","5","6","7","8","9","0"]
						ie=["1","2","3","4","5","6","7","8","9","0"]
						bi=["01","02","00"]
						try:
							num = int(strnum)
							bs = random.choice(bi)
							io = random.choice(ie)
							ss = random.choice(si)
							bis = "gan/" + bs + io + si + ".png"
							cl.sendImage(msg.to, bis)
						except:
							cl.sendText(msg.to,"err")
#================================================================================================================

            elif "weather" in msg.text:
            	if msg.from_ in admin:
                            pisah = msg.text.split("r ")
                            location = msg.text.replace(pisah[0]+"r ","")
                            params = {'kota':location}
                            with requests.session() as web:
                            	web.headers["user-agent"] = random.choice("userAgent")
                                r = requests.get("http://api.corrykalam.net/apicuaca.php?" + urllib.urlencode(params))
                                data = r.text
                                data = json.loads(data)
                                if "result" not in data:
                                    ret_ = "[ Weather Status ]"
                                    ret_ += "\n\nLocation: " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\nTemperature: " + data[1].replace("Suhu : ","")
                                    ret_ += "\nHumidity: " + data[2].replace("Kelembaban : ","")
                                    ret_ += "\nAir pressure: " + data[3].replace("Tekanan udara : ","")
                                    ret_ += "\nWind velocity: " + data[4].replace("Kecepatan angin : ","")
                                else:
                                    ret_ = "[ Weather Status ] Error : Location not found"
                                cl.sendText(msg.to, str(ret_))
                                                                        
#=================================================================================================================
            elif "praytime" in msg.text:
            	if msg.from_ in admin:
                            pisah = msg.text.split("e ")
                            location = msg.text.replace(pisah[0]+"e ","")
                            params = {'lokasi':location}
                            with requests.session() as web:
                                r = requests.get("http://api.corrykalam.net/apisholat.php?" + urllib.urlencode(params))
                                data = r.text
                                data = json.loads(data)
                                if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashr : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                    ret_ = "[ Prayer Schedule ]"
                                    ret_ += "\n\nLocation : " + data[0]
                                    ret_ += "\n" + data[1]
                                    ret_ += "\n" + data[2]
                                    ret_ += "\n" + data[3]
                                    ret_ += "\n" + data[4]
                                    ret_ += "\n" + data[5]
                                else:
                                    ret_ = "[ Prayer Schedule ] Error : Location not found" 
                                cl.sendText(msg.to, str(ret_))
                                                    
#==========================================================================================================================
            elif "location" in msg.text:
            	if msg.from_ in admin:
                            pisah = msg.text.split("n ")
                            location = msg.text.replace(pisah[0]+"n ","")
                            params = {'lokasi':location}
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice("userAgent")
                                r = requests.get("http://api.corrykalam.net/apiloc.php?"+ urllib.urlencode(params))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "[ Details Location ]"
                                    ret_ += "\n\nLocation : " + data[0]
                                    ret_ += "\nGoogle Maps : " + link
                                else:
                                    ret_ = "[ Details Location ] Error : Location not found"
                                cl.sendText(msg.to, str(ret_))
            elif "Apakah " in msg.text:
                  tanya = msg.text.replace("Apakah ","")
                  jawab = ("iya","Tidak")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
            
            elif msg.text in ["About"]:
               if msg.toType == 2:
                today = datetime.today()
                future = datetime(2100,01,31)
                days = (str(future - today))
                comma = days.find(",")
                days = days[:comma]
                cl.sendText(msg.to,"「About 」\n「Ig My creator:  https://www.instagram.com/alrahmanto_selebgram 」\n 「Youtube My creator: https://www.youtube.com/channel/UCHYofFTBQr0n4GXt3uW4VUg 」 \n 「==========BotCreator==========A̩̥͎̫ͪ̕͜ͅa̟̙̦̘̺̍ͤͦ͌̅ͮn̻͕̳͎̾͋̄ͥ̊̾ͭ̓̓҉̶́͜͜ ̴̸͈̫̯̲̹̤̾̐ͨͦͤͦͅ͏j̷̶̢̱̱̱̪̬̱̊ͧ̎̆̈́͘͝u̟̬͈̪͈͖̘͓̿ͬͪ̂́̕͜͡͠ͅt̸̢̤̹̺͈ͧͩͮ̄͒̔̑́͢͠ą̵̴̸̻͙ͯ̎͊̒̅͜n̸͍͇̙͔̼̗͑̎͊ͣ̅̅͆̑̕͢==>Aan jutawan: https://line.me/R/ti/p/%40iyv1920f<==_________________________________」 \n\n「Subscription」\n Expired: " + "\n In days: " + days +  "\n\n「Contact」\n・ LINE me: http://line.me/ti/p/~alrahmantoganteng")
                msg.contentType = 13
                msg.contentMetadata = {'mid':mid}
                cl.sendMessage(msg)
            elif ".google " in msg.text:
                    a = msg.text.replace(".google ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Processing")
                    cl.sendText(msg.to, "https://www.google.com" + b)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Success")
            #===============================
            elif msg.text in ["Gruplist1"]:  
                gruplist = ki.getGroupIdsJoined()
                kontak = ki.getGroups(gruplist)
                num=1
                msgs="═════════List Grup═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.name)
                    num=(num+1)
                msgs+="\n═════════List Grup═════════\n\nTotal Grup : %i" % len(kontak)
                ki.sendText(msg.to, msgs)
            
            elif msg.text in ["Gruplistmid1"]:   
                gruplist = ki.getGroupIdsJoined()
                kontak = ki.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                ki.sendText(msg.to, msgs)
            elif "Grupimage: " in msg.text:
                saya = msg.text.replace('Grupimage: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif msg.text in ["Banlist1"]:   
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Banlist")
                    num=1
                    msgs="══════════List Blacklist═════════"
                    for mi_d in wait["blacklist"]:
                        msgs+="\n[%i] %s" % (num, cl.getContact(mi_d).displayName)
                        num=(num+1)
                    msgs+="\n══════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(wait["blacklist"])
                    cl.sendText(msg.to, msgs)
    
            elif "Picturl @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Picturl @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
#===============================
            elif ".fb" in msg.text:
                    a = msg.text.replace(".fb","")
                    replace = urllib.quote(a)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Processing")
                    cl.sendText(msg.to, "https://www.facebook.com/search/str/"+ replace + "/keywords_search")
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Success")
            elif "image " in msg.text:
                search = msg.text.replace("image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif "lurk on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"Lurking already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "lurk off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))

            elif "cyduk" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "Lurking has not been set.")
            elif 'Youtubemp4 ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubemp4 ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        cl.sendVideoWithURL(msg.to, ght)
                    except:
                        cl.sendText(msg.to, "Could not find it")
            elif "yt-get " in msg.text:
                qt = msg.text.replace("yt-get ","")
                vid = pafy.new(qt)
                stream = vid.streams
                for s in stream:
                      vin = vid.title + "\n\nLink Download" + s.url
                cl.sendvideowithurl(msg.to,vid)
            elif "Youtubesearch " in msg.text:
                    query = msg.text.replace("Youtube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        cl.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
            #========================================
            elif msg.text in ["Reject"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Semua Spam Undangan Telah Di Tolak")
                else:
                    cl.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject"]:
                gid = kk.getGroupIdsInvited()
                for i in gid:
                    kk.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kk.sendText(msg.to,"Semua Spam Undangan Telah Di Tolak")
                else:
                    kk.sendText(msg.to,"拒绝了全部的邀请。")

            elif "Anker playstore: " in msg.text:
                    a = msg.text.replace("Anker playstore:  ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Processing")
                    cl.sendText(msg.to, "•••••••<{ Playstore search page }>•••••••\n\nTitle :"+b+"\nSource : Google play\nLink Download : https://play.google.com/store/search?q=" + b)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Success")
#========================================
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
      
            elif "Getgrup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path)
            elif "Urlgrup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendText(msg.to,path)
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif msg.text in ["Mypict"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid"]:
                    h = cl.getContact(mid)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif "Spam: " in msg.text:
                strnum = msg.text.replace("Spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])
            
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                cl.sendText(msg.to,"Success activated simisimi")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                cl.sendText(msg.to,"Success deactive simisimi")
                
            elif "Coverurl @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Coverurl @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"  
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama "+waktu(eltime)
                cl.sendText(msg.to,van)
            elif "Papset: " in msg.text:
              if msg.from_ in admin:
                    text = msg.text.replace("Papset: ","")
                    try:
                        wait["PAPimages"] = text
                        cl.sendImageWithURL(msg.to,str(wait["PAPimages"]))
                        print "[Notif] Change Message Sucess"
                    except:
                        cl.sendText(msg.to,"Not Found")
            elif msg.text in ["pap","PAP","Pap"]:
                imagess = str(wait["PAPimages"])
                cl.sendImageWithURL(msg.to,imagess)
#===============================

            elif "Mymid" == msg.text:
                cl.sendText(msg.to, msg.from_)
            elif msg.text in ["Memlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="「List Member」"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n「List Member」\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)
            elif "zodiak " in msg.text:
                tanggal = msg.text.replace("zodiak ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"Tanggal Lahir: "+lahir+"\n\nUsia: "+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)
            elif 'wiki ' in msg.text.lower():
                try:
                    wiki = msg.text.lower().replace("wiki ","")
                    wikipedia.set_lang("id")
                    pesan="Title ("
                    pesan+=wikipedia.page(wiki).title
                    pesan+=")\n\n"
                    pesan+=wikipedia.summary(wiki, sentences=3)
                    pesan+="\n"
                    pesan+=wikipedia.page(wiki).url
                    cl.sendText(msg.to, pesan)
                except:
                        try:
                            pesan="Over Text Limit! Please Click link\n"
                            pesan+=wikipedia.page(wiki).url
                            cl.sendText(msg.to, pesan)
                        except Exception as e:
                            cl.sendText(msg.to, str(e))
            elif "say " in msg.text.lower():
                say = msg.text.lower().replace("say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

            elif "Searchid: " in msg.text:
                msgg = msg.text.replace('Searchid: ','')
                conn = cl.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    cl.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    cl.sendMessage(msg)

            elif "Checkig " in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                cl.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                cl.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)
            
#---------------------------------- SONG ------------------------------------
            elif ".lirik " in msg.text.lower():
                songname = msg.text.replace("/lirik ","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    cl.sendText(msg.to,song[5])
                    print "[Command] Lirik"

            elif ".music " in msg.text.lower():
                songname = msg.text.replace(".music ","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    cl.sendText(msg.to,"Judul : " + song[0] + "\nDurasi : " + song[1])
                    cl.sendText(msg.to,song[4])
                    print "[Command] Lagu"
            elif msg.text in ["/steal"]:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,stealMessage)
					else:
						cl.sendText(msg.to,helpt)

#----------------------------------------------------------------------------
            elif "Steal bio" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,contact.statusMessage)
                except:
                    cl.sendText(msg.to,contact.statusMessage)
            elif "Steal mid" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"Mc: " + key1)
            elif "Steal contact" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
            elif "Mc:" in msg.text:
              if msg.from_ in admin:
                mmid = msg.text.replace("Mc:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif "Info @" in msg.text:
              if msg.from_ in admin:
                nama = msg.text.replace("Info @","")
                target = nama.rstrip(' ')
                tob = cl.getGroup(msg.to)
                for g in tob.members:
                    if target == g.displayName:
                        gjh= cl.getContact(g.mid)
                        try:
                            cover = cl.channel.getCover(g.mid)
                        except:
                            cover = ""
                        cl.sendText(msg.to,"[Display Name]:\n" + gjh.displayName + "\n[Mid]:\n" + gjh.mid + "\n[BIO]:\n" + gjh.statusMessage + "\n[pict profile]:\nhttp://dl.profile.line-cdn.net/" + gjh.pictureStatus + "\n[Cover]:\n" + str(cover))
                    else:
                        pass
            elif "Steal cover @" in msg.text:
              if msg.from_ in admin:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal cover @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
            elif "Steal pict " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("Steal pict ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = cl.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    cl.sendImageWithURL(msg.to,image)
                                except Exception as error:
                                    cl.sendText(msg.to,(error))
                                    pass
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                else:
                    cl.sendText(msg.to,"Tidak bisa dilakukan di luar grup")
            elif msg.text in ["BUBAR","bubar","bubar tolol"]:
            	   aan = ["http://dl.profile.line-cdn.net/0m002af1d3725161d09deb2597257acb237065e3003073"]
                   jutawan = random.choice(aan)
                   cl.sendImageWithURL(msg.to,jutawan)
                   
            elif "/youtube " in msg.text:
                query = msg.text.replace("/youtube ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    cl.sendText(msg.to,hasil)
                    print '[Command] Youtube Search'
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"~~~~~FROM ID~~~~~\n" + "" + kata + "\n~~~~~TO EN~~~~~\n" + "" + result)
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Blacklist")
                    h = ""
                    for i in wait["blacklist"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)
            elif msg.text in ["Midban","Mid ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    num=1
                    cocoa = "══════════List Blacklist═════════"
                    for mm in matched_list:
                        cocoa+="\n[%i] %s" % (num, mm)
                        num=(num+1)
                        cocoa+="\n═════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(matched_list)
                    cl.sendText(msg.to,cocoa)
            elif msg.text.lower() == 'scan blacklist':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Tidak ada Daftar Blacklist")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass   
            elif msg.text.lower() == 'welcome':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                tts = gTTS(text=jawaban1, lang='id')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')
            elif "Friendinfo: " in msg.text:
                saya = msg.text.replace('Friendinfo: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    contact = cl.getContact(i)
                    cu = cl.channel.getCover(i)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    if h == saya:
                        cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                        cl.sendImageWithURL(msg.to,image)
                        cl.sendText(msg.to,"Cover " + contact.displayName)
                        cl.sendImageWithURL(msg.to,path)
                
            elif "Friendpict: " in msg.text:
                saya = msg.text.replace('Friendpict: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    gna = cl.getContact(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif msg.text in ["Friendlistmid"]: 
                gruplist = cl.getAllContactIds()
                kontak = cl.getContacts(gruplist)
                num=1
                msgs="═════════List FriendMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.mid)
                    num=(num+1)
                msgs+="\n═════════List FriendMid═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["Blocklist"]: 
                blockedlist = cl.getBlockedContactIds()
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="═════════List Blocked═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif msg.text in ["Memlist1"]:   
                kontak = ki.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═════════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                ki.sendText(msg.to, msgs)
            elif msg.text in ["Friendlist"]:    
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
               
            elif '.lyric ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('.lyric ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
            elif '.instagram ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace(".instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            elif 'music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
            #========================================
            elif "s.stream " in msg.text.lower():
					songname = msg.text.replace("s.stream ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						cl.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						cl.sendAudioWithURL(msg.to,abc)
						cl.sendText(msg.to, "That's the song for " + song[0])   

#========================================
            elif msg.text in ["Up","up","Up Chat","Up chat","up chat","Upchat","upchat"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"Aku belum mandi")
                ki.sendText(msg.to,"Tak tun tuang")
                kk.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"Tapi masih cantik juga")
                ki.sendText(msg.to,"Tak tun tuang")
                kk.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"apalagi kalau sudah mandi")
                ki.sendText(msg.to,"Tak tun tuang")
                kk.sendText(msg.to,"Pasti cantik sekali")
                cl.sendText(msg.to,"yiha")
                ki.sendText(msg.to,"Kalau orang lain melihatku")
                kk.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"Badak aku taba bana")
                ki.sendText(msg.to,"Tak tun tuang")
                kk.sendText(msg.to,"Tak tuntuang")
                cl.sendText(msg.to,"Tapi kalau langsuang diidu")
                ki.sendText(msg.to,"Tak tun tuang")
                kk.sendText(msg.to,"Atagfirullah baunya")
                cl.sendText(msg.to,"Males lanjutin ah")
                ki.sendText(msg.to,"Sepi bat")
                kk.sendText(msg.to,"Iya sepi udah udah")
                cl.sendText(msg.to,"Gaada yang denger juga kita nyanyi")
                ki.sendText(msg.to,"Nah")
                kk.sendText(msg.to,"Mending gua makan dulu")
                cl.sendText(msg.to,"Siyap")
                ki.sendText(msg.to,"Okeh")
                kk.sendText(msg.to,"Katanya owner kita Jomblo ya")
                cl.sendText(msg.to,"Iya emang")
                ki.sendText(msg.to,"Denger denger si lagi nyari pacar doi")
                kk.sendText(msg.to,"Udah ah gosip mulu doain aja biar dapet")
            elif msg.text in ["/translate"]:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,translateMessage)
					else:
						cl.sendText(msg.to,helpt)
#-------------------
            elif "Tr-id " in msg.text:
                nk0 = msg.text.replace("Tr-id ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'id')
                cl.sendText(msg.to,str(trans))
            elif "Tr-th " in msg.text:
                nk0 = msg.text.replace("Tr-th ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'th')
                cl.sendText(msg.to,str(trans))
            elif "Tr-ja " in msg.text:
                nk0 = msg.text.replace("Tr-ja ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ja')
                cl.sendText(msg.to,str(trans))
            elif "Tr-en " in msg.text:
                nk0 = msg.text.replace("Tr-en ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'en')
                cl.sendText(msg.to,str(trans))
            elif "Tr-ms " in msg.text:
                nk0 = msg.text.replace("Tr-ms ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ms')
                cl.sendText(msg.to,str(trans))
            elif "Tr-it " in msg.text:
                nk0 = msg.text.replace("Tr-it ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'it')
                cl.sendText(msg.to,str(trans))
            elif "Tr-tr " in msg.text:
                nk0 = msg.text.replace("Tr-tr ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'tr')
                cl.sendText(msg.to,str(trans))
            elif "Tr-my " in msg.text:
                nk0 = msg.text.replace("Tr-my ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'my')
                cl.sendText(msg.to,str(trans))
            elif "Tr-af " in msg.text:
                nk0 = msg.text.replace("Tr-af ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'af')
                cl.sendText(msg.to,str(trans))
            elif "Tr-sq " in msg.text:
                nk0 = msg.text.replace("Tr-sq ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'sq')
                cl.sendText(msg.to,str(trans))
            elif "Tr-am " in msg.text:
                nk0 = msg.text.replace("Tr-am ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'am')
                cl.sendText(msg.to,str(trans))
            elif "Tr-ar " in msg.text:
                nk0 = msg.text.replace("Tr-ar ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ar')
                cl.sendText(msg.to,str(trans))
            elif "Tr-hy " in msg.text:
                nk0 = msg.text.replace("Tr-hy ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'hy')
                cl.sendText(msg.to,str(trans))
            elif msg.text in ["Kalender"]:
	    	      wait2['setTime'][msg.to] = datetime.today().strftime('TANGGAL : %Y-%m-%d \nHARI : %A \nJAM : %H:%M:%S')
	              cl.sendText(msg.to, "         KALENDER\n\n" + (wait2['setTime'][msg.to]))
            elif "TL: " in msg.text:
	      if msg.from_ in admin:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif ("Cn: " in msg.text):
	     if msg.from_ in admin:
              if msg.toType == 2:
                profile = cl.getProfile()
                X = msg.text.replace("Cn: ","")
                profile.displayName = X
                cl.updateProfile(profile)
                cl.sendText(msg.to,"Name  ~  " + X + " Done")
              else:
                cl.sendText(msg.to,"Failed")
            elif ("2cn: " in msg.text):
             if msg.from_ in admin:
              if msg.toType == 2:
                profile = ki.getProfile()
                X = msg.text.replace("2cn: ","")
                profile.displayName = X
                ki.updateProfile(profile)
                ki.sendText(msg.to,"name " + X + " done")
              else:
                ki.sendText(msg.to,"Failed")
            elif ("3cn: " in msg.text):
             if msg.from_ in admin:
              if msg.toType == 2:
                profile = kk.getProfile()
                X = msg.text.replace("3cn: ","")
                profile.displayName = X
                kk.updateProfile(profile)
                kk.sendText(msg.to,"name " + X + " done")
              else:
                kk.sendText(msg.to,"Failed")
            elif ("4cn: " in msg.text):
             if msg.from_ in admin:
              if msg.toType == 2:
                profile = kc.getProfile()
                X = msg.text.replace("4cn: ","")
                profile.displayName = X
                kc.updateProfile(profile)
                kc.sendText(msg.to,"name " + X + " done")
              else:
                kc.sendText(msg.to,"Failed")
            elif ("5cn: " in msg.text):
             if msg.from_ in admin:
              if msg.toType == 2:
                profile = kb.getProfile()
                X = msg.text.replace("5cn: ","")
                profile.displayName = X
                kb.updateProfile(profile)
                kb.sendText(msg.to,"name " + X + " done")
              else:
                kb.sendText(msg.to,"Failed")
            elif ("6cn: " in msg.text):
             if msg.from_ in admin:
              if msg.toType == 2:
                profile = kd.getProfile()
                X = msg.text.replace("6cn: ","")
                profile.displayName = X
                kd.updateProfile(profile)
                kd.sendText(msg.to,"name " + X + " done")
              else:
                kd.sendText(msg.to,"Failed")
            elif ("7cn: " in msg.text):
             if msg.from_ in admin:
              if msg.toType == 2:
                profile = ke.getProfile()
                X = msg.text.replace("7cn: ","")
                profile.displayName = X
                ke.updateProfile(profile)
                ke.sendText(msg.to,"name " + X + " done")
              else:
                ke.sendText(msg.to,"Failed")
            elif ("8cn: " in msg.text):
             if msg.from_ in admin:
              if msg.toType == 2:
                profile = kg.getProfile()
                X = msg.text.replace("8cn: ","")
                profile.displayName = X
                kg.updateProfile(profile)
                kg.sendText(msg.to,"name " + X + " done")
              else:
                kg.sendText(msg.to,"Failed")
            elif ("9cn: " in msg.text):
             if msg.from_ in admin:
              if msg.toType == 2:
                profile = kh.getProfile()
                X = msg.text.replace("9cn: ","")
                profile.displayName = X
                kh.updateProfile(profile)
                kh.sendText(msg.to,"name " + X + " done")
              else:
                kh.sendText(msg.to,"Failed")
            elif ("10cn: " in msg.text):
             if msg.from_ in admin:
              if msg.toType == 2:
                profile = sw.getProfile()
                X = msg.text.replace("10cn: ","")
                profile.displayName = X
                sw.updateProfile(profile)
                sw.sendText(msg.to,"name " + X + " done")
              else:
                sw.sendText(msg.to,"Failed")
            elif ("Last: " in msg.text):
             if msg.from_ in admin:
              if msg.toType == 2:
                profile = kf.getProfile()
                X = msg.text.replace("Last: ","")
                profile.displayName = X 
                kf.updateProfile(profile)
                kf.sendText(msg.to,"name " + X + " done")
              else: 
                kf.sendText(msg.to,"Failed")
	    elif ("11cn: " in msg.text):
             if msg.from_ in admin:
              if msg.toType == 2:
                profile = sw.getProfile()
                X = msg.text.replace("11cn: ","")
                profile.displayName = X
		sw.updateProfile(profile)
		sw.sendText(msg.to,"Changed ==[ " + X + " ]== Succes")
	      else:
		sw.sendText(msg.to,"Failed")

	    elif ("Mid " in msg.text):
	      if msg.from_ in admin:
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,key1)

	    elif ("Mid: " in msg.text):
	      if msg.from_ in admin:
		   mmid = msg.replace("Mid: ","")
		   msg.contentType = 13
		   msg.contentMetadata = {"mid":mmid}
		   cl.sendMessage(msg)
#---------------------------------------------------------------------------------------------
            elif msg.text in ["Protect on"]:
	      if msg.from_ in admin:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Already on")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON")
                    else:
                        cl.sendText(msg.to,"It is already on")
            elif msg.text in ["Protect qr on"]:
	      if msg.from_ in admin:
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"QR protect already on")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON")
                    else:
                        cl.sendText(msg.to,"It is already On")
            elif msg.text in ["Protect invite on"]:
	      if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect invite already on")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON")
                    else:
                        cl.sendText(msg.to,"It is already On")
            elif msg.text in ["Cancelprotect on"]:
	      if msg.from_ in admin:
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect cancel already on")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON")
                    else:
                        cl.sendText(msg.to,"It is already On")
	    elif msg.text in ["Gnamelock on"]:
	      if msg.from_ in admin:
		if wait["Protectgroupname"] == True:
		    if wait["lang"] == "JP":
			cl.sendText(msg.to,"Protect group name on")
		    else:
			cl.sendText(msg.to,"Protect group name on")
		else:
		    wait["Protectgroupname"] = True
		    if wait["lang"] == "JP":
			cl.sendText(msg.to,"Gnamelock already on")
		    else:
			cl.sendText(msg.to,"Gnamelock already on")
	    elif msg.text in ["Gnamelock off"]:
	      if msg.from_ in admin: 
		if wait["Protectgroupname"] == False:
	 	    if wait["lang"] == "JP": 
			cl.sendText(msg.to,"Protect group name off") 
		    else:
			cl.sendText(msg.to,"Protect group name off")
                else:
                    wait["Protectgroupname"] = False
		    if wait["lang"] == "JP":
			cl.sendText(msg.to,"Gnamelock already off")
		    else:
			cl.sendText(msg.to,"Gnamelock already off")
#---------------------------------------------------------------------------------------------
	    elif msg.text in ["Allprotect on","Sw on","Sw:on"]:
	      if msg.from_ in admin:
                if wait["protectJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect join already on")
                    else:
                        cl.sendText(msg.to,"Protect join already ON")
                else:
                    wait["protectJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Join already On")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Already on")
                    else:
                        cl.sendText(msg.to,"Protection already on")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection already ON")
                    else:
                        cl.sendText(msg.to,"Protection already On")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ProtectQR Already on")
                    else:
                        cl.sendText(msg.to,"ProtectQR already on")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ProtectQR Already On")
                    else:
                        cl.sendText(msg.to,"ProtectQR already On")
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ProtectInvite Already On")
                    else:
                        cl.sendText(msg.to,"ProtectInvite Already ON")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ProtectInvite already ON")
                    else:
                        cl.sendText(msg.to,"ProtectInvite already On")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"CancelProtect Already On")
                    else:
                        cl.sendText(msg.to,"CancelProtect already On")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"CancelProtect already ON")
                    else:
                        cl.sendText(msg.to,"CancelProtect already On")
#-----------------------------------------------------------------------------------------
            elif msg.text in ["Allprotect off","Sw off","Sw:off"]:
              if msg.from_ in admin:
                if wait["protectJoin"] == False:
		    if wait["lang"] == "JP":
			cl.sendText(msg.to,"Protect join already Off")
                    else:
                        cl.sendText(msg.to,"Protect join already Off")
                else:
		    wait["protectJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Join already Off")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Already off")
                    else:
                        cl.sendText(msg.to,"Protection Already off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection already Off")
                    else:
                        cl.sendText(msg.to,"Protection already off")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ProtectQR Already off")
                    else:
                        cl.sendText(msg.to,"ProtectQR Already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ProtectQR already off")
                    else:
                        cl.sendText(msg.to,"ProtectQR already Off")
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ProtectInvite Already off")
                    else:
                        cl.sendText(msg.to,"ProtectInvite Already off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ProtectInvite already off")
                    else:
                        cl.sendText(msg.to,"ProtectInvite already off")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"CancelProtect Already off")
                    else:
                        cl.sendText(msg.to,"CancelProtect Already off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"CancelProtect already off")
                    else:
                        cl.sendText(msg.to,"CancelProtect already off")
#----------------------------------------------------------------------------------------------
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
	      if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["é€��çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
	      if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Join on","Auto join:on"]:
	      if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
		else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Join off","Auto join:off"]:
	      if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif ("Auto cancel:" in msg.text):
	      if msg.from_ in admin:
                try:
                    strnum = msg.text.replace("Auto cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + " The group of people and below decided to automatically refuse invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
	      if msg.from_ in admin:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
	      if msg.from_ in admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share:on","Share on"]:
	      if msg.from_ in admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share:off","Share off"]:
	      if msg.from_ in admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Group id","List group"]:
	      if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[🔹]   %s  \n" % (cl.getGroup(i).name + " :::: " + str(len (cl.getGroup(i).members)))
                cl.sendText(msg.to, "==== [GROUPS] ====\n\n"+ h +"\n[●] TOTAL GROUPS : " +str(len(gid)))
            elif msg.text in ["Reject"]:
	      if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif msg.text in ["Cancelall1"]:
	      if msg.from_ in admin:
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"All invitations have been refused")
                else:
                    ki.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif msg.text in ["TD setting","Set","Set view","Setting"]:
	      if msg.from_ in admin:
                md = "  卐✮ 「 S͞e͞t͞t͞i͞n͞g͞ B͞oт 」卐✮\n\n╔══════════════\n"
                if wait["contact"] == True: md+="🔹 Contact  →  on\n"
                else: md+="🔹 Contact  →  off\n"
                if wait["autoJoin"] == True: md+="🔹 Auto join  →  on\n"
                else: md +="🔹 Auto join  →  off\n"
                if wait["autoCancel"]["on"] == True: md+="🔹 Auto cancel  → "+ str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "🔹 Auto cancel  →  off\n"
                if wait["likeOn"] == True: md+="�� Auto Like  →  on\n"
                else: md+="🔹 Auto Like  →  off\n"
                if wait["leaveRoom"] == True: md+="🔹 Auto leave  →  on\n"
                else: md+="🔹 Auto leave → off\n" 
		if wait["Backup"] == True: md+="🔹 Auto backup → on\n"
                else:md+="🔹 Auto backup  → off\n"
                if wait["timeline"] == True: md+="🔹 Share  →  on\n"
                else: md+="🔹 Share  →  off\n"
                if wait["autoAdd"] == True: md+="🔹 Auto add  →  on\n"
                else: md+="🔹 Auto add  →  off\n"
                if wait["commentOn"] == True: md+="🔹 Comment  →  on\n"
                else: md+="🔹 Comment  →  off\n"
		if wait["protect"] == True: md+="🔐 Protect  →  on\n"
                else:md+="🔐 Protect  →  off\n"
                if wait["linkprotect"] == True: md+="🔐 QRProtect  →  on\n"
                else:md+="🔐 QRprotect  →  off\n"
                if wait["inviteprotect"] == True: md+="🔐 Protect invite  →  on\n"
                else:md+="🔐 Protect invite  →  off \n"
                if wait["Protectgroupname"] == True: md+="🔐  Gnamelock →  on\n"
                else:md+="🔐  Gnamelock →  off \n"
                if wait["cancelprotect"] == True: md+="🔐 Protect cancel  →  on\n"
                else:md+="🔐 Protect cancel  →  off\n"
		if wait["protectJoin"] == True: md+="🔐 Protectjoin → on\n"
		else:md+="🔐 Protect join → off\n" 
		cl.sendText(msg.to,md + "╚═════════════\n\n     🔐 Aan jutawan「😎」")
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {"mid": msg.from_}
                  cl.sendMessage(msg)
                  cl.sendText(msg.to, "Acces denied for you 😆\nKetik 「Creator」 for contact admin")
                  print "COMMENT DENIED"
            elif msg.text in ["Cancelall2"]:
	      if msg.from_ in admin:
                gid = kk.getGroupIdsInvited()
                for i in gid:
                    kk.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kk.sendText(msg.to,"All invitations have been refused")
                else:
                    kk.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif msg.text in ["Backup on","Auto backup on"]:
	      if msg.from_ in admin:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Backup already On")
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup already On")
                    else:
                        cl.sendText(msg.to,"already on")
            elif msg.text in ["Backup off","Auto backup off"]:
	      if msg.from_ in admin:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                    else:
                        cl.sendText(msg.to,"Backup already Off")
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup already Off")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Auto like on"]:
	      if msg.from_ in admin:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Auto like off"]:
	      if msg.from_ in admin:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
	      if msg.from_ in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦��º†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
	      if msg.from_ in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Cek msg" in msg.text:
	      if msg.from_ in admin:
                cl.sendText(msg.to,"Your message ⤵\n\n" + str(wait["message"]))
            elif "Message set: " in msg.text:
	      if msg.from_ in admin:
                m = msg.text.replace("Message set: ","")
                if m in [""," ","\n",None]:
                    cl.sendText(msg.to,"Error")
                else:
                    wait["message"] = m
                    cl.sendText(msg.to,"Changed ⤵\n\n" + m) 
            elif "Comment set: " in msg.text:
	      if msg.from_ in admin:
                c = msg.text.replace("Comment set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Error")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Changed ⤵\n\n" + c)
            elif msg.text in ["Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
	      if msg.from_ in admin:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment:off","Comment off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
	      if msg.from_ in admin:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚") 
            elif msg.text in ["Welcome on"]:
                if wait["welcome"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Welcome already off")
                else:
                    wait["welcome"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Welcome already on")
		if wait["goodbye"] == True:
		    if wait["lang"] == "JP":
			cl.sendText(msg.to,"Message goodbye already on")
		else:
		    wait["goodbye"] = True
		    if wait["lang"] == "JP":
			cl.sendText(msg.to,"Message goodbye already on")
            elif msg.text in ["Welcome off"]:
                if wait["welcome"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Welcome already off")
                else:
                    wait["welcome"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Welcome already off")
		if wait["goodbye"] == False:
		    if wait["lang"] == "JP":
			cl.sendText(msg.to,"Message goodbye off")
		else:
		    wait["goodbye"] = False
		    if wait["lang"] == "JP":
			cl.sendText(msg.to,"Message goodbye off")

            elif msg.text in ["Cek comment"]:
	      if msg.from_ in admin:
                cl.sendText(msg.to,"Your comment ⤵\n\n" + str(wait["comment"]))
            elif msg.text in ["Bot creator","Creator"]:
            	msg.contentType = 13
                msg.contentMetadata = {'mid': 'u84e571575c1f7fe8bda071470a4511a0'}
                cl.sendMessage(msg)
            elif msg.text in ["Gurl"]:
	      if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["1gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["2gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
	      if msg.from_ in admin:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "[]" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
	    elif msg.text in ["Check"]:
	      if msg.from_ in admin:
		if wait["commentBlack"] == {}:
		    cl.sendText(msg.to,"Nothing a blacklist")
		else:
		    cl.sendText(msg.to,"Blacklist user")
		    kontak = cl.getContact(commentBlack)
		num=1
		msgs="Blacklist user\n"
		for ids in kontak:
		    msgs+="\n%si. %s" % (num, ids.displayName)
		    num=(num+1)
		msgs+="\n\n[●] Total %i blacklist user(s)" % len(kontak)
		cl.sendText(msg.to, msgs)

            elif msg.text in ["Clock on"]:
	      if msg.from_ in admin:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Clock off"]:
	      if msg.from_ in admin:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
	      if msg.from_ in admin:
                n = msg.text.replace("Change clock ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
	      if msg.from_ in admin:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,".")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock.")
#-----------------------------------------------------------------------
            elif 'youtube ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")

	   # elif "Remove chat" in msg.text:
	      #if msg.from_ in admin:
	       #try:
        #	 cl.removeAllMessages(op.param2)
        #	 ki.removeAllMessages(op.param2)
           #kc.removeAllMessages(op.param2)
        #	 kb.removeAllMessages(op.param2)
        	 #kd.removeAllMessages(op.param2)
        	#ke.removeAllMessages(op.param2)
        	#kg.removeAllMessages(op.param2)
        	#h.removeAllMessages(op.param2)
 	        #print "Success Remove Chat" 
	       #  except:
	       #     try:
               #  cl.sendText(msg.to,"Chat telah dihapus")
	       # pass
	       

#-----------------------------------------------------------------------
            elif msg.text in ["Lurkers"]:
                    cl.sendText(msg.to, "Waiting in lurkers 􀜁􀅔Har Har􏿿")
                    try:
                     del wait2['readPoint'][msg.to]
                     del wait2['readMember'][msg.to]
                    except:
                     pass
		    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime("%Y-%m-%d %H:%M")
                    wait2['ROM'][msg.to] = {}
                    print wait2

            elif msg.text in ["View"]:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "╔════════════\n%s\n\n╠═══════════\n\n%s\n╠═════════════\n║Reading point creation:\n║ [%s]\n╚══════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik「Lurkers」dulu pekok ahhh 􀜁􀅔Har Har􏿿")

#-------------------------------------------------
	    elif "Spam to @" in msg.text:
	      if msg.from_ in admin:
                _name = msg.text.replace("Spam to @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
		       cl.sendText(msg.to,"Wating in progres...")
                       ke.sendText(g.mid,"Your Account Has Been Spammed !")
                       kk.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       kc.sendText(g.mid,"Your Account Has Been Spammed !")
		       kb.sendText(g.mid,"Your Account Has Been Spammed !")
                       kd.sendText(g.mid,"Your Account Has Been Spammed !")
                       kg.sendText(g.mid,"Your Account Has Been Spammed !")
                       kh.sendText(g.mid,"Your Account Has Been Spammed !")
		       kg.sendText(g.mid,"Your Account Has Been Spammed !")
                       kh.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       kc.sendText(g.mid,"Your Account Has Been Spammed !")
	  	       ke.sendText(g.mid,"Your Account Has Been Spammed !")
                       kk.sendText(g.mid,"Your Account Has Been Spammed !")
                       kb.sendText(g.mid,"Your Account Has Been Spammed !")
                       kd.sendText(g.mid,"Your Account Has Been Spammed !")
		       kh.sendText(g.mid,"Your Account Has Been Spammed !")
                       kg.sendText(g.mid,"Your Account Has Been Spammed !")
                       kh.sendText(g.mid,"Your Account Has Been Spammed !")
                       kc.sendText(g.mid,"Your Account Has Been Spammed !")
		       ke.sendText(g.mid,"Your Account Has Been Spammed !") 
		       kk.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !") 
		       kc.sendText(g.mid,"Your Account Has Been Spammed !")
                       kb.sendText(g.mid,"Your Account Has Been Spammed !")
                       kd.sendText(g.mid,"Your Account Has Been Spammed !")
                       kk.sendText(g.mid,"Your Account Has Been Spammed !") 
		       kh.sendText(g.mid,"Your Account Has Been Spammed !")
                       kg.sendText(g.mid,"Your Account Has Been Spammed !") 
		       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !") 
		       kc.sendText(g.mid,"Your Account Has Been Spammed !")
                       ke.sendText(g.mid,"Your Account Has Been Spammed !")
                       kk.sendText(g.mid,"Your Account Has Been Spammed !")
                       kb.sendText(g.mid,"Your Account Has Been Spammed !") 
		       kd.sendText(g.mid,"Your Account Has Been Spammed !") 
		       kb.sendText(g.mid,"Your Account Has Been Spammed !")
                       kg.sendText(g.mid,"Your Account Has Been Spammed !")
		       kh.sendText(g.mid,"Your Account Has Been Spammed !") 
		       kg.sendText(g.mid,"Your Account Has Been Spammed !")
                       kk.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !") 
		       kc.sendText(g.mid,"Your Account Has Been Spammed !")
                       ke.sendText(g.mid,"Your Account Has Been Spammed !")
                       kk.sendText(g.mid,"Your Account Has Been Spammed !") 
		       kb.sendText(g.mid,"Your Account Has Been Spammed !")
                       kd.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       kg.sendText(g.mid,"Your Account Has Been Spammed !")
                       kh.sendText(g.mid,"Your Account Has Been Spammed !")
                       kk.sendText(g.mid,"Your Account Has Been Spammed !")
                       ke.sendText(g.mid,"Your Account Has Been Spammed !")
                       kk.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       kc.sendText(g.mid,"Your Account Has Been Spammed !")
                       kb.sendText(g.mid,"Your Account Has Been Spammed !")
                       kd.sendText(g.mid,"Your Account Has Been Spammed !")
                       kc.sendText(g.mid,"Your Account Has Been Spammed !")
                       kh.sendText(g.mid,"Your Account Has Been Spammed !")
                       kg.sendText(g.mid,"Your Account Has Been Spammed !")
                       kk.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       kc.sendText(g.mid,"Your Account Has Been Spammed !")
                       ke.sendText(g.mid,"Your Account Has Been Spammed !")
                       kk.sendText(g.mid,"Your Account Has Been Spammed !")
                       kb.sendText(g.mid,"Your Account Has Been Spammed !")
                       kd.sendText(g.mid,"Your Account Has Been Spammed !") 
		       kg.sendText(g.mid,"Your Account Has Been Spammed !")
                       kb.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !") 
		       kc.sendText(g.mid,"Your Account Has Been Spammed !")
                       ke.sendText(g.mid,"Your Account Has Been Spammed !")
                       kk.sendText(g.mid,"Your Account Has Been Spammed !") 
		       kb.sendText(g.mid,"Your Account Has Been Spammed !")
                       kd.sendText(g.mid,"Your Account Has Been Spammed !")
                       kd.sendText(g.mid,"Your Account Has Been Spammed !")
                       kg.sendText(g.mid,"Your Account Has Been Spammed !")
                       kh.sendText(g.mid,"Your Account Has Been Spammed !")
                       kd.sendText(g.mid,"Your Account Has Been Spammed !")
                       ke.sendText(g.mid,"Your Account Has Been Spammed !")
                       kk.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       kc.sendText(g.mid,"Your Account Has Been Spammed !")
                       kb.sendText(g.mid,"Your Account Has Been Spammed !")
                       kd.sendText(g.mid,"Your Account Has Been Spammed !")
                       ke.sendText(g.mid,"Your Account Has Been Spammed !")
                       kh.sendText(g.mid,"Your Account Has Been Spammed !")
                       kg.sendText(g.mid,"Your Account Has Been Spammed !")
                       ke.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       kc.sendText(g.mid,"Your Account Has Been Spammed !")
                       ke.sendText(g.mid,"Your Account Has Been Spammed !")
                       kk.sendText(g.mid,"Your Account Has Been Spammed !")
                       kb.sendText(g.mid,"Your Account Has Been Spammed !")
                       kd.sendText(g.mid,"Your Account Has Been Spammed !")
		       ke.sendText(g.mid,"Your Account Has Been Spammed !")
                       kh.sendText(g.mid,"Your Account Has Been Spammed !")
                       kg.sendText(g.mid,"Your Account Has Been Spammed !")
                       ke.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       kc.sendText(g.mid,"Your Account Has Been Spammed !")
		       ke.sendText(g.mid,"Your Account Has Been Spammed !")
                       kh.sendText(g.mid,"Your Account Has Been Spammed !")
                       kg.sendText(g.mid,"Your Account Has Been Spammed !")
                       kk.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       kc.sendText(g.mid,"Your Account Has Been Spammed !")
		       kc.sendText(g.mid,"Your Account Has Been Spammed !")
                       kh.sendText(g.mid,"Your Account Has Been Spammed !")
                       kg.sendText(g.mid,"Your Account Has Been Spammed !")
                       kc.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       kc.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(msg.to, "Succes")
                       print " Spammed !"
#--------------------------------------------------------------------------
            elif "Admin on @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admin on @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Ditambahkan di perangkat Bot")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command tidak bisa")
                    cl.sendText(msg.to,"Bot ready in admin only")

            elif "Admin off @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admin off @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Dihapus dari perangkat Bot")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command tidak bisa")
                    cl.sendText(msg.to,"Bot ready in admin only")

            elif msg.text in ["Admin list","List admin"]:
                if admin == []:
                    cl.sendText(msg.to,"The admin is empty")
                else:
                    cl.sendText(msg.to,"This is admin bot")
                    mc = ""
                    for mi_d in admin:
                        mc += "[●] " + cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#~~~~~~___________________________________________________________                    
#------------------------------------------------------------------------------
	    elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                text = msg.text
                if text is not None:
                    cl.sendText(msg.to,text)
                else:
                    if msg.contentType == 7:
                        msg.contentType = 7
                        msg.text = None
                        msg.contentMetadata = {
                                             "STKID": "6",
                                             "STKPKGID": "1",
                                             "STKVER": "100" }
                        cl.sendMessage(msg)
                    elif msg.contentType == 13:
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
                        cl.sendMessage(msg)
            elif "Mimic:" in msg.text:
                if msg.from_ in admin:
                    cmd = msg.text.replace("Mimic:","")
                    if cmd == "on":
                        if mimic["status"] == False:
                            mimic["status"] = True
                            cl.sendText(msg.to,"Mimic on")
                        else:
                            cl.sendText(msg.to,"Mimic already on")
                    elif cmd == "off":
                        if mimic["status"] == True:
                            mimic["status"] = False
                            cl.sendText(msg.to,"Mimic off")
                        else:
                            cl.sendText(msg.to,"Mimic already off")
                    elif "add " in cmd:
                        target0 = msg.text.replace("Mimic:add ","")
                        target1 = target0.lstrip()
                        target2 = target1.replace("@","")
                        target3 = target2.rstrip()
                        _name = target3
                        gInfo = cl.getGroup(msg.to)
                        targets = []
                        for a in gInfo.members:
                            if _name == a.displayName:
                                targets.append(a.mid)
                        if targets == []:
                            cl.sendText(msg.to,"No targets")
                        else:
                            for target in targets:
                                try:
                                    mimic["target"][target] = True
                                    cl.sendText(msg.to,"Success added target")
                                    mid.sendMessageWithMention(msg.to,target)
                                    break
                                except:
                                    mid.sendText(msg.to,)
                                    break
                    elif "del " in cmd:
                        target0 = msg.text.replace("Mimic:del ","")
                        target1 = target0.lstrip()
                        target2 = target1.replace("@","")
                        target3 = target2.rstrip()
                        _name = target3
                        gInfo = cl.getGroup(msg.to)
                        targets = []
                        for a in gInfo.members:
                            if _name == a.displayName:
                                targets.append(a.mid)
                        if targets == []:
                            cl.sendText(msg.to,"No targets")
                        else:
                            for target in targets:
                                try:
                                    del mimic["target"][target]
                                    cl.sendText(msg.to,"Success deleted target")
                                    mid.sendMessageWithMention(msg.to,target)
                                    break
                                except:
                                    mid.sendText(msg.to,)
                                    break
                    elif "target" in cmd:
                        if mimic["target"] == {}:
                            ki.sendText(msg.to,"No target")
                        else:
                            lst = "List Target"
                            total = len(mimic["target"])
                            for a in mimic["target"]:
                                if mimic["target"][a] == True:
                                    stat = "On"
                                else:
                                    stat = "Off"
                                lst += "\n->" + me.getContact(a).displayName + " | " + start
                            ki.sendText(msg.to,lst + "\nTotal:" + total)
#----------------------------------------------------------------------------
            elif "Staff on @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Staff on @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Staff Ditambahkan diperangkat bot")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin & staff permission required.")

            elif "Staff off @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Staff off @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Staff Dihapus dari perangkat bot")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin & staff permission required.")

            elif msg.text in ["Staff list"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff in bot")
                    mc = ""
                    for mi_d in staff:
                        mc += "[●]" + cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#-------------------------------------------------------------------------------
	    elif "Eeaa " in msg.text:
                  if msg.from_ in admin:
		       nk0 = msg.text.replace("Eeaa ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:                                    
                                    G = cl.getGroup(msg.to)
                                    ginfo = cl.getGroup(msg.to)
                                    G.preventJoinByTicket = False
                                    cl.updateGroup(G)
                                    invsend = 0
                                    Ticket = cl.reissueGroupTicket(msg.to)
                                    sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    time.sleep(0.2)
                                    G = cl.getGroup(msg.to)
                                    G.preventJoinByTicket = True
                                    sw.kickoutFromGroup(msg.to,[target])
                                    sw.leaveGroup(msg.to)
                                    cl.updateGroup(G)
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Succes ")
                                    kk.sendText(msg.to,"Bye")

            elif "Nk " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:                                    
                                    G = cl.getGroup(msg.to)
                                    ginfo = cl.getGroup(msg.to)
                                    G.preventJoinByTicket = False
                                    cl.updateGroup(G)
                                    invsend = 0
                                    Ticket = cl.reissueGroupTicket(msg.to)
                                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    time.sleep(0.2)
                                    G = cl.getGroup(msg.to)
                                    G.preventJoinByTicket = True
                                    ki.kickoutFromGroup(msg.to,[target])
                                    ki.leaveGroup(msg.to)
                                    cl.updateGroup(G)
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Succes ")
                                    kk.sendText(msg.to,"Bye")

#-----------------------------------------------                   
            elif msg.text in ["TD in"]:
	      if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"

            elif msg.text in ["TD 1"]:
	      if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ticket = cl.reissueGroupTicket(msg.to)
		  ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.2)
                  kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.2)
                  kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.2)
                  kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.2)
                  kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.2)
                  ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.2)
                  kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.2)
		  kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.2)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Sw 2"]:
	      if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ticket = cl.reissueGroupTicket(msg.to) 
		  kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.2)
                  kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.2)
                  kl.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.2)
                  km.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.2)
                  kn.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.2)
                  ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.2)
                  kp.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.2)
                  kq.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.2)
                  G = ko.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ko.updateGroup(G)
                  Ticket = ko.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Kuy3"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kc.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kc.updateGroup(G)
                  Ticket = kc.reissueGroupTicket(msg.to)

	    elif msg.text in ["Kuy4"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kb.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kb.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kb.updateGroup(G)
                  Ticket = kb.reissueGroupTicket(msg.to)

	    elif msg.text in ["Kuy5"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kd.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kd.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kd.updateGroup(G)
                  Ticket = kd.reissueGroupTicket(msg.to)

	    elif msg.text in ["Kuy6"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ke.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ke.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ke.updateGroup(G)
                  Ticket = ke.reissueGroupTicket(msg.to)

	    elif msg.text in ["Kuy7"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kg.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kg.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kg.updateGroup(G)
                  Ticket = kg.reissueGroupTicket(msg.to)

	    elif msg.text in ["Kuy8"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kh.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kh.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kh.updateGroup(G)
                  Ticket = kh.reissueGroupTicket(msg.to)

	    elif msg.text in ["."]:
	      if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  sw.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = sw.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  sw.updateGroup(G)
                  Ticket = sw.reissueGroupTicket(msg.to)
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {"mid": msg.from_}
                  cl.sendMessage(msg)
                  cl.sendText(msg.to, "Acces denied for you 😆\nKetik 「Creator」 for contact admin")
                  print "COMMENT DENIED"
#-----------------------------------------------
	    elif msg.text in ["Mentions","Tagall","Mentionall"]:
	      if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 
	      else:
               	   cl.sendText(msg.to,noticeMessage)
               	   msg.contentType = 13
                   msg.contentMetadata = {"mid": msg.from_}
                   cl.sendMessage(msg)
                   cl.sendText(msg.to, "Acces denied for you 😊\nKetik 「Creator」for contact admin")

#-----------------------------------------------
	    elif msg.text in ["TD all out"]:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = kk.getGroupIdsJoined()
                gid = kc.getGroupIdsJoined()
                gid = kb.getGroupIdsJoined()
                gid = kd.getGroupIdsJoined()
                gid = ke.getGroupIdsJoined()
		gid = kg.getGroupIdsJoined()
                gid = kh.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    kk.leaveGroup(i)
                    kc.leaveGroup(i)
                    kb.leaveGroup(i)
                    kd.leaveGroup(i)
                    ke.leaveGroup(i)
		    kg.leaveGroup(i)
                    kh.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Bot sudah keluar dari semua grup")
                else:
                    cl.sendText(msg.to,"He declined all invitations")

	    elif msg.text in ["TD out"]:
	      if msg.from_ in admin:
		if msg.toType == 2:
		    ginfo = cl.getGroup(msg.to)
		    try:
			cl.sendText(msg.to,"Bye bye " + str(ginfo.name)  + "")
			ki.leaveGroup(msg.to)
			kk.leaveGroup(msg.to)
			kc.leaveGroup(msg.to)
			kb.leaveGroup(msg.to)
			kd.leaveGroup(msg.to)
			ke.leaveGroup(msg.to)
			kg.leaveGroup(msg.to)
			kh.leaveGroup(msg.to)
		    except:
			pass

            elif msg.text in ["TD bye"]:
	      if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
			ki.sendText(msg.to,"Bye Bye  "  +  str(ginfo.name)  + "")
			ki.leaveGroup(msg.to)
			kk.sendText(msg.to,"Bye Bye  "  +  str(ginfo.name)  + "")
			kk.leaveGroup(msg.to)
			kc.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
			kc.leaveGroup(msg.to)
			kb.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
			kb.leaveGroup(msg.to)
			kd.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
			kd.leaveGroup(msg.to)
			ke.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
			ke.leaveGroup(msg.to)
			kg.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
			kg.leaveGroup(msg.to)
			kh.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
			kh.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Leave"]:
	      if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        sw.leaveGroup(msg.to)
                    except:
                        pass
#------------------------[Copy]-------------------------
            elif msg.text in ["TD kembali"]:
	      if msg.from_ in admin:
                    try:
                        cl.updateDisplayPicture(backup.pictureStatus)
                        cl.updateProfile(backup)
                        cl.sendText(msg.to,"Backup done")
                    except Exception as e:
                        cl.sendText(msg.to, str (e))
                        
            elif "kedapkedip " in msg.text.lower():
                txt = msg.text.replace("kedapkedip ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
                        
                        
            elif "TD:Bc " in msg.text:
                bctxt = msg.text.replace("TD:Bc ", "")
                a = cl.getAllContactIds()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))

            elif "TD:Bc " in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("TD:Bc ", "")
                b = ki.getAllContactIds()
                for manusia in b:
                    ki.sendText(manusia, (bctxt))
                c = kk.getAllContactIds()
                for manusia in c:
                    kk.sendText(manusia, (bctxt))
                d = kc.getAllContactIds()
                for manusia in d:
                    kc.sendText(manusia, (bctxt))
                e = kb.getAllContactIds()
                for manusia in e:
                    kb.sendText(manusia, (bctxt))
                f = kd.getAllContactIds()
                for manusia in f:
                    kd.sendText(manusia, (bctxt))
                g = ke.getAllContactIds()
                for manusia in g:
                    ke.sendText(manusia, (bctxt))
                h = kg.getAllContactIds()
                for manusia in h:
                    kg.sendText(manusia, (bctxt))
                i = kh.getAllContactIds()
                for manusia in i:
                    kh.sendText(manusia, (bctxt))
                j = sw.getAllContactIds()
                for manusia in j:
                    sw.sendText(manusia, (bctxt))

#_______________
            elif "InviteMeTo: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("InviteMeTo: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
                            
                            
            elif msg.text in ["TD leaveAllGc"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = kk.getGroupIdsJoined()
                gid = kc.getGroupIdsJoined()
                gid = kb.getGroupIdsJoined()
                gid = kd.getGroupIdsJoined()
                gid = ke.getGroupIdsJoined()
                gid = kg.getGroupIdsJoined()
                gid = kh.getGroupIdsJoined()
                gid = sw.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    kk.leaveGroup(i)
                    kc.leaveGroup(i)
                    kb.leaveGroup(i)
                    kd.leaveGroup(i)
                    ke.leaveGroup(i)
                    kg.leaveGroup(i)
                    kh.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    cl.sendText(msg.to,"He declined all invitations")

	    elif msg.text in ["Sw1 kembali"]:
	      if msg.from_ in admin:
                    try:
                        kc.updateDisplayPicture(backup.pictureStatus)
                        kc.updateProfile(backup)
                        kc.sendText(msg.to,"Backup done")
                    except Exception as e:
                        kc.sendText(msg.to, str (e))

            elif "TD copy @" in msg.text:
	      if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Copy]"
                    _name = msg.text.replace("TD copy @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to, "Not Found")
                    else:                                                                                                                       
                        for target in targets:
                            try:
                                cl.CloneContactProfile(target)
                                cl.sendText(msg.to, "Succes copy")
                            except Exception as e:
                                print e
                                
	    elif "TD clone @" in msg.text:
	      if msg.from_ in admin: 
		if msg.toType == 2:
                    print "[Copy]"
		    _name = msg.text.replace("TD clone @","")
                    _nametarget = _name.rstrip(' ') 
		    gs = kc.getGroup(msg.to)
                    targets = [] 
		    for g in gs.members:
                        if _nametarget == g.displayName: 
			    targets.append(g.mid)
                    if targets == []: 
			kc.sendText(msg.to, "Not Found")
                    else: 
			for target in targets:
                            try: 
				kc.CloneContactProfile(target)
                                kc.sendText(msg.to, "Succes clone") 
			    except Exception as e:
                                print e
                                
                                
                #=====TRANSLATE===========

            elif "/translate-en " in msg.text:
                txt = msg.text.replace("/translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except:
                    cl.sendText(msg.to,'Error.')

            elif "/translate-id " in msg.text:
                txt = msg.text.replace("/translate-id ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except:
                    cl.sendText(msg.to,'Error.')
                                
                                
#-----------------------------------------------
            elif "Glist" in msg.text:
                if msg.from_ in admin:
                        gid = cl.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "=> %s  \n" % (cl.getGroup(i).name + " | Members : [ " + str(len (cl.getGroup(i).members))+" ]")
                        cl.sendText(msg.to, "#[List Grup]# \n"+ h +"Total Group : " +"[ "+str(len(gid))+" ]")
            elif msg.text.lower() == 'group id':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)

            elif msg.text in ["Fuck"]:
	      if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Bye")
                        return
                    for jj in matched_list:
                        try:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass

	    elif "Clearall" in msg.text:
	      if msg.from_ in admin:
                       nk0 = msg.text.replace("Clearall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("all","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                              targets.append(g.mid)
                       if targets == []:
                           cl.sendText(msg.to,"Tidak Ada Member")
                           pass
                       else:
                           for target in targets:
                             if not target in Bots and admin:
                              try:
                                  cl.kickoutFromGroup(msg.to,[target])
                                  print (msg.to,[g.mid])
                              except:
                                  cl.sendText(msg.to,"Salam kenal hehehe...")
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {"mid": msg.from_}
                  cl.sendMessage(msg)
                  cl.sendText(msg.to, "Acces denied for you 😆\nKetik 「Creator」 for contact admin")
                  print "COMMENT DENIED"

            elif "TD play" in msg.text:
	      if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Sw play","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
		    gs = kc.getGroup(msg.to)
		    gs = kb.getGroup(msg.to)
		    gs = kd.getGroup(msg.to)
		    gs = ke.getGroup(msg.to)
		    gs = kg.getGroup(msg.to)
                    gs = kh.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                        kk.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots and admin:
                            try:
                                klist=[cl,ki,kk,kc,kb,kd,ke,kg,kh]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg,to,"Group cleanse")
                                cl.sendText(msg,to,"Group cleanse")
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {"mid": msg.from_}
                  cl.sendMessage(msg)
                  cl.sendText(msg.to, "Acces denied for you 😆\nKetik 「Creator」 for contact admin")
                  print "COMMENT DENIED"
#-------------------------------------------------------------------
            elif "Mk " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Mk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                             if not target in Bots and admin:
                                try:                               
                                    cl.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Succes ")
                                    kk.sendText(msg.to,"Bye")
              	  else:
                      msg.contentType = 13
                      msg.contentMetadata = {"mid": msg.from_}
                      cl.sendMessage(msg)
                      cl.sendText(msg.to, "Acces denied for you 😆\nKetik 「Creator」 for contact admin")
                      print "COMMENT DENIED"
#-----------------------------------------------------------------------
            elif "BL @" in msg.text:
	      if msg.from_ in admin:
                _name = msg.text.replace("BL @","")
                _kicktarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
			      if not target in Bots and admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Succes ")
                                except:
                                    cl.sendText(msg.to,"error")

	    elif "TD del" in msg.text:
	      if msg.from_ in admin:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"Blacklist user succes dibersihkan")

            elif "TD ban" in msg.text:
              if msg.toType == 2:
                  if msg.from_ in admin:                                        
                       ban0 = msg.text.replace("TD ban","")
                       ban1 = ban0.lstrip()
                       ban2 = ban1.replace("@","")
                       ban3 = ban2.rstrip()
                       _name = ban3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"user does not exist")
                           pass
                       else:
                            for target in targets:
			      if not target in Bots and admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                except:
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ Success")
                                
	    elif "Spam" in msg.text:
	      if msg.from_ in admin:
		   _name = msg.text.replace("Spam ","")
		   _nametarget = _name.rstrip(' ')
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   if txt[1] == "on":
                        if jmlh <= 10000:
                             for x in range(jmlh):
                                    cl.sendText(msg.to, teks)
                        else:
                               cl.sendText(msg.to, "Melebihi Batas!!! ")
                   elif txt[1] == "off":
                         if jmlh <= 10000:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Melebihi Batas!!! ")

            elif "Anjuu" in msg.text:
	      if msg.from_ in admin:
                if msg.toType == 2:
                    print "Fuck"
                    _name = msg.text.replace("Anjuu","")
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
			  if not target in Bots and admin:
                            try:
                                cl.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                pass

            elif "Ban @" in msg.text:
              if msg.toType == 2:
                  if msg.from_ in admin:
                       ban0 = msg.text.replace("Ban @","")
                       ban1 = ban0.lstrip()
                       ban2 = ban1.replace("@","")
                       ban3 = ban2.rstrip()
                       _name = ban3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"This contact can't is a blacklist")
                           pass
                       else:
                            for target in targets:
                              if not target in Bots and admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Done blacklist")
                                except:
                                    cl.sendText(msg.to,"Done blacklist")
		  else:
               	   msg.contentType = 13
                   msg.contentMetadata = {"mid": msg.from_}
                   cl.sendMessage(msg)
                   cl.sendText(msg.to, "Acces denied for you 😊\nKetik 「Creator」for contact admin")
#--------------------------------------------------------------------------------- 
            elif "Mayhem" in msg.text:
	      if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Mayhem","")
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"「 mayhem ���\nmayhem is STARTING♪\n abort to abort♪")
                    cl.sendText(msg.to,"「 mayhem 」\nAll victims shall yell hul·la·ba·loo♪\nhələbəˈlo͞o hələbəˌlo͞o")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not Found")
                    else:
                        for target in targets:
                            if target not in Bots and admin:
                                try:
                                   klist=[cl,ki,kk,kc,kb,kd,ke,kf,kg,kh,kj,kl,km,kn,ko,kp,kq]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   cl.sendText(msg.to,"Mayhem done")
#----------------------------------------------------------------------------------
            elif "Cipok" in msg.text:
	      if msg.from_ in admin:
                if msg.contentMetadata is not None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                           cl.kickoutFromGroup(msg.to,[target])
                    else:
                        pass

      	    elif "Sayang" in msg.text:
	      if msg.from_ in admin:
                if msg.contentMetadata is not None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki.kickoutFromGroup(msg.to,[target])
                        except:
                           ki.kickoutFromGroup(msg.to,[target])
                    else:
                        pass
#-----------------------------------------------
            elif "Say " in msg.text:
              if msg.from_ in admin:        
                string = msg.text.replace("Say ","")
                if len(string.decode('utf-8')) <= 50:
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
                    kb.sendText(msg.to," " + string + " ")
                    kd.sendText(msg.to," " + string + " ")
                    ke.sendText(msg.to," " + string + " ")
                    kg.sendText(msg.to," " + string + " ")
                    kh.sendText(msg.to," " + string + " ")

	    elif "Bc: " in msg.text:
	      if msg.from_ in admin:
		bctxt = msg.text.replace("Bc: ","")
		A = cl.getProfile()
		n = cl.getGroupIdsJoined()
		for manusia in n:
			cl.sendText(manusia, (bctxt) + "\n\nBroadcast by : " + (A.displayName))
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {"mid": msg.from_}
                  cl.sendMessage(msg)
                  cl.sendText(msg.to, "Acces denied for you 😆\nKetik 「Creator」 for contact admin")
                  print "COMMENT DENIED"

            elif "Respon" in msg.text:
	      if msg.from_ in admin:
		s = cl.getProfile()
                s1 = ki.getProfile()
                s2 = kk.getProfile()
                s3 = kc.getProfile()
		s4 = kb.getProfile()
                s5 = kd.getProfile()
                s6 = ke.getProfile()
		s7 = kg.getProfile()
                s8 = kh.getProfile()
		cl.sendText(msg.to, s.displayName + "  ready 􀜁􀅔Har Har􏿿")
		ki.sendText(msg.to, s1.displayName + " ready 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to, s2.displayName + " ready 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to, s3.displayName + " ready 􀜁􀅔Har Har􏿿")
                kb.sendText(msg.to, s4.displayName + " ready 􀜁��Har Har􏿿")
                kd.sendText(msg.to, s5.displayName + " ready 􀜁􀅔Har Har􏿿")
                ke.sendText(msg.to, s6.displayName + " ready 􀜁􀅔Har Har􏿿")
		kg.sendText(msg.to, s7.displayName + " ready 􀜁􀅔Har Har􏿿")
                kh.sendText(msg.to, s8.displayName + " ready 􀜁􀅔Har Har􏿿")
#-----------------------------------------------
            elif "Pict @" in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Pict @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#-----------------------------------------------
            elif msg.text in ["TD absen"]:
	      if msg.from_ in admin:
		cl.sendText(msg.to,"Hadirr")              
                ki.sendText(msg.to,"Hadiirrr")
                kk.sendText(msg.to,"Hadirr")
                kc.sendText(msg.to,"Hadirr")
                kb.sendText(msg.to,"Hadiirrr")
                kd.sendText(msg.to,"Hadirr")
                ke.sendText(msg.to,"Hadirr")
                kg.sendText(msg.to,"Hadiirrr")
                kh.sendText(msg.to,"Hadirr")

#-----------------------------------------------
            elif "Sp" in msg.text:
	      if msg.from_ in admin:
                start = time.time()
                cl.sendText(msg.to, "Progress Acces mlaku...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds 􀨁􀄻double thumbs up��" % (elapsed_time))
              else:
               	  msg.contentType = 13
                  msg.contentMetadata = {"mid": msg.from_}
                  cl.sendMessage(msg)
                  cl.sendText(msg.to, "Acces denied for you 😊\nKetik 「Creator」for contact admin")
		  print "COMMEND DENIED"

            elif "speed" in msg.text:
	      if msg.from_ in admin:
                start = time.time()
                cl.sendText(msg.to, "Progress Acces mlaku...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds 􀨁􀄻double thumbs up􏿿" % (elapsed_time))
                ki.sendText(msg.to, "%sseconds 􀨁􀄻double thumbs up􏿿" % (elapsed_time))
                kk.sendText(msg.to, "%sseconds 􀨁􀄻double thumbs up􏿿" % (elapsed_time))
                kc.sendText(msg.to, "%sseconds 􀨁􀄻double thumbs up􏿿" % (elapsed_time))
                kb.sendText(msg.to, "%sseconds 􀨁􀄻double thumbs up􏿿" % (elapsed_time))
              else:
               	  msg.contentType = 13
                  msg.contentMetadata = {"mid": msg.from_}
                  cl.sendMessage(msg)
                  cl.sendText(msg.to, "Acces denied for you 😊\nKetik 「Creator」for contact admin")
		  print "COMMEND DENIED"

            elif "Cbc: " in msg.text:
	      if msg.from_ in admin:
		bctxt = msg.text.replace("Cbc: ", "")
		contact = cl.getAllContactIds()
		for cbc in contact:
			cl.sendText(cbc,(bctxt))

#------------------------------------------------------------------
            elif msg.text in ["Ban:on"]:
	      if msg.from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact to blacklist")

            elif msg.text in ["Unban:on"]:
	      if msg.from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact to unblacklist")

            elif msg.text in ["Banlist"]:
	      if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing a blacklist user")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = "[●]「Blacklist User」[●]\n\n"
                    for mi_d in wait["blacklist"]:
                        mc += "~ " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
	      if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kick ban"]:
	      if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
		    group = ki.getGroup(msg.to)
		    group = kk.getGroup(msg.to)
		    group = kc.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        ki.sendText(msg.to,"There was no blacklist user")
                        kk.sendText(msg.to,"There was no blacklist user")
                        kc.sendText(msg.to,"There was no blacklist user")
                        
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])                        
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist user")
                    ki.sendText(msg.to,"Blacklist user")
                    kk.sendText(msg.to,"Blacklist user")
                    
            elif msg.text in [".."]:
	     if msg.from_ in admin:
              if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"")

#-----------------------------------------------------------------

             
        if op.param3 == "1":
            if op.param1 in Protectgroupmame:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["Protectgrouname"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass


	if op.type == 17:
           if wait["protectJoin"] == True:
               if op.param2 not in Bots:
                   random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			cl.updateGroup(G)
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass

        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['Gnamelock']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = kb.getGroup(op.param1)
                                except:
                                    try:
                                        G = ki.getGroup(op.param1)
				    except:
					try:
                                            G = kc.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['Gnamelock'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    ke.updateGroup(G)
                                except:
                                    try:
                                        kc.updateGroup(G)
                                    except:
                                        try:
                                            ke.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in Bots:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"Gnamelock")
                                        ki.sendText(op.param1,"Haddeuh dikunci Pe'a")
                                        kk.sendText(op.param1,"Wekawekaweka 􀜁􀅔Har Har􏿿")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)

	if op.type == 17:
	    if op.param2 not in Bots:
		joinblacklist = op.param2.replace(".",',') 
		joinblacklistX = joinblacklist.split(",") 
	        matched_list = [] 
		for tag in wait["blacklist"]: 
		    matched_list+=filter(lambda str: str == tag, joinblacklistX)
		if matched_list == []: 
		    pass 
		else:
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

	if op.type == 17:
	   if op.param2 not in Bots:
	      if op.param2 in wait["blacklist"]:
		random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
#--------------------------------------------------------------------------------
	if op.type == 19:
	    if op.param3 in admin and op.param2 in Bots:
		random.choice(KAC).inviteIntoGroup(op.param3)
		random.choice(KAC).findAndAddContactsByMid(op.param3)

	if op.type == 19:
           if op.param3 in admin:
              cl.inviteIntoGroup(op.param1,admin)

	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = cl.getGroup(op.param1)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")

	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"Please contact admin for invite member")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")

	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = cl.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    Ticket = cl.reissueGroupTicket(op.param1)
                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
		    sw.kickoutFromGroup(op.param1,[op.param2])
		    cl.updateGroup(G)
		    sw.leaveGroup(op.param1)
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
		
#-----------------------------------------------------------------------------
	if op.type == 46:
	    if op.param2 in Bots:
		   cl.removeAllMessages()
	   	   ki.removeAllMessages()
	   	   kk.removeAllMessages()
		   kc.removeAllMessages()
		   kb.removeAllMessages()
		   kd.removeAllMessages()
		   ke.removeAllMessages()
		   kg.removeAllMessages()
		   kh.removeAllMessages()
	#	kj.removeAllMessages()
#------------------------------------------------------------------------------
	if op.type == 55:
	    print "NOTIFIED_READ_MESSAGE"
            try:
		if op.param1 in wait2['readPoint']:
		    Name = cl.getContact(op.param2).displayName
		    if Name in wait2['readMember'][op.param1]:
		        pass
		    else:
			wait2['readMember'][op.param1] += "\n• " + Name
                        wait2['ROM'][op.param1][op.param2] = "• " + Name
			wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
		else:
                    cl.sendText
	    except:
		pass

        if op.type == 59:
            print op


           
    except Exception as error:
        print error


def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kk.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kc.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kb.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kd.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ke.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kg.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kh.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   #kj.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                 #  kf.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   #kl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                #   km.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                #   kn.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                  # ko.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
               #    kp.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
               #    kq.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["Owner Guntur ponya selera I like you"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(500)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
