import threading

import FormGUI
import QueryBot
import Prompts
import DataHandler as dhd
import Crawler
import atexit


xForm = FormGUI.FormGUI()
ai = QueryBot.QueryBot()
crawler = Crawler.Crawler()

crmfile = "data/testdata.xlsx"
newfile = "data/new.xlsx"

crmDataFrame = dhd.pd.read_excel(crmfile, header=0)


def DF_APPLY_FUNC(row):
    # if(row["ID"] == 4):
    #     exit()
            
    xForm.resetFinalFormData()
    xForm.resetAIretry()
    xForm.disableGUI()
    
    crm_data = dhd.extractRowData(row)
    
    crawler.searchLinkedin(crm_data["u_url"])
    crawler.searchCompany(crm_data["u_company"])
    pic_url = crawler.getLinkedinPictureURL()
    
    question = ai.createQuestion(crm_data)
    
    if pic_url:
        ai_response = ai.getAIresponse(Prompts.getSystemPrompt_V3(), question, pic_url)
    else:
        ai_response = ai.getAIresponse(Prompts.getSystemPrompt_V2(), question)
    xForm.enableGUI()
    
    while not ai_response:
        ai.AI_ERROR("OpenAI response error", crm_data, question, ai_response)
        xForm.resetAIretry()
        while xForm.getAIretryStatus() is False:
            continue
        xForm.disableGUI()
        ai_response = ai.getAIresponse(Prompts.getSystemPrompt_V2(), question)
        xForm.enableGUI()

    if ai.AIrefused(ai_response):
        ai.AI_ERROR("OpenAI refused", crm_data, question, ai_response)
        exit()

    ai_output = ai.processAIoutput(ai_response)
    
    if not ai_output:
        ai.AI_ERROR("Fatal: OpenAI schema mismatch", crm_data, question, ai_response, ai_output)
        exit()
    
    xForm.sendDataToForm(crm_data, ai_output)
    
    while not xForm.finalFormData:
        continue
    
    f_data = xForm.getFinalFormData()
    print(f_data)
    
    row_dict = dhd.constructOutputRowDict(f_data)
    
    new_df = dhd.fetch_df(newfile, param_indexcol=0, param_header=0)
    new_df = dhd.update_new_df(newfile, new_df, row_dict)


def run_in_thread():
    crmDataFrame.apply(DF_APPLY_FUNC, axis=1)


def run():
    thread = threading.Thread(target=run_in_thread, daemon=True)
    thread.start()
    xForm.run()
    terminator()

def terminator():
    crawler.terminate()



try:
    atexit.register(terminator)
except:
    pass