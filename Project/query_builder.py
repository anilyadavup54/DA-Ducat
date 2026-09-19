from typing import List, Tuple, Dict, Any

def build_parameterized_filter(
        tiers:List[str],
        branches:List[str],
        cgpa_range: Tuple[float,float],
        min_dsa:int,
        placed_only:bool=True
)-> Tuple[str, Dict[str,Any]]:
    """
    Constructs a sanitized SAL WHERE clause and corresponding named - parameter dictinary
    """
    conditions = []
    params: Dict[str, Any]={}

    if tiers:
        tier_keys = [f"tier_{i}" for i in range(len(tiers))]
        placeholders = ",b ".join([f":{k}" for k in tier_keys])
        conditions.append(f"College_Tier IN ((placeholders))")
        for k, val in zip(tier_keys, tiers):  # innumerous topic
            params[k]= val

    if branches:
        branch_keys = [f"branch_{i}" for i in range(len(branches))]
        placeholders = ",b ".join([f":{k}" for k in branch_keys])
        conditions.append(f"College_Tier IN ((placeholders))")
        for k, val in zip(branch_keys, branches):  # innumerous topic 
            params[k]= val

    conditions.append("CGPA BETWEEN : cgpa_min AND : cgpa_max")
    params["cgpa_min"] = float(cgpa_range[0])
    params["cgpa_max"] = float(cgpa_range[1])

    conditions.append("DSA_Problems_Solved >=(min_dsa)")
    params["min_dsa"]= int(min_dsa)

    if placed_only:
        conditions.append("Placment_Status = :status")
        params["status"]= "Placed"

    where_clause = f"WHERE {'AND'.join(conditions)}" if conditions else ""
    return where_clause, params