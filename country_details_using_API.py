from tkinter import *
import requests
import json
root=Tk()
root.title("Country")
root.geometry("450x500")
root.configure(bg="#8370fe")

capital_name_label=Label(root,text="Capital City Name",font=("Helvetica",18,"bold"),bg="#8370fe",fg="white")
capital_name_label.place(relx=0.06,rely=0.15,anchor="w")

capital_enter=Entry(root)
capital_enter.place(relx=0.07,rely=0.25,anchor="w")

label_country=Label(root,text="Country: ",font=(18),bg="#8370fe",fg="white")
label_country.place(relx=0.07,rely=0.45,anchor="w")

label_region=Label(root,text="Region: ",font=(18),bg="#8370fe",fg="white")
label_region.place(relx=0.07,rely=0.55,anchor="w")

label_lang=Label(root,text="Language: ",font=(18),bg="#8370fe",fg="white")
label_lang.place(relx=0.07,rely=0.65,anchor="w")

label_pop=Label(root,text="Population: ",font=(18),bg="#8370fe",fg="white")
label_pop.place(relx=0.07,rely=0.75,anchor="w")

label_area=Label(root,text="Area: ",font=(18),bg="#8370fe",fg="white")
label_area.place(relx=0.07,rely=0.85,anchor="w")

def check():
    api_request = requests.get("https://restcountries.eu/rest/v2/capital/"+capital_enter.get())
    api_output_json = json.loads(api_request.content)
    country=api_output_json[0]["name"]
    region=api_output_json[0]["region"]
    lang=api_output_json[0]["languages"][0]["name"]
    pop=api_output_json[0]["population"]
    area=api_output_json[0]["area"]
    flag=api_output_json[0]["flag"]
    label_country["text"]="Country: "+country
    label_region["text"]="Region: "+region
    label_lang["text"]="Language: "+lang
    label_pop["text"]="Population: "+str(pop)
    label_area["text"]="Area: "+str(area)
    print(flag)
btn=Button(root,text="City Details",bg="yellow",command=check)
btn.place(relx=0.07,rely=0.35,anchor="w")
root.mainloop()
