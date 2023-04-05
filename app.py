import streamlit as st
from streamlit_option_menu import option_menu
import speech_recognition as sr
#import numpy as np
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
#import pandas as pd
from PIL import Image


col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    image = Image.open('logo.png')
    st.image(image)

with col3:
    st.write(' ')


hide_st_style= """ <style> #MainMenu {visibility: hidden;} 
footer {visibility: hidden;} 
header {visibility: hidden;} 
<style> """
st.markdown(hide_st_style,unsafe_allow_html=True)


selected = option_menu(None, ["Anasayfa","Video İçeriğini Analiz Et","Ses İçeriğini Analiz Et"],
                         icons=['house', 'play-btn','soundwave'],#volume-up
                         #menu_icon="spellcheck", #ui-checks
                         default_index=0,
                         orientation="horizontal",
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "#9c8e74", "font-size": "20px"}, 
         "nav-link-selected": {"background-color": "#ebddc0"},
    }
    
    )


r = sr.Recognizer()
def transcribe_large_audio(path):
    """Split audio into chunks and apply speech recognition"""
    # Open audio file with pydub
    sound = AudioSegment.from_wav(path)
    # Split audio where silence is 700ms or greater and get chunks
    chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=-16, keep_silence=500)
    
    # Create folder to store audio chunks
    folder_name = "audio-chunks"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    
    whole_text = ""
    # Process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # Export chunk and save in folder
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # Recognize chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # Convert to text
            try:
                text = r.recognize_google(audio_listened,language="tr-tr")
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # Return text for all chunks
    return whole_text



def predict(text):
    tokenizer= AutoTokenizer.from_pretrained("ennp/bert-turkish-text-classification-cased")
    # build and load model, it take time depending on your internet connection
    model= AutoModelForSequenceClassification.from_pretrained("ennp/bert-turkish-text-classification-cased",num_labels=5)
    model=pipeline("sentiment-analysis", model=model,tokenizer=tokenizer)
    code_to_label={
    'LABEL_0': 'Haraket ve Aşağılama İçerir ',
    'LABEL_1': 'Irkçı Söylem İçerir ',
    'LABEL_2': 'Cinsiyetçi Söylem İçerir',
    'LABEL_3': 'Küfür ve Kötü Söz İçerir ',
    'LABEL_4': 'Temiz İçerik ' }
    code_to_label[model(text)[0]['label']]

def get_split(text):
    l_total= []
    l_partial=[]
    if len(text.split())//150 >0:
        n=len(text.split())//150
    else:
        n=1
    for w in range(n):
        if w ==0:
            l_partial=text.split()[:200]
            l_total.append(" ".join(l_partial))
        else:
            l_partial=text.split()[w*150:w*150+200]
            l_total.append(" ".join(l_partial))
    return l_total

import ffmpeg
def get_wav(video:str):
	#com1 = f"ffmpeg -i {video} -vn speech.wav"
	#com2 = "ffmpeg -i speech.mp3 speech.wav"
	#os.system(com1)
    file_var=AudioSegment.from_file(video,format="mp4")
    file_var.export("speech.wav",format='wav')
	#os.system(com2)
	
if selected == "Anasayfa":
    #st.write(f"**You selected {selected}**")
    st.markdown("""İnternet Üzerinden TV (OTT), 
    TV/video içeriğinin doğrudan internetten aktarılması anlamına gelmektedir. Video akış veya kayıtlı video (VOD)
    formatında sunulabildiği gibi farklı türleri de mevcuttur: OTT video akışı, OTT müzik akışı, OTT mesajlaşma ve
    OTT sesli arama platformları.""")
    
    st.markdown("""Bu platformlar aracılığı ile yayınlanan kimi ses ve dijital medya ürünlerinin (radyo programları, videolar vs.)  intihara yönlendirme, çocuk istismarı, müstehcenlik, 
    taraflı  ırkçı  veya herhangi bir etnik grubu yeren söylemler barındırabilmektir.""")
    
    st.markdown("""Bu açıdan içeriğin analizi , önem kazanmaktadır.""")
    
    st.markdown(""" **Gören Göz uygulaması, içeriklerin öncesinde görülerek karar alınabilmesine yönelik yardımcı olabilmek amacıyla
    geliştirilmiştir.**""") 

    st.markdown("""Sisteme yüklemiş olduğunuz dosyalar **'Haraket ve Aşağılama İçerir'**,**'Irkçı Söylem İçerir'**,
    **'Cinsiyetçi Söylem İçerir'**,**'Küfür ve Kötü Söz İçerir'** veya **'Temiz İçerik'** olacak şekilde 
    tespit edilerek tarafınıza sunulmaktadır.""")

    st.markdown("""Bir **video dosyasının içeriğini kontrol etmek isterseniz**""") 
    image=Image.open('video.png')
    st.image(image)
    st.markdown("""**ses dosyasının içeriğini kontrol etmek istemeniz** dahilinde ise """) 
    image=Image.open('ses.png')
    st.image(image)
    st.markdown("""kısımlarına tıklamanız yeterli olacaktır. """) 

if selected == "Video İçeriğini Analiz Et":
    #st.markdown(f"**You selected {selected}**")
    #from pydub import AudioSegment
    st.markdown("##### İçeriğini Görmek İstediğiniz Video Dosyasını(mp4 formatında) Yükleyiniz:")
    video=st.file_uploader("Dosyanızı yükleyip 'Browse File' butonunu tıklayınız.",type=["mp4"])
    if st.button("Analiz Et/İncele"):
        if video is not None:
            st.success("İçerik İnceleniyor Lütfen Bekleyiniz.")
            get_wav(video)
            text=transcribe_large_audio("speech.wav")
            #st.markdown(text)
            #st.markdown(predict(get_split(text)))
            predict(get_split(text))
        else:
            st.sidebar.error("Lütfen Dosyayı Yükleyiniz! ")

if selected == "Ses İçeriğini Analiz Et":
    #st.markdown(f"**You selected {selected}**")
    st.markdown("##### İçeriğini  Görmek İstediğiniz Ses Dosyasını(wav formatında) Yükleyiniz:")
    ses=st.file_uploader("Dosyanızı yükleyip 'Browse File' butonunu tıklayınız.",type=["wav"])
    if st.button("Analiz Et/İncele"):
        if ses is not None:
            st.success("İçerik İnceleniyor Lütfen Bekleyiniz.")
            text=transcribe_large_audio(ses)
            #st.markdown(text)
            #st.markdown(predict(get_split(text)))
            predict(get_split(text))
        else:
            st.sidebar.error("Lütfen Dosyayı Yükleyiniz!")




