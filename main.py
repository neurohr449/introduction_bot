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

class StateMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data: dict):
        state = data['state']
        current_state = await state.get_state()
        data['current_state'] = current_state
        return await handler(event, data)

@router.message(Command("get_chat_id"))
async def chat_command(message: Message, state: FSMContext):
    chat_id = message.chat.id
    chat_type = message.chat.type
    await message.reply(
        f"🆔 Chat ID: <code>{chat_id}</code>\n"
        f"📌 Тип чата: {chat_type}",
        parse_mode="HTML"
    )


@router.callback_query(StateFilter(UserState.welcome))
async def pd1(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    sheet_range= user_data.get('sheet_range')
    await state.update_data(
        survey_started=datetime.now(),
        survey_completed=False
    )
    # asyncio.create_task(check_survey_completion(callback_query.message.chat.id, state))
    
    try:
            await get_job_data(sheet_id, sheet_range, state)
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
async def pd5(callback_query: CallbackQuery, state: FSMContext):
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
    text = user_data.get('text_1')
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
    promt = f"Ты HR менеджер с опытом более 30 лет в найме, поиске и обучении персонала, с учетом всего своего опыта, чтобы в будущем подобрать кандидата для нашей вакансии: {user_data.get('job_name')}, тебе надо дать оценку ответам на вопросы по стобальной шкале и выдать общий балл по кандидату. Не нужно давать комментарий или писать любые буквы, нужно строго только одно число с общим баллом. (Обязательно без спецсимволов, например точки). Для принятия решения сравни текст вакансии {user_data.get('job_text')}, портрет кандидата {user_data.get('portrait')} и вопросы и ответы пользователя который надо оценить и написать. Вопрос 1: {user_data.get('q1')}, ответ: {user_data.get('ans1')}; Вопрос 2: {user_data.get('q2')}, ответ: {user_data.get('ans2')}; Вопрос 3: {user_data.get('q3')}, ответ: {user_data.get('ans3')}; Вопрос 4: {user_data.get('q4')}, ответ: {user_data.get('ans4')}; Вопрос 5: {user_data.get('q5')}, ответ: {user_data.get('ans5')}; Вопрос 6: {user_data.get('q6')}, ответ: {user_data.get('ans6')}; Вопрос 7:{user_data.get('q7')}, ответ: {user_data.get('ans7')}; Вопрос 8: {user_data.get('q8')}, ответ: {user_data.get('ans8')}; Вопрос 9: {user_data.get('q9')}, ответ: {user_data.get('ans9')}; Вопрос 10:{user_data.get('q10')}, ответ: {user_data.get('ans10')}. Дополнительно если в тексте меньше 10 вопросов, то последний ответ будет для крайнего вопроса"
    promt_2 = f"Ты HR менеджер с опытом более 30 лет в найме, поиске и обучении персонала, с учетом всего своего опыта, чтобы в будущем подобрать идеального кандидата для нашей вакансии: {user_data.get('job_name')}, тебе надо оценить кандидата, сравнить его с вакансией и написать комментарии что ты считаешь по нему. Вот вопросы и ответы пользователя который надо оценить и написать свои комментарии по кандидату строго до 1000 символов: Вопрос 1: {user_data.get('q1')}, ответ: {user_data.get('ans1')}; Вопрос 2: {user_data.get('q2')}, ответ: {user_data.get('ans2')}; Вопрос 3: {user_data.get('q3')}, ответ: {user_data.get('ans3')}; Вопрос 4: {user_data.get('q4')}, ответ: {user_data.get('ans4')}; Вопрос 5: {user_data.get('q5')}, ответ: {user_data.get('ans5')}; Вопрос 6: {user_data.get('q6')}, ответ: {user_data.get('ans6')}; Вопрос 7:{user_data.get('q7')}, ответ: {user_data.get('ans7')}; Вопрос 8: {user_data.get('q8')}, ответ: {user_data.get('ans8')}; Вопрос 9: {user_data.get('q9')}, ответ: {user_data.get('ans9')}; Вопрос 10:{user_data.get('q10')}, ответ: {user_data.get('ans10')} Вот текст вакансии для анализа {user_data.get('job_text')} и портрет кандидата {user_data.get('portrait')}. Дополнительно если в тексте меньше 10 вопросов, то последний ответ будет для крайнего вопроса"
    user_qa = f"Вопрос 1: {user_data.get('q1')}, ответ: {user_data.get('ans1')}; Вопрос 2: {user_data.get('q2')}, ответ: {user_data.get('ans2')}; Вопрос 3: {user_data.get('q3')}, ответ: {user_data.get('ans3')}; Вопрос 4: {user_data.get('q4')}, ответ: {user_data.get('ans4')}; Вопрос 5: {user_data.get('q5')}, ответ: {user_data.get('ans5')}; Вопрос 6: {user_data.get('q6')}, ответ: {user_data.get('ans6')}; Вопрос 7:{user_data.get('q7')}, ответ: {user_data.get('ans7')}; Вопрос 8: {user_data.get('q8')}, ответ: {user_data.get('ans8')}; Вопрос 9: {user_data.get('q9')}, ответ: {user_data.get('ans9')}; Вопрос 10:{user_data.get('q10')}, ответ: {user_data.get('ans10')}"
    response_score = await get_chatgpt_response(promt)
    response_2 = await get_chatgpt_response(promt_2)
    target_score = user_data.get('score')
    if int(response_score) >= int(target_score):
        response = "2.Собеседование"
    else:
        response = "3.Отказ"
    gpt_response = f"Баллы кандидата: {response_score}\n\n AI комментарий: {response_2}"     
    await state.update_data(response=response, 
                            response_2=response_2,
                            user_qa = user_qa,
                            response_score=response_score,
                            gpt_response=gpt_response
                            )
    # await message.answer(f"{response_score}\n\n{response}\n\n {response_2}")
    company_name = user_data.get('company_name')
    job_name = user_data.get('job_name')
        
    if response == "2.Собеседование":
        await state.set_state(UserState.result_yes)
        await write_to_google_sheet(
            sheet_id = sheet_id, 
            username = message.from_user.username,
            first_name=message.from_user.first_name,
            status=response,
            gpt_response=gpt_response,
            qa_data=user_qa,
            company_name = company_name,
            job_name = job_name,
            user_score=response_score
            )
        text_3 = user_data.get('text_3')
        await message.answer(text=text_3)
        await message.answer("Пожалуйста напишите ваше ФИО.")
    
    
    
    elif response == "3.Отказ":
        await state.set_state(UserState.result_no)
        await message.answer(f"{user_data.get('text_4')}") 
        # Записываем в таблицу
        await write_to_google_sheet(
        sheet_id=sheet_id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        status=response,  
        gpt_response=gpt_response,
        qa_data=user_qa,
        company_name = company_name,
        job_name = job_name,
        user_score=response_score
        )


async def main() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.include_router(router)
    dp.message.middleware(StateMiddleware())
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(
        parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())