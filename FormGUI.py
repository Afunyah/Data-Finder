import tkinter as tk

class FormGUI():
    x_width = 50
    
    finalFormData = {}
    ai_retry_status = False

    root = tk.Tk()
    
    idlabel = tk.Label(master=root, text="ID")
    id_var = tk.StringVar()
    f_id = tk.Label(master=root, textvariable=id_var, width= x_width)
    
    firstnamelabel = tk.Label(master=root, text="First Name")
    f_firstname = tk.Entry(master=root, text="", width= x_width)

    lastnamelabel = tk.Label(master=root, text="Last Name")
    f_lastname = tk.Entry(master=root, text="", width= x_width)

    urllabel = tk.Label(master=root, text="URL")
    f_url = tk.Entry(master=root, text="", width= x_width)

    emaillabel = tk.Label(master=root, text="Email Addr")
    f_email = tk.Entry(master=root, text="", width= x_width)
    
    companylabel = tk.Label(master=root, text="Company")
    f_company = tk.Entry(master=root, text="", width= x_width)

    positionlabel = tk.Label(master=root, text="Position")
    f_position = tk.Entry(master=root, text="", width= x_width)

    connectedlabel = tk.Label(master=root, text="Connected")
    f_connected = tk.Entry(master=root, text="", width= x_width)

    genderlabel = tk.Label(master=root, text="Gender")
    gender_options = ["Male","Female"]
    gender_var = tk.StringVar(value="Male")
    f_gender = tk.OptionMenu(root, gender_var, *gender_options)

    ethnicititylabel = tk.Label(master=root, text="Ethnicity")
    ethnicity_options = ["African", "Caucasian", "Hispanic", "East Asian", "South Asian", "Middle Eastern"]
    ethnicity_var = tk.StringVar(value="Caucasian")
    f_ethnicity = tk.OptionMenu(root, ethnicity_var, *ethnicity_options)

    agelabel = tk.Label(master=root, text="Age Bracket")
    age_options = ["0-29","30-39","40-49","50-59","60-100"]
    age_var = tk.StringVar(value="40-49")
    f_age = tk.OptionMenu(root, age_var, *age_options)

    industrylabel = tk.Label(master=root, text="Industry")
    industry_options = ["Livery Company","Charity","Church Association","Finance/Business"]
    industry_var = tk.StringVar(value="Finance/Business")
    f_industry = tk.OptionMenu(root, industry_var, *industry_options)

    confirm_var = tk.IntVar()
    confirm = tk.Checkbutton(master=root, text="Confirm?", variable=confirm_var)
    
    # Allow buttons to be created before command functions
    def createSubmitButton(self):
        submitButton = tk.Button(master=self.root, text="Submit", command=self.submitForm)
        return submitButton
    
    def createRetryButton(self):
        retryButton = tk.Button(master=self.root, text="Retry AI", command=self.retryAI)
        return retryButton


    def __init__(self):
        self.submit = self.createSubmitButton()
        self.retry = self.createRetryButton()
        self.configUI(self.submit)
        
    def run(self):
        self.root.mainloop()
    
    def disableGUI(self):
        for child in self.root.winfo_children():
            child.configure(state='disabled')
    
    def enableGUI(self):
        for child in self.root.winfo_children():
            child.configure(state='normal')
    
    def configUI(self, submit):
        self.root.config(bg="#E4E2E2")
        self.root.title("root Window")
        self.root.geometry("700x450")
        
        self.idlabel.config(bg="#E4E2E2", fg="#000")
        self.idlabel.grid(row=0,column=0)

        self.f_id.config(bg="#fff", fg="#000")
        self.f_id.grid(row=0,column=1)

        self.firstnamelabel.config(bg="#E4E2E2", fg="#000")
        self.firstnamelabel.grid(row=1,column=0)

        self.f_firstname.config(bg="#fff", fg="#000")
        self.f_firstname.grid(row=1,column=1)

        self.lastnamelabel.config(bg="#E4E2E2", fg="#000")
        self.lastnamelabel.grid(row=2,column=0)

        self.f_lastname.config(bg="#fff", fg="#000")
        self.f_lastname.grid(row=2,column=1)

        self.urllabel.config(bg="#E4E2E2", fg="#000")
        self.urllabel.grid(row=3,column=0)
        
        self.f_url.config(bg="#fff", fg="#000")
        self.f_url.grid(row=3,column=1)
        
        self.emaillabel.config(bg="#E4E2E2", fg="#000")
        self.emaillabel.grid(row=4,column=0)
        
        self.f_email.config(bg="#fff", fg="#000")
        self.f_email.grid(row=4,column=1)
        
        self.companylabel.config(bg="#E4E2E2", fg="#000")
        self.companylabel.grid(row=5,column=0)
        
        self.f_company.config(bg="#fff", fg="#000")
        self.f_company.grid(row=5,column=1)
        
        self.positionlabel.config(bg="#E4E2E2", fg="#000")
        self.positionlabel.grid(row=6,column=0)
        
        self.f_position.config(bg="#fff", fg="#000")
        self.f_position.grid(row=6,column=1)
        
        self.connectedlabel.config(bg="#E4E2E2", fg="#000")
        self.connectedlabel.grid(row=7,column=0)
        
        self.f_connected.config(bg="#fff", fg="#000")
        self.f_connected.grid(row=7,column=1)
        
        self.genderlabel.config(bg="#E4E2E2", fg="#000")
        self.genderlabel.grid(row=8,column=0)
        
        self.f_gender.config(bg="#fff", fg="#000")
        self.f_gender.grid(row=8,column=1,sticky=tk.N+tk.W)

        self.ethnicititylabel.config(bg="#E4E2E2", fg="#000")
        self.ethnicititylabel.grid(row=9,column=0)

        self.f_ethnicity.config(bg="#fff", fg="#000")
        self.f_ethnicity.grid(row=9,column=1,sticky=tk.N+tk.W)

        self.agelabel.config(bg="#E4E2E2", fg="#000")
        self.agelabel.grid(row=10,column=0)

        self.f_age.config(bg="#fff", fg="#000")
        self.f_age.grid(row=10,column=1,sticky=tk.N+tk.W)

        self.industrylabel.config(bg="#E4E2E2", fg="#000")
        self.industrylabel.grid(row=11,column=0)

        self.f_industry.config(bg="#fff", fg="#000")
        self.f_industry.grid(row=11,column=1,sticky=tk.N+tk.W)

        self.confirm.config(bg="#fff", fg="#000")
        self.confirm.place(x=360.8518880208333, y=349.598388671875, width=139, height=39)
        
        submit.config(bg="#E4E2E2", fg="#000")
        submit.place(x=524.5185546875, y=315.2650553385416, width=103, height=93)
        
        self.retry.config(bg="#E4E2E2", fg="#000")
        self.retry.place(x=84.5185546875, y=349.598388671875, width=103, height=33)
    
    def set_id(self,x):
        self.id_var.set(x)
    
    def get_id(self):
        return self.id_var.get()

    def set_entry(self, widg, text):
        widg.delete(0,tk.END)
        widg.insert(0,text)

    def get_entry(self, widg):
        return widg.get()

    def get_option(self, widg):
        if(widg==self.f_gender):
            return self.gender_var.get()
        if(widg==self.f_ethnicity):
            return self.ethnicity_var.get()
        if(widg==self.f_age):
            return self.age_var.get()
        if(widg==self.f_industry):
            return self.industry_var.get()
        pass

    def set_option(self, widg, opt):
        ind = 0
        if(widg==self.f_gender):
            try:
                ind = self.gender_options.index(opt)
            except:
                pass
            self.gender_var.set(self.gender_options[ind])
            return
            
        if(widg==self.f_ethnicity):
            try:
                ind = self.ethnicity_options.index(opt)
            except:
                pass
            self.ethnicity_var.set(self.ethnicity_options[ind])
            return
            
        if(widg==self.f_age):
            try:
                ind = self.age_options.index(opt)
            except:
                pass
            self.age_var.set(self.age_options[ind])
            return
            
        if(widg==self.f_industry):
            try:
                ind = self.industry_options.index(opt)
            except:
                pass
            self.industry_var.set(self.industry_options[ind])
            return
        pass

    def resetConfirm(self):
        self.confirm.deselect()

    def getConfirmState(self):
        return self.confirm_var.get()

    def submitForm(self):
        # global finalFormData
        self.finalFormData = {}
        if(self.getConfirmState()):
            self.finalFormData = {   
            "f_id": self.get_id(),
            "f_firstname" : self.get_entry(self.f_firstname),
            "f_lastname" : self.get_entry(self.f_lastname),
            "f_url" : self.get_entry(self.f_url),
            "f_email" : self.get_entry(self.f_email),
            "f_company" : self.get_entry(self.f_company),
            "f_position" : self.get_entry(self.f_position),
            "f_connected" : self.get_entry(self.f_connected),
            "f_gender" : self.get_option(self.f_gender),
            "f_ethnicity" : self.get_option(self.f_ethnicity),
            "f_age" : self.get_option(self.f_age),
            "f_industry" : self.get_option(self.f_industry)
            }

        self.resetConfirm()
        
    def retryAI(self):
        self.ai_retry_status = True
    
    def resetAIretry(self):
        self.ai_retry_status = False
        
    def getAIretryStatus(self):
        return self.ai_retry_status
    
    def sendDataToForm(self, crmData, regxData):
        self.set_id(crmData["u_id"])
        self.set_entry(self.f_firstname, crmData["u_firstname"])
        self.set_entry(self.f_lastname, crmData["u_lastname"])
        self.set_entry(self.f_url, crmData["u_url"])
        self.set_entry(self.f_email, crmData["u_email"])
        self.set_entry(self.f_company, crmData["u_company"])
        self.set_entry(self.f_position, crmData["u_position"])
        self.set_entry(self.f_connected, crmData["u_connected"])
        self.set_option(self.f_gender, regxData["gender"])
        self.set_option(self.f_ethnicity, regxData["ethnicity"])
        self.set_option(self.f_age, regxData["age"])
        self.set_option(self.f_industry, regxData["industry"])

    def getFinalFormData(self):
        # global finalFormData
        return self.finalFormData

    def resetFinalFormData(self):
        # global finalFormData
        self.finalFormData = {}