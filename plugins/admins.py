from asyncio.queues import QueueEmpty
from config import BOT_USERNAME
from config import que
from pyrogram import Client, filters
from pyrogram.types import Message
import sira
import asad
from cache.admins import set
from helpers.decorators import authorized_users_only, errors
from helpers.channelmusic import get_chat_id
from helpers.filters import command, other_filters
from Client import callsmusic
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream


@Client.on_message(command(["pause", "jeda"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    await callsmusic.pytgcalls.pause_stream(message.chat.id)
    await message.reply_photo(
                             photo="https://telegra.ph/file/5017169a6cc138ecd1000.jpg", 
                             caption="**⏸ Mᴜsɪᴄ ᴘᴀᴜsᴇᴅ 🙄.\n ᴜsᴇ /resume ᴛᴏ ᴘʟᴀʏ ᴀɢᴀɪɴ ᴏɴ [ʀᴏᴄᴋs sᴇʀᴠᴇʀ](https://t.me/Shayri_Music_Lovers)**"
    )


@Client.on_message(command(["resume", "lanjut"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    await callsmusic.pytgcalls.resume_stream(message.chat.id)
    await message.reply_photo(
                             photo="https://telegra.ph/file/fc19d98891c4ba91261c1.jpg", 
                             caption="**▶️ Mᴜsɪᴄ ʀᴇsᴜᴍᴇᴅ 😜.\n ᴜsᴇ /pause ᴛᴏ ᴘᴀᴜsᴇ ᴍᴜsɪᴄ ᴏɴ [ʀᴏᴄᴋs sᴇʀᴠᴇʀ](https://t.me/Shayri_Music_Lovers)**"
    )


@Client.on_message(command(["end", "stop"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    try:
        callsmusic.queues.clear(message.chat.id)
    except QueueEmpty:
        pass

    await callsmusic.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_photo(
                             photo="https://telegra.ph/file/20beff13e5a9b9118daf0.jpg", 
                             caption="❌ **Sᴏɴɢ ɪs ᴇɴᴅᴇᴅ 😔\n use /play ᴛᴏ ᴘʟᴀʏ ɴᴇᴡ ᴍᴜsɪᴄ ᴏɴ [ʀᴏᴄᴋs sᴇʀᴠᴇʀ](https://t.me/Shayri_Music_Lovers)**"
    )

@Client.on_message(command(["skip", "second", "next", f"next@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = message.chat.id
    ACTV_CALLS = {}
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("❌ **ɴᴏ ᴍᴜsɪᴄ ᴘʟᴀʏɪɴɢ ᴏɴ [ʀᴏᴄᴋs sᴇʀᴠᴇʀ](https://t.me/Shayri_Music_Lovers)**"**")
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            await callsmusic.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        callsmusic.queues.get(chat_id)["file"],
                    ),
                ),
            )
                
    qeue = que.get(chat_id)
    if qeue:
        qeue.pop(0)
    if not qeue:
        return
    await message.reply_text("⏭ **Yᴏᴜ'ᴠᴇ sᴋɪᴘᴘᴇᴅ ᴛᴏ ᴛʜᴇ ɴᴇxᴛ sᴏɴɢ...😉**")




@Client.on_message(command(["reload", f"reload@{BOT_USERNAME}"]) & other_filters)
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        f"""**━━━━━━━━━━━━━━━━━━━
💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ [ʀᴏᴄᴋs](https://t.me/Shayri_Music_Lovers) ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs.
┏━━━━━━━━━━━━━━━━━┓
┣★ ʙᴏᴛ : [ʀᴇʟᴏᴀᴅᴇᴅ](https://t.me/rocks_music_bot)
┣★ ᴀᴅᴍɪɴ : [ʀᴇғʀᴇsʜᴇᴅ](https://t.me/Shayri_Music_Lovers)
┣★ sᴜᴘᴘᴏʀᴛ : [ʙᴏᴛ ᴜᴘᴅᴀᴛᴇs](https://t.me/AsadSupport)
┗━━━━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ » ǫᴜᴇsᴛɪᴏɴ
ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](https://t.me/Dr_Asad_Ali).
━━━━━━━━━━━━━━━━━━━**""",
    )
