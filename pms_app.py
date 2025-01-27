# packages
import pandas as pd
import numpy as np
import sklearn
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#Prediction Function

def machinealignmentstatus(value):
    if value == "Aligned":
        return int(1)
    elif value == "Not Aligned":
        return int(0)

def operationmode(value):
    if value == "Manual":
        return int(1)
    elif value == "Automatic":
        return int(0)

def tooltype(value):
    if value == "HSS":
        ca, ce, hss = (0, 0, 1)
    elif value == "Carbide":
        ca, ce, hss = (1, 0, 0)
    elif value == "Ceramic":
        ca, ce, hss = (0, 1, 0)
    return ca, ce, hss

def materialtype(value):
    if value == "Titanium":
        alu, pla, ste, tit = (0, 0, 0, 1)
    elif value == "Plastic":
        alu, pla, ste, tit = (0, 1, 0, 0)
    elif value == "Aluminium":
        alu, pla, ste, tit = (1, 0, 0, 0)
    elif value == "Steel":
        alu, pla, ste, tit = (0, 0, 1, 0)

    return alu, pla, ste, tit

def price_prediction(Operation_Time,
                     Cutting_Speed,
                     Feed_Rate,
                     Tool_Type,
                     Tool_Diameter,
                     Spindle_Speed,
                     Motor_Current,
                     Power_Consumption,
                     Lubrication_Level,
                     Cooling_System_Efficiency,
                     Cycle_Time,
                     Machine_Age,
                     Part_Defect_Rate,
                     Maintenance_Frequency,
                     Vibration_Level,
                     Machine_Health_Status,
                     Tool_Wear_Rate,
                     Cutting_Temperature,
                     Material_Type,
                     Material_Hardness,
                     Pressure_Level,
                     Machine_Stability,
                     Machine_Alignment_Status,
                     Power_Surge_Rate,
                     Machine_Calibration,
                     Tool_Change_Interval,
                     Spindle_Health_Status,
                     Lubrication_Condition,
                     Coolant_Flow_Rate,
                     Cutting_Force,
                     Operation_Mode,
                     Machine_Load,
                     Spindle_Torque,
                     Spindle_Condition,
                     Power_Supply_Voltage):
    
    MachineAlignmentStatus_int = machinealignmentstatus(Machine_Alignment_Status)
    OperationMode_int = operationmode(Operation_Mode)
    ca, ce, hss = tooltype(Tool_Type)
    alu, pla, ste, tit = materialtype(Material_Type)

    with open("Random_forest_model.pkl","rb") as f:
        model = pickle.load(f)

    user_data = np.array([[Operation_Time, Cutting_Speed, Feed_Rate,Tool_Diameter, Spindle_Speed,
                           Motor_Current, Power_Consumption, Lubrication_Level, Cooling_System_Efficiency,
                            Cycle_Time, Machine_Age, Part_Defect_Rate,Maintenance_Frequency, Vibration_Level,
                            Machine_Health_Status, Tool_Wear_Rate, Cutting_Temperature, Material_Hardness,
                            Pressure_Level, Machine_Stability, MachineAlignmentStatus_int, Power_Surge_Rate,
                            Machine_Calibration, Tool_Change_Interval, Spindle_Health_Status, Lubrication_Condition,
                            Coolant_Flow_Rate, Cutting_Force, OperationMode_int, Machine_Load, Spindle_Torque,
                            Spindle_Condition, Power_Supply_Voltage, ca, ce, hss, alu, pla, ste, tit]])
    
    y_pred = model.predict(user_data)


    # Define the failure types and recommendations
    failure_types = ['Electrical Surge', 'Misalignment', 'Overheating', 'Wear and Tear']
    recommendations = ['Check power supply', 'Inspect cooling system', 'Realign machine components', 'Replace worn-out tools']

    # Output from the system
    output = [y_pred[0][0], y_pred[0][1], y_pred[0][2], y_pred[0][3], y_pred[0][4],
              y_pred[0][5], y_pred[0][6], y_pred[0][7], y_pred[0][8]]

    # Map the output to failure status, type, and recommendation
    if output[0] == 0:
        failure_status = "No Failure"
    else:
        failure_status = "One Failure Occurred"

    failure_detected = []
    recommendations_required = []

    # Identify failure types
    for i in range(1, 5):
        if output[i] == 1:
            failure_detected.append(failure_types[i - 1])

    # Identify recommendations
    for i in range(5, 9):
        if output[i] == 1:
            recommendations_required.append(recommendations[i - 5])

    # Print the results
    

    st.write(f"### :blue[Failure Status:{failure_status}]")
    if failure_detected:
        st.write(f"### :blue[Failure Type: {', '.join(failure_detected)}]")
    else:
        st.write("### :blue[Failure Type: None]")

    if recommendations_required:
        st.write(f"### :blue[Recommendation: {', '.join(recommendations_required)}]")
    else:
        st.write("### :blue[Recommendation: None]")




# Streamlit Part
st.set_page_config(layout= "wide")

def setting_bg():
    st.markdown(f""" <style>.stApp {{
                        background:url("https://t3.ftcdn.net/jpg/06/54/92/60/240_F_654926042_OFgg2UoFkDn09TQeEXzpVlWqCSyd0fWd.jpg");
                        background-size: cover}}
                     </style>""", unsafe_allow_html=True)


setting_bg()

st.title("PREDICTIVE MAINTENANCE SYSTEM")
with st.sidebar:
    select = option_menu("Main Menu",["Predictive Maintenance", "Prediction", "About"])

if select == "Predictive Maintenance":

    st.header("Predictive Maintenance System")
    st.write("""
    A **Predictive Maintenance System (PdM)** uses data-driven technologies, machine learning models, and IoT sensors to predict equipment failure before it happens.
    By analyzing historical data and real-time inputs, the system helps prevent downtime, optimize resources, and reduce maintenance costs.
    """)

    st.header("Benefits of a Predictive Maintenance System")
    st.write("""
    **1. Reduced Downtime:**  
    Identify potential failures early and address them before they lead to breakdowns, ensuring smoother operations.

    **2. Cost Efficiency:**  
    Prevent unnecessary maintenance and reduce repair costs by addressing issues only when they arise. Helps optimize the maintenance budget.

    **3. Extended Equipment Life:**  
    Regular monitoring ensures timely interventions, which can increase the lifespan of machines and reduce the need for costly replacements.

    **4. Improved Safety:**  
    Avoid accidents and hazardous situations caused by equipment failures, ensuring the safety of personnel.
    """)

    st.header("Why Implement a Predictive Maintenance System?")
    st.write("""
    Predictive Maintenance Systems help industries transition from reactive to proactive maintenance approaches, minimizing unplanned downtime and optimizing operations.
    These systems combine cutting-edge AI technologies with IoT tools to ensure efficient resource utilization, safety, and long-term cost savings.
    By predicting failures before they happen, industries can avoid costly repairs and improve the overall efficiency of their operations.
    """)

if select == "Prediction":
    col1, col2, col3, col4 = st.columns(4)

    with col1:

        Operation_Time = st.number_input("Select the Operation Time")
        Cutting_Speed = st.number_input("Select the Cutting Speed")
        Feed_Rate = st.number_input("Select the Feed Rate")
        Tool_Type =st.selectbox("Select of Tool Type",["HSS", "Carbide", "Ceramic"])   
        Tool_Diameter = st.number_input('Enter the Tool Diameter')
        Spindle_Speed = st.number_input('Enter the Spindle Speed')
        Motor_Current= st.number_input('Enter the Motor_Current')
        Power_Consumption= st.number_input('Enter the Power_Consumption')
        Lubrication_Level = st.number_input('Enter the Lubrication Level')

    with col2:
       
        Cooling_System_Efficiency = st.number_input('Enter the Cooling System Efficiency')
        Cycle_Time = st.number_input('Enter the Cycle Time')
        Machine_Age = st.number_input('Enter the Machine Age')
        Part_Defect_Rate = st.number_input('Enter the Part Defect Rate')
        Maintenance_Frequency = st.number_input('Enter the Maintenance Frequency')
        Vibration_Level = st.number_input('Enter the Vibration Level')
        Machine_Health_Status = st.number_input('Enter the Machine Health Status')
        Tool_Wear_Rate = st.number_input('Enter the Tool Wear Rate')
        Cutting_Temperature = st.number_input('Enter the Cutting Temperature')


    with col3:
       

        Material_Type = st.selectbox('Enter the Material Type',["Titanium", "Plastic", "Aluminium", "Steel"])
        Material_Hardness = st.number_input('Enter the Material Hardness')
        Pressure_Level = st.number_input('Enter the Pressure Level')
        Machine_Stability = st.number_input('Enter the Machine Stability')
        Machine_Alignment_Status = st.selectbox('Enter the Machine Alignment Status',["Aligned", "Not Aligned"])
        Power_Surge_Rate = st.number_input('Enter the Power Surge Rate')
        Machine_Calibration = st.number_input('Enter the Machine Calibration')
        Tool_Change_Interval = st.number_input('Enter the Tool Change Interval')
        Spindle_Health_Status = st.number_input('Enter the Spindle Health Status')


    with col4:
        
        
        Lubrication_Condition = st.number_input('Enter the Lubrication Condition')
        Coolant_Flow_Rate = st.number_input('Enter the Coolant Flow Rate')
        Cutting_Force = st.number_input('Enter the Cutting Force')
        Operation_Mode = st.selectbox('Enter the Operation Mode',["Manual", "Automatic"])
        Machine_Load = st.number_input('Enter the Machine Load')
        Spindle_Torque = st.number_input('Enter the Tool Spindle Torque')
        Spindle_Condition = st.number_input('Enter the Spindle Condition')
        Power_Supply_Voltage = st.number_input('Enter the Power Supply Voltage')

    button = st.button("Submit",use_container_width = True)
    if button:        

        price_prediction(Operation_Time,Cutting_Speed,Feed_Rate,Tool_Type,Tool_Diameter,Spindle_Speed,
                        Motor_Current,Power_Consumption,Lubrication_Level,Cooling_System_Efficiency,
                        Cycle_Time,Machine_Age,Part_Defect_Rate,Maintenance_Frequency,Vibration_Level,
                        Machine_Health_Status,Tool_Wear_Rate,Cutting_Temperature,Material_Type,Material_Hardness,
                        Pressure_Level,Machine_Stability,Machine_Alignment_Status,Power_Surge_Rate,
                        Machine_Calibration,Tool_Change_Interval,Spindle_Health_Status,Lubrication_Condition,
                        Coolant_Flow_Rate,Cutting_Force,Operation_Mode,Machine_Load,Spindle_Torque,
                        Spindle_Condition,Power_Supply_Voltage)
        
    
       
