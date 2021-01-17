# Use gitlab history to check the explaination 

def html_tag(tag):

    def wrap_text(msg):
        print "<{0}>{1}</{0}>".format(tag, msg)

    return wrap_text

print_h1 = html_tag('h1')  # Assign variable print_h1 to a function 
print print_h1             # print function at memory address

print_h1('Test Headline')  # print_h1 is now a function and can add the msg.
print_h1('Another Headline')