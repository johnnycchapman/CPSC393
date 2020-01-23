
import dropbox
import csv



client = dropbox.Dropbox('XXXXXXXXXXXXXXXXXXXXXXXXX')
# print(client.users_get_current_account())
metadata = client.files_list_folder('/All onboard images').entries
# metadata = metadata.json()
#print(metadata)

with open('dates.csv', mode='w') as metadata_file:
    writer = csv.writer(metadata_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    writer.writerow(['date','filename'])
    
    for i in range(0, 10):
        #print(metadata[i].client_modified)
        #print(metadata[i].name)
        
        dates = metadata[i].client_modified
        
        
        files = metadata[i].name
        
        
        writer.writerow([dates,files]) 
