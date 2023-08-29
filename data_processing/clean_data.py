import csv
import re

def clean_text(text):
    return text

def clean_languages(text):
    languages = [lang.strip() for lang in text.replace("I speak", "").split(',')]
    return ', '.join(languages)

def clean_completed_amount(text):
    amount = text.split()[0]
    return amount

def clean_level(text):
    return text

def clean_reviews(text):
    reviews = text.split()[0]
    return reviews

def clean_star(text):
    star = text.replace("(","")
    star = star.replace(")", "")
    return star

def clean_pro(text):
    if text == 'N/A':
        return 0
    else:
        return 1

def extract_values(item):
    pattern = r'\+\d+\s*more'
    parts = item.split(':')
    if len(parts) > 1:
        value = parts[1].split('•')
        if len(value) > 1:
            return  re.sub(pattern, '', ', '.join(value))
        else:
            return  re.sub(pattern, '', parts[1])
    return ""

def clean_tags(text):
    tags = ', '.join(text.split('||')[1:])
    pattern = r',\s*\+\d+'
    tags = re.sub(pattern, '', tags)
    return tags

def clean_special_characters(text):
    cleaned_string = re.sub(r'[^\w\s]', '', text)
    return cleaned_string


cleaned_rows = []
with open('raw_data.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        programming_language = "N/A"
        expertise = "N/A"
        frontend_framework = "N/A"
        backend_framework = "N/A"
        if 'extra' in row:
            items = row['extra'].split('||')
            for item in items:
                if 'Programming language' in item:
                    programming_language = extract_values(item)
                elif 'Expertise' in item:
                    expertise = extract_values(item)
                elif 'Frontend framework' in item:
                    frontend_framework = extract_values(item)
                elif 'Backend framework' in item:
                    backend_framework = extract_values(item)
        cleaned_row = {
            'username': clean_text(row['username']),
            'location': clean_text(row['location']),
            'languages': clean_languages(row['languages']),
            'completed_amount': clean_completed_amount(row['completed_amount']),
            'title': clean_text(row['title']),
            'level': clean_level(row['level']),
            'rating_score': clean_text(row['rating_score']),
            'reviews': clean_reviews(row['reviews']),
            'collect_count': clean_text(row['collect_count']),
            'tags': clean_tags(row['tags']),
            'five_star': clean_star(row['five_star']),
            'four_star': clean_star(row['four_star']),
            'three_star': clean_star(row['three_star']),
            'two_star': clean_star(row['two_star']),
            'one_star': clean_star(row['one_star']),
            'pro': clean_pro(row['pro']),
            'description': clean_special_characters(row['description']),
            'about': clean_text(row['about']),
            'programming_language': programming_language,
            'expertise': expertise,
            'frontend_framework': frontend_framework,
            'backend_framework': backend_framework
        }
        cleaned_rows.append(cleaned_row)

fieldnames = ['username', 'location', 'languages', 'completed_amount', 'title', 'level',
              'rating_score', 'reviews', 'collect_count', 'tags', 'five_star', 'four_star',
              'three_star', 'two_star', 'one_star', 'pro', 'description', 'about', 'programming_language', 'expertise', 'frontend_framework', 'backend_framework']

with open('cleaned_output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_rows)

print("Cleaning and writing complete.")
