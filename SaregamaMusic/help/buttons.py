from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

import config
from SONALI_MUSIC import app

class BUTTONS(object):
    BBUTTON = [
        [
            InlineKeyboardButton("ʙᴧη", callback_data="MANAGEMENT_BACK HELP_14"),
            InlineKeyboardButton("ᴋɪᴄᴋ", callback_data="MANAGEMENT_BACK HELP_15"),
            InlineKeyboardButton("ϻυᴛє", callback_data="MANAGEMENT_BACK HELP_16"),
        ],
        [
            InlineKeyboardButton("ᴘɪη", callback_data="MANAGEMENT_BACK HELP_17"),
            InlineKeyboardButton("sᴛᴧғғ", callback_data="MANAGEMENT_BACK HELP_18"),
            InlineKeyboardButton("sєᴛ-υᴘ", callback_data="MANAGEMENT_BACK HELP_19"),
        ],
        [
            InlineKeyboardButton("ᴢσϻʙɪє", callback_data="MANAGEMENT_BACK HELP_20"),
            InlineKeyboardButton("ɢᴧϻє", callback_data="MANAGEMENT_BACK HELP_21"),
            InlineKeyboardButton("ɪϻᴘσsᴛєʀ", callback_data="MANAGEMENT_BACK HELP_22"),
        ],
        [
            InlineKeyboardButton("sɢ", callback_data="MANAGEMENT_BACK HELP_23"),
            InlineKeyboardButton("ᴛʀ", callback_data="MANAGEMENT_BACK HELP_24"),
            InlineKeyboardButton("ɢʀᴧᴘʜ", callback_data="MANAGEMENT_BACK HELP_26"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data=f"MAIN_CP"), 
        ]
        ]
    PBUTTON = [
        [
            InlineKeyboardButton("˹ ᴄσηᴛᴧᴄᴛ ˼", url="https://t.me/Sarker_xd")
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data="MAIN_CP"),
            
        ]
        ]
    
    ABUTTON = [
        [
            InlineKeyboardButton("˹ sυᴘᴘσʀᴛ ˼", url="https://t.me/lll_BADNAM_BABY_lll"),
            InlineKeyboardButton("˹ υᴘᴅᴧᴛєs ˼", url="https://t.me/About_badnam_xd"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
    
    SBUTTON = [
        [
            InlineKeyboardButton("ϻᴜѕɪᴄ", callback_data="settings_back_helper"),
            InlineKeyboardButton("ϻᴧηᴧɢєϻєηᴛ", callback_data="TOOL_CP"),
        ],
        [
            InlineKeyboardButton("ᴧʟʟ ʙσᴛ's", callback_data="MAIN_BACK HELP_ABOUT"),
            InlineKeyboardButton("ᴘʀσϻσᴛɪση", callback_data="PROMOTION_CP"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]



