import streamlit as st
import urllib.parse
import math
from datetime import date

st.set_page_config(page_title="Pro GES Hesaplayıcı", page_icon="☀️", layout="wide")

# --- BAŞLIK VE SLOGAN ---
st.markdown("<h1 style='text-align: center; color: #1B5E20;'>☀️ Güneşle Gelen Bereket</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; color: #388E3C;'>\"Toprağınız Suya, Cebiniz Rahata Kavuşsun.\"</p>", unsafe_allow_html=True)
st.write("---")

# --- SIDEBAR: GİRİŞLER ---
with st.sidebar:
    st.header("👤 Müşteri & Proje")
    ilce = st.text_input("İlçe / Köy")
    ada_parsel = st.text_input("Ada / Parsel")
    
    st.divider()
    
    st.header("💰 Birim Fiyat Güncelleme")
    st.info("Firmadan aldığınız güncel rakamları buraya girin.")
    fiyat_panel = st.number_input("Panel Fiyatı (TL/Adet)", value=8250)
    fiyat_surucu = st.number_input("Sürücü Fiyatı (TL)", value=65000)
    fiyat_ayak = st.number_input("Panel Başı Çelik Ayak (TL)", value=1600)
    fiyat_kablo = st.number_input("Kablo Metre Fiyatı (TL)", value=70)

# --- ANA EKRAN: HESAPLAMA ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("💧 Sistem Verileri")
    pompa_kw = st.number_input("Pompa Gücü (kW)", min_value=0.0, value=37.0)
    panel_watt = st.selectbox("Panel Gücü (Watt)", [450, 545, 550, 600], index=2)

# Hesaplamalar
gereken_ges_kw = pompa_kw * 1.35 
panel_sayisi = math.ceil((gereken_ges_kw * 1000) / panel_watt)
toplam_kurulu_guc = (panel_sayisi * panel_watt) / 1000
tahmini_kablo_metraj = panel_sayisi * 3 

# Maliyetler
total_panel = panel_sayisi * fiyat_panel
total_ayak = panel_sayisi * fiyat_ayak
total_kablo = tahmini_kablo_metraj * fiyat_kablo
genel_toplam = total_panel + fiyat_surucu + total_ayak + total_kablo

with col2:
    st.subheader("📊 Özet Bilgi")
    st.write(f"**Toplam Panel:** {panel_sayisi} Adet")
    st.write(f"**Kurulu Güç:** {toplam_kurulu_guc:.2f} kWp")
    st.write(f"**Yatırım Tutarı:** {genel_toplam:,.0f} TL")

# --- MALİYET TABLOSU ---
st.subheader("📋 Teknik Detay ve Maliyet Tablosu")
tablo_verisi = f"""
| Malzeme | Miktar | Birim Fiyat | Toplam |
| :--- | :--- | :--- | :--- |
| **Güneş Paneli ({panel_watt}W)** | {panel_sayisi} Adet | {fiyat_panel:,} TL | {total_panel:,} TL |
| **Solar Sürücü** | 1 Adet | {fiyat_surucu:,} TL | {fiyat_surucu:,} TL |
| **Çelik Ayak Sistemi** | {panel_sayisi} Takım | {fiyat_ayak:,} TL | {total_ayak:,} TL |
| **Solar Kablolama** | {tahmini_kablo_metraj} Metre | {fiyat_kablo:,} TL | {total_kablo:,} TL |
| **GENEL TOPLAM** | | | **{genel_toplam:,.0f} TL** |
"""
st.markdown(tablo_verisi)
st.caption("⚠️ *Bu fiyatlar ortalama olup, uygulama detaylarına göre ±%10 değişkenlik gösterebilir.*")

# --- İMZA VE KAPANIŞ ---
st.write("---")
c1, c2 = st.columns([2, 1])
with c2:
    st.markdown(f"""
    **Hazırlayan:** **Ahmet Fikret Temeltaş** 📞 0507 503 19 90  
    📅 Tarih: {date.today().strftime('%d.%m.%Y')}
    """)

# --- WHATSAPP ---
if st.button("✅ TEKLİFİ WHATSAPP İLE GÖNDER", use_container_width=True):
    mesaj = (
        f"*☀️ GES SULAMA SİSTEMİ TEKLİFİ*\\n"
        f"---------------------------\\n"
        f"📍 *Bölge:* {ilce} / {ada_parsel}\\n"
        f"⚡ *Sistem:* {toplam_kurulu_guc:.2f} kWp / {panel_sayisi} Panel\\n"
        f"💰 *Tahmini Yatırım:* {genel_toplam:,.0f} TL\\n"
        f"---------------------------\\n"
        f"*Saygılarımla,*\\n"
        f"*Ahmet Fikret Temeltaş*\\n"
        f"📞 0507 503 19 90"
    )
    url = f"https://wa.me/905075031990?text={urllib.parse.quote(mesaj)}"
    st.markdown(f"[Mesajı Gönderilmek Üzere Hazırla]({url})")

