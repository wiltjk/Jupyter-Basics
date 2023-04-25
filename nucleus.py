# update or install the necessary libraries
# pip install --upgrade openai
# pip install --upgrade langchain
# pip install --upgrade python-dotenv

import openai
import os

from langchain.llms import OpenAI
from dotenv import load_dotenv

# Pull out environment variables for API config & set LangChain env
load_dotenv()
OAIkey    = os.getenv("OPENAI_API_KEY")
# print (f"OPENAI_API_KEY='{OAIkey}'\n")

# os.environ["OPENAI_API_KEY"] = OAIkey

# Set Open AI parameters...
def setOpenAIparams (
    model             = "text-davinci-003",
    max_tokens        = 256,
    temperature       = 0.7,
    n                 = 1,
    frequency_penalty = 0,
    presence_penalty  = 0 ):
 
    openai_params = {}    

    openai_params['model']             = model
    openai_params['max_tokens']        = max_tokens
    openai_params['temperature']       = temperature
    openai_params['n']                 = n
    openai_params['frequency_penalty'] = frequency_penalty
    openai_params['presence_penalty']  = presence_penalty
    return openai_params

# Get Open AI completion... 
def getOpenAIcompletion(params, top_p, prompt):
    
    openai.api_key = OAIkey
    response       = openai.Completion.create (
        engine            = params['model'],
        prompt            = prompt,
        temperature       = params['temperature'],
        max_tokens        = params['max_tokens'],
        top_p             = top_p,
        n                 = params['n'],
        frequency_penalty = params['frequency_penalty'],
        presence_penalty  = params['presence_penalty'] )
    return response
    
# Test Open AI
def testOpenAI ():
    
    yourInput  = ''
    top_ps     = [0.1, 0.5, 1.0]
    params     = setOpenAIparams ()
    
    # Solicit input until it is correct.
    while(yourInput == ''):
    	yourInput = input("\nEnter an Open AI request ---> ")
    
    # Display response(s)
    print ("\nNucleus Responses\n")
       
    for tp in top_ps:
        #  Get a response from Open AI
        try:
            response = getOpenAIcompletion(params, tp, yourInput)
            # print (response.choices)
            
        except Exception as err:
            print(f"\n\n*** Unexpected Error ***\n\n{err=}\n\n{type(err)=}")
            return
    
        responseText = response.choices[0].text
        print (f"\nNucleus {tp} is: {responseText}\n\n")   
    return
    
# Main
if __name__ == "__main__":
    print ("\n\n—BOJ—\n\n")
    testOpenAI ()
    print ("\n\n—EOJ—\n\n")
    