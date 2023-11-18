
# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.
class ProfanityFilter:

    def __init__(self, keywords, template):
        self.keywords = keywords
        self.template = template

    def filter(self, msg):
        msg_words = msg.split()
        profane_indices = []

        for i, word in enumerate(msg_words):
            lower_word = word.lower()
            for bad_word in self.keywords:
                lower_bad_word = bad_word.lower()
                if len(lower_bad_word) > len(lower_word):
                    continue
                for j in range(len(lower_word) - len(lower_bad_word) + 1):
                    if lower_word[j:j + len(lower_bad_word)] == lower_bad_word:
                        profane_indices.append((i, j, j + len(lower_bad_word)))

        for i, start, end in profane_indices:
            replacement = ""
            template_idx = 0
            for _ in range(end - start):
                replacement += self.template[template_idx]
                template_idx = (template_idx + 1) % len(self.template)
            msg_words[i] = msg_words[i][:start] + replacement + msg_words[i][end:]

        return ' '.join(msg_words)

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["Duck", "duckling", "shot", "batch", "Mastard"], "?#$")
    offensive_msg = "abc defghi mAstardddd jklmno xxducklingk"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
