
![Logo](https://github.com/esmanp/gorengoz/blob/main/logo.png?raw=true)
  
# Gören Göz

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Streamlit App](https://docs.streamlit.io/logo.svg)](https://docs.streamlit.io)

Gören Göz, ses ve dijital medya ürünlerinin(radyo programları,videolar vs) içerikleri analiz ederek kullanıcılara sunan online bir Doğal Dil İşleme aracıdır. İçeriklerin öncesinde görülerek karar alınabilmesine yönelik yardımcı olabilmek amacıyla geliştirilmiştir.

![uygulama](https://github.com/esmanp/gorengoz/blob/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC.png?raw=true)


## Problem Tanımı

İnternet Üzerinden TV (OTT), TV/video içeriğinin doğrudan internetten aktarılması anlamına gelmektedir. Video akış veya kayıtlı video (VOD) formatında sunulabildiği gibi farklı türleri de mevcuttur: OTT video akışı, OTT müzik akışı, OTT mesajlaşma ve OTT sesli arama platformları.

Bu platformlar aracılığı ile yayınlanan kimi ses ve dijital medya ürünlerinin (radyo programları, videolar vs.) intihara yönlendirme, çocuk istismarı, müstehcenlik, taraflı ırkçı veya herhangi bir etnik grubu yeren söylemler barındırabilmektir.

Bu açıdan içeriğin analizi , önem kazanmaktadır.

Sisteme yüklemiş olduğunuz dosyalar 'Haraket ve Aşağılama İçerir','Irkçı Söylem İçerir', 'Cinsiyetçi Söylem İçerir','Küfür ve Kötü Söz İçerir' veya 'Temiz İçerik' olacak şekilde tespit edilerek tarafınıza sunulmaktadır.


Bir video dosyasının içeriğini kontrol etmek isterseniz ' Video İçeriğini Analiz Et';
ses dosyasının içeriğini kontrol etmek istemeniz dahilinde ise 'Ses İçeriğini Analiz Et'
kısımlarına tıklamanız yeterli olacaktır.


## Katkılarımız

### Hugging Face Modeli
Oluşturulan veri modelini MIT lisansı ile uluslararası doğal dil platformu olan huggingface te paylaşarak Türkçe modellere yeni ve başarılı bir model eklenilmesi sağlanılmıştır. 

[ennp/bert-turkish-text-classification-cased](https://huggingface.co/ennp/bert-turkish-text-classification-cased)


![Model](https://github.com/esmanp/gorengoz/blob/main/huggingfacemodel.png?raw=true)


### Site 
Demo:
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gorengoz.streamlit.app)
  

##### Bu web uygulamasını kendi bilgisayarınızda yeniden oluşturmak için aşağıdaki adımları takip edebilirsiniz: 



```bash
  wget https://github.com/esmanp/gorengoz/blob/main/requirements.txt

```

```bash
pip install -r requirements.txt
```

```bash
  wget https://github.com/esmanp/gorengoz/archive/refs/heads/main.zip
```

```bash
 unzip main.zip
```

```bash
 streamlit run app2.py
```

  
    


  
