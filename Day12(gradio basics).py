import gradio as gr
import pandas as pd

# ==============================================================================
# GRADIO BEGINNER GUIDE & TUTORIAL
# ==============================================================================
# Gradio is a Python library used to quickly build web user interfaces for 
# machine learning models, APIs, and data workflows.
#
# There are TWO main ways to build apps in Gradio:
# 1. gr.Interface(): Quick, high-level class for wrapping any Python function.
# 2. gr.Blocks(): Low-level layout for custom page structures, tabs, & events.
# ==============================================================================


# ------------------------------------------------------------------------------
# 1. SIMPLE FUNCTION FOR TAB 1 (Quick gr.Interface Example)
# ------------------------------------------------------------------------------
def greet_user(name, intensity):
    """Simple greeting function showing basic input -> output flow."""
    if not name:
        name = "Stranger"
    return f"Hello, {name}! " + "Welcome to Gradio! 🎉" * int(intensity)


# ------------------------------------------------------------------------------
# 2. FORM PROCESSING FUNCTION FOR TAB 2 (Mirroring Streamlit Day11 Form)
# ------------------------------------------------------------------------------
def process_user_form(name, age, gender, education, skills, experience, resume, relocate):
    """
    Processes all user inputs when the 'Submit' button is clicked.
    Returns: JSON dict, Pandas DataFrame, and File status string.
    """
    # Handle list of skills (from CheckboxGroup)
    skills_str = ", ".join(skills) if skills else "None selected"
    
    # Create result dictionary
    result = {
        "Name": name if name else "Not provided",
        "Age": int(age) if age is not None else 18,
        "Gender": gender if gender else "Not specified",
        "Education": education if education else "Not specified",
        "Skills": skills_str,
        "Experience": int(experience),
        "Relocate": "Yes" if relocate else "No"
    }
    
    # Convert dictionary to Pandas DataFrame for table output
    df = pd.DataFrame([result])
    
    # Check file upload status
    if resume is not None:
        # Gradio passes file paths or file objects depending on configuration
        file_name = resume if isinstance(resume, str) else resume.name
        file_status = f"✅ Uploaded File: {file_name}"
    else:
        file_status = "ℹ️ No resume uploaded yet."
        
    return result, df, file_status


# ------------------------------------------------------------------------------
# 3. LIVE CALCULATOR FOR TAB 3 (Interactive ML/Math Demo)
# ------------------------------------------------------------------------------
def calculate(num1, num2, operation):
    if operation == "Add (+)":
        return num1 + num2
    elif operation == "Subtract (-)":
        return num1 - num2
    elif operation == "Multiply (×)":
        return num1 * num2
    elif operation == "Divide (÷)":
        return num1 / num2 if num2 != 0 else "Error: Division by Zero"
    return 0


# ==============================================================================
# BUILDING THE UI WITH GR.BLOCKS
# ==============================================================================
with gr.Blocks(title="Beginner's Guide to Gradio", theme=gr.themes.Soft()) as demo:
    
    gr.Markdown(
        """
        # 🚀 Beginner's Guide to Gradio
        Welcome to **Day 12: Gradio Basics**! This guide demonstrates core Gradio components and mirrors the input widgets learned in Streamlit (`Day11`).
        """
    )
    
    with gr.Tabs():
        
        # ======================================================================
        # TAB 1: Quick Interface Basics
        # ======================================================================
        with gr.TabItem("1️⃣ Quick Interface Basics"):
            gr.Markdown("### How `gr.Interface` works under the hood")
            gr.Markdown("In Gradio, `Interface` takes 3 main parameters: **`fn`** (Python function), **`inputs`**, and **`outputs`**.")
            
            with gr.Row():
                with gr.Column():
                    name_input = gr.Textbox(label="Enter Your Name", placeholder="e.g. Vasan")
                    intensity_slider = gr.Slider(minimum=1, maximum=5, value=1, step=1, label="Greeting Intensity")
                    greet_btn = gr.Button("Say Hello", variant="primary")
                with gr.Column():
                    greeting_output = gr.Textbox(label="Greeting Output", interactive=False)
            
            # Link button click to the greet_user function
            greet_btn.click(
                fn=greet_user,
                inputs=[name_input, intensity_slider],
                outputs=greeting_output
            )

        # ======================================================================
        # TAB 2: Dynamic User Input Form (Mirrors Day11 Streamlit Basics)
        # ======================================================================
        with gr.TabItem("2️⃣ Dynamic User Input Form"):
            gr.Markdown("### Comprehensive Input Widgets Demonstration")
            gr.Markdown("This section maps each Streamlit widget from `Day11` to its equivalent in `Gradio`.")
            
            with gr.Row():
                # LEFT COLUMN: User Input Controls
                with gr.Column(scale=1):
                    gr.Markdown("#### 📝 Personal Information")
                    
                    form_name = gr.Textbox(
                        label="Enter your Name",
                        placeholder="Full Name"
                    )
                    
                    form_age = gr.Number(
                        label="Enter Age",
                        value=18,
                        minimum=1,
                        maximum=100
                    )
                    
                    form_gender = gr.Radio(
                        choices=["Male", "Female", "Other"],
                        label="Select Gender",
                        value="Male"
                    )
                    
                    form_education = gr.Dropdown(
                        choices=["High School", "Diploma", "Bachelor's", "Master's", "PhD"],
                        label="Highest Qualification",
                        value="Bachelor's"
                    )
                    
                    form_skills = gr.CheckboxGroup(
                        choices=["Python", "Java", "SQL", "Machine Learning", "Deep Learning", "Gradio"],
                        label="Select Skills"
                    )
                    
                    form_experience = gr.Slider(
                        minimum=0,
                        maximum=20,
                        value=1,
                        step=1,
                        label="Years of Experience"
                    )
                    
                    form_resume = gr.File(
                        label="Upload Resume (PDF / DOCX)",
                        file_types=[".pdf", ".docx"]
                    )
                    
                    form_relocate = gr.Checkbox(
                        label="Willing to Relocate",
                        value=False
                    )
                    
                    submit_btn = gr.Button("Submit Form", variant="primary")

                # RIGHT COLUMN: Display Results
                with gr.Column(scale=1):
                    gr.Markdown("#### 📊 Collected Information & Results")
                    
                    file_status_output = gr.Textbox(
                        label="File Upload Status",
                        interactive=False
                    )
                    
                    json_output = gr.JSON(
                        label="Result as JSON (Dictionary)"
                    )
                    
                    dataframe_output = gr.Dataframe(
                        label="Result as Pandas DataFrame",
                        interactive=False
                    )
            
            # Event Listener: When 'Submit Form' is clicked, process inputs and send to outputs
            submit_btn.click(
                fn=process_user_form,
                inputs=[
                    form_name, form_age, form_gender, form_education,
                    form_skills, form_experience, form_resume, form_relocate
                ],
                outputs=[json_output, dataframe_output, file_status_output]
            )

        # ======================================================================
        # TAB 3: Live Interactivity Demo
        # ======================================================================
        with gr.TabItem("3️⃣ Live Interactivity Demo"):
            gr.Markdown("### Real-Time Live Updates")
            gr.Markdown("Notice how Gradio can trigger updates *instantly* as inputs change without needing a submit button!")
            
            with gr.Row():
                with gr.Column():
                    num1 = gr.Number(label="Number 1", value=10)
                    num2 = gr.Number(label="Number 2", value=5)
                    op = gr.Radio(["Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)"], label="Operation", value="Add (+)")
                with gr.Column():
                    calc_result = gr.Textbox(label="Calculated Result", interactive=False)
            
            # Live updates when any number or operation radio changes
            for component in [num1, num2, op]:
                component.change(
                    fn=calculate,
                    inputs=[num1, num2, op],
                    outputs=calc_result
                )

# ==============================================================================
# LAUNCH THE GRADIO APPLICATION
# ==============================================================================
if __name__ == "__main__":
    # Launching the app. Set share=True if you want to create a public link.
    demo.launch(debug=True)
