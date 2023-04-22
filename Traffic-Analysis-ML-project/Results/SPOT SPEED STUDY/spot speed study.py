import numpy as np 
import pandas as pd
import os
import matplotlib.pyplot as plt
import dataframe_image as dfi
from fpdf import FPDF
from pdfrw import PageMerge, PdfReader, PdfWriter

#relative path setting

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.chdir(path)

df = pd.read_excel("speed_data.xlsx")
print(df)

min_speed = df['Speed (Kmph)'].min()
max_speed = df['Speed (Kmph)'].max()
print(min_speed,max_speed)

df1 = pd.DataFrame(columns=['Speed range','Mid','Frequency'])

count =0
min = 0
max = 10

while (count < df['Speed (Kmph)'].count()): 
    
    d1 = str(min) + '-' + str(max)
    d2 = int((max + min)/2)
    
    a1 = df['Speed (Kmph)'].values <= min 
    a2 = df['Speed (Kmph)'].values <= max 
          
    d3 = np.flatnonzero(a2).size  - np.flatnonzero(a1).size

    data = {'Speed range' : [d1], 'Mid' : [d2], 'Frequency' : [d3]}
    df2 = pd.DataFrame(data)
    df1 = pd.concat([df1,df2], ignore_index = True )
    #display(df3)

    count += d3
    min += 10
    max += 10
       

dfi.export(df1.style.background_gradient(), "df1.png")


i = 0
e = 0
d=[]

while(e < df['Speed (Kmph)'].count()):
 
    e += df1['Frequency'][i]
    d.append(e)
    i+=1
     
df1['ΣF'] = d

df1[f'%F'] = (df1['Frequency']/df['Speed (Kmph)'].count())*100
df1[f'%ΣF'] = (df1["ΣF"]/df['Speed (Kmph)'].count())*100
print(df1)

median_speed = df['Speed (Kmph)'].median()
print("median speed = ",median_speed)

mode_speed = df['Speed (Kmph)'].mode()
print("modal-speed =\n",mode_speed)

df1['f * V']= df1['Mid']*df1['Frequency']
print(df1)

mean_speed = df1['f * V'].sum()/df1['Frequency'].sum()
print('Mean-Speed = ',mean_speed)

df1['V-Vm'] = df1['Mid'] - mean_speed
df1['(V-Vm)^2'] = df1['V-Vm']*df1['V-Vm']
df1['f*(V-Vm)^2'] = df1['Frequency']*df1['(V-Vm)^2']
print(df1) 

Std = df1['f*(V-Vm)^2'].sum()/df1['Frequency'].sum()
print("Standard Deviation = ",Std**0.5) 

s50 = df1['%ΣF'].values <= 50
s85 = df1['%ΣF'].values <= 85
s98 = df1['%ΣF'].values <= 98

# getting non zero indices
pos50 = np.flatnonzero(s50)
pos85 = np.flatnonzero(s85)
pos98 = np.flatnonzero(s98)


print("50 percentile speed is = ",df1['Mid'][pos50[-1]],"m/s")
print("85 percentile speed is = ",df1['Mid'][pos85[-1]],"m/s")
print("98 percentile speed is = ",df1['Mid'][pos98[-1]],"m/s")


con = mean_speed + 3*Std
print("confidence bounds =",con)

# plots 

x = df1['Mid']
y = df1['Frequency']

plt.xlabel("Speed kmph")
plt.ylabel("Frequency")
plt.title("Spot Speed Study")
plt.bar(x,y,width = 3,color = 'blue')
plt.savefig("barchart.png", format="png", bbox_inches="tight")
#plt.show()
plt.close()

x = df1['Mid']
y = df1['%ΣF']

plt.xlabel("Speed kmph")
plt.ylabel(" % Cumulative Frequency")
plt.title("Spot Speed Study")
plt.plot(x,y, color = 'blue')
plt.axhline(y=98, color="black", linestyle="-",label = '98 percentile')
plt.axhline(y=85, color="black", linestyle="--",label = '85 percentile')
plt.axhline(y=50, color="black", linestyle="-.",label = '50 percentile')
plt.axhline(y=15, color="black", linestyle=":",label = '15 percentile')
plt.legend()
plt.savefig("graph.png", format="png", bbox_inches="tight")
#plt.show()

# creating result_s.pdf

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial','BU',20)
pdf.cell(0, 10,'SPOT SPEED-STUDY',ln = 1 ,border = 1,align = 'C')



pdf.cell(0,20, ln = 1)
pdf.set_font('Arial','B',15)
pdf.cell(100, 10, 'Maximum Speed found is ' + str(int(max_speed)) + 'Kmph',ln = 0 ,border = 0)

pdf.set_font('Arial','B',15)
pdf.cell(100, 10, 'Minimum Speed found is ' + str(int(min_speed)) + 'Kmph' ,ln = 1 ,border = 0)

pdf.cell(0,10,ln = 1)
pdf.set_font('Arial','BIU',17)
pdf.cell(0,10,'Statistical Speeds are :- ',ln =1,border = 0)

pdf.cell(0,5, ln = 1)
pdf.set_font('Arial','B',15)
pdf.cell(0, 10, 'Mean Speed is ' + str(int(mean_speed)) + 'Kmph' ,ln = 1 , border = 0, align = 'C')

pdf.set_font('Arial','B',15)
pdf.cell(0, 10, '   Median Speed is ' + str(int(median_speed)) + 'Kmph' ,ln = 1 ,border = 0, align = 'C')

pdf.set_font('Arial','B',15)
pdf.cell(0, 10, ' Modal Speed is/are '+ str([i for i in mode_speed]) + ' Kmph' ,ln = 1 ,border = 0, align = 'C')

pdf.cell(0,5, ln = 1)
pdf.set_font('Arial','B',15)
pdf.cell(0, 10, 'Standard Deviation is found to be ' + str(Std*0.05) ,ln = 1 ,border = 0, align = 'C')

pdf.cell(0,10,ln=1)
pdf.set_font('Arial','BIU',17)
pdf.cell(100,10, 'Percentile Speeds are :-',ln = 1 ,border = 0)

pdf.set_font('Arial','B',15)
pdf.cell(0,15, ln = 1)
pdf.cell(0, 5,'50 percentile speed is : ' + str(df1['Mid'][pos50[-1]]) + 'Kmph' ,ln = 1 , border = 0, align = 'C')

pdf.cell(0,5, ln = 1)
pdf.cell(0, 5,'85 percentile speed is : ' + str(df1['Mid'][pos85[-1]]) + 'Kmph' ,ln = 1 ,border = 0, align = 'C')

pdf.cell(0,5,ln = 1)
pdf.cell(0, 5,'98 percentile speed is : ' + str(df1['Mid'][pos98[-1]]) + 'Kmph' ,ln = 1 ,border = 0, align = 'C')

pdf.cell(0,5,ln = 1)
pdf.set_font('Arial','BUI',18)
pdf.cell(0,10,'PLOTS',ln = 1)

pdf.cell(50,5,ln = 1)
pdf.image('barchart.png', x = 10, y = 200, w = 80 ,h =80, type = '', link = '',)
pdf.image('graph.png', x = 120, y = 200, w = 80 ,h =80 , type = '', link = '',)

pdf.add_page()

pdf.set_font('Arial','BUI',18)
pdf.cell(0,10,'Speed Data :-',ln = 1)
pdf.cell(0,10, ln = 1)
pdf.cell(40,30,ln = 0)
pdf.image('df1.png', x = None, y = None, type = '', link = '', )

pdf.output(r'result_s.pdf', 'F')

# merging pdfs
from pypdf import PdfMerger

pdfs = [r'..\VOLUME STUDY\result_v.pdf' , r'result_s.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(r"..\result.pdf")
merger.close()