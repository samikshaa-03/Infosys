import streamlit as st
from scripts.ticket_ai import generate_ticket

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Ticket Automation System",
    layout="wide"
)


# ---------------- HEADER ----------------
st.markdown("""
<h1 style="text-align:center;">🛠️ AI Ticket Automation System</h1>
<p style="text-align:center; color:gray;">
Smart ticket creation using NLP & Machine Learning
</p>
<hr>
""", unsafe_allow_html=True)

# ---------------- LAYOUT ----------------
col1, col2 = st.columns([1.1, 1])

# ---------------- INPUT SECTION ----------------
with col1:
    st.markdown("### 📥 Submit Your Issue")

    user_input = st.text_area(
        "Describe your issue clearly:",
        height=180,
        placeholder="Example: My laptop is not working urgently. Error 404 appears."
    )

    generate_btn = st.button("🚀 Generate Ticket", use_container_width=True)

# ---------------- OUTPUT SECTION ----------------
with col2:
    st.markdown("### 📄 Ticket Preview (Confirmation)")

    if generate_btn:
        if user_input.strip() == "":
            st.warning("⚠️ Please enter an issue description.")
        else:
            ticket = generate_ticket(user_input)

            # Priority color
            priority_color = "red" if ticket["priority"] == "High" else "green"

            st.success("✅ Ticket generated successfully!")

            # ---------- MAIN CARD ----------
            st.markdown(f"""
            <div style="padding:15px; border-radius:10px; background-color:#1e1e1e;">
                <h3>🏷️ {ticket['title']}</h3>
                <p><b>Category:</b> <span style="color:#4da6ff;">{ticket['category']}</span></p>
                <p><b>Priority:</b> <span style="color:{priority_color};">{ticket['priority']}</span></p>
                <p><b>Status:</b> {ticket['status']}</p>
                <p><b>Created At:</b> {ticket['created_at']}</p>
            </div>
            """, unsafe_allow_html=True)

            # ---------- DESCRIPTION ----------
            st.markdown("#### 📝 Issue Description")
            st.info(ticket["description"])

            # ---------- ENTITIES ----------
            st.markdown("#### 🔍 Extracted Information")

            devices = ticket["entities"]["devices"]
            error_codes = ticket["entities"]["error_codes"]

            st.markdown("**🖥️ Devices Detected:**")
            if devices:
                for d in devices:
                    st.write(f"• {d}")
            else:
                st.write("No devices detected.")

            st.markdown("**⚠️ Error Codes Detected:**")
            if error_codes:
                st.write(", ".join(error_codes))
            else:
                st.write("No error codes detected.")

            # ---------- RAW JSON (OPTIONAL BUT GOOD FOR VIVA) ----------
            with st.expander("📄 View Full Ticket JSON"):
                st.json(ticket)
