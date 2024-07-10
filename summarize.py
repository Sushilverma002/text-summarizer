import click;
from transformers import pipeline;

summarizer = pipeline("summarization")

@click.command()
@click.option("--text","-t", required=False, help="Please write your input text to summarize")
@click.option("--file","-f", type=click.File('r')   , required=False, help="Please input your text file to summarize")

def summarize(text, file):

    if(file):
        text = file.read()
    
    if(text):
        summary =  summarizer(text,max_length= 150,min_length= 30, do_sample= False)
        print("\n summary: \n",summary[0]['summary_text'])
    else:
        print("Please provide either text or a file to summarize.")

if __name__ == '__main__':
    summarize()