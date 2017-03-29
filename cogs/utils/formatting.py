def quote(msg: str):
    return msg.replace("`", "")

def cleanup_code(content):
    if content.startswith("```") and content.endswith("```"):
        output = content[3:-3].rstrip("\n").lstrip("\n")
        return output
    return content.strip("` \n")