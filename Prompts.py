from pydantic import BaseModel
from typing import Literal

def getSystemPrompt_V1():
    systemprompt = """
    The information for each person is: Name, Company, Position in company and LinkedIn URL.

    The information will be provided in the following format:
    Name:{first name} {last name}
    Company:{company}
    Position:{position}
    Linkedin URL:{URL}

    Your task is to find the following bits of information about the person:
    Age, Ethnicity, Gender and Industry of the Company.
    Note the livery companies are London Livery Companies (Feltmakers for example).

    Once you find this information, categorise it as follows:
    For age, the categories are "-29","30-39","40-49","50-59","60+"
    For ethnicity, the categories are "African","Asian","Caucasian"
    For industry of company, the categories are "Livery Company","Charity","Church Association","Finance/Business"
    For gender, the categories are “Male”, “Female”

    Use the exact same spellings.

    Afterwards, strictly format your answer as follows, replacing [category] with the right category
    Age:[category]
    Ethnicity:[category]
    Gender:[category]
    Industry:[category]

    Provide the answer in the format given. Do not add any additional text.
    """
    
    return systemprompt


def getSystemPrompt_V2():    
    systemprompt = """
    A person's Information will be provided as:
    Name:name
    Company:company
    Position:position
    Linkedin:URL

    Find Age, Ethnicity, Gender, Company Industry.
    Factor the persons full name in finding Ethnicity, and first name in finding Gender
    
    Format your answer as categories:
    Age:["-29","30-39","40-49","50-59","60+"]
    Ethnicity:["African", "Caucasian", "Hispanic", "East Asian", "South Asian", "Middle Eastern"]
    Industry:["Livery Company","Charity","Church Association","Finance/Business"]
    Gender:[“Male”, “Female”]
    
    Livery companies are London Livery Companies (like Feltmakers)
    """
    
    return systemprompt

def getSystemPrompt_V3():    
    systemprompt = """
    A person's Information will be provided as:
    Name:name
    Company:company
    Position:position
    Linkedin:URL

    Find Age, Ethnicity, Gender, Company Industry.
    Factor the persons full name in finding Ethnicity, and first name in finding Gender
    An image will be provided. If feasible, also use it to determine gender and ethnicity
    
    Format your answer as categories:
    Age:["-29","30-39","40-49","50-59","60+"]
    Ethnicity:["African", "Caucasian", "Hispanic", "East Asian", "South Asian", "Middle Eastern"]
    Industry:["Livery Company","Charity","Church Association","Finance/Business"]
    Gender:[“Male”, “Female”]
    
    Livery companies are London Livery Companies (like Feltmakers)
    """
    
    return systemprompt



class ContactData(BaseModel):
    Gender: Literal["Male", "Female"]
    Ethnicity: Literal["African", "Caucasian", "Hispanic", "East Asian", "South Asian", "Middle Eastern"]
    Age: Literal["0-29","30-39","40-49","50-59","60-100"]
    Industry: Literal["Livery Company", "Charity", "Church Association", "Finance/Business"]