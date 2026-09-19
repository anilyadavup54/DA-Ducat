import pandas as pd
import numpy as np
from Database import run_query


def compute_future_projections():
    """"computes marginal package returns across DSA tiers and projects future hiring inflation cursur for technical profiles."""

    placed_df = run_query("""SELECT DSA_Problems_Solved, Package_LPA, College_Tier, GitHub_Contributions FROM students WHERE Placement_Status = 'Placed'; """)

    # Group DSA counts into step  bins of 100
    bins = pd.cut(placed_df['DSA_Problems_Solved'], bins=range(0,1290,100))
    dsa_agg=placed_df.groupby(bins,observed=False)['Package_LPA'].mean().reset_index()
    dsa_agg['bin_mid']=[int(b.mid) for b in dsa_agg['DSA_Problems_Solved']]
    dsa_agg=dsa_agg.dropna()

    # Model projected skills remium cursur ( exponential compounding on technical milestones)
    dsa_agg['projected_lpa']= dsa_agg['Package_LPA']*(1+(dsa_agg['bin_mid']/1000)*0.35)

    # Tier Parity comnparison by skill band
    placed_df['Skill_Band']= pd.qcut(
        placed_df['DSA_Problems_Solved'],
        q=3,
        labels=['Foundational (<120)', 'Intermediate (120-220)', 'Advanced (>220)']
    )

    tier_parity = placed_df.groupby(['Skill_Band', 'College_Tier'], observed=False)['Package_LPA'].mean().reset_index()

    return {
        "dsa_curve": dsa_agg.to_dict(orient="records"),
        "tier_parity": tier_parity.to_dict(orient="records")
    }