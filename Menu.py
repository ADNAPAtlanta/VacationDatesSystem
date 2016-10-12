from firebase import firebase
from tkinter import *
from geopy.geocoders import Nominatim



Firebase = firebase.FirebaseApplication('https://vacation-dd8a7.firebaseio.com/')
print(Firebase)


countries = ["Afghanistan",
"Aland Islands",
"Albania","Algeria","American Samoa",
"Andorra","Angola","Anguilla",
"Antarctica","Antigua and Barbuda","Argentina","Armenia",
"Aruba",
"Australia","Austria",
"Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin",
"Bermuda","Bhutan","Bolivia, Plurinational State of",
"Bonaire, Sint Eustatius and Saba","Bosnia and Herzegovina","Botswana","Bouvet Island","Brazil",
"British Indian Ocean Territory",
"Brunei Darussalam","Bulgaria","Burkina Faso",
"Burundi","Cambodia","Cameroon","Canada","Cape Verde","Cayman Islands","Central African Republic","Chad","Chile","China",
"Christmas Island","Cocos (Keeling) Islands","Colombia","Comoros","Congo",
"Congo, The Democratic Republic of the",
"Cook Islands","Costa Rica","Côte d'Ivoire","Croatia","Cuba","Curaçao","Cyprus","Czech Republic","Denmark",
"Djibouti","Dominica","Dominican Republic","Ecuador",
"Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Falkland Islands (Malvinas)","Faroe Islands","Fiji",
"Finland","France","French Guiana","French Polynesia","French Southern Territories","Gabon","Gambia",
"Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guadeloupe",
"Guam",
"Guatemala","Guernsey","Guinea","Guinea-Bissau","Guyana","Haiti","Heard Island and McDonald Islands",
"Holy See (Vatican City State)","Honduras","Hong Kong","Hungary",
"Iceland","India","Indonesia","Iran, Islamic Republic of","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kiribati","Korea, Democratic People's Republic of",
              "Korea, Republic of",
"Kuwait",
"Kyrgyzstan","Lao People's Democratic Republic","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein",
"Lithuania",
"Luxembourg","Macao","Macedonia, Republic of","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Martinique","Mauritania","Mauritius","Mayotte","Mexico",
              "Micronesia, Federated States of",
"Moldova, Republic of",
"Monaco",
"Mongolia","Montenegro","Montserrat","Morocco","Mozambique",
"Myanmar","Namibia","Nauru","Nepal","Netherlands","New Caledonia","New Zealand","Nicaragua","Niger",
"Nigeria","Niue","Norfolk Island","Northern Mariana Islands","Norway",
"Oman","Pakistan","Palau",
"Palestinian Territory, Occupied","Panama",
"Papua New Guinea","Paraguay",
"Peru","Philippines","Pitcairn","Poland","Portugal",
"Puerto Rico","Qatar",
"Réunion","Romania",
"Russian Federation","Rwanda","Saint Barthélemy","Saint Helena, Ascension and Tristan da Cunha","Saint Kitts and Nevis","Saint Lucia","Saint Martin (French part)","Saint Pierre and Miquelon",
"Saint Vincent and the Grenadines","Samoa",
"San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia",
"Seychelles","Sierra Leone",
"Singapore","Sint Maarten (Dutch part)",
"Slovakia","Slovenia",
"Solomon Islands","Somalia","South Africa",
"South Georgia and the South Sandwich Islands","Spain","Sri Lanka","Sudan",
"Suriname","South Sudan","Svalbard and Jan Mayen",
"Swaziland","Sweden","Switzerland","Syrian Arab Republic",
"Taiwan, Province of China","Tajikistan","Tanzania, United Republic of",
"Thailand","Timor-Leste","Togo","Tokelau",
"Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan",
"Turks and Caicos Islands","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom",
"United States","United States Minor Outlying Islands",
"Uruguay","Uzbekistan","Vanuatu","Venezuela, Bolivarian Republic of","Viet Nam",
"Virgin Islands, British","Virgin Islands, U.S.",
"Wallis and Futuna","Western Sahara","Yemen","Zambia","Zimbabwe"]

class vacationAdder:
    def __init__(self,master):
        self.master = master
        master.title("ADNAP Vacation Systems")
        master.minsize(width=290,height=300)
        self.type = StringVar()
        self.type.set("Vacation")

        #entry variables
        self.name = StringVar()
        self.address = StringVar()
        self.state = StringVar()
        self.family = StringVar()
        self.lat = DoubleVar()
        self.longitude = DoubleVar()
        self.setting = StringVar()
        self.country = StringVar()
        self.noise = StringVar()
        self.feel = StringVar()

        self.vacation = StringVar()
        self.date = StringVar()

        self.choice = Menubutton(master,textvariable=self.type,relief=RAISED,width=10)
        self.choice.grid(row=1,column=1)
        self.choice.menu = Menu(self.choice, tearoff=0)
        self.choice["menu"] = self.choice.menu
        self.choice.menu.add_radiobutton(label="Vacation",variable=self.type)
        self.choice.menu.add_radiobutton(label="Date",variable=self.type)

        self.mode = Button(master,text="View list of vacations",command=self.list)
        self.mode.grid(row=1,column=3)

        #entry labels
        self.nameLabel = Label(master, text="Name of Place",underline=0)
        self.nameLabel.grid(row=2,column=2)
        self.nameEntry = Entry(master,bd=3,textvariable=self.name)
        self.nameEntry.grid(row=3,column=2)

        self.addressLabel = Label(master, text="Enter address",underline=0)
        self.addressLabel.grid(row=4,column=2)
        self.addressEntry = Entry(master, bd=3,textvariable=self.address)
        self.addressEntry.grid(row=5,column=2)

        self.stateLabel = Label(master, text="Enter state or territory",underline=0)
        self.stateLabel.grid(row=6,column=2)
        self.stateEntry = Entry(master,bd=3,textvariable=self.state)
        self.stateEntry.grid(row=7,column=2)

        self.countryLabel = Label(master, text="Enter country.",underline=0)
        self.countryLabel.grid(row=8,column=2)
        self.country.set("United States")
        self.countryEntry = OptionMenu(master,self.country,*countries)
        self.countryEntry.grid(row=9,column=2)

        self.familyLabel = Label(master, text="Family oriented? (Not needed for Date)",underline=0)
        self.familyLabel.grid(row=10,column=2)
        self.family.set("Yes")
        self.familyEntry = OptionMenu(master,self.family,"Yes","No")
        self.familyEntry.grid(row=11,column=2)
        if self.type.get() == "Vacation":
            self.familyEntry.lower()

        self.latLabel = Label(master, text="Enter latitude",underline=0)
        self.latLabel.grid(row=12,column=2)
        self.latEntry = Entry(master,bd=3,textvariable=self.lat)
        self.latEntry.grid(row=13,column=2)

        self.longitudeLabel = Label(master, text="Enter longitude",underline=0)
        self.longitudeLabel.grid(row=14,column=2)
        self.longitudeEntry = Entry(master,bd=3,textvariable=self.longitude)
        self.longitudeEntry.grid(row=15,column=2)

        self.settingLabel = Label(master, text="Rural or Urban",underline=0)
        self.settingLabel.grid(row=16,column=2)
        self.setting.set("Rural")
        self.settingEntry = OptionMenu(master,self.setting,"Urban","Rural")
        self.settingEntry.grid(row=17,column=2)

        self.noiseLabel = Label(master, text="Calm or Noisy")
        self.noiseLabel.grid(row=18,column=2)
        self.noise.set("Calm")
        self.noiseEntry = OptionMenu(master,self.noise,"Noisy","Calm")
        self.noiseEntry.grid(row=19,column=2)
        #Submit Button
        self.submitButton = Button(master,text="Submit",command=self.addtofirebase)
        self.submitButton.grid(row=20,column=2)

    def addtofirebase(self):
        country = self.country.get()
        state = self.stateEntry.get()
        name = self.nameEntry.get()
        address = self.addressEntry.get()
        familyOriented = self.family.get()
        lat = self.latEntry.get()
        longitude = self.longitudeEntry.get()
        setting = self.setting.get()
        noise = self.noise.get()

        geolocator = Nominatim()
        location = geolocator.geocode("1016 Howell Mill Rd, Atlanta, GA 30318")
        print(location.latitude,location.longitude)

        print("/" + country.title() +"/" + state.title()+ "/" + name.title())
        print(self.type.get())

        #print(Firebase.put("/" + self.country.get()+"/"+self.state.get()))
        #result = Firebase.put("/"+self.country.get()+)
    def list(self):
        t = self.Toplevel(self)
        t.wm_title("Vacation List")

if __name__ == "__main__":
    root = Tk()
    GUI = vacationAdder(root)
    root.mainloop()















