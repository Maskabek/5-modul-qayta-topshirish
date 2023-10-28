from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.youtube.com/@pdpuz/videos')
    ttl = page.query_selector_all('#video-title')
    prsmtr=page.query_selector('.grid style-scope ytd-rich-grid-media')
    print(prsmtr)
    k=0

    print('Ohirgi 5 ta video title : ')
    for i in ttl[:5]:
        k+=1
        sty =""
        sty+=' '+str(k)+' :'
        sty+=str(i.text_content())
        print(sty)
    page.wait_for_timeout(10000)
