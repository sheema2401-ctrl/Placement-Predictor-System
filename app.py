import streamlit as st
import pandas as pd
import joblib


# =======================
# PAGE DESIGN
# =======================

st.markdown(
"""
<style>


.stApp {

background: linear-gradient(
120deg,
#0f172a,
#1e3a8a,
#7c3aed,
#0ea5e9
);

background-size:400% 400%;

animation: gradient 12s ease infinite;

}



@keyframes gradient {


0%{
background-position:0% 50%;
}


50%{
background-position:100% 50%;
}


100%{
background-position:0% 50%;
}

}




h1 {


color:white !important;

text-align:center;

font-size:55px !important;

font-weight:900;

text-shadow:
0px 0px 25px cyan;

}





p, label {


color:white !important;

font-size:18px;


}





.stNumberInput input {


background:white;

border-radius:15px;

height:45px;

font-size:18px;


}




.stSelectbox div {


background:white;

border-radius:15px;


}




.stSlider {


background:rgba(255,255,255,0.15);

padding:15px;

border-radius:20px;


}





.stButton button {


background:

linear-gradient(
90deg,
#22c55e,
#06b6d4
);


color:white;

font-size:20px;

font-weight:bold;

height:55px;

border-radius:30px;


border:none;


box-shadow:

0px 0px 25px cyan;



}




.stButton button:hover {


transform:scale(1.05);

box-shadow:

0px 0px 40px white;


}





.card {


background:

rgba(255,255,255,0.18);


backdrop-filter:

blur(15px);


padding:25px;

border-radius:25px;


box-shadow:

0px 0px 30px black;


}



.company {


background:voilet;

padding:15px;

margin:10px;

border-radius:15px;


box-shadow:

0px 5px 15px black;


font-size:18px;


}




#MainMenu {

visibility:hidden;

}


footer {

visibility:hidden;

}


</style>

""",

unsafe_allow_html=True
)




# =======================
# LOAD MODEL
# =======================


model = joblib.load("placement_model.pkl")





# =======================
# TITLE
# =======================


st.markdown(

"""

<h1>
🚀 Placement Predictor System
</h1>


<center>

<p>
 Career Guidance & Placement Recommendation System
</p>

</center>

""",

unsafe_allow_html=True

)




# =======================
# INPUTS
# =======================



cgpa = st.number_input(
"🎓 CGPA",
0.0,
10.0
)



tenth = st.number_input(
"📘 10th Percentage",
0.0,
100.0
)



twelfth = st.number_input(
"📗 12th Percentage",
0.0,
100.0
)



internships = st.number_input(
"💼 Internships",
0,
10
)



projects = st.number_input(
"🛠 Projects",
0,
10
)




coding = st.slider(
"💻 Coding Skill",
1,
10
)




communication = st.slider(
"🗣 Communication Skill",
1,
10
)




backlogs = st.number_input(
"❌ Backlogs",
0,
10
)





branch = st.selectbox(

"🏫 Branch",

[
"CSE",
"IT",
"ECE",
"EEE",
"MECH",
"CIVIL"
]

)





branch_map = {


"CSE":0,

"ECE":1,

"EEE":2,

"MECH":3,

"CIVIL":4,

"IT":5

}




# =======================
# PREDICTION
# =======================



if st.button("⚡ Predict Placement"):



    input_data = pd.DataFrame([[


        cgpa,
        tenth,
        twelfth,
        internships,
        projects,
        coding,
        communication,
        backlogs,
        branch_map[branch]


    ]],

    columns=[


        "cgpa",
        "10th_percent",
        "12th_percent",
        "internships",
        "projects",
        "coding_skill",
        "communication_skill",
        "backlogs",
        "branch"

    ])



    probability = model.predict_proba(input_data)


    chance = probability[0][1]*100





    # ======================
    # RESULT
    # ======================




    if cgpa >= 7.5:



        st.markdown(

        f"""

        <div class="card">


        <h2>
        🟢 Excellent Placement Profile
        </h2>


        <h3>
        Placement Probability:
        {chance:.2f}%
        </h3>


        <p>
        Student is ready for top placement opportunities.
        </p>


        </div>

        """,

        unsafe_allow_html=True

        )




        st.subheader("🏢 Target Companies")



        companies=[


        "Google",

        "Microsoft",

        "Amazon",

        "Adobe",

        "TCS"


        ]





    elif cgpa >= 7.0:



        st.markdown(

        """

        <div class="card">


        <h2>
        🟡 Good Placement Chance
        </h2>


        <p>
        Improve projects and interview preparation.
        </p>


        </div>


        """,

        unsafe_allow_html=True

        )



        st.subheader("🏢 Suitable Companies")



        companies=[


        "TCS",

        "Infosys",

        "Accenture",

        "Cognizant"


        ]






    elif cgpa >= 6.0:



        st.markdown(

        """

        <div class="card">


        <h2>
        📚 Skill Improvement Required
        </h2>


        <p>
        Complete courses and certifications.
        </p>


        </div>


        """,

        unsafe_allow_html=True

        )



        st.subheader("📌 Must Learn")



        courses=[


        "Python",

        "Data Structures",

        "Machine Learning",

        "SQL",

        "Cloud Computing"


        ]


        for c in courses:

            st.write("📘",c)



        companies=[]




    else:



        st.markdown(

        """

        <div class="card">


        <h2>
        🔴 Need More Improvement
        </h2>


        <p>
        Work harder on academics and skills.
        </p>


        </div>


        """,

        unsafe_allow_html=True

        )


        companies=[]






    # COMPANY DISPLAY


    if companies:


        st.subheader("🚀 Recommended Companies")


        for company in companies:


            st.markdown(

            f"""

            <div class="company">

            ⭐ {company}

            </div>


            """,

            unsafe_allow_html=True

            )




        st.subheader("💼 Suggested Roles")


        roles=[

        "Software Developer",

        "Data Analyst",

        "ML Engineer"

        ]



        for role in roles:


            st.write("🔹",role)
