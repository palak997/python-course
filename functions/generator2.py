#WAP TO GENERATE A LIST OF ACRONYMNS FROM A LIST OF WORDS USING GENERATORS & * ARGS


def acronym(*words):
    for word in words:
        yield ''.join ([i[0].upper() for i in word.split()]) 

#ex call
for item in acronym('project manager', 'software engineer','data analytics'):
    print(item)



print (list(acronym('project manager', 'software engineer','data analytics','team leading')))
