def transcription_arn(brin_codant):
    arn = ""
    for c in brin_codant:
        if c == "T":
            arn += "U"
        else:
            arn += c
    return arn
