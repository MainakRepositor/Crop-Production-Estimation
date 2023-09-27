"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Harvest Production Estimation System")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            In the heartlands of agriculture, where fields stretch like canvases painted with green and gold, a symphony of data orchestrates the dance of harvest. Here, the ingenious random forest classifier emerges as a wizardly conductor, summoning its sylvan ensemble of decision trees to harmonize nature's secrets. Like a whispering breeze, it gathers insights from sun-soaked days, rain-soaked nights, and the earth's fertile embrace. Each tree, a custodian of knowledge, casts its vote on the forthcoming yield, and together, they compose a predictive masterpiece, a ballad of abundance or moderation. As the seasons waltz on, this arboreal ensemble learns and refines its rhythm, its predictions ripening like the very crops it tends to foresee. And so, in this realm where technology serenades tradition, the random forest reigns—a virtuoso in the grand opera of agriculture, where data and destiny entwine in the poetry of prediction.
        </p>
    """, unsafe_allow_html=True)
