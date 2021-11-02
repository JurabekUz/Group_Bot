from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("set_photo","Rasm o'zgartirish"),
            types.BotCommand("set_title", "Gr nomini o'zgartirish"),
            types.BotCommand("set_description","xabar qadash"),
            types.BotCommand("ro","only-read"),
            types.BotCommand("unro", "no-only-read"),
            types.BotCommand("ban","guruhdan haydash"),
            types.BotCommand("unban","unban qilish"),
        ]
    )
