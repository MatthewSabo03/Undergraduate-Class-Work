# Exceptions needed for Lab 03

# An exception class for representing a stack exception
class StackException(Exception):
    pass

# An stack exception class for representing an empty stack exception
class EmptyStackException(StackException):
    pass

# An exception class for representing a queue exception
class QueueException(Exception):
    pass

# An queue exception class for representing an empty queue exception
class EmptyQueueException(QueueException):
    pass

# An exception class for representing an error with processing an RPN equation
class RPNError(Exception):
    pass
