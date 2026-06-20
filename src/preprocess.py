import pandas as pd
import re


def clean_text(text):

    text = str(text)

    # lowercase
    text = text.lower()

    # remove urls
    text = re.sub(
        r"http\S+",
        "",
        text
    )

    # remove special characters
    text = re.sub(
        r"[^a-zA-Z\s]",
        "",
        text
    )

    # remove extra spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()



def preprocess(input_file, output_file):

    df = pd.read_csv(input_file)


    # remove duplicates
    df = df.drop_duplicates()


    # remove empty articles
    df = df.dropna(
        subset=["Article Text"]
    )


    # clean article text
    df["clean_text"] = (
        df["Article Text"]
        .apply(clean_text)
    )


    df.to_csv(
        output_file,
        index=False
    )


    print(
        "Logistics data preprocessing completed"
    )

