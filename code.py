import pandas as pd
import cv2
df = pd.read_csv('metadata.csv')
df.finding


c=df[df["finding"]=="Pneumonia/Viral/COVID-19"]       
y=c[c["RT_PCR_positive"]=="Y"]
n=c[c["RT_PCR_positive"]=="Unclear"]
#y.shape[0]
#n.shape
#c.shape

yes_f=[]
for i in range(1,360):
    f=y.iloc[i]['filename']
    yes_f.append(f)
#yes_f    
   
no_f=[]
for j in range(1,216):
    f=n.iloc[j]['filename']
    no_f.append(f)
   
def read_file(path,path2,file_list,key):
    for i in file_list:
        try:
            filename = path+'/'+i
            #print(filename)
            img = cv2.imread(filename)
            filename = path2+'/'+key+'/'+i
            cv2.imwrite(filename,img)
        except:
            print(key,'=',i)
read_file(path='images',path2='covid',file_list=yes_f,key='yes')
read_file(path='images',path2='covid',file_list=no_f,key='no')

y_xray=y[y["modality"]=="X-ray"]
y_ct=y[y["modality"]=="CT"]
n_xray=n[n["modality"]=="X-ray"]
n_ct=n[n["modality"]=="CT"]

#y_xray
#y_xray.shape
#y_ct.shape

yes_xray=list()
for a in range(1,y_xray.shape[0]):
    f = y_xray.iloc[a]['filename']
    yes_xray.append(f)
yes_ct=list()
for b in range(1,y_ct.shape[0]):
    f = y_ct.iloc[b]['filename']
    yes_ct.append(f)
no_ct=list()
for c in range(1,n_ct.shape[0]):
    f = n_ct.iloc[c]['filename']
    no_ct.append(f)
no_xray=list()
for d in range(1,n_xray.shape[0]):
    f = n_xray.iloc[d]['filename']
    no_xray.append(f)
print(no_xray)


read_file(path='covid/no',path2='ct_xray_covid',file_list=no_ct,key='no_ct_covid')

read_file(path='covid/yes',path2='ct_xray_covid',file_list=yes_ct,key='yes_ct_covid')

read_file(path='covid/no',path2='ct_xray_covid',file_list=no_xray,key='no_xray_covid')

read_file(path='covid/yes',path2='ct_xray_covid',file_list=yes_xray,key='yes_xray_covid')
