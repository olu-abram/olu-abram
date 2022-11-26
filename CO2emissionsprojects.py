# ~~~~~~~~~~~~~~~~~~~~~~~~ CO2 per km traveled depending on Carmodel/Fuel Consumption ~~~~~~~~~~~~~


# carmodel = input("What type of car do you drive?:")
km_traveled = float(input("how many km did you drive?:")) # Calgary  to Tuscany 21.6 km
# from downtown to Tuscany on a RAV4 is average 21.6km
# RAV4 Fuel consumptionn is 8.8 L/100km Average see factor 
# that is equal to 1.9L/21.6km (factor: 4.63)
# https://www.nrcan.gc.ca/sites/nrcan/files/oee/pdf/transportation/fuel-efficient-technologies/2022%20Fuel%20Consumption%20Guide.pdf

car_fc_Lperkm = {"RAV4": 8.8, "Rogue": 8.5, "CX-5 AWD": 10.2}

# converts km to L of gasoline burned = km * fuel consumption (L/100km)
def kmtoLconvers(km, Lperkm):
    return (float(Lperkm)/100 * km)  

def gasolinetoCO2_Ltokg(L):
    return float(L)  * float(2.3)

print(kmtoLconvers(km_traveled, car_fc_Lperkm["RAV4"]))
print ("You released", gasolinetoCO2_Ltokg(kmtoLconvers(km_traveled, car_fc_Lperkm["RAV4"])), "kilograms of CO2.")