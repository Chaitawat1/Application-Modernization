import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ***************************************************************
# 1. การตั้งค่าหน้าเพจหลัก (ใช้สำหรับ Dashboard)
# ***************************************************************
st.set_page_config(page_title="Application Modernization Dashboard",
                   page_icon="📊",
                   layout="wide")

# ***************************************************************
# 2. CSS Styles (รวม CSS จากทั้งสองชุดโค้ด)
# ***************************************************************
st.markdown("""
<style>


.st-emotion-cache-1jmveez, .st-emotion-cache-z5xscj, .block-container { 
    padding-top: 0rem !important; /* ล้าง Padding ด้านบน */
    margin-top: 0rem !important;  /* ล้าง Margin ด้านบน */
}

div[data-testid="stVerticalBlock"] > div:first-child {
    padding-top: 0px !important; 
    margin-top: 0px !important;
}

section.main { 
    padding-top: 0rem !important;
}

header[data-testid="stHeader"] {
    height: 0px !important;
    visibility: hidden !important;
}

.main-title { 
    margin-top: 0px !important; 
    padding-top: 10px !important; 
}
     
    .main-title { text-align: center; font-size: 36px; font-weight: 700; color: #1a1a1a; margin-bottom: 5px; }
    .main-subtitle { text-align: center; font-size: 18px; color: #666; margin-bottom: 20px; }
    .stTabs [data-baseweb="tab-list"] {
        max-width: 1000px; 
        margin: auto;
    }

    .stTabs [data-baseweb="tab"] {
        flex-grow: 1; 
        text-align: center;
        padding: 10px 20px;
        border-radius: 8px 8px 0 0;
        font-weight: 600;
    }
    .info-card { 
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
        padding: 5px; border-radius: 13px; color: white; text-align: center; margin-bottom: 10px; 
        width: 600px; margin: 0 auto;
        
    }
    .info-card h2 { margin: 0; font-size: 36px; font-weight: 600; }

    /* CSS สำหรับ Card รายละเอียด Phase (category-card) */
    .category-card {
        background-color: white; padding: 20px; border-radius: 8px; border-left: 5px solid;
        box-shadow: 0 2px 4px rgba(0.04,0,0,0.09); height: 100%; margin-bottom: 20px;
    }
    .card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
    .card-title { font-size: 18px; font-weight: 600; color: #333; margin: 0; }
    .card-subtitle { font-size: 16px; color: #666; margin: 5px 0 15px 0; }
    .card-percentage { 
        background-color: #f0f0f0; padding: 4px 12px; border-radius: 12px; 
        font-size: 13px; color: #666; font-weight: 500; 
    }
    .card-number { font-size: 36px; font-weight: 500; color: #1a1a1a; margin: 1px 0; line-height: 1; }
    .card-description { font-size: 15px; color: #666; line-height: 1.5; margin-top: 10px; }
    .overview-section { text-align: center; margin-bottom: 30px; }
    .overview-title { font-size: 28px; font-weight: 600; color: #1a1a1a; margin-bottom: 5px; }
    .overview-subtitle { font-size: 16px; color: #666; }
    .stDataFrame .ag-cell-value {
        white-space: pre-wrap !important; /* บังคับให้ข้อความตัดคำ */
        word-break: break-word !important; /* ตัดคำยาวๆ ที่ไม่มีช่องว่าง */
        line-height: 1.4; /* ปรับระยะห่างบรรทัดให้เหมาะสมเมื่อมีการตัดคำ */
        padding-top: 5px !important;
        padding-bottom: 5px !important;
    }
    
</style>
""",
            unsafe_allow_html=True)

# ***************************************************************
# 3. ส่วน Title และ Card หลัก (รวม Application ทั้งหมด)
# ***************************************************************
st.markdown("""
<div class="main-title">📊 Application Modernization Dashboard</div>
""",
            unsafe_allow_html=True)

# Card 349 อยู่ตรงกลาง
col_center = st.columns([1, 2, 1])[1]
with col_center:
    st.markdown("""
    <div class="info-card">
        <h2> 349 Application </h2> 
    </div>
    """,
                unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ***************************************************************
# 4. สร้าง Tabs สำหรับสลับ Phase
# ***************************************************************
tab1, tab2 = st.tabs(["📈 Phase 1: 2569-2570", "📊 Phase 2: 2570-2571"])

# ===============================================================
# TAB 1: เนื้อหา Phase 1
# ===============================================================
with tab1:
    # นำเข้าโค้ด Phase 1 (จากโค้ดที่คุณให้มาก่อนหน้า)

    st.markdown("""
    <div class="overview-section">
        <div class="overview-title">Phase 1: 2569-2570</div>
        <div class="overview-subtitle">รวม 349 แอปพลิเคชัน</div>
    </div>
    """,
                unsafe_allow_html=True)

    phase1_data = [{
        'category': 'Retain',
        'icon': '⭕',
        'subtitle': 'คงระบบไว้ที่เดิม',
        'count': 184,
        'percentage': 52.72,
        'description':
        'การคงระบบงานในสภาพแวดล้อมเดิม เนื่องจากยังไม่เหมาะสมต่อการย้าย อาจเป็นเหตุผลด้านความมั่นคงปลอดภัย หรือข้อจำกัดเชิงเทคนิค',
        'color': '#A8C5E4'
    }, {
        'category': 'Rehost',
        'icon': '🔄',
        'subtitle': 'Lift & Shift',
        'count': 123,
        'percentage': 35.24,
        'description':
        'การย้ายระบบงานหรือข้อมูลขึ้นสู่ระบบคลาวด์โดยไม่มีการแก้ไขระบบงาน (Lift & Shift) และคงสถาปัตยกรรมเดิมไว้',
        'color': '#90C9A5'
    }, {
        'category': 'Retire',
        'icon': '🗑️',
        'subtitle': 'ยกเลิก/ยุติระบบที่ไม่จำเป็น',
        'count': 22,
        'percentage': 6.3,
        'description':
        'การยุติหรือยกเลิกระบบงานที่หมดความจำเป็น ลดความซ้ำซ้อน และลดภาระค่าใช้จ่ายในการดูแลระบบ ',
        'color': '#C5A8E4'
    }, {
        'category': 'Replatform',
        'icon': '⚙️',
        'subtitle': 'Tinker & Shift',
        'count': 11,
        'percentage': 3.15,
        'description':
        'การย้ายแอปพลิเคชันไปยัง Cloud พร้อมกับการปรับปรุงบางส่วน เพื่อใช้ประโยชน์จากบริการจัดการของ Cloud (Managed Services)',
        'color': '#8DD9D9'
    }, {
        'category': 'Repurchase',
        'icon': '🛒',
        'subtitle': 'ใช้ SaaS หรือ COTS แทนระบบเดิม',
        'count': 9,
        'percentage': 2.58,
        'description':
        'การเลิกใช้ระบบงานเดิมและเปลี่ยนไปใช้บริการซอฟต์แวร์สำเร็จรูป หรือ บริการรูปแบบซอฟต์แวร์เป็นบริการ (SaaS) แทน',
        'color': '#F4A7B9'
    }]

    row1_cols_p1 = st.columns(3)
    for idx, item in enumerate(phase1_data[:3]):
        with row1_cols_p1[idx]:
            st.markdown(f"""
            <div class="category-card" style="border-left-color: {item['color']};">
                <div class="card-header">
                    <div>
                        <div class="card-title">{item['icon']} {item['category']}</div>
                        <div class="card-subtitle">{item['subtitle']}</div>
                    </div>
                    <div class="card-percentage">{item['percentage']}%</div>
                </div>
                <div class="card-number">{item['count']}</div>
                <div class="card-description">{item['description']}</div>
            </div>
            """,
                        unsafe_allow_html=True)

    row2_cols_p1 = st.columns([1, 1, 1])
    for idx, item in enumerate(phase1_data[3:]):
        with row2_cols_p1[idx]:
            st.markdown(f"""
            <div class="category-card" style="border-left-color: {item['color']};">
                <div class="card-header">
                    <div>
                        <div class="card-title">{item['icon']} {item['category']}</div>
                        <div class="card-subtitle">{item['subtitle']}</div>
                    </div>
                    <div class="card-percentage">{item['percentage']}%</div>
                </div>
                <div class="card-number">{item['count']}</div>
                <div class="card-description">{item['description']}</div>
            </div>
            """,
                        unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.divider()

    st.subheader("📊 ภาพรวมข้อมูล Phase 1")

    df_phase1 = pd.DataFrame(phase1_data)
    df_phase1 = df_phase1[['category', 'count', 'percentage', 'description']]
    df_phase1.columns = ['Category', 'จำนวน', 'เปอร์เซ็นต์', 'คำอธิบาย']

    col_chart1_p1, col_chart2_p1 = st.columns(2)

    with col_chart1_p1:
        st.markdown("#### สัดส่วนการแบ่ง Category")
        colors_p1 = [item['color'] for item in phase1_data]
        fig_pie_p1 = go.Figure(data=[
            go.Pie(
                labels=[item['category'] for item in phase1_data],
                values=[item['count'] for item in phase1_data],
                marker=dict(colors=colors_p1),
                textposition='auto',
                textinfo='label+percent',
                hovertemplate=
                '<b>%{label}</b><br>จำนวน: %{value}<br>เปอร์เซ็นต์: %{percent}<extra></extra>'
            )
        ])
        fig_pie_p1.update_layout(height=400,
                                 showlegend=False,
                                 margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig_pie_p1, use_container_width=True)

    with col_chart2_p1:
        st.markdown("#### จำนวน Applications ตาม Category")
        fig_bar_p1 = go.Figure(data=[
            go.Bar(x=[item['category'] for item in phase1_data],
                   y=[item['count'] for item in phase1_data],
                   text=[
                       f"{item['count']}<br>({item['percentage']}%)"
                       for item in phase1_data
                   ],
                   textposition='outside',
                   marker=dict(color=colors_p1),
                   hovertemplate='<b>%{x}</b><br>จำนวน: %{y}<extra></extra>')
        ])
        fig_bar_p1.update_layout(height=400,
                                 xaxis_title="",
                                 yaxis_title="จำนวน Applications",
                                 showlegend=False,
                                 margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig_bar_p1, use_container_width=True)

    st.divider()
    st.markdown("#### 📋 ตารางสรุปข้อมูล Phase 1")
    df_display_p1 = df_phase1.copy()
    df_display_p1['เปอร์เซ็นต์'] = [f"{x}%" for x in df_display_p1['เปอร์เซ็นต์']]
    st.dataframe(df_display_p1,
                 use_container_width=True,
                 hide_index=True,
                 column_config={
                     "Category":
                     st.column_config.TextColumn("Category", width="small"),
                     "จำนวน":
                     st.column_config.NumberColumn("จำนวน", width="small"),
                     "เปอร์เซ็นต์":
                     st.column_config.TextColumn("เปอร์เซ็นต์", width="small"),
                     "คำอธิบาย":
                     st.column_config.TextColumn("คำอธิบาย", width="large")
                 })
    st.info(
        f"**รวมทั้งหมด Phase 1: {df_phase1['จำนวน'].sum()} Applications (100%)**"
    )

# ===============================================================
# TAB 2: เนื้อหา Phase 2 (โค้ดที่คุณให้มาล่าสุด)
# ===============================================================
with tab2:
    st.markdown("""
    <div class="overview-section">
        <div class="overview-title">Phase 2: 2570-2571</div>
        <div class="overview-subtitle">รวม 114 แอปพลิเคชัน (จาก 349)</div>
    </div>
    """,
                unsafe_allow_html=True)

    phase2_data = [{
        'category': 'Refactor',
        'icon': '⚙️',
        'subtitle': 'การปรับปรุงโค้ด',
        'count': 54,
        'percentage': 15.47,
        'description':
        'การปรับปรุงโค้ดเพื่อเพิ่มประสิทธิภาพและความยืดหยุ่นของระบบ โดยไม่เปลี่ยนแปลงฟังก์ชันการทำงานหลัก',
        'color': '#A8D5E4'
    }, {
        'category': 'Retire',
        'icon': '🗑️',
        'subtitle': 'ยกเลิก/ยุติระบบที่ไม่จำเป็น',
        'count': 38,
        'percentage': 10.89,
        'description':
        'การยุติหรือยกเลิกระบบงานที่หมดความจำเป็น ลดความซ้ำซ้อน และลดภาระค่าใช้จ่ายในการดูแลระบบ',
        'color': '#E4B5D1'
    }, {
        'category': 'Rehost',
        'icon': '🔄',
        'subtitle': 'Lift & Shift',
        'count': 15,
        'percentage': 4.30,
        'description':
        'การย้ายระบบงานหรือข้อมูลขึ้นสู่ระบบคลาวด์โดยไม่มีการแก้ไขระบบงาน (Lift & Shift) และคงสถาปัตยกรรมเดิมไว้',
        'color': '#B5E4C5'
    }, {
        'category': 'Replatform',
        'icon': '🔧',
        'subtitle': 'Tinker & Shift',
        'count': 4,
        'percentage': 1.15,
        'description':
        'การย้ายแอปพลิเคชันไปยัง Cloud พร้อมกับการปรับปรุงบางส่วน เพื่อใช้ประโยชน์จากบริการจัดการของ Cloud (Managed Services)',
        'color': '#A8E4E4'
    }, {
        'category': 'Repurchase',
        'icon': '🛒',
        'subtitle': 'ใช้ SaaS หรือ COTS แทนระบบเดิม',
        'count': 2,
        'percentage': 0.57,
        'description':
        'การเลิกใช้ระบบงานเดิมและเปลี่ยนไปใช้บริการซอฟต์แวร์สำเร็จรูป หรือ บริการรูปแบบซอฟต์แวร์เป็นบริการ (SaaS) แทน',
        'color': '#F4C7B9'
    }, {
        'category': 'Re-architect',
        'icon': '🏗️',
        'subtitle': 'ปรับโครงสร้างใหม่เป็น Cloud-Native',
        'count': 1,
        'percentage': 0.29,
        'description':
        'การออกแบบและพัฒนาปรับปรุงสถาปัตยกรรมระบบงานใหม่ ให้เป็นรูปแบบ (Cloud-Native) ',
        'color': '#D9C8F4'
    }]

    row1_cols_p2 = st.columns(3)
    for idx, item in enumerate(phase2_data[:3]):
        with row1_cols_p2[idx]:
            st.markdown(f"""
            <div class="category-card" style="border-left-color: {item['color']};">
                <div class="card-header">
                    <div>
                        <div class="card-title">{item['icon']} {item['category']}</div>
                        <div class="card-subtitle">{item['subtitle']}</div>
                    </div>
                    <div class="card-percentage">{item['percentage']}%</div>
                </div>
                <div class="card-number">{item['count']}</div>
                <div class="card-description">{item['description']}</div>
            </div>
            """,
                        unsafe_allow_html=True)

    row2_cols_p2 = st.columns(3)
    for idx, item in enumerate(phase2_data[3:]):
        with row2_cols_p2[idx]:
            st.markdown(f"""
            <div class="category-card" style="border-left-color: {item['color']};">
                <div class="card-header">
                    <div>
                        <div class="card-title">{item['icon']} {item['category']}</div>
                        <div class="card-subtitle">{item['subtitle']}</div>
                    </div>
                    <div class="card-percentage">{item['percentage']}%</div>
                </div>
                <div class="card-number">{item['count']}</div>
                <div class="card-description">{item['description']}</div>
            </div>
            """,
                        unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.divider()

    st.subheader("📊 ภาพรวมข้อมูล Phase 2")

    df_phase2 = pd.DataFrame(phase2_data)
    df_phase2 = df_phase2[['category', 'count', 'percentage', 'description']]
    df_phase2.columns = ['Category', 'จำนวน', 'เปอร์เซ็นต์', 'คำอธิบาย']

    col_chart1_p2, col_chart2_p2 = st.columns(2)

    with col_chart1_p2:
        st.markdown("#### สัดส่วนการแบ่ง Category")
        colors_p2 = [item['color'] for item in phase2_data]
        fig_pie_p2 = go.Figure(data=[
            go.Pie(
                labels=[item['category'] for item in phase2_data],
                values=[item['count'] for item in phase2_data],
                marker=dict(colors=colors_p2),
                textposition='auto',
                textinfo='label+percent',
                hovertemplate=
                '<b>%{label}</b><br>จำนวน: %{value}<br>เปอร์เซ็นต์: %{percent}<extra></extra>'
            )
        ])
        fig_pie_p2.update_layout(height=400,
                                 showlegend=False,
                                 margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig_pie_p2, use_container_width=True)

    with col_chart2_p2:
        st.markdown("#### จำนวน Applications ตาม Category")
        fig_bar_p2 = go.Figure(data=[
            go.Bar(x=[item['category'] for item in phase2_data],
                   y=[item['count'] for item in phase2_data],
                   text=[
                       f"{item['count']}<br>({item['percentage']}%)"
                       for item in phase2_data
                   ],
                   textposition='outside',
                   marker=dict(color=colors_p2),
                   hovertemplate='<b>%{x}</b><br>จำนวน: %{y}<extra></extra>')
        ])
        fig_bar_p2.update_layout(height=400,
                                 xaxis_title="",
                                 yaxis_title="จำนวน Applications",
                                 showlegend=False,
                                 margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig_bar_p2, use_container_width=True)

    st.divider()
    st.markdown("#### 📋 ตารางสรุปข้อมูล Phase 2")
    df_display_p2 = df_phase2.copy()
    df_display_p2['เปอร์เซ็นต์'] = [f"{x}%" for x in df_display_p2['เปอร์เซ็นต์']]
    st.dataframe(df_display_p2,
                 use_container_width=True,
                 hide_index=True,
                 column_config={
                     "Category":
                     st.column_config.TextColumn("Category", width="small"),
                     "จำนวน":
                     st.column_config.NumberColumn("จำนวน", width="small"),
                     "เปอร์เซ็นต์":
                     st.column_config.TextColumn("เปอร์เซ็นต์ (จาก 349)",
                                                 width="small"),
                     "คำอธิบาย":
                     st.column_config.TextColumn("คำอธิบาย", width="large")
                 })

    st.info(
        f"**รวมทั้งหมด Phase 2: {df_phase2['จำนวน'].sum()} Applications ({round(df_phase2['เปอร์เซ็นต์'].sum(), 2)}% จากทั้งหมด 349)**"
    )

    st.markdown("""
    ### 📌 สรุปข้อมูล Phase 2
    - **Refactor (15.47%)** เป็น Category ที่มีจำนวนมากที่สุดใน Phase 2 โดยมี 54 Applications
    - **Retire (10.89%)** เป็น Category ที่มีจำนวนมากเป็นอันดับสอง โดยมี 38 Applications
    - **Rehost (4.30%)** มี 15 Applications
    - **Re-architect (0.29%)** มีจำนวนน้อยที่สุด โดยมีเพียง 1 Application
    """)
