import os
from dotenv import load_dotenv
import aiohttp

# Environment variable 
load_dotenv()
HF_TOKEN = os.environ.get('HUGGINGFACEHUB_API_TOKEN')

def get_language_code(language):
    normalized_language = ' '.join(word.capitalize() for word in language.strip().split())

    language_codes = {
        'Arabic': 'ar_AR',
        'Czech': 'cs_CZ',
        'German': 'de_DE',
        'English': 'en_XX',
        'Spanish': 'es_XX',
        'Estonian': 'et_EE',
        'Finnish': 'fi_FI',
        'French': 'fr_XX',
        'Gujarati': 'gu_IN',
        'Hindi': 'hi_IN',
        'Italian': 'it_IT',
        'Japanese': 'ja_XX',
        'Kazakh': 'kk_KZ',
        'Korean': 'ko_KR',
        'Lithuanian': 'lt_LT',
        'Latvian': 'lv_LV',
        'Burmese': 'my_MM',
        'Nepali': 'ne_NP',
        'Dutch': 'nl_XX',
        'Romanian': 'ro_RO',
        'Russian': 'ru_RU',
        'Sinhala': 'si_LK',
        'Turkish': 'tr_TR',
        'Vietnamese': 'vi_VN',
        'Chinese': 'zh_CN',
        'Afrikaans': 'af_ZA',
        'Azerbaijani': 'az_AZ',
        'Bengali': 'bn_IN',
        'Persian': 'fa_IR',
        'Hebrew': 'he_IL',
        'Croatian': 'hr_HR',
        'Indonesian': 'id_ID',
        'Georgian': 'ka_GE',
        'Khmer': 'km_KH',
        'Macedonian': 'mk_MK',
        'Malayalam': 'ml_IN',
        'Mongolian': 'mn_MN',
        'Marathi': 'mr_IN',
        'Polish': 'pl_PL',
        'Pashto': 'ps_AF',
        'Portuguese': 'pt_XX',
        'Swedish': 'sv_SE',
        'Swahili': 'sw_KE',
        'Tamil': 'ta_IN',
        'Telugu': 'te_IN',
        'Thai': 'th_TH',
        'Tagalog': 'tl_XX',
        'Ukrainian': 'uk_UA',
        'Urdu': 'ur_PK',
        'Xhosa': 'xh_ZA',
        'Galician': 'gl_ES',
        'Slovene': 'sl_SI'
    }
    
    return language_codes.get(normalized_language, 'wrong')


def transform_text(text):
    sentences = text.split('.')
    line = sentences[0] + '.'
    return line


def save_to_file(text, default_filename):
    user_choice = input(f"Do you want to save the result to '{default_filename}'? (y/n): ").strip().lower()
    
    if user_choice == 'y':
        filename = input("Enter the file name (leave blank for default): ").strip()
        if not filename:
            filename = default_filename
        
        try:
            with open(filename, 'a+', encoding='utf-8') as file:
                file.write(text)
            print(f"Result saved to '{filename}'.")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")
    else:
        print("Result not saved.")



async def summarize_text(text):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"https://api-inference.huggingface.co/models/facebook/bart-large-cnn",
            headers={"Authorization": f"Bearer {HF_TOKEN}"},
            json={"inputs": text,  "options" : {"wait_for_model": True}}
        ) as response:
            result = await response.json()
            if result[0]['summary_text']:
                return result[0]['summary_text']
            else:
                return f"Something went wrong!! response : {result}"
        


async def translate_text(text, target_language):

    target_language_code = get_language_code(target_language)

    if target_language_code == 'wrong':
        return "Invalid target language or Target language not found!  Please try again."

    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-many-mmt",
            headers={"Authorization": f"Bearer {HF_TOKEN}"},
            json={"inputs": text, "parameters": {"src_lang": "en_XX", "tgt_lang": target_language_code}, "options" : {"wait_for_model": True}}
        ) as response:
            result = await response.json()
            if result[0]['translation_text']:
                return result[0]['translation_text']
            else:
                return f"Something went wrong!! response : {result}"
        


async def expand_text(text):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3",
            headers={"Authorization": f"Bearer {HF_TOKEN}"},
            json={"inputs": text, "options" : {"wait_for_model": True}}
        ) as response:
            result = await response.json()
            if result[0]['generated_text']:
                expanded_Result = transform_text(result[0]['generated_text'])
                return expanded_Result
            else:
                return f"Something went wrong!! response : {result}"
        


async def fact_check_text(fact):
    text = f"Is this true? {fact}"
    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3",
            headers={"Authorization": f"Bearer {HF_TOKEN}"},
            json={"inputs": text, "options" : {"wait_for_model": True}}
        ) as response:
            result = await response.json()
            if result[0]['generated_text']:
                return result[0]['generated_text']
            else:
                return f"Something went wrong!! response : {result}"
