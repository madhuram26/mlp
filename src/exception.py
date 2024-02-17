import sys #This is cool library does a lot of hardcore, low-level stuff close to the interpreter itself
from src.logger import logging # This is fun, you are importing a file you made in a folder

def error_message_detail(error, error_detail:sys):
    """
    This function gives an error message if something goes wrong. 
    It takes the error rasied, traces it back to the orginal line or function that erred.
    Then it returns an error message.
    All the boring words or the formats are just fancy stuff.
    Onyl goal is to properly give you an error message in return.
    """
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error Occured in Pyton script name [{0}, line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):  #The Exception inside the brackets is another built-in class.
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) #The super() is being used to call the parent 'Exception' class
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message #This returns the error message as created by the function defined above.
    logging.info("Annotated the Exception file and fixed the str method.")