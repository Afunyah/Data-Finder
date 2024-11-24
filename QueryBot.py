from openai import OpenAI
from Prompts import ContactData

class QueryBot():    
    
    def __init__(self):
        self.client = OpenAI(api_key="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")
        pass

    def createQuestion(self, u_data):
        question = f"Name:{u_data['u_firstname']} {u_data['u_lastname']}\nCompany:{u_data['u_company']}\nPosition:{u_data['u_position']}\nLinkedin URL:{u_data['u_url']}"
        return question
    
    def getAIresponse(self, s_prompt, u_prompt, pic_url="",model="gpt-4o-mini"):
        response = {}
        
        if pic_url:
            messages = [{"role": "system", "content": s_prompt},
                        {"role": "user", "content": [
                            {"type":"text","text":u_prompt},
                            {"type":"image_url",
                            "image_url": {"url": pic_url}
                            }]
                        }]
        else:
            messages = [{"role": "system", "content": s_prompt},
                        {"role": "user", "content": u_prompt}]

        try:
            completion = self.client.beta.chat.completions.parse( model=model, messages=messages, response_format=ContactData)
            response = completion.choices[0].message
        except Exception as e:
            print(e)
        
        return response
    
    def AIrefused(self, response):
        if response.parsed:
            return False
        elif response.refusal:
            return True        
    
    def processAIoutput(self, response):
        r_data = {}
        try:
            r_age = response.parsed.Age
            r_gender = response.parsed.Gender
            r_industry = response.parsed.Industry
            r_ethnicity = response.parsed.Ethnicity
            
            r_data = {
                "age":r_age,
                "gender":r_gender,
                "industry":r_industry,
                "ethnicity":r_ethnicity
            }
        except Exception as e:
            print(e)
        
        return r_data
    
    def AI_ERROR(err, crm_data, question, ai_response, ai_output={}):
        print(err)
        print("Contact info")
        print(crm_data)
        print(question)
        print("AI response:")
        print(ai_response)
        print("AI output:")
        print(ai_output)
        print("\nPlease fix the issue manually")