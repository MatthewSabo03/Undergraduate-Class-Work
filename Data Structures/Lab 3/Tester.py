from palindrome import *
from postfix import *

print("Stack-Based\n-----------------------------")
print("racecar:\t\tTrue = " + str(is_palindrome_stack("racecar")))
print("Bob:\t\t\tTrue = " + str(is_palindrome_stack("Bob")))
print("Bo!b:\t\t\tTrue = " + str(is_palindrome_stack("Bo!b")))
print("ABC:\t\t\tFalse = " + str(is_palindrome_stack("ABC")))
print("12321\t\t\tTrue = " + str(is_palindrome_stack("12321")))
print("1 2 3 2 1\t\tTrue = " + str(is_palindrome_stack("1 2 3 2 1")))
print("123\t\t\tFalse = " + str(is_palindrome_stack("123")))
print("12321A\t\t\tFalse = " + str(is_palindrome_stack("12321A")))
print("a12321A\t\t\tTrue = " + str(is_palindrome_stack("a12321A")))
print("madam\t\t\tTrue = " + str(is_palindrome_stack("madam")))
print("madamk\t\t\tFalse = " + str(is_palindrome_stack("madamk")))
print("madamam\t\t\tFalse = " + str(is_palindrome_stack("madamam")))
print("45madam\t\t\tFalse = " + str(is_palindrome_stack("45madam")))
print("Too bad I hid a boot\tTrue = " + str(is_palindrome_stack("Too bad I hid a boot")))
print("Rise to vote, sir!\tTrue = " + str(is_palindrome_stack("Rise to vote, sir!")))
print("¡Ŗīŝę Ťő VŐťĘ, ŜĪŗ!\tTrue = " + str(is_palindrome_stack("¡Ŗīŝę Ťő VŐťĘ, ŜĪŗ!")))

print("-----------------------------\nQueue-Based\n-----------------------------")
print("racecar:\t\tTrue = " + str(is_palindrome_queue("racecar")))
print("Bob:\t\t\tTrue = " + str(is_palindrome_queue("Bob")))
print("Bo!b:\t\t\tTrue = " + str(is_palindrome_queue("Bo!b")))
print("ABC:\t\t\tFalse = " + str(is_palindrome_queue("ABC")))
print("12321\t\t\tTrue = " + str(is_palindrome_queue("12321")))
print("1 2 3 2 1\t\tTrue = " + str(is_palindrome_queue("1 2 3 2 1")))
print("123\t\t\tFalse = " + str(is_palindrome_queue("123")))
print("12321A\t\t\tFalse = " + str(is_palindrome_queue("12321A")))
print("a12321A\t\t\tTrue = " + str(is_palindrome_queue("a12321A")))
print("2madam2\t\t\tTrue = " + str(is_palindrome_queue("2madam2")))
print("madam\t\t\tTrue = " + str(is_palindrome_queue("madam")))
print("mammadam\t\tFalse = " + str(is_palindrome_queue("mammadam")))
print("2madam52\t\tFalse = " + str(is_palindrome_queue("2madam52")))
print("Too bad I hid a boot\tTrue = " + str(is_palindrome_queue("Too bad I hid a boot")))
print("Rise to vote, sir!\tTrue = " + str(is_palindrome_queue("Rise to vote, sir!")))
print("¡Ŗīŝę Ťő VŐťĘ, ŜĪŗ!\tTrue = " + str(is_palindrome_queue("¡Ŗīŝę Ťő VŐťĘ, ŜĪŗ!")))

print("-----------------------------\nValid Equations\n-----------------------------")
print("4 2 + 5 + =\t\t\t11.0 : " + str(postfix_calculator("4 2 + 5 +")))
print("4 2 / 5 + =\t\t\t7.0  : " + str(postfix_calculator("4 2 / 5 +")))
print("4 2 - 5 + =\t\t\t7.0  : " + str(postfix_calculator("4 2 - 5 +")))
print("4 2 * 5 + =\t\t\t13.0 : " + str(postfix_calculator("4 2 * 5 +")))
print("12 10 + 2 * =\t\t\t44.0 : " + str(postfix_calculator("12 10 + 2 *")))
print("1 2 + 5 6 * + 8 + =\t\t41.0 : " + str(postfix_calculator("1 2 + 5 6 * + 8 +")))
print("72000 12000 / 6 2 * + 2 * =\t36.0 : " + str(postfix_calculator("72000 12000 / 6 2 * + 2 *")))
print("5 5 + 5 + =\t\t\t15.0 : " + str(postfix_calculator("5 5 + 5 +")))
print("3 2 / 9 + =\t\t\t10.5 : " + str(postfix_calculator("3 2 / 9 +")))
print("3 2 - 9 + =\t\t\t10.0 : " + str(postfix_calculator("3 2 - 9 +")))
print("5 5 * 5 + =\t\t\t30.0 : " + str(postfix_calculator("5 5 * 5 +")))
print("12 5 / 5 + =\t\t\t7.4  : " + str(postfix_calculator("12 5 / 5 +")))
print("0 1 - 9 * 2 / =\t\t\t-4.5  : " + str(postfix_calculator("0 1 - 9 * 2 /")))

print("-----------------------------\nInvalid Equations\n-----------------------------")
try:
    print("'2 + 5 6 * + 8 +': SHOULD ERROR = " + str(postfix_calculator("2 + 5 6 * + 8 +")))
except RPNError:
    print("GOOD! RPNError caught!")
except:
    print("Bad. Should be an RPNError.")
    
try:
    print("'1 2 + 5 6 * + 8': SHOULD ERROR = " + str(postfix_calculator("1 2 + 5 6 * + 8")))
except RPNError:
    print("GOOD! RPNError caught!")
except:
    print("Bad. Should be an RPNError.")
    
try:
    print("'1 2 + 5 6 * + 8 + +': SHOULD ERROR = " + str(postfix_calculator("1 2 + 5 6 * + 8 + +")))
except RPNError:
    print("GOOD! RPNError caught!")
except:
    print("Bad. Should be an RPNError.")
    
try:
    print("'': SHOULD ERROR = " + str(postfix_calculator("")))
except RPNError:
    print("GOOD! RPNError caught!")
except:
    print("Bad. Should be an RPNError.")
    
try:
    print("'pass': SHOULD ERROR = " + str(postfix_calculator("pass")))
except RPNError:
    print("GOOD! RPNError caught!")
except:
    print("Bad. Should be an RPNError.")
    
try:
    print("'1 2 ÷ 5 6 × ×': SHOULD ERROR = " + str(postfix_calculator("1 2 ÷ 5 6 × ×")))
except RPNError:
    print("GOOD! RPNError caught!")
except:
    print("Bad. Should be an RPNError.")
