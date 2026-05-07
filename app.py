import streamlit as st
import joblib
import xgboost

model = joblib.load("task_model.pkl")   # your file already exists

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Task Manager",
    page_icon="🚀",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.main {
    background-color: #0f172a;
}
.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
}
.metric {
    font-size: 22px;
    font-weight: bold;
}
.big-title {
    font-size: 40px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="big-title">🚀 AI Task Management System</div>', unsafe_allow_html=True)
st.write("Automate task classification, prioritization, and assignment")

# ---------------- SESSION TEAM ----------------
if "team" not in st.session_state:
    st.session_state.team = {
        "Alice": 4,
        "Bob": 3,
        "Charlie": 2
    }

def assign_task():
    team = st.session_state.team
    person = min(team, key=team.get)
    team[person] += 1
    return person

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Team Settings")

for member in st.session_state.team:
    st.session_state.team[member] = st.sidebar.slider(
        f"{member} workload",
        0, 10,
        st.session_state.team[member]
    )

# ---------------- INPUT SECTION ----------------
st.markdown("### 📌 Enter Task Details")

col1, col2 = st.columns([2,1])

with col1:
    task = st.text_area("📝 Task Description", placeholder="e.g. Book flight tickets")

with col2:
    deadline = st.slider("⏳ Deadline (days)", 1, 10, 3)

# ---------------- BUTTON ----------------
if st.button("🔍 Analyze Task", use_container_width=True):

    if not task.strip():
        st.warning("⚠️ Please enter a task")
    else:
        # -------- DUMMY LOGIC (REPLACE WITH MODEL LATER) --------
        task_lower = task.lower()

        if "gym" in task_lower or "exercise" in task_lower:
            category = "Health & Wellness"
        elif "flight" in task_lower or "travel" in task_lower:
            category = "Travel"
        elif "bill" in task_lower or "pay" in task_lower:
            category = "Finance"
        else:
            category = "Personal"

        if deadline <= 2:
            priority = "High"
        elif deadline <= 5:
            priority = "Medium"
        else:
            priority = "Low"

        assigned = assign_task()

        st.success("✅ Task Processed Successfully!")

        # ---------------- OUTPUT CARDS ----------------
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
            <div class="card">
                <div class="metric">📂 Category</div>
                <h2>{category}</h2>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="card">
                <div class="metric">🔥 Priority</div>
                <h2>{priority}</h2>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="card">
                <div class="metric">👨‍💻 Assigned To</div>
                <h2>{assigned}</h2>
            </div>
            """, unsafe_allow_html=True)

# ---------------- TEAM WORKLOAD ----------------
st.markdown("### 📊 Team Workload")

for member, tasks in st.session_state.team.items():
    st.progress(tasks / 10)
    st.write(f"{member}: {tasks} tasks")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("💡 Built with Streamlit | Advanced UI Version")
model = joblib.load("final_model.pkl")
category = model.predict([task])[0]