print("Hello world!")

acronyms = {}

acronyms['LOL'] = 'Laugh out loud'
acronyms['IDK'] = "I don't know"
acronyms['TBH']  = 'to be honest.'
acronyms['LGTM'] = 'looks good to me'


sentence = 'IDK' + ' what happened, ' + 'TBH'
translation = acronyms.get('IDK') + ' what happened, ' + acronyms.get('TBH')

print('sentence:' , sentence)
print('translation:', translation)
