######################
# Import libraries
######################

import pandas as pd
import streamlit as st
import altair as alt

######################
# Page Title
######################

st.write("""
# *DNA Nucleotide Count Web App*

This app counts the nucleotide composition of query DNA! and then spits out some stats about it!\n
Made by Aniket Sonawane using the Data Professor Youtube Course (Thank you professor!)

***
""")


######################
# Input Text Box
######################

#st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequences')

sequence_input = "GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)

sequence = st.text_area("Input sequence here", sequence_input, height=250)
result = st.button("Search")
if result:
  sequence = sequence.splitlines()
  sequence = ''.join(sequence)
st.write("""
***
""")

## Prints the input DNA sequence
st.header(' *Just to double check..*')
sequence

st.write("""
***
""")
         

### 1. Print dictionary

def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d

X = DNA_nucleotide_count(sequence)

#X_label = list(X)
#X_values = list(X.values())




### 2. Print text
st.subheader('*So from what you have given me:*')
st.write('There are  ' + str(X['A']) + ' adenine (A) nucleotides')
st.write('There are  ' + str(X['T']) + ' thymine (T) nucleotides')
st.write('There are  ' + str(X['G']) + ' guanine (G) nucleotides')
st.write('There are  ' + str(X['C']) + ' cytosine (C) nucleotides')

st.write("""
***
""")
         
total_length = X['A'] + X['T'] + X['G'] + X['C']
count_a = X['A']
count_t = X['T']
count_c = X['C']
count_g = X['G']

percentage_a = round((count_a / total_length) * 100)
percentage_t = round((count_t / total_length) * 100)
percentage_c = round((count_c / total_length) * 100)
percentage_g = round((count_g / total_length) * 100)

st.subheader("*Percentages %*")
st.write('Percentage of A nucleotides: ',str(percentage_a),'%')
st.write('Percentage of T nucleotides:' ,str(percentage_t), '%')
st.write('Percentage of C nucleotides :', str(percentage_c), '%') 
st.write('Percentage of G nucleotides :', str(percentage_g), '%')


st.write("""
***
""")
st.subheader("*The Guanine-Cytosine (GC) content and Predicted Melting Temperature(Tm)*")
st.write("""
The GC content has a proportional relationship with the melting temperature of the sequence

The formula used to predict the melting temperature is the simplified *Marmur and Doty* (1962) formula as shown if the length of the string is lesser than 13 nucleotides


$Tm = (wA+xT)*2 + (yG+zC)*4$ 

otherwise it is, 

$Tm= 64.9 +41*(yG+zC-16.4)/(wA+xT+yG+zC)$

*where w, x, y and z are the number of the A, T, G and C nucleotides*

""") 
st.write("""
""")
st.write("""
""")

if total_length < 13: 
  Tm = round(((X['C'] + X['G'])*4) + ((X['A']+ X['T']*2)))
else:
  Tm = round(64.9 + 41 * (((X['G'] + X['C']-16.4)/total_length)))
gc = round(((X['G'] + X['C'])/total_length)*100)
st.write("**The predicted melting temperature is**")
st.write(str(Tm), 'C')     
st.write("**The GC content is**")
st.write(str(gc), '%')

st.write("""
""")
st.write("""
""")

st.write("""
Try messing around with the sequence to verify this relationship!
***
""")


### 3. Display DataFrame
st.subheader('*Tabluar Form*')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

st.write("""
***
""")
         
### 4. Display Bar Chart using Altair
st.subheader('*Bar Chart*')
p = alt.Chart(df).mark_bar(color= 'orange').encode(
    x ='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)

st.write("""
***
""")
         
st.subheader(" *And also a Pie Chart! :100:* ")
q = alt.Chart(df).mark_arc().encode(
  theta= 'count',
  color= 'nucleotide'
)

q

st.subheader('Thank you!!!')
