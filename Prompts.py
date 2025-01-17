from pydantic import BaseModel
from typing import Literal

class ContactData(BaseModel):
    Gender: Literal["Male", "Female"]
    Ethnicity: Literal["African", "Caucasian", "Hispanic", "East Asian", "South Asian", "Middle Eastern"]
    Age: Literal["0-29","30-39","40-49","50-59","60-100"]
    Industry: Literal["Livery Company", "Charity", "Church Association", "Finance/Business", "Education", "Government"]
    
    
def getGenderCategory():
    return list(ContactData.__annotations__["Gender"].__args__)

def getEthnicityCategory():
    return list(ContactData.__annotations__["Ethnicity"].__args__)

def getAgeCategory():
    return list(ContactData.__annotations__["Age"].__args__)

def getIndustryCategory():
    return list(ContactData.__annotations__["Industry"].__args__)


def getSystemPrompt_V2():    
    systemprompt = f"""
    A person's Information will be provided as:
    Name:name
    Company:company
    Position:position
    Linkedin:URL

    Find Age, Ethnicity, Gender, Company Industry.
    Factor the persons full name in finding Ethnicity, and first name in finding Gender
    
    Format your answer as categories:
    Age:{getAgeCategory()}
    Ethnicity:{getEthnicityCategory()}
    Industry:{getIndustryCategory()}
    Gender:{getGenderCategory()}
    
    Livery companies are London Livery Companies (like Feltmakers)
    """
    
    return systemprompt

def getSystemPrompt_V3():
    systemprompt = f"""
    A person's Information will be provided as:
    Name:name
    Company:company
    Position:position
    Linkedin:URL

    Find Age, Ethnicity, Gender, Company Industry.
    Factor the persons full name in finding Ethnicity, and first name in finding Gender
    An image will be provided. If feasible, also use it to determine gender and ethnicity
    
    Format your answer as categories:
    Age:{getAgeCategory()}
    Ethnicity:{getEthnicityCategory()}
    Industry:{getIndustryCategory()}
    Gender:{getGenderCategory()}
    
    Livery companies are London Livery Companies (like Feltmakers)
    """
    
    return systemprompt


def getSystemPrompt_V4():    
    systemprompt = f"""
    A person's Information will be provided as:
    Name:name
    Company:company
    Position:position

    Find Age, Ethnicity, Gender, Company Industry.
    Factor the persons full name in finding Ethnicity, and first name in finding Gender
    
    Format your answer as categories:
    Age:{getAgeCategory()}
    Ethnicity:{getEthnicityCategory()}
    Industry:{getIndustryCategory()}
    Gender:{getGenderCategory()}
    
    Livery companies are London Livery Companies (like Feltmakers)
    """
    
    return systemprompt