import pandas as pd
import json

from dotenv import load_dotenv

from llm_extractor import extract_risk


load_dotenv()



df = pd.read_csv(
    "data/labeled_logistics_news.csv"
)


df = df.head(5)
results=[]



for index,row in df.iterrows():

    print(
        "Processing:",
        index
    )


    output = extract_risk(
    row["clean_text"]
)


# handle list response from Gemini
    if isinstance(output, list):

        output = output[0]



    output["text"] = row["clean_text"]


    results.append(output)



with open(
    "outputs/llm_risk_results.json",
    "w"
) as f:


    json.dump(
        results,
        f,
        indent=4
    )



print(
    "LLM extraction completed"
)