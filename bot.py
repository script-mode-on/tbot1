from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message,CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command
from aiogram.utils.callback_data import CallbackData
import os

TOKEN = os.environ.get('BOT_TOKEN)
bot = Bot(TOKEN)
dp = Dispatcher(bot)

# gans
#gan x category
URL_GANx = 'https://cccstore.ru/catalog/kubiki-rubika/gan-356-x-numerical-3x3x3/'
URL_GANxv5= 'https://cccstore.ru/catalog/kubiki-rubika/gan-356-x-3x3x3/'

# gan 354 category
URL_GAN354 = 'https://cccstore.ru/catalog/kubiki-rubika/gan-3-54m-3x3x3/'
URL_GAN354v2 = 'https://cccstore.ru/catalog/kubiki-rubika/gan-354-m-v2-3x3x3/'

# gan air category
URL_GANAIR_MASTER = 'https://cccstore.ru/catalog/kubiki-rubika/gan3-56-3x3x3-air-master/'
URL_GANAIR_PRO = 'https://cccstore.ru/catalog/kubiki-rubika/gan-356-air-pro/'
URL_GANAIR_SM = 'https://cccstore.ru/catalog/kubiki-rubika/gan3-56-3x3x3-air-sm/'
URL_GANAIR_S = 'https://cccstore.ru/catalog/kubiki-rubika/gan3-56-3x3x3-air-s/'
URL_GANAIR_M = 'https://cccstore.ru/catalog/kubiki-rubika/gan-356-air-m-3x3x3/'
URL_GANAIR_ML = 'https://cccstore.ru/catalog/kubiki-rubika/gan-356-m-3x3x3-light-version/'

# gan r category
URL_GANRS = 'https://cccstore.ru/catalog/kubiki-rubika/gan-356-rs-3x3x3/'
URL_GANR = 'https://cccstore.ru/catalog/kubiki-rubika/gan-356-r-3x3x3/'

# gan 330
URL_GAN330 = 'https://cccstore.ru/catalog/kubiki-rubika/3x3/gan-330-3x3x3-brelok/'

# gan i
URL_GANI = 'https://cccstore.ru/catalog/kubiki-rubika/gan-356-i-3x3x3/'
URL_GANIp = 'https://cccstore.ru/catalog/kubiki-rubika/gan-356-i-play-3x3x3/'

URL_GAN356M = 'https://cccstore.ru/catalog/kubiki-rubika/gan-356-m-3x3x3/'

URL_GAN356LM = 'https://cccstore.ru/catalog/kubiki-rubika/gan-356-m-3x3x3-light-version/'

# valks
#valk power
URL_VALKP = 'https://cccstore.ru/catalog/kubiki-rubika/qiyi-3x3x3-mofangge-valk-3-power/'

URL_VALKPM = 'https://cccstore.ru/catalog/kubiki-rubika/qiyi-3x3x3-mofangge-valk-3-power-m/'

URL_VALKF = 'https://cccstore.ru/catalog/kubiki-rubika/qiyi-mofangge-3x3x3-valk-3-power-force'

URL_VALKFM = 'https://cccstore.ru/catalog/kubiki-rubika/qiyi-mofangge-3x3x3-valk-3-power-m-force/'

#valk3
URL_VALK3 = 'https://cccstore.ru/catalog/kubiki-rubika/qiyi-mofangge-3x3x3-valk-3/'

URL_VALK3M = 'https://cccstore.ru/catalog/kubiki-rubika/qiyi-mofangge-3x3x3-valk-3m/'

# valk mini
URL_VALKmini = 'https://cccstore.ru/catalog/kubiki-rubika/qiyi-mofangge-3x3x3-valk-3-mini/'

URL_VALKmp = 'https://cccstore.ru/catalog/kubiki-rubika/qiyi-3x3x3-mofangge-valk-3-mini-rose-pink/'
# valk elite
URL_VALKE = 'https://cccstore.ru/catalog/kubiki-rubika/qiyi-mofangge-3x3x3-valk-3-elite-m/'

#moyu
URL_MOYUWGTS = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-weilong-gts/'

URL_MOYUWGTS2 = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-weilong-gts-2/'

URL_MOYUWGTS2m = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-weilong-gts-2m/'

URL_MOYUWGTS2WRV = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-weilong-gts-2m-wca-record-version/'

URL_MOYUWGTS3m = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-weilong-gts-3m/'

URL_MOYUWGTS3 = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-weilong-gts-3/'

URL_MOYUWGTS3lm = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-weilong-gts-3m-lower-magnetic/'

URL_MOYUWR = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-weilong-wr/'

URL_MOYUWRm = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-weilong-wr-m/'

URL_MOYUWv2 = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-weilong-v2/'

#aolong
URL_MOYUa = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-aolong-gt/'

URL_MOYUa2 = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-aolong-v2/'

# Moyu cubing classroom

URL_MF3Scarbon = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-cubing-classroom-mf3s-carbon/'

URL_MF3 = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-cubing-classroom-mf3/'

URL_MF3S = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-cubing-classroom-mf3s/'

URL_MF3mini = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-cubing-classroom-mf3-mini-50mm/'

URL_MF3RS = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-cubing-classroom-mf3rs/'

URL_MF3RS2 = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-cubing-classroom-mf3rs2/'

URL_MF3RS3 = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-cubing-classroom-mf3rs3/'

URL_MF3RS3m = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-cubing-classroom-mf3rs3-m/'

URL_GUOGUANpro = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-guoguan-yuexiao-pro/'

URL_GUOGUAN = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-guoguan-yuexiao/'

URL_GUOGUANprom = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-guoguan-yuexiao-pro-magnetic/'

URL_GUOGUANE = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-guoguan-yuexiao-e/'

URL_GUOGUANEDM = 'https://cccstore.ru/catalog/kubiki-rubika/moyu-3x3x3-guoguan-yuexiao-edm/'

# callback
bot_callback = CallbackData(
	'buy', 'item_name', 'quantity')

#
#buttons
choice = InlineKeyboardMarkup(row_width=2)

buy_gan_button = InlineKeyboardButton(text=
	'Gan', callback_data='buy:gan:10')
choice.insert(buy_gan_button)

buy_valk_button = InlineKeyboardButton(text=
	'Valk', callback_data='buy:valk:10')
choice.insert(buy_valk_button)

buy_moyu_button = InlineKeyboardButton(text = 
	'Moyu', callback_data='buy:moyu:10')
choice.insert(buy_moyu_button)

cancel_button = InlineKeyboardButton(text=
	'отмена покупки', callback_data='cancel')
choice.add(cancel_button)

#
# gans category buttons
choice_gans_category  = InlineKeyboardMarkup(
	row_width=2)

gan_x_category = InlineKeyboardButton(text=
	'Gan X', callback_data='buy:ganx:10')
choice_gans_category.insert(gan_x_category)

gan_354_category = InlineKeyboardButton(text=
	'Gan 354 M', callback_data='buy:gan354:10')
choice_gans_category.insert(gan_354_category)

gan_air_category = InlineKeyboardButton(text=
	'Gan air', callback_data='buy:ganair:10')
choice_gans_category.insert(gan_air_category)

gan_r_category = InlineKeyboardButton(text=
	'Gan R', callback_data='buy:ganr:10')
choice_gans_category.insert(gan_r_category)

gan_330_category = InlineKeyboardButton(text=
	'Gan 330', callback_data='buy:gan330:10')
choice_gans_category.insert(gan_330_category)

gan_i_category = InlineKeyboardButton(text=
	'Gan 356 I', callback_data='buy:gani:10')
choice_gans_category.insert(gan_i_category)

gan_365m_category = InlineKeyboardButton(
	text='Gan 356 m',
	callback_data='buy:gan356:10')
choice_gans_category.insert(
	gan_365m_category)

# valks category buttons
choice_valks_category = InlineKeyboardMarkup(
	row_width=2)

valk_power_category = InlineKeyboardButton( 
	text='Valk power',
	callback_data='buy:valkpower:10')
choice_valks_category.insert(
	valk_power_category)

valk_3_category=InlineKeyboardButton(
	text='Valk 3', 
	callback_data='buy:valk3:10')
choice_valks_category.insert(valk_3_category)

valk_mini_category = InlineKeyboardButton(
	text='Valk mini', 
	callback_data='buy:valkmini:10')
choice_valks_category.insert(
	valk_mini_category)

valk_elite_category = InlineKeyboardButton(
	text='Valk Elite', 
	callback_data='buy:valkelite:10')
choice_valks_category.insert(
	valk_elite_category)

#moyu category buttons
choice_moyu_category = InlineKeyboardMarkup(
	row_width=2)

moyu_weilong_category = InlineKeyboardButton(
	text='Moyu weilong', 
	callback_data='buy:moyuweilong:10')
choice_moyu_category.insert(
	moyu_weilong_category)

moyu_aolong_category = InlineKeyboardButton(
	text='Moyu aolong', 
	callback_data='buy:moyuaolong:10')
choice_moyu_category.insert(
	moyu_aolong_category)

moyu_mf_category = InlineKeyboardButton(
	text='Moyu cubing classroom', 
	callback_data='buy:moyumf:10')
choice_moyu_category.insert(
	moyu_mf_category)

moyu_guoguan_category = InlineKeyboardButton(
	text='Moyu Guoguan', 
	callback_data='buy:moyugg:10')
choice_moyu_category.insert(
	moyu_guoguan_category)


#
#gans version
#gan x version
ganx_keyboard = InlineKeyboardMarkup(
		inline_keyboard=[
			[
				InlineKeyboardButton(text= 
					'Gan 356 X Numerical IPG', 				
					url=URL_GANx),
			InlineKeyboardButton(text= 
				'Gan 356 X IPG v5', 
				url=URL_GANxv5)
			]
		]
	)

#gan 354 version
gan354_keyboard = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text= 
				'Gan 354 M',
				url=URL_GAN354),
			InlineKeyboardButton(text= 
				'Gan 354 M v2',
				url=URL_GAN354v2)
		]
	]
)

#gan air
ganair_keyboard = InlineKeyboardMarkup( 
	inline_keyboard = [
		[
			InlineKeyboardButton(text= 
				'Gan Air SM', 
				url=URL_GANAIR_SM),
			InlineKeyboardButton(text= 
				'Gan Air S', 
				url=URL_GANAIR_S)
		], 
		[
			InlineKeyboardButton(text= 
				'Gan Air Master',
				url=URL_GANAIR_MASTER),
			InlineKeyboardButton(text= 
				'Gan Air PRO', 
				url=URL_GANAIR_PRO)
		], 
		[
			InlineKeyboardButton(text= 
				'Gan Air M', 
				url=URL_GANAIR_M),
			InlineKeyboardButton(text= 
				'Gan Air M lite version',
				url=URL_GANAIR_ML)
		]
	]
)

#gan 330
gan330_keyboard = InlineKeyboardMarkup(
	inline_keyboard = [ 	
		[
			InlineKeyboardButton(text= 
				'Gan 330', 
				url=URL_GAN330)
		]
	]
)

#gan i
gani_keyboard = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= 
				'Gan 356 I', 
				url=URL_GANI),
			InlineKeyboardButton(text= 
				'Gan 356 I play', 
				url=URL_GANIp)
		]
	]
)

gan356m_keyboard = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= 
				'Gan 356 m', 
				url=URL_GAN356M),
			InlineKeyboardButton(text= 
				'Gan 356 m lite', 
				url=URL_GAN356LM)
		]
	]
)

#valks version
#valk power
valkpower_keyboard = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= 
				'Valk 3 power M', 
				url=URL_VALKPM),
			InlineKeyboardButton(text= 
				'Valk 3 power', 
				url=URL_VALKP)
		], 
		[
			InlineKeyboardButton(text= 
				'Valk 3 power Forse', 
				url=URL_VALKF),
			InlineKeyboardButton(text= 
				'Valk 3 power Forse M', 
				url=URL_VALKFM)
		]
	]
)

valk3_keyboard = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= 
				'Valk 3', 
				url=URL_VALK3),
			InlineKeyboardButton(text= 
				'Valk 3 M', 
				url=URL_VALK3M)
		]
	]
)

valk3_mini_keyboard = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= 
				'Valk 3 mini', 
				url=URL_VALKmini),
			InlineKeyboardButton(text= 
				'Valk 3 mini pink', 
				url=URL_VALKmp)
		]
	]
)

valk3_elite_keyboard = InlineKeyboardMarkup( 
	inline_keyboard = [
		[
			InlineKeyboardButton(text= 
				'Valk 3 elite', 
				url=URL_VALKE)
		]
	]
)


# moyu buttons
moyuweilong_keyboard = InlineKeyboardMarkup(
	inline_keyboard =[
		[
			InlineKeyboardButton(text= 
				'Moyu welong gts 3',
				url=URL_MOYUWGTS3),
			InlineKeyboardButton(text= 
				'Moyu welong gts 2',
				url=URL_MOYUWGTS2)
		], 
		[
			InlineKeyboardButton(text= 
				'Moyu welong gts', 
				url=URL_MOYUWGTS),
			InlineKeyboardButton(text= 
				'Moyu welong gts 3m',
				url=URL_MOYUWGTS3m)
		], 
		[
			InlineKeyboardButton(text= 
				'Moyu welong gts 2m',
				url=URL_MOYUWGTS2m),
			InlineKeyboardButton(text= 
				'Moyu welong gts 3lm',
				url=URL_MOYUWGTS3lm)
		],
		[
			InlineKeyboardButton(text= 
				'Moyu welong gts 2 WCA record version',
				url=URL_MOYUWGTS2WRV),
			InlineKeyboardButton(text= 
				'Moyu welong Wr', 
				url=URL_MOYUWR)
		], 
		[
			InlineKeyboardButton(text= 
				'Moyu welong Wrm',
				url=URL_MOYUWRm),
			InlineKeyboardButton(text= 
				'Moyu welong v2', 
				url=URL_MOYUWv2)
		]
	]
)

moyuaolong_keyboard = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= 
				'Moyu aolong GT', 
				url=URL_MOYUa),
			InlineKeyboardButton(text= 
				'Moyu aolong v2',
				 url=URL_MOYUa2)
		]
	]
)

moyumf3_keyboard = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= 
				'Moyu RS3', 
				url=URL_MOYUWGTS3),
			InlineKeyboardButton(text= 
				'Moyu MF3', 
				url=URL_MOYUWGTS2)
		], 
		[
			InlineKeyboardButton(text= 
				'Moyu MF3 carbon',
				url=URL_MOYUWGTS),
			InlineKeyboardButton(text= 
				'Moyu MF3RS', 
				url=URL_MOYUWGTS3m)
		], 
		[
			InlineKeyboardButton(text= 
				'Moyu MF3RS2',
				url=URL_MOYUWGTS2m),
			InlineKeyboardButton(text= 
				'Moyu MF3RS3', 
				url=URL_MOYUWGTS3lm)
		], 
		[
			InlineKeyboardButton(text= 
				'Moyu MF3RS3m', 
				url=URL_MOYUWGTS2WRV),
			InlineKeyboardButton(text= 
				'Moyu MF3 mini', 
				url=URL_MOYUWR)
		], 
		[
			InlineKeyboardButton(text= 
				'Moyu MF3S', 
				url=URL_MOYUWRm)
		]
	]
)

moyugg_keyboard = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= 
				'Moyu GuoGuan', 
				url=URL_GUOGUAN),
			InlineKeyboardButton(text= 
				'Moyu GuoGuan pro',
				url=URL_GUOGUANpro)
		], 
		[
			InlineKeyboardButton(text= 
				'Moyu GuoGuan pro m',
				url=URL_GUOGUANprom),
			InlineKeyboardButton(text= 
				'Moyu GuoGuan E', 
				url=URL_GUOGUANE)
		], 
		[
			InlineKeyboardButton(text= 
				'Moyu GuoGuan EDM', 
				url=URL_GUOGUANEDM)
		]
	]
)
#

#
# handlers
@dp.message_handler(Command('start'))
async def start_command(msg: Message):
	await msg.reply(
	text='используйте комманду /help что бы ознакомиться с функциями бота')

@dp.message_handler(Command('buy'))
async def buy_cube(msg: Message):
	await msg.answer(
		'выбирайте фирму куба',
		reply_markup=choice)
 
@dp.callback_query_handler(
	bot_callback.filter(item_name='gan'))
async def buying_gan(
	call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time=60)
	await call.message.answer(
		text='вот все возможные кубы фирмы Gan', 
		reply_markup=choice_gans_category)

@dp.callback_query_handler(
	bot_callback.filter(item_name='gan'))
async def buying_gan(
	call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time=60)
	await call.message.answer(
		text='вот все возможные кубы фирмы Gan', 
		reply_markup=choice_gans_category)

@dp.callback_query_handler(
	bot_callback.filter(item_name='ganx'))
async def buying_gan(
	call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time=60)
	await call.message.answer(
		text='кубы из категории Gan X',
		reply_markup=ganx_keyboard)

@dp.callback_query_handler(
	bot_callback.filter(item_name='gan354'))
async def buying_gan(
	call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time=60)
	await call.message.answer(
		text='кубы из категории Gan 354', 
		reply_markup=gan354_keyboard)

@dp.callback_query_handler(
	bot_callback.filter(item_name='ganair'))
async def buying_gan(
	call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time=60)
	await call.message.answer(
		text='кубы из категории Gan Air', 
		reply_markup=ganair_keyboard)

@dp.callback_query_handler(
	bot_callback.filter(item_name='ganr'))
async def buying_gan(
	call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time=60)
	await call.message.answer(
		text='кубы из категории Gan 354', 
		reply_markup=ganr_keyboard)

@dp.callback_query_handler(
	bot_callback.filter(item_name='gan330'))
async def buying_gan(
	call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time=60)
	await call.message.answer(
		text='куб Gan330', 
		reply_markup=gan330_keyboard)
 
@dp.callback_query_handler(
	bot_callback.filter(item_name='gani'))
async def buying_gan(
	call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time=60)
	await call.message.answer(
		text='куб Gan 365 I', 
		reply_markup=gani_keyboard)
 
# валки
@dp.callback_query_handler(
	bot_callback.filter(item_name='valk'))
async def buying_gan(
	call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time=60)
	await call.message.answer(
		text='вот все возможные кубы фирмы Valk', 
		reply_markup=choice_valks_category)

@dp.callback_query_handler(
	bot_callback.filter(item_name='valkpower'))
async def buying_gan(
	call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time=60)
	await call.message.answer(
		text='кубы категории  valk power', 
		reply_markup=valkpower_keyboard)
 
@dp.callback_query_handler(
	bot_callback.filter(item_name='valk3'))
async def buying_gan(
	call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time=60)
	await call.message.answer(
		text='кубы категории  valk 3', 
		reply_markup=valk3_keyboard)
 
@dp.callback_query_handler(
	bot_callback.filter(item_name='valkmini'))
async def buying_gan(
	call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time=60)
	await call.message.answer(
		text='кубы категории  valk 3 mini', 
		reply_markup=valk3_mini_keyboard)
 
@dp.callback_query_handler(
	bot_callback.filter(item_name='valkelite'))
async def buying_gan(
	call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time=60)
	await call.message.answer(
		text='кубы категории  valk elite', 
		reply_markup=valk3_elite_keyboard)
	
# moyu
@dp.callback_query_handler(
	bot_callback.filter(item_name='moyu'))
async def buying_moyu(
	call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time=60)
	await call.message.answer(
		text='вот все возможные кубы фирмы Moyu',
		reply_markup=choice_moyu_category)
	
@dp.callback_query_handler(
	bot_callback.filter(item_name='moyuweilong'))
async def buying_gan(
		call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time=60)
	await call.message.answer(
		text='кубы категории Weilong', 
		reply_markup=moyuweilong_keyboard)
	
@dp.callback_query_handler(
	bot_callback.filter(item_name='moyuaolong'))
async def buying_gan(
	call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time=60)
	await call.message.answer(
		text='кубы категории aolong', 
		reply_markup=moyuaolong_keyboard)
	
@dp.callback_query_handler(
	bot_callback.filter(item_name='moyumf'))
async def buying_gan(
	call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time=60)
	await call.message.answer(
		text='кубы категории Cubing Classroom', 
		reply_markup=moyumf3_keyboard)
	
@dp.callback_query_handler(
	bot_callback.filter(item_name='moyugg'))
async def buying_gan(
	call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time=60)
	await call.message.answer(
		text='кубы категории GuoGuan', 
		reply_markup=moyugg_keyboard)
	
#отмена
@dp.callback_query_handler(text='cancel')
async def cancel_buying(call: CallbackQuery):
	await call.answer(
		'Покупка отменена', show_alert=True)
	await call.message.edit_reply_markup(
		reply_markup=None)
	
@dp.message_handler(Command('updates'))
async def updates_command(msg: Message):
	await msg.reply(text='v1.0.0. релиз бота')

@dp.message_handler(Command('help'))
async def help_command(msg: Message):
	await msg.answer(text='''
	это тестовый бот, который был сделан для 
	проверки моих знаний в создании ботов.
	
	Нажмите комманду ( /buy ) что бы выбрать куб. 
	Вы будете перемещены по ссылке в 
	cccstore.ru на выбранный вами куб
	
	Просьба отписать о багах мне в вк @speedcuber_sml
	
	для того, что бы узнать какие были обновления используйте комманду /updates
	
	версия бота: v1.0.0
	
	Удачного использования''')
#
#

if __name__ == '__main__':
  executor.start_polling(dp)
