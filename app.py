import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Application Modernization Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 36px;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 10px;
    }
    .main-subtitle {
        text-align: center;
        font-size: 18px;
        color: #666;
        margin-bottom: 40px;
    }
    .info-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }
    .info-card h2 {
        margin: 0;
        font-size: 48px;
        font-weight: 700;
    }
    .info-card p {
        margin: 10px 0 0 0;
        font-size: 18px;
        opacity: 0.9;
    }
    .phase-card {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        border-left: 5px solid;
    }
    .phase-title {
        font-size: 24px;
        font-weight: 600;
        margin-bottom: 10px;
    }
    .phase-subtitle {
        font-size: 14px;
        color: #666;
        margin-bottom: 15px;
    }
    .phase-stats {
        font-size: 32px;
        font-weight: 700;
        color: #1a1a1a;
    }
    .category-list {
        margin-top: 15px;
        padding-left: 20px;
    }
    .category-list li {
        margin-bottom: 8px;
        color: #555;
        line-height: 1.6;
    }
    .category-name {
        font-weight: 600;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-title">📊 Application Modernization Dashboard</div>
<div class="main-subtitle">แดชบอร์ดรายงานโครงการ Modernization</div>
""", unsafe_allow_html=True)

col_center = st.columns([1, 2, 1])[1]
with col_center:
    st.markdown("""
    <div class="info-card">
        <h2>349</h2>
        <p>จำนวน Application ทั้งหมด</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="phase-card" style="border-left-color: #90C9A5;">
        <div class="phase-title">📈 Phase 1: 2568-2570</div>
        <div class="phase-subtitle">การดำเนินการทุกระบบ</div>
        <div class="phase-stats">349 แอปพลิเคชัน</div>
        <div class="category-list">
            <ul>
                <li><span class="category-name">Retain (184)</span> - การคงระบบไว้ที่เดิม</li>
                <li><span class="category-name">Rehost (123)</span> - การย้ายระบบแบบคงสภาพเดิม</li>
                <li><span class="category-name">Retire (22)</span> - การยุติการใช้งานระบบ</li>
                <li><span class="category-name">Replatform (11)</span> - การย้ายและปรับเปลี่ยนแพลตฟอร์ม</li>
                <li><span class="category-name">Repurchase (9)</span> - การจัดหาบริการมาทดแทน</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="phase-card" style="border-left-color: #A8D5E4;">
        <div class="phase-title">📊 Phase 2: 2570-2571</div>
        <div class="phase-subtitle">การดำเนินการต่อเนื่อง</div>
        <div class="phase-stats">114 แอปพลิเคชัน</div>
        <div class="category-list">
            <ul>
                <li><span class="category-name">Refactor (54)</span> - การปรับปรุงโค้ด</li>
                <li><span class="category-name">Retire (38)</span> - การยุติการใช้งานระบบ</li>
                <li><span class="category-name">Rehost (15)</span> - การย้ายระบบแบบคงสภาพเดิม</li>
                <li><span class="category-name">Replatform (4)</span> - การย้ายและปรับเปลี่ยนแพลตฟอร์ม</li>
                <li><span class="category-name">Repurchase (2)</span> - การจัดหาบริการมาทดแทน</li>
                <li><span class="category-name">Re-architect (1)</span> - การปรับปรุงสถาปัตยกรรมใหม่</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.divider()

st.markdown("### 📋 คำอธิบาย Categories")

col_desc1, col_desc2 = st.columns(2)

with col_desc1:
    st.markdown("""
    #### Phase 1 Categories:
    - **Rehost** - การย้ายระบบแบบคงสภาพเดิม (Lift and Shift)
    - **Replatform** - การย้ายระบบและปรับเปลี่ยนแพลตฟอร์ม (Lift and Reshape)
    - **Repurchase** - การจัดหาบริการมาทดแทน
    - **Retain** - การคงระบบไว้ที่เดิม
    - **Retire** - การยุติการใช้งานระบบ
    """)

with col_desc2:
    st.markdown("""
    #### Phase 2 Categories:
    - **Refactor** - การปรับปรุงโค้ด
    - **Re-architect** - การปรับปรุงสถาปัตยกรรมใหม่
    - **Rehost** - การย้ายระบบแบบคงสภาพเดิม (Lift and Shift)
    - **Replatform** - การย้ายระบบและปรับเปลี่ยนแพลตฟอร์ม
    - **Repurchase** - การจัดหาบริการมาทดแทน
    - **Retire** - การยุติการใช้งานระบบ
    """)

st.markdown("<br>", unsafe_allow_html=True)
st.info("👈 กรุณาเลือก Phase ที่ต้องการดูรายละเอียดจากแถบด้านซ้าย")
