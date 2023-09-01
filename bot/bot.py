import os
from dotenv import load_dotenv
from aiogram import Bot,Dispatcher
from aiogram.types import Message
from aiogram.utils import executor
import requests
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
load_dotenv()

TOKEN= os.environ.get("TOKEN")

bot =Bot(token=TOKEN)
dp=Dispatcher(bot,storage=MemoryStorage())
req_ip="http://192.168.31.212:8001/"


keyboard_unsub = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_unsub.add("Отписаться")
keyboard_unsub.add("Рассылка")
keyboard_unsub.add("Отключить рассылку")
keyboard_unsub.add("Включить рассылку")



keyboard_sub= ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_sub.add(KeyboardButton(text="Зарегистрироваться",request_contact=True))
keyboard_sub.add("Подписаться")
keyboard_sub.add("Рассылка")
keyboard_sub.add("Отключить рассылку")
keyboard_sub.add("Включить рассылку")



class Newsletter(StatesGroup):
    state1=State()



@dp.message_handler(commands="start")
async def start_command(message:Message):

    await message.answer("Привет",reply_markup=keyboard_sub)




@dp.message_handler(lambda message: message.text=="Подписаться")
async def keyboard(message:Message):

    user_id=message.from_user.id
    data={
        "user_id": user_id,
        "is_active": True

         }
    check_user=requests.get(f"{req_ip}/telegram/telegramuser/?user_id={user_id}").json()
    check_sub=requests.get(f"{req_ip}/telegram/user/?user__user_id={user_id}").json()

    if not check_user:
        return await message.answer("Тебя нет в базе нажми на /start чтобы зарегистрироваться")

    if check_sub:
        return await message.answer("Ты есть в подписках",reply_markup=keyboard_unsub)
    
    req=requests.post(f"{req_ip}/telegram/user/",data=data)
    if req.status_code ==201:
        await message.answer("Привет ты успешно подписался",reply_markup=keyboard_unsub)
    else:
        await message.answer("error")




@dp.message_handler(lambda message: message.text=="Отписаться")
async def keyboard(message:Message):

    user_id=message.from_user.id

    check_user=requests.get(f"{req_ip}/telegram/user/?user__user_id={user_id}").json()
    if not check_user:
        return await message.answer("Ты и так не подписался")
    
    delete_id=check_user[0]["id"]
    delete_sub=requests.delete(f"{req_ip}/telegram/user/{delete_id}/")
    if delete_sub.status_code==204:
        await message.answer("Ты успешно отписался",reply_markup=keyboard_sub)
    else:
        await message.answer("Что то пошло не так")
    



@dp.message_handler(lambda message: message.text=="Рассылка")
async def keyboard(message:Message):
    
    await Newsletter.state1.set()
    await message.answer("Введите тект рассылки")




@dp.message_handler(state=Newsletter.state1)
async def letter(message:Message,state:FSMContext):

    if message.from_user.id == 6619761521:
        async with state.proxy()as data:
            text=data["state1"]=message.text
        check_user=requests.get(f"{req_ip}/telegram/user_true/").json()
        successfully=0
        fail=0
        for check in check_user:
            try:
                await bot.send_message(check["user_id"], text=text)
                successfully+=1
            except Exception:
                fail+=1
                continue
        await message.answer(f'Данные о рассылки\nТекст: {text}\n✅Успешно: {successfully}\n❌Ошибки: {fail}\nРассылка завершенна🔔',reply_markup=keyboard_unsub)
        await state.finish()
    
    else:
        await message.answer("Ты не можешь делать рассылки")





@dp.message_handler(lambda message: message.text=="Отключить рассылку")
async def keyboard(message:Message):

    user_id=message.from_user.id

    check_user=requests.get(f"{req_ip}/telegram/user/?user__user_id={user_id}").json()
    if not check_user:
        return await message.answer("Ты и так не подписался")
    id_sub=check_user[0]["id"]
    patch_sub=requests.patch(f"{req_ip}/telegram/user/{id_sub}/",data={"is_active": False})
    if patch_sub.status_code ==200:
        await message.answer("Вы отключили рассылку")
    else:
        await message.answer("Что то пошло не так")



@dp.message_handler(lambda message: message.text=="Включить рассылку")
async def keyboard(message:Message):

    user_id=message.from_user.id

    check_user=requests.get(f"{req_ip}/telegram/user/?user__user_id={user_id}").json()
    if not check_user:
        return await message.answer("Тебя нет в подписках")
    id_sub=check_user[0]["id"]
    patch_sub=requests.patch(f"{req_ip}/telegram/user/{id_sub}/",data={"is_active": True})
    if patch_sub.status_code ==200:
        await message.answer("Вы включили рассылку")
    else:
        await message.answer("Что то пошло не так")



@dp.message_handler(content_types=types.ContentType.CONTACT)
async def process_contact(message: Message):
    contact=message.contact.phone_number

    user_id=message.from_user.id
    data={
        "nickname": message.from_user.first_name,
        "user_id":user_id,
        "phone": contact
         }
    
    
    check_user=requests.get(f"{req_ip}/telegram/telegramuser/?user_id={user_id}").json()
    if check_user:
        return await message.answer("Привет ты есть в базе",reply_markup=keyboard_sub)
    
    req=requests.post(f"{req_ip}/telegram/telegramuser/",data=data)
    if req.status_code ==201:
        await message.answer("Привет ты успешно зарегистрирован",reply_markup=keyboard_sub)
    else:
        await message.answer("error")
    


if __name__=="__main__":  
    executor.start_polling(dp,skip_updates=True)




    
        

