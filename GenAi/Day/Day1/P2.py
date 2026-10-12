#function:
def build_prompt(topic:str,word_limit:int=150)->str:
    return f"write about {topic},with atmost{word_limit}word"

print(build_prompt("gen ai"))
print(build_prompt("prompt eng",word_limit=200))

# brushup 
#*args ,**kwargs
#list comprehension,dict comprehension