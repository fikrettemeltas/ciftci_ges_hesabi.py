import streamlit as st
import urllib.parse

# Sayfa ayarları ve ikon
st.set_page_config(page_title="Çiftçi GES Hesapla", page_icon="🚜")

# Sayfa Başlığı
st.markdown("<h2 style='text-align: center; color: #2E7D32;'>🚜 Çiftçi GES & Sulama Destek</h2>", unsafe_allow_html=True)
st.write("---")

# Bilgi Girişleri
isim = st.text_input("👤 Ad Soyad")
ilce = st.text_input("📍 İlçe / Köy")

col1, col2 = st.columns(2)
with col1:
    ada = st.text_input("🔢 Ada")
with col2:
    parsel = st.text_input("🔢 Parsel")

st.divider()

sulama = st.selectbox("💧 Basınçlı Sulama Sistemi", 
                      ["Damlama", "Yağmurlama", "Pivot", "Güneş Enerjili Sulama", "Diğer"])

pompa_hp = st.number_input("⚡ Pompa Gücü (HP)", min_value=0.0, step=0.5, value=0.0)
elektrik_tuketimi = st.text_input("🔌 Yıllık Tüketim (kWh)")

# HESAPLAMA MOTORU
if pompa_hp > 0:
    # 1 HP = 0.75 kW varsayımı ve %50 emniyet payı (1.5 katsayısı)
    önerilen_panel = pompa_hp * 0.75 * 1.5 
    st.info(f"💡 Tavsiye Edilen Panel Gücü: **~{önerilen_panel:.2f} kWp**")
else:
    önerilen_panel = 0

st.divider()

if st.button("✅ HESAPLA VE WHATSAPP'A GÖNDER", use_container_width=True):
    if isim and ilce:
        mesaj = (
            f"*Yeni GES & Sulama Talebi*\n"
            f"-------------------\n"
            f"👤 *İsim:* {isim}\n"
            f"📍 *Konum:* {ilce} ({ada}/{parsel})\n"
            f"💧 *Sistem:* {sulama}\n"
            f"⚡ *Pompa Gücü:* {pompa_hp} HP\n"
            f"☀️ *Hesaplanan Panel İhtiyacı:* {önerilen_panel:.2f} kWp\n"
            f"🔌 *Yıllık Tüketim:* {elektrik_tuketimi} kWh\n\n"
            f"Geliştiren: Ahmet Fikret Temeltaş"
        )
        
        tel = "905075031990" 
        mesaj_kodlu = urllib.parse.quote(mesaj)
        wa_link = f"https://wa.me/{tel}?text={mesaj_kodlu}"
        
        st.markdown(f'''
            <a href="{wa_link}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #25D366; color: white; padding: 18px; text-align: center; border-radius: 12px; font-weight: bold; font-size: 1.2em;">
                    📱 WhatsApp'tan Bilgileri Gönder
                </div>
            </a>
            ''', unsafe_allow_html=True)
    else:
        st.warning("Lütfen Ad Soyad ve İlçe alanlarını doldurun.")

# İMZA BÖLÜMÜ (En Alta Şık Bir Şekilde)
st.write("\n" * 5) # Biraz boşluk bırakalım
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #888888; font-style: italic; font-size: 0.9em;'>"
    "Software Developed by<br>"
    "<strong style='color: #2E7D32; font-size: 1.2em;'>Ahmet Fikret Temeltaş</strong>"
    "</p>", 
    unsafe_allow_html=True
)
