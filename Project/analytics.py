import pandas as pd
import numpy as np
from Database import run_query


def compute_future_projections():
    """"computes marginal package returns across DSA tiers and projects future hiring inflation cursur for technical profiles."""
    placed_df = run_query("""SELECT DSA_Problems_Solved, Package_LPA, College_Tier, GitHub_Contributions FROM students WHERE Placement_Status = 'Placed'l; """)

    # Group DSA counts into 