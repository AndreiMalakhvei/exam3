import string

class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    # Так как в letters будут и uppercase, и lowercase, то выводим на печать только половину
    def print(self):
        print(self.letters[:int(len(self.letters)/2)])

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):

    __letters_num = 26
    # неясно, зачем в условиях задачи просят взять только uppercase, когда можно взять все сразу
    def __init__(self):
        Alphabet.__init__(self,'En', string.ascii_letters)

    def is_en_letter(self, letter):
        # проверяем, передана ли в качестве аргумента 1) буква, причём 2) лишь одна буква
        try:
            letter.isalpha()
        except AttributeError:
            return('ONLY TYPE STRING CAN BE PASSED AS ARGUMENT!')
        else:
            if len(letter) == 1:
                if letter in self.letters:
                    return f'LETTER {letter} BELONGS TO ENGLISH ALPHABET'
                return f'LETTER {letter} IS DEFINITELY NOT ENGLISH'
            return ('ONLY ONE LETTER CAN BE PASSED AS ARGUMENT')

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print('''Harvest time for tomatoes should ideally occur
        when the fruit is a mature green and
        then allowed to ripen off the vine.
        This prevents splitting or bruising
        and allows for a measure of control over the ripening process.''')




eng_inst = EngAlphabet()
eng_inst.print()
print(eng_inst.letters_num())
print(eng_inst.is_en_letter('F'))
print(eng_inst.is_en_letter('Щ'))
EngAlphabet.example()