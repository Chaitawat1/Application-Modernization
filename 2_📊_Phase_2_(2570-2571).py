import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Phase 2 (2570-2571)",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
    .category-card {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        height: 100%;
        margin-bottom: 20px;
    }
    .card-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }
    .card-title {
        font-size: 18px;
        font-weight: 600;
        color: #333;
        margin: 0;
    }
    .card-subtitle {
        font-size: 16px;
        color: #666;
        margin: 5px 0 15px 0;
    }
    .card-percentage {
        background-color: #f0f0f0;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 13px;
        color: #666;
        font-weight: 500;
    }
    .card-number {
        font-size: 36px;
        font-weight: 700;
        color: #1a1a1a;
        margin: 10px 0;
        line-height: 1;
    }
    .card-description {
        font-size: 15px;
        color: #666;
        line-height: 1.5;
        margin-top: 10px;
    }
    .overview-section {
        text-align: center;
        margin-bottom: 30px;
    }
    .overview-title {
        font-size: 28px;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 5px;
    }
    .overview-subtitle {
        font-size: 16px;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="overview-section">
    <div class="overview-title">Phase 2: 2570-2571</div>
    <div class="overview-subtitle">รวม 114 แอปพลิเคชัน (จาก 349)</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

phase2_data = [
    {
        'category': 'Refactor',
        'icon': '⚙️',
        'subtitle': 'การปรับปรุงโค้ด',
        'count': 54,
        'percentage': 15.47,
        'description': 'การปรับปรุงโค้ดเพื่อเพิ่มประสิทธิภาพและความยืดหยุ่นของระบบ โดยไม่เปลี่ยนแปลงฟังก์ชันการทำงานหลัก',
        'color': '#A8D5E4'
    },
    {
        'category': 'Retire',
        'icon': '🗑️',
        'subtitle': 'การยุติการใช้งานระบบ',
        'count': 38,
        'percentage': 10.89,
        'description': 'การยกเลิกการใช้งานระบบที่ไม่จำเป็น เพื่อลดภาระการดูแลรักษา ',
        'color': '#E4B5D1'
    },
    {
        'category': 'Rehost',
        'icon': '🔄',
        'subtitle': 'Lift & Shift',
        'count': 15,
        'percentage': 4.30,
        'description': 'การย้ายระบบแบบคงสภาพเดิมโดยไม่มีการปรับเปลี่ยนสถาปัตยกรรมหรือโค้ด',
        'color': '#B5E4C5'
    },
    {
        'category': 'Replatform',
        'icon': '🔧',
        'subtitle': 'การย้ายและปรับเปลี่ยนแพลตฟอร์ม',
        'count': 4,
        'percentage': 1.15,
        'description': 'เป็นการย้ายระบบโดยมีการปรับเปลี่ยนองค์ประกอบบางส่วนในเพื่อให้สามารถใช้ประโยชน์จากบริการจัดการของคลาวด์',
        'color': '#A8E4E4'
    },
    {
        'category': 'Repurchase',
        'icon': '🛒',
        'subtitle': 'การจัดหาบริการทดแทน',
        'count': 2,
        'percentage': 0.57,
        'description': 'เป็นการยุติการใช้งานระบบงานเดิม และเปลี่ยนไปใช้บริการซอฟต์แวร์สำเร็จรูป(Software-as-a-Service: SaaS)',
        'color': '#F4C7B9'
    },
    {
        'category': 'Re-architect',
        'icon': '🏗️',
        'subtitle': 'ปรับสถาปัตยกรรมใหม่',
        'count': 1,
        'percentage': 0.29,
        'description': 'การออกแบบสถาปัตยกรรมระบบใหม่ทั้งหมดเพื่อรองรับความต้องการในอนาคต',
        'color': '#D9C8F4'
    }
]

row1_cols = st.columns(3)
for idx, item in enumerate(phase2_data[:3]):
    with row1_cols[idx]:
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
        """, unsafe_allow_html=True)

row2_cols = st.columns(3)
for idx, item in enumerate(phase2_data[3:]):
    with row2_cols[idx]:
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
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.divider()

st.subheader("📊 ภาพรวมข้อมูล Phase 2")

df_phase2 = pd.DataFrame(phase2_data)
df_phase2 = df_phase2[['category', 'count', 'percentage', 'description']]
df_phase2.columns = ['Category', 'จำนวน', 'เปอร์เซ็นต์', 'คำอธิบาย']

col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.markdown("#### สัดส่วนการแบ่ง Category")
    
    colors = [item['color'] for item in phase2_data]
    
    fig_pie = go.Figure(data=[go.Pie(
        labels=[item['category'] for item in phase2_data],
        values=[item['count'] for item in phase2_data],
        marker=dict(colors=colors),
        textposition='auto',
        textinfo='label+percent',
        hovertemplate='<b>%{label}</b><br>จำนวน: %{value}<br>เปอร์เซ็นต์: %{percent}<extra></extra>'
    )])
    
    fig_pie.update_layout(
        height=400,
        showlegend=False,
        margin=dict(t=20, b=20, l=20, r=20)
    )
    
    st.plotly_chart(fig_pie, use_container_width=True)

with col_chart2:
    st.markdown("#### จำนวน Applications ตาม Category")
    
    fig_bar = go.Figure(data=[go.Bar(
        x=[item['category'] for item in phase2_data],
        y=[item['count'] for item in phase2_data],
        text=[f"{item['count']}<br>({item['percentage']}%)" for item in phase2_data],
        textposition='outside',
        marker=dict(color=colors),
        hovertemplate='<b>%{x}</b><br>จำนวน: %{y}<extra></extra>'
    )])
    
    fig_bar.update_layout(
        height=400,
        xaxis_title="",
        yaxis_title="จำนวน Applications",
        showlegend=False,
        margin=dict(t=20, b=20, l=20, r=20)
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

st.markdown("#### 📋 ตารางสรุปข้อมูล Phase 2")

df_display = df_phase2.copy()
df_display['เปอร์เซ็นต์'] = df_display['เปอร์เซ็นต์'].apply(lambda x: f"{x}%")

st.dataframe(
    df_display,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Category": st.column_config.TextColumn("Category", width="small"),
        "จำนวน": st.column_config.NumberColumn("จำนวน", width="small"),
        "เปอร์เซ็นต์": st.column_config.TextColumn("เปอร์เซ็นต์ (จาก 349)", width="small"),
        "คำอธิบาย": st.column_config.TextColumn("คำอธิบาย", width="large")
    }
)

st.info(f"**รวมทั้งหมด Phase 2: {df_phase2['จำนวน'].sum()} Applications ({round(df_phase2['เปอร์เซ็นต์'].sum(), 2)}% จากทั้งหมด 349)**")

st.markdown("""
### 📌 สรุปข้อมูล Phase 2
- **Refactor (15.47%)** เป็น Category ที่มีจำนวนมากที่สุดใน Phase 2 โดยมี 54 Applications
- **Retire (10.89%)** เป็น Category ที่มีจำนวนมากเป็นอันดับสอง โดยมี 38 Applications
- **Rehost (4.30%)** มี 15 Applications
- **Re-architect (0.29%)** มีจำนวนน้อยที่สุด โดยมีเพียง 1 Application
""")
