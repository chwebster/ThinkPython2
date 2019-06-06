"""
A module to test out what value __name__ takes when the module gets called from another program.
"""

def blah():
    print('Blah')
    print(__name__)

# Excecute the following code only if this program is being run as a script
if __name__ == '__main__':
    blah()
