import asyncio
from pyppeteer import launch

async def main(search):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(f'https://dle.rae.es/{search}?m=form')
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')
    await page.waitForSelector('#resultados')

    existe = await page.querySelector('header.f')
    existe2 = await page.querySelector('div.otras') 
    if (existe or existe2):
        return True
    else:
        return False

    








