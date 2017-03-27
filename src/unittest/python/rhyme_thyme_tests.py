import unittest

from rhyme_thyme import RhymeThyme

class test_rhyme_thyme(unittest.TestCase):

    def test_rhyme_thyme(self):
        self.assertEqual(RhymeThyme.rhyme_thyme(self,'abcd'), 'Thyme\n', 'Not returning rhyming word')

    def test_goodbye(self):
        text = 'Goodbye!\n' 
        self.assertEqual(RhymeThyme.print_goodbye_text(self), text, 'Not printing goodbye text properly!')
    
    def test_welcome(self):
        text = "Welcome to Rhyme Thyme - the awesome rhyming time. \n"
        self.assertEqual(RhymeThyme.print_welcome_text(self), text, 'Not printing welcome text properly!')

    def test_output_to_user(self):
        word = 'whazzup'
        text = 'Rhyming word:  ' + word
        self.assertEqual(RhymeThyme.output_to_user(self, word), text, 'Not outputting to user properly!')
