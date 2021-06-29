import pandas as pd

#pull ips from excel column and turn into a list
df = pd.read_excel('columns.xlsx',"Sheet1") # can also index sheet by name or fetch all sheets
ARP_IP = df['ARP IP Address'].tolist()

df = pd.read_excel('columns.xlsx',"Sheet1") # can also index sheet by name or fetch all sheets
DHCP_RESERVED = df['DHCP Reservation'].tolist()
print(DHCP_RESERVED)
Active_Reserved_Set = set(ARP_IP) & set(DHCP_RESERVED)
Active_Reserved = list(Active_Reserved_Set)
#print(Active_Reserved)

  
df1 = pd.DataFrame()
  

df1['A'] = Active_Reserved
# Converting to excel
df1.to_excel('ActiveReservedIPs4.xlsx', index = False)