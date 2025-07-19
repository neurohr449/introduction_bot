import asyncio
import logging
import sys
import os
import json
from datetime import datetime, timedelta
import aiohttp
from aiogram import Bot, Dispatcher, html, Router, BaseMiddleware
from aiogram import F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.filters.state import StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.filters.command import CommandObject
import shelve
import gspread
import re

from google.oauth2.service_account import Credentials
from openai import AsyncOpenAI
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from functions import *
# from database import *


BOT_TOKEN = os.getenv("BOT_TOKEN")
FAIL_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Попробовать снова", callback_data="retry")]
            ])
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MOSCOW_TZ = ZoneInfo("Europe/Moscow")
SERVER_TZ = ZoneInfo("UTC")
TELEGRAM_VIDEO_PATTERN = r'https://t\.me/'


bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(
    parse_mode=ParseMode.HTML))
storage = MemoryStorage()
router = Router()
dp = Dispatcher(storage=storage)

class UserState(StatesGroup):
    welcome = State()
    block = State()
    module = State()
    pd1 = State()
    pd2 = State()
    pd3 = State()
    pd4 = State()
    pd5 = State()
    pd6 = State()
    pd7 = State()
    pd8 = State()
    pd9 = State()
    pd10 = State()
    pd11 = State()
    pd12 = State()
    pd13 = State()
    pd14 = State()
    pd15 = State()
    pd16 = State()
    pd17 = State()
    pd18 = State()
    pd19 = State()
    pd20 = State()
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()
    q6 = State()
    q7 = State()
    q8 = State()
    q9 = State()
    q10 = State()
    result_no = State()
    result_yes = State()
    user_name = State()
    user_phone = State()
    user_resume = State()
    slot_day = State()
    slot_time = State()
    process_time_change = State()



@router.message(Command("get_chat_id"))
async def chat_command(message: Message, state: FSMContext):
    chat_id = message.chat.id
    chat_type = message.chat.type
    await message.reply(
        f"🆔 Chat ID: <code>{chat_id}</code>\n"
        f"📌 Тип чата: {chat_type}",
        parse_mode="HTML"
    )

@router.callback_query(lambda c: c.data == 'notification')
async def notification_cb_handler(callback_query: CallbackQuery, state: FSMContext) -> None:
    current_state = await state.get_state()

    if current_state == UserState.pd1.state:
         await pd1(callback_query, state)
    elif current_state == UserState.pd2.state:
         await pd2(callback_query, state)
    elif current_state == UserState.pd3.state:
         await pd3(callback_query, state)
    elif current_state == UserState.pd4.state:
         await pd4(callback_query, state)
    elif current_state == UserState.pd5.state:
         await pd5(callback_query, state)
    elif current_state == UserState.pd6.state:
         await pd6(callback_query, state)
    elif current_state == UserState.pd7.state:
         await pd7(callback_query.message, state)
    elif current_state == UserState.pd8.state:
         await pd8(callback_query.message, state)
    elif current_state == UserState.pd9.state:
         await pd9(callback_query.message, state)
    elif current_state == UserState.pd10.state:
         await pd10(callback_query.message, state)
    elif current_state == UserState.pd11.state:
         await pd11(callback_query.message, state)
    elif current_state == UserState.pd12.state:
         await pd12(callback_query.message, state)
    elif current_state == UserState.pd13.state:
         await pd13(callback_query.message, state)
    elif current_state == UserState.pd14.state:
         await pd14(callback_query.message, state)
    elif current_state == UserState.pd15.state:
         await pd15(callback_query.message, state)
    elif current_state == UserState.pd16.state:
        await pd16(callback_query, state)
    elif current_state == UserState.pd17.state:
         await pd17(callback_query, state)
    elif current_state == UserState.pd18.state:
         await pd18(callback_query, state)
    elif current_state == UserState.pd19.state:
         await pd19(callback_query, state)
    elif current_state == UserState.pd20.state:
         await pd20(callback_query, state)
    elif current_state == UserState.q1.state:
         await q1(callback_query, state)
    elif current_state == UserState.q2.state:
         await q2(callback_query.message, state)
    elif current_state == UserState.q3.state:
         await q3(callback_query.message, state)
    elif current_state == UserState.q4.state:
         await q4(callback_query.message, state)
    elif current_state == UserState.q5.state:
         await q5(callback_query.message, state)
    elif current_state == UserState.q6.state:
         await q6(callback_query.message, state)
    elif current_state == UserState.q7.state:
         await q7(callback_query.message, state)
    elif current_state == UserState.q8.state:
         await q8(callback_query.message, state)
    elif current_state == UserState.q9.state:
         await q9(callback_query.message, state)
    elif current_state == UserState.q10.state:
         await q10(callback_query.message, state)

@router.message(CommandStart())
async def command_start_handler(message: Message, command: CommandObject, state: FSMContext) -> None:
    await state.set_state(UserState.welcome)
    args = command.args
    if args:
        parts = args.rsplit('_', 1)
        if len(parts) > 1 and parts[1].isdigit():  
            sheet_id = parts[0]  
            sheet_range = parts[1]  
            only_sheet = 0
        else:  
            sheet_id = args  
            sheet_range = 2
            only_sheet = 1
        
        print(f"sheetid {sheet_id}", "sheet_range",sheet_range)
    else:
        await message.answer("👋 Здравствуйте. Запустите бота по уникальной ссылке!")
        

    if sheet_id:
        try:
            await state.update_data(sheet_id=sheet_id,
                                    sheet_range=sheet_range)
            await get_table_data(sheet_id, sheet_range, state)
            user_data = await state.get_data()
            if only_sheet == 1:
                match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_block'))
                if match:           
                    await message.answer_video(video=user_data.get('video_block'))
                    await message.answer(text=f"{user_data.get('welcome')}")  
                else:                    
                    await message.answer(f"{user_data.get('welcome')}")
            else:
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                        [InlineKeyboardButton(text="Продолжить", callback_data="next")]
                        ])
                await message.answer(text = f"Нажмите на кнопку чтобы изучить модуль \"{user_data.get('module')}\"", reply_markup = keyboard)
                
        except Exception as e:
            await message.answer(f"❌ Ошибка при загрузке данных: {str(e)}", reply_markup = FAIL_KEYBOARD)
    else:
        await message.answer("👋 Здравствуйте. Запустите бота по уникальной ссылке!")

@router.message(F.text.startswith("/select_"))
async def handle_command(message: Message, state: FSMContext):
    
    user_send = message.text

    
    parts = user_send.rsplit('_')
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')

    if len(parts) > 2:  
        block_id = parts[1]
        module_id = parts[2]
        
        sheet_range = await get_module_range(sheet_id, block_id, module_id)
        sheet_range = sheet_range + 1
        
        if sheet_range is None:
            await message.answer("Модуль не найден")
        else:

            await get_table_data(sheet_id, sheet_range, state)
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
                            ])
            await message.answer(text = f"Нажмите на кнопку чтобы изучить модуль \"{user_data.get('module')}\"", reply_markup = keyboard)
            
    else:  
        block_id = parts[1]
        text, video = await get_block_text(sheet_id, block_id)
        if video: 
            await message.answer_video(video)
        await message.answer(text=text)
        


@router.callback_query(StateFilter(UserState.welcome))
async def pd1(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    await state.update_data(
        survey_started=datetime.now(),
        survey_completed=False
    )
    asyncio.create_task(check_survey_completion(callback_query.message.chat.id, state))
    
    try:
            
            user = callback_query.from_user
            username = user.username
            first_name = user.first_name
            company_name = user_data.get('company_name')
            job_name = user_data.get('job_name')
            user_check = await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                first_name = first_name,
                                company_name = company_name,
                                job_name = job_name
                         )
            if user_check != False:
                
                user_data = await state.get_data()
                text = user_data.get('pd1')
                if text:
                    match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_1'))
                    if match:           
                        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                        [InlineKeyboardButton(text="Продолжить", callback_data="next")]
                        ])
                        await callback_query.message.answer_video(video=user_data.get('video_1'))
                        await callback_query.message.answer(text=f"{user_data.get('pd1')}", reply_markup = keyboard)
                        await state.set_state(UserState.pd1)
                        await callback_query.answer()
                    else:                    
                        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                        [InlineKeyboardButton(text="Продолжить", callback_data="next")]
                        ])
                        await callback_query.message.answer(f"{user_data.get('pd1')}", reply_markup = keyboard)
                        await state.set_state(UserState.pd1)
                        await callback_query.answer()
                else:
                    await state.set_state(UserState.pd5)
                    await q1(callback_query, state)     
            else:
                 await callback_query.message.answer("Вы уже получили отказ")
    except Exception as e:
            await callback_query.message.answer(f"❌ Ошибка при загрузке данных: {str(e)}", reply_markup = FAIL_KEYBOARD)



@router.callback_query(StateFilter(UserState.pd1))
async def pd2(callback_query: CallbackQuery, state: FSMContext):
    
    user_data = await state.get_data()
    text = user_data.get('pd2')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_2'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_2'))
            await callback_query.message.answer(text=f"{user_data.get('pd2')}", reply_markup = keyboard)
            await state.set_state(UserState.pd2)
            await callback_query.answer()
        else:
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd2')}", reply_markup = keyboard)
            await state.set_state(UserState.pd2)
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd5)
         await q1(callback_query, state)



@router.callback_query(StateFilter(UserState.pd2))
async def pd3(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('pd3')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_3'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_3'))
            await callback_query.message.answer(text=f"{user_data.get('pd3')}", reply_markup = keyboard)
            await state.set_state(UserState.pd3)
            await callback_query.answer()
        else: 
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd3')}", reply_markup = keyboard)
            await state.set_state(UserState.pd3)
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd5)
         await q1(callback_query, state)



@router.callback_query(StateFilter(UserState.pd3))
async def pd4(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('pd4')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_4'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_4'))
            await callback_query.message.answer(text=f"{user_data.get('pd4')}", reply_markup = keyboard)
            await state.set_state(UserState.pd4)
            await callback_query.answer()
        else:
        
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd4')}", reply_markup = keyboard)
            await state.set_state(UserState.pd4)
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd5)
         await q1(callback_query, state)
    


@router.callback_query(StateFilter(UserState.pd4))
async def pd5(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('pd5')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_5'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_5'))
            await callback_query.message.answer(text=f"{user_data.get('pd5')}", reply_markup = keyboard)
            await state.set_state(UserState.pd5)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd5')}", reply_markup = keyboard)
            await state.set_state(UserState.pd5)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd5)
         await q1(callback_query, state)

@router.callback_query(StateFilter(UserState.pd5))
async def pd6(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('pd6')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_6'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_6'))
            await callback_query.message.answer(text=f"{user_data.get('pd6')}", reply_markup = keyboard)
            await state.set_state(UserState.pd6)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd6')}", reply_markup = keyboard)
            await state.set_state(UserState.pd6)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd6)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd6))
async def pd7(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('pd7')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_7'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_7'))
            await callback_query.message.answer(text=f"{user_data.get('pd7')}", reply_markup = keyboard)
            await state.set_state(UserState.pd7)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd7')}", reply_markup = keyboard)
            await state.set_state(UserState.pd7)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd7)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd7))
async def pd8(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('pd8')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_8'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_8'))
            await callback_query.message.answer(text=f"{user_data.get('pd8')}", reply_markup = keyboard)
            await state.set_state(UserState.pd8)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd8')}", reply_markup = keyboard)
            await state.set_state(UserState.pd8)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd8)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd8))
async def pd9(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('pd9')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_9'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_9'))
            await callback_query.message.answer(text=f"{user_data.get('pd9')}", reply_markup = keyboard)
            await state.set_state(UserState.pd9)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd9')}", reply_markup = keyboard)
            await state.set_state(UserState.pd9)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd9)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd9))
async def pd10(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('pd10')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_10'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_10'))
            await callback_query.message.answer(text=f"{user_data.get('pd10')}", reply_markup = keyboard)
            await state.set_state(UserState.pd10)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd10')}", reply_markup = keyboard)
            await state.set_state(UserState.pd10)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd10)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd10))
async def pd11(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('pd11')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_11'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_11'))
            await callback_query.message.answer(text=f"{user_data.get('pd11')}", reply_markup = keyboard)
            await state.set_state(UserState.pd11)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd11')}", reply_markup = keyboard)
            await state.set_state(UserState.pd11)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd11)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd11))
async def pd12(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('pd12')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_12'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_12'))
            await callback_query.message.answer(text=f"{user_data.get('pd12')}", reply_markup = keyboard)
            await state.set_state(UserState.pd12)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd12')}", reply_markup = keyboard)
            await state.set_state(UserState.pd12)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd12)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd12))
async def pd13(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('pd13')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_13'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_13'))
            await callback_query.message.answer(text=f"{user_data.get('pd13')}", reply_markup = keyboard)
            await state.set_state(UserState.pd13)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd13')}", reply_markup = keyboard)
            await state.set_state(UserState.pd13)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd13)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd13))
async def pd14(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('pd14')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_14'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_14'))
            await callback_query.message.answer(text=f"{user_data.get('pd14')}", reply_markup = keyboard)
            await state.set_state(UserState.pd14)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd14')}", reply_markup = keyboard)
            await state.set_state(UserState.pd14)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd14)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd14))
async def pd15(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('pd15')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_15'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_15'))
            await callback_query.message.answer(text=f"{user_data.get('pd15')}", reply_markup = keyboard)
            await state.set_state(UserState.pd15)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd15')}", reply_markup = keyboard)
            await state.set_state(UserState.pd15)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd15)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd15))
async def pd16(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('pd16')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_16'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_16'))
            await callback_query.message.answer(text=f"{user_data.get('pd16')}", reply_markup = keyboard)
            await state.set_state(UserState.pd16)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd16')}", reply_markup = keyboard)
            await state.set_state(UserState.pd16)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd16)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd16))
async def pd17(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('pd17')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_17'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_17'))
            await callback_query.message.answer(text=f"{user_data.get('pd17')}", reply_markup = keyboard)
            await state.set_state(UserState.pd17)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd17')}", reply_markup = keyboard)
            await state.set_state(UserState.pd17)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd17)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd17))
async def pd18(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('pd18')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_18'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_18'))
            await callback_query.message.answer(text=f"{user_data.get('pd18')}", reply_markup = keyboard)
            await state.set_state(UserState.pd18)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd18')}", reply_markup = keyboard)
            await state.set_state(UserState.pd18)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd18)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd18))
async def pd19(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('pd19')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_19'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_19'))
            await callback_query.message.answer(text=f"{user_data.get('pd19')}", reply_markup = keyboard)
            await state.set_state(UserState.pd19)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd19')}", reply_markup = keyboard)
            await state.set_state(UserState.pd19)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd19)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd19))
async def pd20(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('pd20')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_20'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_20'))
            await callback_query.message.answer(text=f"{user_data.get('pd20')}", reply_markup = keyboard)
            await state.set_state(UserState.pd20)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd20')}", reply_markup = keyboard)
            await state.set_state(UserState.pd20)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd20)
         await q1(callback_query, state)





@router.callback_query(StateFilter(UserState.pd20))
async def q1(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('text_1')
    text_2 = user_data.get('q1')
    if text and text_2:
        await callback_query.message.answer(f"{text}")
        await callback_query.answer()
        await callback_query.message.answer(f"{user_data.get('q1')}")
        await state.set_state(UserState.q1)
    else:
        await state.update_data(survey_completed = True)
        await state.set_state(UserState.result_yes)
        await bot.send_message(chat_id=callback_query.message.chat.id, text="Пожалуйста напишите ваше ФИО.")


@router.message(StateFilter(UserState.q1))
async def q2(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans1=ans1)
    user_data = await state.get_data()
    text = user_data.get('q2')
    if text:
        await message.answer(f"{user_data.get('q2')}")
        await state.set_state(UserState.q2)
    else:
        await state.set_state(UserState.q10)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q2))
async def q3(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans2=ans1)
    user_data = await state.get_data()
    text = user_data.get('q3')
    if text:
        await message.answer(f"{user_data.get('q3')}")
        await state.set_state(UserState.q3)
    else:
        await state.set_state(UserState.q10)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q3))
async def q4(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans3=ans1)
    user_data = await state.get_data()
    text = user_data.get('q4')
    if text:
        await message.answer(f"{user_data.get('q4')}")
        await state.set_state(UserState.q4)
    else:
        await state.set_state(UserState.q10)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q4))
async def q5(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans4=ans1)
    user_data = await state.get_data()
    text = user_data.get('q5')
    if text:
        await message.answer(f"{user_data.get('q5')}")
        await state.set_state(UserState.q5)
    else:
        await state.set_state(UserState.q10)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q5))
async def q6(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans5=ans1)
    user_data = await state.get_data()
    text = user_data.get('q6')
    if text:
        await message.answer(f"{user_data.get('q6')}")
        await state.set_state(UserState.q6)
    else:
        await state.set_state(UserState.q10)
        await process_answers(message, state)    

@router.message(StateFilter(UserState.q6))
async def q7(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans6=ans1)
    user_data = await state.get_data()
    text = user_data.get('q7')
    if text:
        await message.answer(f"{user_data.get('q7')}")
        await state.set_state(UserState.q7)
    else:
        await state.set_state(UserState.q10)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q7))
async def q8(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans7=ans1)
    user_data = await state.get_data()
    text = user_data.get('q8')
    if text:
        await message.answer(f"{user_data.get('q8')}")
        await state.set_state(UserState.q8)
    else:
        await state.set_state(UserState.q10)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q8))
async def q9(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans8=ans1)
    user_data = await state.get_data()
    text = user_data.get('q9')
    if text:
        await message.answer(f"{user_data.get('q9')}")
        await state.set_state(UserState.q9)
    else:
        await state.set_state(UserState.q10)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q9))
async def q10(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans9=ans1)
    user_data = await state.get_data()
    text = user_data.get('q10')
    if text:
        await message.answer(f"{user_data.get('q10')}")
        await state.set_state(UserState.q10)
    else:
        await state.set_state(UserState.q10)
        await process_answers(message, state)


@router.message(StateFilter(UserState.q10))
async def process_answers(message: Message, state: FSMContext):
    user_data = await state.get_data()
    text = user_data.get('closing_text')
    if message.video:
        video=message.video.file_id
        await state.update_data(video=video)
        ans10 = "Видео от кандидата получено"
    elif message.video_note:
        video_note = message.video_note.file_id
        await state.update_data(video_note=video_note)
        ans10 = "Видео от кандидата получено"
    elif message.audio:
        audio = message.audio.file_id
        await state.update_data(audio = audio)
        ans10 = "Аудио от кандидата получено"
    elif message.voice:
        voice = message.voice.file_id
        await state.update_data(voice = voice)
        ans10 = "Аудио от кандидата получено"
    elif message.text:  
        ans10 = message.text
    else:
        ans10 = "Неизвестный формат сообщения"
    await state.update_data(ans10=ans10)
    user_data = await state.get_data()
    text = user_data.get('text_2')
    await message.answer(f"{text}")
    await state.update_data(survey_completed = True)
    
    sheet_id = user_data.get('sheet_id')
    user_qa = f"Вопрос 1: {user_data.get('q1')}, \nОтвет 1: {user_data.get('ans1')}; \nВопрос 2: {user_data.get('q2')}, \nОтвет 2: {user_data.get('ans2')}; \nВопрос 3: {user_data.get('q3')}, \nОтвет 3: {user_data.get('ans3')}; \nВопрос 4: {user_data.get('q4')}, \nОтвет 4: {user_data.get('ans4')}; \nВопрос 5: {user_data.get('q5')}, \nОтвет 5: {user_data.get('ans5')}; \nВопрос 6: {user_data.get('q6')}, \nОтвет 6: {user_data.get('ans6')}; \nВопрос 7:{user_data.get('q7')}, \nОтвет 7: {user_data.get('ans7')}; \nВопрос 8: {user_data.get('q8')}, \nОтвет 8: {user_data.get('ans8')}; \nВопрос 9: {user_data.get('q9')}, \nОтвет 9: {user_data.get('ans9')}; \nВопрос 10:{user_data.get('q10')}, \nОтвет 10: {user_data.get('ans10')}"
    
    promt = user_data.get('promt')
    promt_2 = user_data.get('promt_2')
    response_score = await get_chatgpt_response(promt)
    ai_comment = await get_chatgpt_response(promt_2)
    target_score = user_data.get('target_score')
    if int(response_score) >= int(target_score):
        response = "Тестирование пройдено"
    else:
        response = "Тестирование не пройдено"
    gpt_response = f"Баллы кандидата: {response_score}"     
    await state.update_data(response=response,
                            user_qa = user_qa,
                            response_score=response_score,
                            gpt_response=gpt_response
                            )
 
        
    if response == "2.Собеседование":
        await state.set_state(UserState.result_yes)
        await write_to_google_sheet(
            sheet_id = sheet_id, 
            username = message.from_user.username,
            first_name=message.from_user.first_name,
            status=response,
            gpt_response=gpt_response,
            qa_data=user_qa,
            user_score=response_score
            )
        text_3 = user_data.get('result_yes')
        await message.answer(text=text_3)
        await message.answer("Пожалуйста напишите ваше ФИО.")
    
    
    
    elif response == "3.Отказ":
        await state.set_state(UserState.result_no)
        await message.answer(f"{user_data.get('result_no')}") 
        
        await write_to_google_sheet(
        sheet_id=sheet_id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        status=response,  
        gpt_response=gpt_response,
        qa_data=user_qa,
        user_score=response_score
        )


@router.message(StateFilter(UserState.result_yes))
async def process_name(message: Message, state: FSMContext):
        user_fio = message.text
        await state.update_data(user_fio=user_fio)
        await state.set_state(UserState.user_phone)
        await message.answer("Напишите ваш телефон для связи.")       

@router.message(StateFilter(UserState.user_phone))
async def process_phone(message: Message, state: FSMContext):
        user_phone = message.text
        await state.update_data(user_phone=user_phone)
        await state.set_state(UserState.slot_day)
         
        
        user_data = await state.get_data()
        sheet_id = user_data.get('sheet_id')
        
        
        keyboard = await check_empty_cells(sheet_id)
        
        if keyboard:
                await message.answer(
                "Выберите дату для записи",
                reply_markup=keyboard
                )
                
                
        else:
                await message.answer("Нет доступного времени")



@router.callback_query(lambda c: c.data.startswith("select_date_"), UserState.slot_day)
async def process_date_selection(callback: CallbackQuery, state: FSMContext):
    # Получаем выбранную ячейку даты (например "B2")
    selected_date_cell = callback.data.split("_")[2]  # "select_date_B2" → "B2"
    
    # Получаем sheet_id из состояния
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    
    # Получаем клавиатуру с доступным временем
    keyboard = await get_available_times(sheet_id, selected_date_cell)
    
    if keyboard:
        await callback.message.edit_text(
            "Доступное время для записи:",
            reply_markup=keyboard
        )
        await state.set_state(UserState.slot_time)
    else:
        await callback.answer("К сожалению, на этот день нет свободного времени.")
    
    await callback.answer()



@router.callback_query(lambda c: c.data.startswith("select_time_"), UserState.slot_time)
async def process_time_selection(callback: CallbackQuery, state: FSMContext):
    try:
        
        parts = callback.data.split("_")
        column_letter = parts[2].upper()  # Буква столбца (B, C, ...)
        row_number = parts[3]             # Номер строки
        
        
        user_data = await state.get_data()
        sheet_id = user_data.get('sheet_id')
        
        if not sheet_id:
            await callback.answer("❌ ID таблицы не найден", show_alert=True)
            return

        
        sheet = await get_google_sheet(sheet_id, 0)
        
        target_cell = f"{column_letter}{row_number}"
        await state.update_data(target_cell = target_cell)

        #Проверяем ячейку (асинхронно через run_in_executor)
        cell_value = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: sheet.acell(target_cell).value
        )
        
        #Проверка на занятость ячейки
        if cell_value and cell_value.strip() and cell_value.lower() != 'none':
            await callback.answer(
                f"⏳ Время занято: {cell_value}",
                show_alert=True
            )
            return
        
        #Получаем время для отображения пользователю
        time_value = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: sheet.acell(f'A{row_number}').value
        )
        date_value = await asyncio.get_event_loop().run_in_executor(
             None,
            lambda: sheet.acell(f'{column_letter}3').value
        )
        
        

        #Подготовка данных для записи
        record_text = (
            f"{date_value} {time_value} #{user_data.get('response')}\n\n"
            f"Компания: {user_data.get('company_name')}\n"
            f"Вакансия: {user_data.get('job_name')}\n\n"
            f"ФИО: {user_data.get('user_fio', 'Без имени')}\n"
            f"ТГ: @{callback.from_user.username}\n"
            f"Ссылка на переписку: https://t.me/{callback.from_user.username}\n"
            f"Номер: {user_data.get('user_phone', 'Без телефона')}\n"
            f"Резюме: {user_data.get('user_resume')}\n"
            f"Cылка на таблицу: https://docs.google.com/spreadsheets/d/{user_data.get('sheet_id')}\n\n"
            f"Баллы кандидата: {user_data.get('response_score')}\n\n"
            f"AI комментарий: {user_data.get('response_2')}"
            
        )
        
        await state.update_data(time_value=time_value, 
                            date_value=date_value
                            )
        
        #Запись в таблицу
        await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: sheet.update(
                range_name=target_cell,
                values=[[record_text]],
                value_input_option='USER_ENTERED'
            )
        )
        
        
        keyboard =  InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Изменить время", callback_data="change_time")],
                [InlineKeyboardButton(text="Удалить запись", callback_data="delete_time")]
                ])
        user_data = await state.get_data()
        #Отправляем подтверждение пользователю
        await callback.message.edit_text(
            f"Ждем Вас в {date_value} в {time_value} на собеседование\n\n"
            f"{user_data.get('text_5')}", reply_markup=keyboard
        )

        
        chat_id = user_data.get('chat_id')
        sheet_range = user_data.get('sheet_range')
        await state.set_state(UserState.process_time_change)
        decline_text=user_data.get('decline_text')
        learn_text=user_data.get('learn_text')
        practice_text=user_data.get('practice_text')
        accept_text=user_data.get('accept_text')
        candidate_chat_id = callback.message.chat.id
        
        action_keyboard = await get_action_keyboard(
                                                pool=pool,
                                                column_letter=column_letter,
                                                row_number=row_number,
                                                candidate_chat_id=str(candidate_chat_id),
                                                sheet_id=sheet_id,
                                                sheet_range=sheet_range,
                                                decline_text=decline_text,
                                                learn_text=learn_text,
                                                practice_text=practice_text,
                                                accept_text=accept_text
                                            )
        await bot.send_message(chat_id=chat_id,
                                text=f"{record_text}",
                                reply_markup=action_keyboard,
                                disable_web_page_preview=True
                                )
        video = user_data.get('video')
        if video:
            await bot.send_video(chat_id=chat_id,
                                video=video,
                                caption="Видео от кандидата"
                                )
        
        video_note = user_data.get('video_note')
        if video_note:
            await bot.send_video_note(chat_id=chat_id,
                                video_note=video_note
                                )
        audio = user_data.get('audio')
        if audio:
             await bot.send_audio(chat_id = chat_id,
                                  audio = audio)
        voice = user_data.get('voice')
        if voice:
            await bot.send_voice(chat_id = chat_id,
                                 voice = voice)
            
        # 10. Сохраняем данные в Google Sheets (асинхронно)
        success = await write_to_google_sheet(
            sheet_id=sheet_id,
            username=callback.from_user.username,
            first_name=callback.from_user.first_name,
            status="2.Собеседование",
            gpt_response=user_data.get('gpt_response', ''),
            full_name=user_data.get('user_fio'),
            phone_number=user_data.get('user_phone'),
            resume_link=user_data.get('user_resume'),
            interview_date=date_value,
            interview_time=time_value,
            qa_data=user_data.get('user_qa'),
            job_name=user_data.get('job_name'),
            company_name=user_data.get('company_name'),
            user_score=user_data.get('response_score')
        )
        
        user_data = await state.get_data()
        interview_time = parse_interview_datetime(date_value, time_value)
        interview_time_utc = interview_time.astimezone(SERVER_TZ)
        task1 = asyncio.create_task(send_reminder_at_time(callback.message.chat.id, interview_time_utc - timedelta(hours=1), f"{user_data.get('notification_hour')}"))
        task2 = asyncio.create_task(send_reminder_at_time(callback.message.chat.id, interview_time_utc, f"{user_data.get('notification_now')}"))
        
        await state.update_data(
        date_value=date_value,
        time_value=time_value,
        reminder_tasks=[id(task1), id(task2)]  
        )
        if not success:
            await callback.message.answer("⚠️ Ошибка сохранения данных в таблицу")
        
        
        
    except Exception as e:
        logging.error(f"Ошибка записи: {str(e)}", exc_info=True)
        await callback.answer("⚠️ Ошибка сервера, попробуйте позже", show_alert=True)


@router.callback_query(StateFilter(UserState.process_time_change))
async def time_change(callback_query: CallbackQuery, state: FSMContext):
    if callback_query.data == "change_time":
        user_data = await state.get_data()
        sheet_id = user_data.get('sheet_id')
        target_cell = user_data.get('target_cell')
        await clear_cell(sheet_id, target_cell)
        await state.set_state(UserState.slot_day)
         
        # Получаем sheet_id из состояния или базы данных
        user_data = await state.get_data()
        sheet_id = user_data.get('sheet_id')
        
        # Получаем клавиатуру с кнопками
        keyboard = await check_empty_cells(sheet_id)
        
        if keyboard:
                await callback_query.message.answer(
                "Выберите дату для записи",
                reply_markup=keyboard
                )
                
        else:
                await callback_query.message.answer("Нет доступного времени")

        await callback_query.answer()

    elif callback_query.data == "delete_time":
        user_data = await state.get_data()
        sheet_id = user_data.get('sheet_id')
        target_cell = user_data.get('target_cell')
        
        await  clear_cell(sheet_id, target_cell)
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Новая запись", callback_data="change_time")]
        ])

        await callback_query.message.answer("Запись успешно удалена!", reply_markup = keyboard)

        await callback_query.answer()
    

##########################################################################################################################################################################################################
async def check_survey_completion(chat_id: int, state: FSMContext):
    await asyncio.sleep(3600)  
    
    data = await state.get_data()
    if not data.get("survey_completed", False):
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Продолжить", callback_data="notification")]
        ])
        await bot.send_message(chat_id, f"{data.get('notification_pd')}",reply_markup=keyboard)


async def send_reminder(chat_id: int, text: str):
    await bot.send_message(chat_id, text)


async def send_reminder_at_time(chat_id: int, time_utc: datetime, text: str):
    delay = (time_utc - datetime.now(SERVER_TZ)).total_seconds()
    if delay > 0:
        await asyncio.sleep(delay)
        await send_reminder(chat_id, text)


async def cancel_old_reminders(state: FSMContext):
    data = await state.get_data()
    if "reminder_tasks" in data:
        for task_id in data["reminder_tasks"]:
            task = asyncio.all_tasks().get(task_id)
            if task and not task.done():
                task.cancel()

##########################################################################################################################################################################################################
##########################################################################################################################################################################################################
##########################################################################################################################################################################################################
class StateMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data: dict):
        state = data['state']
        current_state = await state.get_state()
        data['current_state'] = current_state
        return await handler(event, data)


async def main() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.include_router(router)
    dp.message.middleware(StateMiddleware())
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(
        parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())