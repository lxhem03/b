nsfw_keywords = {
    "general": [
        "pr0n", "s3x", "n00d", "fck", "bj", "hj", "l33t", "p0rn", "h3ntai", "h-ntai", "pnwh",
        "p0rnhwa", "l33tsp34k", "l3wd", "cultur3d", "s3xual"
    ],
    "hentai": [
        "pr0n", "s3x", "n00d", "fck", "bj", "hj", "l33t", "p0rn", "h3ntai", "h-ntai", "pnwh",
        "p0rnhwa", "l33tsp34k", "l3wd", "cultur3d", "s3xual"
    ],
    "abbreviations": [
        "pr0n", "s3x", "n00d", "fck", "bj", "hj", "l33t", "p0rn", "h3ntai", "h-ntai", "pnwh",
        "p0rnhwa", "l33tsp34k", "l3wd", "cultur3d", "s3xual"
    ],
    "offensive_slang": [
        "pr0n", "s3x", "n00d", "fck", "bj", "hj", "l33t", "p0rn", "h3ntai", "h-ntai", "pnwh",
        "p0rnhwa", "l33tsp34k", "l3wd", "cultur3d", "s3xual"
    ]
}

exception_keywords = ["nxivm", "classroom", "assassination", "geass"]

async def check_anti_nsfw(new_name, message):
    lower_name = new_name.lower()
    for keyword in exception_keywords:
        if keyword.lower() in lower_name:
            return False
    
    for category, keywords in nsfw_keywords.items():
        for keyword in keywords:
            if keyword.lower() in lower_name:
                await message.reply_text("You can't rename files with NSFW content.")
                return True
    return False
