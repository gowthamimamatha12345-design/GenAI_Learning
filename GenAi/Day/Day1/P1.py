print("hlo")
# variables
#type hint
model_name:str="gemini-2.0"
temp:float=0.7#float
max_token:int =2345 # int
content_box: strNone= None #none
print(type(model_name))

#string immutable | string fromat
#older version 
name="llm"
score=9.8
print("hello  %s"  %name)
print("score %.2f" %score)
 #f-string (py 3.6+)
print(f"hello{name}")
print(f"score:{score:.1f}")
 #expression inside f-string
world_limit=200
print(f"{'over' if world_limit> 150 else 'under'} limit")
data ={"topic":"rag"}
print(f"Topic:{data['topic']}")

 # format specifiers
pi= 3.14159
print(f"{pi:.2f}")

#debugging =
temp=0.5
print(f"{temp=}")
#mulit -line -f-string format
user_input = "what is Langchain?"
context_text = "Langchain is a framework for building applications with LLMs."
system_prompt = f"""you are a helpful assistant.
context provided: {context_text}
student question: {user_input}
Instructions:
-answer based only on the context above 
-if the answer is not in the context, say "I don't know"
-keep your answers under 3 sentences
""".strip() # remove leading and trailing whitespace
print(system_prompt)

#lists:ordered,mutable,hertogenenous sequences
# IN gen AI:chat history,chunks of retrived documents
#token sequencesa 
chat_history:list[dict]=[
    {"role":"user","content":"what is an LLM?"},
    {"role":"assistant","content":"A LLM is a neural network model trained on large amounts of text."}, 
]
# Acess
first_msg = chat_history[0]
print(first_msg) 
print(chat_history[-1]['content']) # last element in the list
#modify
chat_history.append({"role":"user","content":"what is a rag"})
print(chat_history)
chat_history.pop(0)
print(chat_history)

#Itreate
for msg in chat_history:
    print(f"{msg['role'].upper()}:{msg['content']}")
#list of doucument chunks
chunks:list[str]=[
    "rag stands for retreival augmented generation",
    "it combian a retreiver with a generator",
]   

# filter chunks based on length
valid_chnuks= [c for c in chunks if len(c.split())>=6]
print(valid_chnuks)