import sys
import nltk

class RhymeThyme(object):

    def rhyme_thyme(self, word): 
        entries = nltk.corpus.cmudict.entries()
        syllables = [(inp, syl) for inp, syl in entries if inp == word]
        level = 2
        rhymes = []
        for (inp, syllable) in syllables:
            rhymes += [inp for inp, pron in entries if pron[-level:] == syllable[-level:]]
        # TODO: Remove the below comments...
		#answers = list(set(rhymes))[0:5] #Five answers
        #output = [] 
        #for i in range(len(answers)):
            #output.append(str(answers[i]))
        if len(list(set(rhymes))) > 1:
            answers = list(set(rhymes))[0] #One answer
            output = str(answers)
        else:
            answers = 'Failed to find rhyming word..'
            output = str(answers)
        return output
        #return 'Thyme\n'

    def input_from_user(self):
        # Input word
        version_info = sys.version_info[:2]
        using_python_v3 = version_info[0] == 3
        out_str = 'Input word:   '
        word = input(out_str) if using_python_v3 else raw_input(out_str)
        return word

    def output_to_user(self, word):
        # Output word to user
        text = 'Rhyming word:  ' + word
        print(text)
        return text

    def print_welcome_text(self):
        text = "Welcome to Rhyme Thyme - the awesome rhyming time. \n"
        print(text)
        return text

    def print_goodbye_text(self):
        text = "Goodbye!\n" 
        print(text)
        return text

    def __init__(self):
        self.print_welcome_text()
        word = self.input_from_user()
        rhyming_word = self.rhyme_thyme(word)
        #for i in range(len(rhyming_word)):
            #self.output_to_user(rhyming_word[i])
        self.output_to_user(rhyming_word)

if __name__ == '__main__':
    RhymeThyme()
