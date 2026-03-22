from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model = ChatOpenAI(model="gpt-5-mini")

class Reviews(TypedDict):
    summary: Annotated[str,"a brief summary of the review"]
    sentiment: Annotated[str,"return sentiment of the review either negative, positive or neutral"]

structured_model = model.with_structured_output(Reviews)

result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-istalled apps that i cant remove.
                      Also, the UI looks outdated compared to other brands. Hoping for software update to fix this""")

print(type(result))
print(result)
print(result['summary'])
print(result['sentiment'])

