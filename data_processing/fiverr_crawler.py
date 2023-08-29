from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time
import random
import undetected_chromedriver as uc

def crawl_client_info(url, driver):
  # driver = webdriver.Chrome()

  driver.get(url)
  time.sleep(3)
  soup = BeautifulSoup(driver.page_source, 'html.parser')
  programing_languages = None
  frontend_framework = None
  backend_framework = None
  expertise = None
  try:
    username = soup.find('a', class_='zle7n023q zle7n023r zle7n01yu zle7n01yv zle7n015l zle7n013s zle7n08 zle7n02')
  except:
    username = None
  try:
    location = soup.find('p', class_='zle7n020u zle7n0151 zle7n0138 zle7n06 zle7n02')
  except:
    location = None
  try:
    languages = soup.find('span', class_='zle7n020u zle7n0151 zle7n0138 zle7n06 zle7n02')
  except:
    None
  try:
    completed_amount = soup.findAll('div', class_='zle7n0xe zle7n00 zle7n0ru zle7n01bu zle7n0115')[2]
  except:
    completed_amount = None
  try:
    title = soup.find('p', class_='zle7n020y zle7n0156 zle7n013d zle7n07 zle7n02')
  except:
    title = None
  try:
    level = soup.find('p', class_='zle7n020u zle7n0156 zle7n013d zle7n08 zle7n02')
  except:
    level = None

  more = soup.findAll('div', class_='zle7n0zr zle7n010g zle7n0xe zle7n00 zle7n01d3 zle7n0rz zle7n0115')
  extra = 'N/A' if len(more) <= 0 else ''
  for item in more:
    extra  = extra + '||' + item.text 


  # try:
  #   programing_languages = soup.findAll('div', class_='zle7n0zr zle7n010g zle7n0xe zle7n00 zle7n01d3 zle7n0rz zle7n0115')[0]
  # except:
  #   programing_languages = None
  # try:
  #   frontend_framework = soup.findAll('div', class_='zle7n0zr zle7n010g zle7n0xe zle7n00 zle7n01d3 zle7n0rz zle7n0115')[1]
  # except:
  #   frontend_framework = None
  # try:
  #   backend_framework = soup.findAll('div', class_='zle7n0zr zle7n010g zle7n0xe zle7n00 zle7n01d3 zle7n0rz zle7n0115')[2]
  # except:
  #   backend_framework = None
  
  
  crawled_tags = soup.findAll('div', class_='zle7n0k7 zle7n0mu zle7n0pc zle7n0hf zle7n00 zle7n021i zle7n0x4')
  tags = 'N/A' if len(crawled_tags) <= 0 else ''
  for item in crawled_tags:
    tags = tags + '||' + item.text

  try:
    about = soup.findAll('div', class_='zle7n0x9 zle7n00 zle7n0s9 zle7n01d3 zle7n0115')[2]
  except:
    about = None
  # rating_score = soup.find('b', class_='rating-score')
  # reviews = soup.find('span', class_='vUmzpwS')
  # five_star = soup.findAll('td', class_='star-num')[0]
  # four_star = soup.findAll('td', class_='star-num')[1]
  # three_star = soup.findAll('td', class_='star-num')[2]
  # two_star = soup.findAll('td', class_='star-num')[3]
  # one_star = soup.findAll('td', class_='star-num')[4]
  # collect_count = soup.find('span', class_='collect-count')
  # tags = soup.find('div', class_='zle7n010g zle7n0xe zle7n00 zle7n01d3 zle7n0rz zle7n0115')
  # pro = soup.find('div', class_='PnAdo9t')
  # description = soup.find('div', class_='zle7n0x9 zle7n00 zle7n0rz zle7n01d3 zle7n0115')

  rating_score = None
  reviews = None
  five_star = None
  four_star = None
  three_star = None
  two_star = None
  one_star = None
  collect_count = None
  pro = None
  description = None

  try:
    rating_score = soup.find('b', class_='rating-score')
  except:
    pass

  try:
    reviews = soup.find('span', class_='vUmzpwS')
  except:
    pass

  try:
    five_star = soup.findAll('td', class_='star-num')[0]
  except:
    pass

  try:
    four_star = soup.findAll('td', class_='star-num')[1]
  except:
    pass

  try:
    three_star = soup.findAll('td', class_='star-num')[2]
  except:
    pass

  try:
    two_star = soup.findAll('td', class_='star-num')[3]
  except:
    pass

  try:
    one_star = soup.findAll('td', class_='star-num')[4]
  except:
    pass

  try:
    collect_count = soup.find('span', class_='collect-count')
  except:
    pass

  # try:
  #   tags = soup.find('div', class_='zle7n010g zle7n0xe zle7n00 zle7n01d3 zle7n0rz zle7n0115')
  # except:
  #   pass

  try:
    pro = soup.find('div', class_='PnAdo9t')
  except:
    pass

  try:
    description = soup.findAll('div', class_='zle7n0x9 zle7n00 zle7n0rz zle7n01d3 zle7n0115')[1]
  except:
    pass

  client_info = {
    'username': 'N/A' if username is None else username.text,
    'location': 'N/A' if location is None else location.text,
    'languages': 'N/A' if languages is None else languages.text,
    'completed_amount': 'N/A' if completed_amount is None else completed_amount.text,
    'title': 'N/A' if title is None else title.text ,
    'level': 'N/A' if level is None else level.text,
    'rating_score': 'N/A' if rating_score is None else rating_score.text,
    'reviews': 'N/A' if reviews is None else reviews.text,
    'collect_count': 'N/A' if collect_count is None else collect_count.text,
    'tags': tags,
    'five_star': 'N/A' if five_star is None else five_star.text,
    'four_star': 'N/A' if four_star is None else four_star.text,
    'three_star': 'N/A' if three_star is None else three_star.text,
    'two_star': 'N/A' if two_star is None else two_star.text,
    'one_star': 'N/A' if one_star is None else one_star.text,
    'pro': 'N/A' if pro is None else pro.text,
    'description': 'N/A' if description is None else description.text,
    'about': 'N/A' if about is None else about.text,
    # 'expertise': 'N/A' if expertise is None else expertise.text,
    'extra': extra,
  }
  # driver.quit()
  return client_info

def main():
  client_urls = [
  'https://www.fiverr.com//samridhsrivasta/create-python-bots-scripts-automate-jobs?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=1&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=5c283248-6a93-4178-a7f0-85848ee124dd', 'https://www.fiverr.com//ossamaben/create-a-custom-perfex-crm-module-and-fix-bugs?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=2&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=8c9376fb-0357-4b86-a6bf-6534c8c95a24', 'https://www.fiverr.com//hanmaslah/create-a-fully-functioning-web-application-from-scatch?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=3&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=64d5e65b-7fa8-429b-b3b7-9c3eae386b30', 'https://www.fiverr.com//bilalraza517/develop-upgrade-fix-your-php-laravel-wordpress-website?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=4&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=47dc0dc1-557e-4058-adc4-33e6ed711ce9', 'https://www.fiverr.com//hassanbintariq6/do-your-c-cpp-codes-for-just-5-dollars?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=5&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=fd7847c3-7f4f-431b-b321-e54fb8c3310a', 'https://www.fiverr.com//heyevgenii/write-after-effects-script-or-expression?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=6&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=f621baa3-a868-4207-8193-c61fa1fdeca5', 'https://www.fiverr.com//bugxsols/create-customize-and-fix-modules-for-you?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=7&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=42a8ca5c-4c38-48f4-af3b-1c2eebda4f0a', 'https://www.fiverr.com//fixkit/develop-python-django-web-application-professionally?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=8&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=7388b6e4-955d-4b88-854f-fccfd3d4834a', 'https://www.fiverr.com//spirinn/create-desktop-wpf-forms-app-using-c-sharp?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=9&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=ba1b737f-f5b9-4372-8ed1-0b1ee90e32ed', 'https://www.fiverr.com//nitinrungta/do-ui-ux-design-website-software-app-development?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=10&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=9f4b5258-c6dc-454f-9404-945a6d27af58', 'https://www.fiverr.com//star_works07/do-figma-to-nextjs?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=11&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=14894e1c-adb0-4481-9c0d-0cfb01d29103', 'https://www.fiverr.com//bichralaoui/scrap-extract-data-and-automize-tasks-for-you?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=12&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=00fe9a7c-dad1-48c2-9302-8657071940ad', 'https://www.fiverr.com//fahadnaeem424/create-desktop-application-using-c-sharp-with-dot-net?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=13&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=8e6cc2f4-e9d9-454d-aa34-fb27160296f8', 'https://www.fiverr.com//yasirkhewa/convert-psd-to-html-with-fully-responsive?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=14&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=68e034d3-a926-44bb-91e9-19218d6945ab', 'https://www.fiverr.com//haseebbutt99/create-shopify-app-for-you-using-laravel?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=15&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=0ab01980-f1a3-4057-a2b2-d0c263587046', 'https://www.fiverr.com//mmhamzap10/do-your-c-sharp-java-python-programming-assignments-or-projects?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=16&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=83ffeec1-284b-4ffd-8fb8-9164a7f4e169', 'https://www.fiverr.com//kasperandersen/take-care-of-your-html-css-and-php-problems?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=17&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=284a23b1-399a-4c62-b44d-934e7ee1457a', 'https://www.fiverr.com//rishidevkota164/do-golang-api-and-projects?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=18&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=8707846c-9114-4831-8af8-36a5a8184ab9', 'https://www.fiverr.com//omnixoft/web-developer-php-laravel-codeigniter-website-design-website-development-bug-fix?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=19&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=4b8fbfe5-1dd4-48ac-aa78-2dc1dd09ef71', 'https://www.fiverr.com//takenthumbnail/create-a-cross-platform-desktop-app?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=20&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=b1b01447-ec4f-42e0-95d5-583ca6ae3aa0', 'https://www.fiverr.com//fahadshah04/do-any-python-related-projects-for-you?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=21&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=a506f370-7fed-4bba-bcb8-cef68af36ebb', 'https://www.fiverr.com//nsoftwaredev/do-both-frontend-and-backend-for-professional-website?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=22&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=febb631b-1863-416a-ae1c-4f46d72eccd8', 'https://www.fiverr.com//ahmedmaz/make-web-apps-using-react-nextjs-nodejs-or-any-other-backend?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=23&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=3caf22e2-5ce5-447d-9d8a-b400c1d02b6e', 'https://www.fiverr.com//adityaprem/make-webapp-website-in-react-js?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=24&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=f1296588-c461-48b6-a2c2-a471d906f0ad', 'https://www.fiverr.com//mohdhasnainn/create-custom-web-calculator-using-javascript?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=25&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=29f5fd6c-0403-4ed8-8bb3-515c330cd868', 'https://www.fiverr.com//sanaver786/develop-your-web-app-in-react-js-with-material-ui?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=26&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=a590eb34-ecb9-465d-a8e2-12046bfb28f2', 'https://www.fiverr.com//webit_791/convert-figma-xd-psd-to-react-js-as-a-react-developer?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=27&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&seller_online=true&imp_id=ae9de983-db5f-4469-8db5-19336f6f71c1', 'https://www.fiverr.com//dev_sohan/develop-your-next-js-web-app?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=28&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=87fc3260-4cf2-4fe4-b30f-88703a68add5', 'https://www.fiverr.com//jrartech/fix-bugs-develop-and-upgrade-laravel?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=29&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=46035626-be65-4961-89b1-9a857f4f3933', 'https://www.fiverr.com//creativecolumn/develop-bot-for-automate-your-heavy-and-bulk-tasks?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=30&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=937ace9f-3378-4d4b-b079-35d277cdfc30', 'https://www.fiverr.com//shanavasindia/convert-psd-to-bootstrap?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=31&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=2933f17a-7ead-48b8-b7bb-7f379c14e84e', 'https://www.fiverr.com//chamithdw/do-odoo-erp-services?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=32&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=e1674be4-f198-4080-aaab-17415844785c', 'https://www.fiverr.com//teh_developer/design-a-php-website-for-you?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=33&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=41ffff8d-87fd-41b3-b3bd-29944634910f', 'https://www.fiverr.com//abhijitk260/chrome-firefox-opera-any-browser-extension-add-ons?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=34&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=e2dfd93c-7025-47e7-a85d-58519da06b09', 'https://www.fiverr.com//khbuilder/make-a-perfect-web-app-in-reactjs-and-redux?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=35&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=96098ccd-e786-455c-b23f-d23df43ed899', 'https://www.fiverr.com//sameermallah911/add-new-features-apis-in-wowonder-playtube-quickdate?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=36&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=780a458c-a036-42b8-8b59-dbde4cbad23f', 'https://www.fiverr.com//muneeb_ahmad_ch/make-python-project-gui-algorithm-and-programming?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=37&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=c8d54f7c-a11f-42d3-a0f1-f96c2ccf21fc', 'https://www.fiverr.com//anaghchaubey/be-python-django-flask-web-app-full-stack-web-developer?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=38&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=e162e0fb-1982-4519-912c-e2b00c7124a9', 'https://www.fiverr.com//victortomoloju/create-your-c-cpp-and-c-sharp-programs?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=39&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=9d17fd2d-8695-4f80-8b31-a171ac906abe', 'https://www.fiverr.com//mbshehzad/deploy-node-js-app-to-heroku?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=40&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=a885be9a-b8a1-4ab4-9825-0333bdeec510', 'https://www.fiverr.com//ifrahshahid_dev/be-your-django-or-python-flask-full-stack-web-developer?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=41&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=3883421f-a67f-418d-aa1a-3cca87c1f74e', 'https://www.fiverr.com//sohaibnoyyan19/be-your-php-laravel-developer-and-bug-fixer?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=42&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=f05d6f62-6f26-4c14-a78b-3ef0f10af58a', 'https://www.fiverr.com//miiiks/build-a-custom-app-using-microsoft-powerapps-and-power-automate?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=43&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=7666a214-63bf-4ad0-9e42-2be3a951fd1f', 'https://www.fiverr.com//a_selmani/convert-psd-to-html-xd-to-html-figma-to-html-sketch-to-html-css?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=44&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&seller_online=true&imp_id=6ab57d97-9c41-4f25-9acb-1a3534911bf3', 'https://www.fiverr.com//fatehmuhammad36/do-python-programming-task-project-and-guide-you-in-assignment?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=45&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=57af513b-6dbf-4f4e-9ff5-343c3208de5f', 'https://www.fiverr.com//farhan687/develop-php-laravel-websites-and-apps-or-build-api-backend-and-fix-errors?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=46&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=88b5aa15-6d2c-424f-bafc-5954113c3edc', 'https://www.fiverr.com//pythoniantips/install-configure-and-make-custom-odoo-modules?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=47&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=6b4784d1-6d0f-4b10-a6ed-62a5b3910937', 'https://www.fiverr.com//mohsan_mustafa/fix-errors-bugs-in-html-css-bootstrap-js-jquery-laravel-php-mysql-vuejs?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=cdf7c7fe0dc2a02f2366c1bef0b95aef&pckg_id=1&pos=48&context_type=rating&funnel=cdf7c7fe0dc2a02f2366c1bef0b95aef&imp_id=7ef18f9c-3fd4-429d-b92d-ba1d069714fa',
  'https://www.fiverr.com//basir1937/develop-or-fix-reactjs-nodejs-typescript-javascript?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=1&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=25e32127-a2d5-4b80-b4f3-9403cb4010ce', 'https://www.fiverr.com//kjaved8/make-metatrader-custom-programs?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=2&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=1e096ab4-7da2-456b-974e-ba4509c8a87b', 'https://www.fiverr.com//iamsulok/create-or-fix-script-for-google-sheets-automation?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=3&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=5e110b4d-f425-4889-9e32-8b28946660fb', 'https://www.fiverr.com//h_kalathiya/customize-high-level-of-code-in-wordpress?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=4&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=ae6e8fd9-5115-4adc-ae49-9a182926bb57', 'https://www.fiverr.com//pranjalk2902/transform-raw-data-into-custom-format-output-using-excel-vba-macros?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=5&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=0b73dfd6-68ba-4a86-92a1-e9eaffc45202', 'https://www.fiverr.com//sohailsultan/create-web-app-or-website-in-react-js-mongodb-next-js-express-node-and-redux?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=6&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=ee4df892-cc6a-4edb-96cf-011807d666da', 'https://www.fiverr.com//jpst00/code-you-a-quality-java-program?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=7&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=37f7cbb3-4246-49ab-876f-931179b5c77a', 'https://www.fiverr.com//mahzaib_mirza/be-your-chrome-extension-developer?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=8&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=bf18be26-0476-48b5-9e69-e3b98a8eb38c', 'https://www.fiverr.com//dhia_eddine_ben/develop-a-custom-website-using-html-css-and-javascript?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=9&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=048727c9-9f13-4636-b159-2dc08094aad4', 'https://www.fiverr.com//deemehfooz/develop-your-web-backend-using-django-bootstrap-and-postgresql?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=10&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=e71cee20-4479-4e9a-a2f4-4f13a6133b29', 'https://www.fiverr.com//codestorms/work-on-vtiger-crm?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=11&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=cb3334c2-45b6-470b-ba66-2deb9ef37ee5', 'https://www.fiverr.com//moaz_2303/do-web-development-using-mern-stack-or-be-your-mern-stack-web-developer?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=12&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=b3ddf5b0-1096-4bf2-aba0-05a770e16a9b', 'https://www.fiverr.com//softexprt92/add-stripe-or-paypal-payment-in-your-website?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=13&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=4b63e0c5-2903-42d2-bf67-d4f1ecafa374', 'https://www.fiverr.com//nzhr75/develop-your-website-with-php-laravel?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=14&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=3720f02c-c12c-4054-8e2c-6c9ce4ad6959', 'https://www.fiverr.com//shah_jalal_jr/convert-psd-xd-to-html-responsive?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=15&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=88d1eb71-c20e-4b27-a213-2e91985c62d7', 'https://www.fiverr.com//samridhsrivasta/do-python-web-scraping-and-automation?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=16&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=d7b4f39e-8009-414b-8e65-4c81f9044145', 'https://www.fiverr.com//smshahnawazz/design-website-with-html-css-and-bootstrap?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=17&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=fb7c9890-f262-4a08-b229-196adc0da0c9', 'https://www.fiverr.com//muhemmed_usama/create-photoshop-script-based-on-user-interface?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=18&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=ae23038a-a6ca-419e-bd84-e1c36f123fb8', 'https://www.fiverr.com//mohammedibra583/create-some-new-application?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=19&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=b10c5007-1b5f-4e20-8762-335bbd899d98', 'https://www.fiverr.com//ali_dev_code/design-responsive-website-with-html-css-bootstrap-1674?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=20&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=2db9985e-606c-4eb8-93f0-10578cb9033f', 'https://www.fiverr.com//ae_fiverr/do-any-custom-chrome-automation-tasks?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=21&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=1f804394-4556-4843-b1a8-90531cb4f1dd', 'https://www.fiverr.com//sumanfiverr/automate-your-google-sheet-using-app-script?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=22&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=af26e4b6-da89-4fc1-8726-7bea90762e6d', 'https://www.fiverr.com//developer_forum/be-an-expert-full-stack-developer-using-react-js-next-js-mern?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=23&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=543e5f78-9c41-47b7-917e-883202fbf4cc', 'https://www.fiverr.com//adiraimaji/make-after-effects-script-that-will-automate-your-workflow?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=24&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=a24429a0-f8c9-40bb-8483-dae0350343e1', 'https://www.fiverr.com//eyalchen/create-troubleshoot-and-help-with-your-psychopy-experiment?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=25&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=75c84c00-de21-485a-919c-78ad90d09dc0', 'https://www.fiverr.com//hemalathakk/develop-web-apps-in-spring-boot-react-js-and-jsp?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=26&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=e25fbf4a-b119-4fcb-aea4-1fe75e65dbda', 'https://www.fiverr.com//christoffel16/create-scripts-to-automate-a-lot-of-things-with-python?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=27&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=2a11e430-a0ff-4cbe-bd34-97cff40d2e27', 'https://www.fiverr.com//victortomoloju/build-a-custom-windows-desktop-application?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=28&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=67f5074f-28f6-488e-9a3f-762742b21d2b', 'https://www.fiverr.com//jazz365/be-your-full-stack-python-django-developer?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=29&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=abe11043-e39f-4cae-8a21-1d31ba9653e5', 'https://www.fiverr.com//jahanzaibbabar3/code-python-projects-assignments-flask-web-app-scraping-automation?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=30&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=1859881b-5150-4389-901c-1dddd0de88d6', 'https://www.fiverr.com//abkale/do-html-css-javascript-cpp-python-java-projects?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=31&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&seller_online=true&imp_id=7fc2bd5b-5507-4dcf-b717-a57fbe61bb2f', 'https://www.fiverr.com//vishwas_chandra/do-matlab-and-python-coding?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=32&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=34ff85b2-806c-46e7-abf4-c41fb8a53d1d', 'https://www.fiverr.com//naim1337/build-and-deploy-nextjs-strapi-full-stack-website-and-connect-sanity-with-nextjs?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=33&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=b4663597-ce70-4d33-80e3-7f54fb1b412f', 'https://www.fiverr.com//marratainwd/do-psd-to-html-xd-to-html-responsive-bootstrap-4?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=34&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&seller_online=true&imp_id=bc2de236-5c5b-4f93-9342-1191bbc31ca4', 'https://www.fiverr.com//abdullah_iqbal7/be-your-front-end-web-developer-angular-bootstrap-react-html-material-wordpress?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=35&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=b187a0c4-8c19-4d1e-9cb3-712156c5edc7', 'https://www.fiverr.com//bmtmadushanka/php-laravel-web-developer?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=36&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=b6155578-b224-42ba-8c97-5fe5efbb5bd7', 'https://www.fiverr.com//itsphpdev/develop-laravel-codeigniter-vuejs-yii2-web-applications?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=37&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=7919414e-3897-4096-b4f5-6eefc3914cc3', 'https://www.fiverr.com//podionatics/help-you-in-your-podio-globiflow-requirements?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=38&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=25bfbff4-1e4c-4907-9acd-ba078adc6629', 'https://www.fiverr.com//jawadkhan760/develop-your-desktop-software-desktop-application-custom-app?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=39&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=7050aab1-82fb-46d1-87b8-4da6a4e4394d', 'https://www.fiverr.com//shuaib_khalid/be-your-frontend-angular-developer?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=40&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=f2734d3b-3285-412f-86ac-e8558658cc6f', 'https://www.fiverr.com//vishalsundrani/do-oop-data-structure-and-data-base-in-java-cpp-python-projects?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=41&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=16a17546-8856-4c1b-8bcd-96f2f968b446', 'https://www.fiverr.com//ojasya007/fix-any-html-css-or-js-issues?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=42&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=083df748-43d5-4ad0-8839-4f3a54ea77f9', 'https://www.fiverr.com//coder_expert121/write-any-script-in-html-css-php-python-javascript-jquery?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=43&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&seller_online=true&imp_id=b4c3a439-f508-4d1c-a6cf-e7ed6839d2f2', 'https://www.fiverr.com//bilalasif956/add-localization-in-your-react-website-using-i18n?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=44&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=df01c847-41e2-4cbb-b324-7b1e81448a3c', 'https://www.fiverr.com//ibraboumedian/design-responsive-website-in-css-flexbox-and-grid?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=45&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=624530ce-dbad-4b84-b178-f4a2d194aa54', 'https://www.fiverr.com//phpcraze/do-any-mvc-work-codeignite-laravel-yii-kohana?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=46&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=15b1e89f-f70e-4156-ac32-87b006069d27', 'https://www.fiverr.com//shubhpokhriyal/create-a-custom-web-application-with-php-laravel-and-mysql?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=47&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=fcaa841d-3b26-4955-8241-9cc30539dac8', 'https://www.fiverr.com//walayatkhan/create-web-application-in-bootstrap-javascript-jquery-php-and-mysql?context_referrer=subcategory_listing&source=pagination&ref_ctx_id=ebca314e0a2624bf5228bb8e7fb17305&pckg_id=1&pos=48&context_type=rating&funnel=ebca314e0a2624bf5228bb8e7fb17305&imp_id=49f8a662-ca6a-4fb9-ab08-2723a2c6db56'
  
  ]
  client_info_list = []
  options = webdriver.ChromeOptions()
  options.add_argument('--headless')
  # driver = webdriver.Chrome(options=options)
  # driver = webdriver.Chrome()
  driver = uc.Chrome()
  for client_url in client_urls:
    client_info = crawl_client_info(client_url, driver)
    client_info_list.append(client_info)
    # time.sleep(5)
  driver.quit()
  csv_file_path = 'client_info.csv'

# List of keys for the CSV header
  csv_header = list(client_info_list[0].keys())  # Assuming all dictionaries have the same keys

  # Write the CSV file
  with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
      writer = csv.DictWriter(csv_file, fieldnames=csv_header)
      writer.writeheader()  # Write the header

      for client_info in client_info_list:
          writer.writerow(client_info)  
  print(client_info_list)

if __name__ == '__main__':
  main()
