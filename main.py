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
    gpt_1 = State()
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
    pd21 = State()
    pd22 = State()
    pd23 = State()
    pd24 = State()
    pd25 = State()
    pd26 = State()
    pd27 = State()
    pd28 = State()
    pd29 = State()
    pd30 = State()
    pd31 = State()
    pd32 = State()
    pd33 = State()
    pd34 = State()
    pd35 = State()
    pd36 = State()
    pd37 = State()
    pd38 = State()
    pd39 = State()
    pd40 = State()
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
    q11 = State()
    q12 = State()
    q13 = State()
    q14 = State()
    q15 = State()
    q16 = State()
    q17 = State()
    q18 = State()
    q19 = State()
    q20 = State()
    q21 = State()
    q22 = State()
    q23 = State()
    q24 = State()
    q25 = State()
    q26 = State()
    q27 = State()
    q28 = State()
    q29 = State()
    q30 = State()
    q31 = State()
    q32 = State()
    q33 = State()
    q34 = State()
    q35 = State()
    q36 = State()
    q37 = State()
    q38 = State()
    q39 = State()
    q40 = State()
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
         await pd7(callback_query, state)
    elif current_state == UserState.pd8.state:
         await pd8(callback_query, state)
    elif current_state == UserState.pd9.state:
         await pd9(callback_query, state)
    elif current_state == UserState.pd10.state:
         await pd10(callback_query, state)
    elif current_state == UserState.pd11.state:
         await pd11(callback_query, state)
    elif current_state == UserState.pd12.state:
         await pd12(callback_query, state)
    elif current_state == UserState.pd13.state:
         await pd13(callback_query, state)
    elif current_state == UserState.pd14.state:
         await pd14(callback_query, state)
    elif current_state == UserState.pd15.state:
         await pd15(callback_query, state)
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
    if current_state == UserState.pd21.state:
         await pd21(callback_query, state)
    elif current_state == UserState.pd22.state:
         await pd22(callback_query, state)
    elif current_state == UserState.pd23.state:
         await pd23(callback_query, state)
    elif current_state == UserState.pd24.state:
         await pd24(callback_query, state)
    elif current_state == UserState.pd25.state:
         await pd25(callback_query, state)
    elif current_state == UserState.pd26.state:
         await pd26(callback_query, state)
    elif current_state == UserState.pd27.state:
         await pd27(callback_query, state)
    elif current_state == UserState.pd28.state:
         await pd28(callback_query, state)
    elif current_state == UserState.pd29.state:
         await pd29(callback_query, state)
    elif current_state == UserState.pd30.state:
         await pd30(callback_query, state)
    elif current_state == UserState.pd31.state:
         await pd31(callback_query, state)
    elif current_state == UserState.pd32.state:
         await pd32(callback_query, state)
    elif current_state == UserState.pd33.state:
         await pd33(callback_query, state)
    elif current_state == UserState.pd34.state:
         await pd34(callback_query, state)
    elif current_state == UserState.pd35.state:
         await pd35(callback_query, state)
    elif current_state == UserState.pd36.state:
        await pd36(callback_query, state)
    elif current_state == UserState.pd37.state:
         await pd37(callback_query, state)
    elif current_state == UserState.pd38.state:
         await pd38(callback_query, state)
    elif current_state == UserState.pd39.state:
         await pd39(callback_query, state)
    elif current_state == UserState.pd40.state:
         await pd40(callback_query, state)
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
    elif current_state == UserState.q11.state:
         await q11(callback_query.message, state)
    elif current_state == UserState.q12.state:
         await q12(callback_query.message, state)
    elif current_state == UserState.q13.state:
         await q13(callback_query.message, state)
    elif current_state == UserState.q14.state:
         await q14(callback_query.message, state)
    elif current_state == UserState.q15.state:
         await q15(callback_query.message, state)
    elif current_state == UserState.q16.state:
         await q16(callback_query.message, state)
    elif current_state == UserState.q17.state:
         await q17(callback_query.message, state)
    elif current_state == UserState.q18.state:
         await q18(callback_query.message, state)
    elif current_state == UserState.q19.state:
         await q19(callback_query.message, state)
    elif current_state == UserState.q20.state:
         await q20(callback_query.message, state)
    elif current_state == UserState.q21.state:
         await q21(callback_query.message, state)
    elif current_state == UserState.q22.state:
         await q22(callback_query.message, state)
    elif current_state == UserState.q23.state:
         await q23(callback_query.message, state)
    elif current_state == UserState.q24.state:
         await q24(callback_query.message, state)
    elif current_state == UserState.q25.state:
         await q25(callback_query.message, state)
    elif current_state == UserState.q26.state:
         await q26(callback_query.message, state)
    elif current_state == UserState.q27.state:
         await q27(callback_query.message, state)
    elif current_state == UserState.q28.state:
         await q28(callback_query.message, state)
    elif current_state == UserState.q29.state:
         await q29(callback_query.message, state)
    elif current_state == UserState.q30.state:
         await q30(callback_query.message, state)
    elif current_state == UserState.q31.state:
         await q31(callback_query.message, state)
    elif current_state == UserState.q32.state:
         await q32(callback_query.message, state)
    elif current_state == UserState.q33.state:
         await q33(callback_query.message, state)
    elif current_state == UserState.q34.state:
         await q34(callback_query.message, state)
    elif current_state == UserState.q35.state:
         await q35(callback_query.message, state)
    elif current_state == UserState.q36.state:
         await q36(callback_query.message, state)
    elif current_state == UserState.q37.state:
         await q37(callback_query.message, state)
    elif current_state == UserState.q38.state:
         await q38(callback_query.message, state)
    elif current_state == UserState.q39.state:
         await q39(callback_query.message, state)
    elif current_state == UserState.q40.state:
         await q40(callback_query.message, state)



##################################################################################################################################################################################################################
##################################################################################################################################################################################################################
##################################################################################################################################################################################################################
@router.callback_query(lambda c: c.data == 'gpt_question')
async def gpt_question_1(callback_query: CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    await state.update_data(previous_state=current_state)
    await state.set_state(UserState.gpt_1)
    await callback_query.message.answer("Напишите ваш вопрос")


@router.message(StateFilter(UserState.gpt_1))
async def gpt_question_2(message: Message, state: FSMContext, current_state: State):
    user_data = await state.get_data()
    previous_state = user_data.get('previous_state')
    assistant_id = user_data.get('assistant_id')
    question = message.text
    if previous_state:
        await state.set_state(previous_state)
    if assistant_id:  
        thread = await client.beta.threads.create()
        await client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=question
        )
        
        run = await client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id
        )
        
        while True:
            run_status = await client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            if run_status.status == "completed":
                break
            await asyncio.sleep(1)
        
        messages = await client.beta.threads.messages.list(thread.id)
        result = messages.data[0].content[0].text.value
    else:  
        response = await client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": question}]
        )
        result = response.choices[0].message.content
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить обучение", callback_data="notification")],
            [InlineKeyboardButton(text="Задать еще вопрос", callback_data="gpt_question")]
            ])
    await message.answer (text = result, reply_markup = keyboard)
##################################################################################################################################################################################################################
##################################################################################################################################################################################################################
##################################################################################################################################################################################################################


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
            user = message.from_user
            username = user.username
            first_name = user.first_name
            block_name = user_data.get('block')
            module_name = user_data.get('module')
            await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                first_name = first_name,
                                block_name = block_name,
                                module_name = module_name
                         )
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


async def handle_module_end(message: Message, state: FSMContext):
    user_data = await state.get_data()
    match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_block'))
    if match:           
        await message.answer_video(video=user_data.get('video_block'))
        await message.answer(text=f"{user_data.get('welcome')}")  
    else:                    
        await message.answer(f"{user_data.get('welcome')}")

async def handle_module_end_cb(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()

    match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_block'))
    if match:           
        await callback_query.message.answer_video(video=user_data.get('video_block'))
        await callback_query.message.answer(text=f"{user_data.get('welcome')}")  
    else:                    
        await callback_query.message.answer(f"{user_data.get('welcome')}")


@router.message(F.text.startswith("/select_"))
async def handle_command(message: Message, state: FSMContext):
    try:

        user_send = message.text
        await state.set_state(UserState.welcome)
        
        parts = user_send.split('_')
        user_data = await state.get_data()
        sheet_id = user_data.get('sheet_id')

        if len(parts) > 2:  
            block_id = parts[1]
            module_id = parts[2]
            
            sheet_range = await get_module_range(sheet_id, block_id, module_id)
            
            if sheet_range is None:
                await message.answer("Модуль не найден")
            else:
                await state.update_data(sheet_range=sheet_range)
                
                await get_table_data(sheet_id, sheet_range, state)
                user_data = await state.get_data()
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
    except Exception as e:
        print(e)
        


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
            block_name = user_data.get('block')
            module_name = user_data.get('module')
            await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                first_name = first_name,
                                block_name = block_name,
                                module_name = module_name,
                                status = "ПД 1"
                         )
            
            user_data = await state.get_data()
            text = user_data.get('pd1')
            if text:
                match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_1'))
                if match:           
                    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="Продолжить", callback_data="next")],
                    [InlineKeyboardButton(text="Задать вопрос", callback_data="gpt_question")]
                    ])
                    await callback_query.message.answer_video(video=user_data.get('video_1'))
                    await callback_query.message.answer(text=f"{user_data.get('pd1')}", reply_markup = keyboard)
                    await state.set_state(UserState.pd1)
                    await callback_query.answer()
                else:                    
                    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="Продолжить", callback_data="next")],
                    [InlineKeyboardButton(text="Задать вопрос", callback_data="gpt_question")]
                    ])
                    await callback_query.message.answer(f"{user_data.get('pd1')}", reply_markup = keyboard)
                    await state.set_state(UserState.pd1)
                    await callback_query.answer()
            else:
                await state.set_state(UserState.pd40)
                await q1(callback_query, state)     
        
    except Exception as e:
            await callback_query.message.answer(f"❌ Ошибка при загрузке данных: {str(e)}", reply_markup = FAIL_KEYBOARD)



@router.callback_query(StateFilter(UserState.pd1))
async def pd2(callback_query: CallbackQuery, state: FSMContext):
    
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 2"
                         )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)



@router.callback_query(StateFilter(UserState.pd2))
async def pd3(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 3"
    )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)



@router.callback_query(StateFilter(UserState.pd3))
async def pd4(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 4"
    )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)
    


@router.callback_query(StateFilter(UserState.pd4))
async def pd5(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 5"
    )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)

@router.callback_query(StateFilter(UserState.pd5))
async def pd6(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 6"
    )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd6))
async def pd7(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 7"
    )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd7))
async def pd8(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 8"
    )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd8))
async def pd9(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 9"
    )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd9))
async def pd10(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 10"
    )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd10))
async def pd11(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 11"
    )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd11))
async def pd12(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 12"
    )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd12))
async def pd13(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 13"
    )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd13))
async def pd14(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 14"
    )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd14))
async def pd15(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 15"
    )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd15))
async def pd16(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 16"
    )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd16))
async def pd17(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 17"
    )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd17))
async def pd18(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 18"
    )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd18))
async def pd19(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 19"
    )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd19))
async def pd20(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 20"
    )
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
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)
##############
@router.callback_query(StateFilter(UserState.pd20))
async def pd21(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 21"
    )
    text = user_data.get('pd21')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_21'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_21'))
            await callback_query.message.answer(text=f"{user_data.get('pd21')}", reply_markup = keyboard)
            await state.set_state(UserState.pd21)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd21')}", reply_markup = keyboard)
            await state.set_state(UserState.pd21)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)

@router.callback_query(StateFilter(UserState.pd21))
async def pd22(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 22"
    )
    text = user_data.get('pd22')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_22'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_22'))
            await callback_query.message.answer(text=f"{user_data.get('pd22')}", reply_markup = keyboard)
            await state.set_state(UserState.pd22)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd22')}", reply_markup = keyboard)
            await state.set_state(UserState.pd22)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd22))
async def pd23(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 23"
    )
    text = user_data.get('pd23')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_23'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_23'))
            await callback_query.message.answer(text=f"{user_data.get('pd23')}", reply_markup = keyboard)
            await state.set_state(UserState.pd23)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd23')}", reply_markup = keyboard)
            await state.set_state(UserState.pd23)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd23))
async def pd24(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 24"
    )
    text = user_data.get('pd24')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_24'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_24'))
            await callback_query.message.answer(text=f"{user_data.get('pd24')}", reply_markup = keyboard)
            await state.set_state(UserState.pd24)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd24')}", reply_markup = keyboard)
            await state.set_state(UserState.pd24)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd24))
async def pd25(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 25"
    )
    text = user_data.get('pd25')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_25'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_25'))
            await callback_query.message.answer(text=f"{user_data.get('pd25')}", reply_markup = keyboard)
            await state.set_state(UserState.pd25)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd25')}", reply_markup = keyboard)
            await state.set_state(UserState.pd25)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd25))
async def pd26(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 26"
    )
    text = user_data.get('pd26')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_26'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_26'))
            await callback_query.message.answer(text=f"{user_data.get('pd26')}", reply_markup = keyboard)
            await state.set_state(UserState.pd26)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd26')}", reply_markup = keyboard)
            await state.set_state(UserState.pd26)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd26))
async def pd27(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 27"
    )
    text = user_data.get('pd27')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_27'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_27'))
            await callback_query.message.answer(text=f"{user_data.get('pd27')}", reply_markup = keyboard)
            await state.set_state(UserState.pd27)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd27')}", reply_markup = keyboard)
            await state.set_state(UserState.pd27)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd27))
async def pd28(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 28"
    )
    text = user_data.get('pd28')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_28'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_28'))
            await callback_query.message.answer(text=f"{user_data.get('pd28')}", reply_markup = keyboard)
            await state.set_state(UserState.pd28)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd28')}", reply_markup = keyboard)
            await state.set_state(UserState.pd28)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd28))
async def pd29(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 29"
    )
    text = user_data.get('pd29')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_29'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_29'))
            await callback_query.message.answer(text=f"{user_data.get('pd29')}", reply_markup = keyboard)
            await state.set_state(UserState.pd29)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd29')}", reply_markup = keyboard)
            await state.set_state(UserState.pd29)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd29))
async def pd30(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 30"
    )
    text = user_data.get('pd30')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_30'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_30'))
            await callback_query.message.answer(text=f"{user_data.get('pd30')}", reply_markup = keyboard)
            await state.set_state(UserState.pd30)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd30')}", reply_markup = keyboard)
            await state.set_state(UserState.pd30)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd30))
async def pd31(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 31"
    )
    text = user_data.get('pd31')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_31'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_31'))
            await callback_query.message.answer(text=f"{user_data.get('pd31')}", reply_markup = keyboard)
            await state.set_state(UserState.pd31)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd31')}", reply_markup = keyboard)
            await state.set_state(UserState.pd31)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd31))
async def pd32(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 32"
    )
    text = user_data.get('pd32')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_32'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_32'))
            await callback_query.message.answer(text=f"{user_data.get('pd32')}", reply_markup = keyboard)
            await state.set_state(UserState.pd32)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd32')}", reply_markup = keyboard)
            await state.set_state(UserState.pd32)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd32))
async def pd33(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 33"
    )
    text = user_data.get('pd33')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_33'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_33'))
            await callback_query.message.answer(text=f"{user_data.get('pd33')}", reply_markup = keyboard)
            await state.set_state(UserState.pd33)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd33')}", reply_markup = keyboard)
            await state.set_state(UserState.pd33)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd33))
async def pd34(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 34"
    )
    text = user_data.get('pd34')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_34'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_34'))
            await callback_query.message.answer(text=f"{user_data.get('pd34')}", reply_markup = keyboard)
            await state.set_state(UserState.pd34)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd34')}", reply_markup = keyboard)
            await state.set_state(UserState.pd34)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd34))
async def pd35(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 35"
    )
    text = user_data.get('pd35')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_35'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_35'))
            await callback_query.message.answer(text=f"{user_data.get('pd35')}", reply_markup = keyboard)
            await state.set_state(UserState.pd35)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd35')}", reply_markup = keyboard)
            await state.set_state(UserState.pd35)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd35))
async def pd36(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 36"
    )
    text = user_data.get('pd36')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_36'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_36'))
            await callback_query.message.answer(text=f"{user_data.get('pd36')}", reply_markup = keyboard)
            await state.set_state(UserState.pd36)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd36')}", reply_markup = keyboard)
            await state.set_state(UserState.pd36)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd36))
async def pd37(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 37"
    )
    text = user_data.get('pd37')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_37'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_37'))
            await callback_query.message.answer(text=f"{user_data.get('pd37')}", reply_markup = keyboard)
            await state.set_state(UserState.pd37)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd37')}", reply_markup = keyboard)
            await state.set_state(UserState.pd37)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd37))
async def pd38(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 38"
    )
    text = user_data.get('pd38')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_38'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_38'))
            await callback_query.message.answer(text=f"{user_data.get('pd38')}", reply_markup = keyboard)
            await state.set_state(UserState.pd38)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd38')}", reply_markup = keyboard)
            await state.set_state(UserState.pd38)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd38))
async def pd39(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 39"
    )
    text = user_data.get('pd39')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_39'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_39'))
            await callback_query.message.answer(text=f"{user_data.get('pd39')}", reply_markup = keyboard)
            await state.set_state(UserState.pd39)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd39')}", reply_markup = keyboard)
            await state.set_state(UserState.pd39)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)


@router.callback_query(StateFilter(UserState.pd39))
async def pd40(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "ПД 40"
    )
    text = user_data.get('pd40')
    if text:
        match = re.search(TELEGRAM_VIDEO_PATTERN, user_data.get('video_40'))
        if match:           
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer_video(video=user_data.get('video_40'))
            await callback_query.message.answer(text=f"{user_data.get('pd40')}", reply_markup = keyboard)
            await state.set_state(UserState.pd40)
            await callback_query.answer()
        else:
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Продолжить", callback_data="next")]
            ])
            await callback_query.message.answer(f"{user_data.get('pd40')}", reply_markup = keyboard)
            await state.set_state(UserState.pd40)
            
            await callback_query.answer()
    else:
         await state.set_state(UserState.pd40)
         await q1(callback_query, state)




@router.callback_query(StateFilter(UserState.pd40))
async def q1(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    questionare = user_data.get('questionare')
    if questionare == "Нет":
        await handle_quest_skip(callback_query, state)
        return
    sheet_id = user_data.get('sheet_id')
    user = callback_query.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 1"
    )
    
        

    text = user_data.get('test_tiser')
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
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 2"
    )
    text = user_data.get('q2')
    if text:
        await message.answer(f"{user_data.get('q2')}")
        await state.set_state(UserState.q2)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q2))
async def q3(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans2=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 3"
    )
    text = user_data.get('q3')
    if text:
        await message.answer(f"{user_data.get('q3')}")
        await state.set_state(UserState.q3)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q3))
async def q4(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans3=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 4"
    )
    text = user_data.get('q4')
    if text:
        await message.answer(f"{user_data.get('q4')}")
        await state.set_state(UserState.q4)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q4))
async def q5(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans4=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 5"
    )
    text = user_data.get('q5')
    if text:
        await message.answer(f"{user_data.get('q5')}")
        await state.set_state(UserState.q5)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q5))
async def q6(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans5=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 6"
    )
    text = user_data.get('q6')
    if text:
        await message.answer(f"{user_data.get('q6')}")
        await state.set_state(UserState.q6)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)    

@router.message(StateFilter(UserState.q6))
async def q7(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans6=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 7"
    )
    text = user_data.get('q7')
    if text:
        await message.answer(f"{user_data.get('q7')}")
        await state.set_state(UserState.q7)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q7))
async def q8(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans7=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 8"
    )
    text = user_data.get('q8')
    if text:
        await message.answer(f"{user_data.get('q8')}")
        await state.set_state(UserState.q8)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q8))
async def q9(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans8=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 9"
    )
    text = user_data.get('q9')
    if text:
        await message.answer(f"{user_data.get('q9')}")
        await state.set_state(UserState.q9)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q9))
async def q10(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans9=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 10"
    )
    text = user_data.get('q10')
    if text:
        await message.answer(f"{user_data.get('q10')}")
        await state.set_state(UserState.q10)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q10))
async def q11(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans10=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 11"
    )
    text = user_data.get('q11')
    if text:
        await message.answer(f"{user_data.get('q11')}")
        await state.set_state(UserState.q11)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q11))
async def q12(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans11=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 12"
    )
    text = user_data.get('q12')
    if text:
        await message.answer(f"{user_data.get('q12')}")
        await state.set_state(UserState.q12)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q12))
async def q13(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans12=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 13"
    )
    text = user_data.get('q13')
    if text:
        await message.answer(f"{user_data.get('q13')}")
        await state.set_state(UserState.q13)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q13))
async def q14(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans13=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 14"
    )
    text = user_data.get('q14')
    if text:
        await message.answer(f"{user_data.get('q14')}")
        await state.set_state(UserState.q14)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q14))
async def q15(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans14=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 15"
    )
    text = user_data.get('q15')
    if text:
        await message.answer(f"{user_data.get('q15')}")
        await state.set_state(UserState.q15)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)    

@router.message(StateFilter(UserState.q15))
async def q16(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans15=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 16"
    )
    text = user_data.get('q16')
    if text:
        await message.answer(f"{user_data.get('q16')}")
        await state.set_state(UserState.q16)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q16))
async def q17(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans16=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 17"
    )
    text = user_data.get('q17')
    if text:
        await message.answer(f"{user_data.get('q17')}")
        await state.set_state(UserState.q17)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q17))
async def q18(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans17=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 18"
    )
    text = user_data.get('q18')
    if text:
        await message.answer(f"{user_data.get('q18')}")
        await state.set_state(UserState.q18)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q18))
async def q19(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans18=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 19"
    )
    text = user_data.get('q19')
    if text:
        await message.answer(f"{user_data.get('q19')}")
        await state.set_state(UserState.q19)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q19))
async def q20(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans19=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 20"
    )
    text = user_data.get('q20')
    if text:
        await message.answer(f"{user_data.get('q20')}")
        await state.set_state(UserState.q20)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q20))
async def q21(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans20=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 21"
    )
    text = user_data.get('q21')
    if text:
        await message.answer(f"{user_data.get('q21')}")
        await state.set_state(UserState.q21)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q21))
async def q22(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans21=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 22"
    )
    text = user_data.get('q22')
    if text:
        await message.answer(f"{user_data.get('q22')}")
        await state.set_state(UserState.q22)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q22))
async def q23(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans22=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 23"
    )
    text = user_data.get('q23')
    if text:
        await message.answer(f"{user_data.get('q23')}")
        await state.set_state(UserState.q23)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q23))
async def q24(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans23=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 24"
    )
    text = user_data.get('q24')
    if text:
        await message.answer(f"{user_data.get('q24')}")
        await state.set_state(UserState.q24)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q24))
async def q25(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans24=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 25"
    )
    text = user_data.get('q25')
    if text:
        await message.answer(f"{user_data.get('q25')}")
        await state.set_state(UserState.q25)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)    

@router.message(StateFilter(UserState.q25))
async def q26(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans25=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 26"
    )
    text = user_data.get('q26')
    if text:
        await message.answer(f"{user_data.get('q26')}")
        await state.set_state(UserState.q26)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q26))
async def q27(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans26=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 27"
    )
    text = user_data.get('q27')
    if text:
        await message.answer(f"{user_data.get('q27')}")
        await state.set_state(UserState.q27)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q27))
async def q28(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans27=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 28"
    )
    text = user_data.get('q28')
    if text:
        await message.answer(f"{user_data.get('q28')}")
        await state.set_state(UserState.q28)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q28))
async def q29(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans28=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 29"
    )
    text = user_data.get('q29')
    if text:
        await message.answer(f"{user_data.get('q29')}")
        await state.set_state(UserState.q29)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q29))
async def q30(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans29=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 30"
    )
    text = user_data.get('q30')
    if text:
        await message.answer(f"{user_data.get('q30')}")
        await state.set_state(UserState.q30)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)


@router.message(StateFilter(UserState.q30))
async def q31(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans30=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 31"
    )
    text = user_data.get('q31')
    if text:
        await message.answer(f"{user_data.get('q31')}")
        await state.set_state(UserState.q31)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q31))
async def q32(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans31=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 32"
    )
    text = user_data.get('q32')
    if text:
        await message.answer(f"{user_data.get('q32')}")
        await state.set_state(UserState.q32)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q32))
async def q33(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans32=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 33"
    )
    text = user_data.get('q33')
    if text:
        await message.answer(f"{user_data.get('q33')}")
        await state.set_state(UserState.q33)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q33))
async def q34(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans33=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 34"
    )
    text = user_data.get('q34')
    if text:
        await message.answer(f"{user_data.get('q34')}")
        await state.set_state(UserState.q34)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q34))
async def q35(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans34=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 35"
    )
    text = user_data.get('q35')
    if text:
        await message.answer(f"{user_data.get('q35')}")
        await state.set_state(UserState.q35)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)    

@router.message(StateFilter(UserState.q35))
async def q36(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans35=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 36"
    )
    text = user_data.get('q36')
    if text:
        await message.answer(f"{user_data.get('q36')}")
        await state.set_state(UserState.q36)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q36))
async def q37(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans36=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 37"
    )
    text = user_data.get('q37')
    if text:
        await message.answer(f"{user_data.get('q37')}")
        await state.set_state(UserState.q37)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q37))
async def q38(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans37=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 38"
    )
    text = user_data.get('q38')
    if text:
        await message.answer(f"{user_data.get('q38')}")
        await state.set_state(UserState.q38)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q38))
async def q39(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans38=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 39"
    )
    text = user_data.get('q39')
    if text:
        await message.answer(f"{user_data.get('q39')}")
        await state.set_state(UserState.q39)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q39))
async def q40(message: Message, state: FSMContext):
    ans1 = message.text
    await state.update_data(ans39=ans1)
    user_data = await state.get_data()
    sheet_id = user_data.get('sheet_id')
    user = message.from_user
    username = user.username
    await write_to_google_sheet(
                                sheet_id = sheet_id, 
                                username = username,
                                status = "Вопрос 40"
    )
    text = user_data.get('q40')
    if text:
        await message.answer(f"{user_data.get('q40')}")
        await state.set_state(UserState.q40)
    else:
        await state.set_state(UserState.q40)
        await process_answers(message, state)

@router.message(StateFilter(UserState.q40))
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
    await state.update_data(ans40=ans10)
    user_data = await state.get_data()
    text = user_data.get('processing_answers')
    await message.answer(text = text)
    await state.update_data(survey_completed = True)
    
    sheet_id = user_data.get('sheet_id')
    questions = []
    for i in range(1, 41):
        questions.append(f"Вопрос {i}: {user_data.get(f'q{i}')}, \nОтвет {i}: {user_data.get(f'ans{i}')}")
    user_qa = ";\n".join(questions)
    
    raw_promt = user_data.get('promt')
    raw_promt_2 = user_data.get('promt_2')
    promt = f"Твоя задача оценить ответы на вопросы и выдать балл за ответы от 0 до 100. ВАЖНО в твоем ответе должны быть строго только цифры для дальнейшего использования в коде, так же можно использовать знак\"-\". Вот критерии для оценки: {raw_promt} Если есть вопросы или ответы которые отсутствуют, игнорируй.(Вопросы не были заданы) Вопросы и ответы пользователя{user_qa}"
    promt_2 = f"{raw_promt_2} Если есть вопросы или ответы которые отсутствуют, игнорируй.(Вопросы не были заданы) Вопросы и ответы пользователя{user_qa}"
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
                            gpt_response=gpt_response,
                            gpt_response_2 = ai_comment
                            )
 
        
    if response == "Тестирование пройдено":
        await state.set_state(UserState.result_yes)
        await write_to_google_sheet(
            sheet_id = sheet_id, 
            username = message.from_user.username,
            first_name=message.from_user.first_name,
            status=response,
            user_score=response_score,
            gpt_response=ai_comment,
            qa_data=user_qa
            
            )
        text_3 = user_data.get('result_yes')
        await message.answer(text=text_3)
        await handle_quest_skip_m(message, state)
    
    
    
    elif response == "Тестирование не пройдено":
        await state.set_state(UserState.welcome)
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Попробовать снова", callback_data="try_again")]
            ])
        await message.answer(text = f"{user_data.get('result_no')}", reply_markup=keyboard) 
        
        await write_to_google_sheet(
            sheet_id = sheet_id, 
            username = message.from_user.username,
            first_name=message.from_user.first_name,
            status=response,
            user_score=response_score,
            gpt_response=ai_comment,
            qa_data=user_qa
            
            )

async def handle_quest_skip_m(message: Message, state: FSMContext):
    user_data = await state.get_data()
    meeting = user_data.get('meeting')
    if meeting == "Нет":
        await handle_module_end(message, state)
    else:
        await state.set_state(UserState.result_yes)
        await message.answer("Пожалуйста, напишите ваше имя.")



async def handle_quest_skip(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    meeting = user_data.get('meeting')
    if meeting == "Нет":
        await handle_module_end_cb(callback_query, state)
    else:
        await state.set_state(UserState.result_yes)
        await callback_query.message.answer("Пожалуйста, напишите ваше имя.")



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
            f"{date_value} {time_value}\n\n"
            f"Название блока: {user_data.get('block')}\n"
            f"Название модуля: {user_data.get('module')}\n\n"
            f"ФИО: {user_data.get('user_fio', 'Без имени')}\n"
            f"ТГ: @{callback.from_user.username}\n"
            f"Ссылка на переписку: https://t.me/{callback.from_user.username}\n"
            f"Номер: {user_data.get('user_phone', 'Без телефона')}\n"
            f"Cылка на таблицу: https://docs.google.com/spreadsheets/d/{user_data.get('sheet_id')}\n\n"
            f"Баллы кандидата: {user_data.get('response_score')}\n\n"
            f"AI комментарий: {user_data.get('gpt_response_2')}"
            
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
            f"{user_data.get('confurmation_message')}", reply_markup=keyboard
        )

        
        chat_id = user_data.get('chat_id')
        
        await state.set_state(UserState.process_time_change)
        
        await bot.send_message(chat_id=chat_id,
                                text=f"{record_text}",
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
            status="Записался на встречу",
            block_name=user_data.get('block'),
            module_name=user_data.get('module'),
            full_name=user_data.get('user_fio'),
            phone_number=user_data.get('user_phone'),
            gpt_response=user_data.get('gpt_response_2', ''),
            
            interview_date=date_value,
            interview_time=time_value,
            qa_data=user_data.get('user_qa'),
            user_score=user_data.get('response_score')
        )
        
        user_data = await state.get_data()
        interview_time = parse_interview_datetime(date_value, time_value)
        interview_time_utc = interview_time.astimezone(SERVER_TZ)
        task1 = asyncio.create_task(send_reminder_at_time(callback.message.chat.id, interview_time_utc - timedelta(hours=1), f"{user_data.get('notification_hour')}"))
        task2 = asyncio.create_task(send_reminder_at_time(callback.message.chat.id, interview_time_utc, f"{user_data.get('notification_now')}"))
        task3 = asyncio.create_task(clear_state_after_delay(state))

        await state.update_data(
        date_value=date_value,
        time_value=time_value,
        reminder_tasks=[id(task1), id(task2), id(task3)]  
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

async def clear_state_after_delay(state: FSMContext, delay: int = 86400):
    await asyncio.sleep(delay)
    await state.clear()


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