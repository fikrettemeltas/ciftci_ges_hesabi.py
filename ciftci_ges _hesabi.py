import streamlit as st
import urllib.parse
import math

st.set_page_config(page_title="Pro GES Hesaplayıcı", page_icon="☀️")

st.markdown("<h2 style='text-align: center; color: #1B5E20;'>☀️ Gelişmiş GES & Pompa Hesaplayıcı</h2>", unsafe_allow_html=True)
st.write("---")

# Giriş Bölümü
with st.sidebar:
    st.header("👤 Müşteri Bilgileri")
    isim = st.text_input("Ad Soyad")
    ilce = st.text_input("İlçe / Köy")
    ada_parsel = st.text_input("Ada / Parsel")

col1, col2 = st.columns(2)

with col1:
    st.subheader("💧 Pompa & Su Verileri")
    hesap_yontemi = st.radio("Hesap Yöntemi", ["Pompa Gücünü Biliyorum", "Debi ve Derinlikten Hesapla"])
    
    if hesap_yontemi == "Pompa Gücünü Biliyorum":
        pompa_kw = st.number_input("Pompa Gücü (kW)", min_value=0.0, value=37.0, step=1.0)
    else:
        debi = st.number_input("İstenen Debi (m³/saat)", min_value=0.0, value=50.0)
        derinlik = st.number_input("Toplam Basma Yüksekliği (Metre)", min_value=0.0, value=100.0)
        # Hidrolik güç formülü (Verim dahil yaklaşık)
        pompa_kw = (debi * derinlik) / 200 # Pratik katsayı

with col2:
    st.subheader("⚙️ Panel Özellikleri")
    panel_watt = st.selectbox("Panel Gücü (Watt)", [450, 545, 550, 600], index=2)
    emniyet_katsayisi = 1.45 # Kayıplar ve sabah/akşam çalışma payı

# HESAPLAMALAR
gereken_ges_kw = pompa_kw * emniyet_katsayisi
panel_sayisi = math.ceil((gereken_ges_kw * 1000) / panel_watt)

# Sürücü ve Alan Hesapları
surucu_kw = pompa_kw * 1.2 # Bir üst sınıf sürücü önerilir
toplam_alan = panel_sayisi * 2.6 # 550W panel yaklaşık 2.58 m2'dir

# Dizilim (String) Önerisi (Ortalama 800V DC girişe göre)
# 550W paneller genelde 18-20'li seriler halinde bağlanır
seri_sayisi = 18
paralel_sayisi = math.ceil(panel_sayisi / seri_sayisi)

st.divider()

# SONUÇ EKRANI
st.success(f"### 📊 Teknik Analiz Sonuçları")
res_col1, res_col2, res_col3 = st.columns(3)

with res_col1:
    st.metric("Gereken GES Gücü", f"{gereken_ges_kw:.1f} kWp")
    st.metric("Panel Adedi", f"{panel_sayisi} Adet")

with res_col2:
    st.metric("Sürücü Gücü", f"{surucu_kw:.1f} kW")
    st.metric("Tahmini Alan", f"{toplam_alan:.0f} m²")

with res_col3:
    st.metric("Dizilim (String)", f"{paralel_sayisi} x {seri_sayisi}")
    st.info("💡 Öneri: Panelleri 18'li seriler halinde bağlayın.")

st.divider()

# WHATSAPP GÖNDERİMİ
if st.button("✅ TEKNİK RAPORU WHATSAPP'A GÖNDER", use_container_width=True):
    if isim and ilce:
        mesaj = (
            f"*GES SULAMA TEKNİK RAPORU*\n"
            f"---------------------------\n"
            f"👤 *Müşteri:* {isim} / {ilce}\n"
            f"🔢 *Ada Parsel:* {ada_parsel}\n"
            f"⚡ *Pompa Gücü:* {pompa_kw:.1f} kW\n"
            f"☀️ *Kurulacak GES:* {gereken_ges_kw:.1f} kWp\n"
            f"🧩 *Panel:* {panel_sayisi} Adet {panel_watt}W\n"
            f"🔌 *Sürücü:* {surucu_kw:.1f} kW Solar Driver\n"
            f"📐 *Gereken Alan:* ~{toplam_alan:.0f} m²\n"
            f"⛓️ *Dizilim:* {paralel_sayisi} paralel x {seri_sayisi} seri\n"
            f"---------------------------\n"
            f"Hazırlayan: Ahmet Fikret Temeltaş"
        )
        
        tel = "905075031990" 
        wa_link = f"https://wa.me/{tel}?text={urllib.parse.quote(mesaj)}"
        st.markdown(f'<a href="{wa_link}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:15px;text-align:center;border-radius:10px;">WhatsApp Mesajını Onayla</div></a>', unsafe_allow_html=True)
    else:
        st.error("Lütfen isim ve ilçe bilgilerini girin!")
