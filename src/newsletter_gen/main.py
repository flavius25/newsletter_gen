#!/usr/bin/env python
from newsletter_gen.crew import NewsletterGenCrew

def load_html_template(): 
    # with open('config/newsletter_template.html', 'r') as file: # for debug
    with open('src/newsletter_gen/config/newsletter_template.html', 'r') as file:
        html_template = file.read()
        
    return html_template


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    # inputs = {
    #     'topic': input('Enter the topic for your newsletter: '),
    #     'personal_message': input('Enter a personal message for your newsletter: '),
    #     'html_template': load_html_template()
    # }
    inputs = {
        'topic': "Multi-agent AI systems",
        'personal_message': "Hello, here is the news from boogEYnewsletter!",
        'html_template': load_html_template()
    }
    NewsletterGenCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()