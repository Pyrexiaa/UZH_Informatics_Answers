import re

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def analyze(posts):
    pattern = r'#(?:[a-zA-Z][a-zA-Z0-9]*)'
    hashtags = []
    # Find all valid hashtags in the text
    for post in posts:
        valid_hashtags = re.findall(pattern, post)
        hashtags.extend(valid_hashtags)

    result_dict = {}
    
    for hashtag in hashtags:
        hashtag_ = hashtag[1:].strip()
        if hashtag_ not in result_dict:
            result_dict[hashtag_] = 1
        else:
            result_dict[hashtag_] += 1
    
    return result_dict


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = [
    "hi #weekend",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3"]
print(analyze(posts))
