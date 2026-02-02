import streamlit as st
import urllib.parse

# SAYFA AYARLARI
st.set_page_config(page_title="Çiftçi Enerji & Sulama", page_icon="⚡")

st.title("🚜 Çiftçi Proje & Enerji Destek Formu")
st.write("Lütfen aşağıdaki bilgileri doldurun, size en uygun sistemi hesaplayalım.")

# FORM ALANLARI
with st.container():
    isim = st.text_input("Ad Soyad")
    ilce = st.text_input("İlçe / Köy")
    
    col1, col2 = st.columns(2)
    with col1:
        ada = st.text_input("Ada")
    with col2:
        parsel = st.text_input("Parsel")
    
    st.divider()
    
    # "Basınçlı Sulama Sistemi" başlığı güncellendi
    sulama = st.selectbox("Kullanılan Basınçlı Sulama Sistemi", 
                          ["Damlama", "Yağmurlama", "Pivot", "Güneş Enerjili Sulama", "Diğer"])
    
    col3, col4 = st.columns(2)
    with col3:
        pompa_gucu = st.text_input("Pompa Gücü (HP veya kW)")
    with col4:
        elektrik_tuketimi = st.text_input("Yıllık Elektrik Tüketimi (kWh)")

# GÖNDERME BUTONU
st.divider()
if st.button("BİLGİLERİ HAZIRLA VE WHATSAPP'A GEÇ"):
    if isim and ilce:
        # Mesaj formatı (Ekili ürün çıkarıldı)
        mesaj = (
            f"*Yeni GES & Sulama Talebi*\n\n"
            f"👤 *İsim:* {isim}\n"
            f"📍 *Konum:* {ilce} (Ada: {ada}, Parsel: {parsel})\n"
            f"💧 *Sistem:* {sulama}\n"
            f"⚡ *Pompa Gücü:* {pompa_gucu}\n"
            f"🔌 *Yıllık Tüketim:* {elektrik_tuketimi} kWh\n\n"
            f"Bu veriler ışığında teklif ve projelendirme desteği rica ediyorum."
        )
        
        # Numaranı kontrol etmeyi unutma
        tel = "905075031990" 
        
        mesaj_kodlu = urllib.parse.quote(mesaj)
        wa_link = f"https://wa.me/{tel}?text={mesaj_kodlu}"
        
        st.success("Bilgiler hazırlandı!")
        
        st.markdown(f'''
            <a href="{wa_link}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #25D366; color: white; padding: 15px; text-align: center; border-radius: 10px; font-weight: bold; font-size: 1.1em;">
                    📱 WhatsApp üzerinden Gönder
                </div>
            </a>
            ''', unsafe_allow_html=True)
    else:
        st.error("Lütfen Ad Soyad ve İlçe kısımlarını doldurun!")