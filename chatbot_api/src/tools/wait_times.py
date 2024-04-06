import os
from typing import Any
import numpy as np
from langchain_community.graphs import Neo4jGraph

def _get_current_hospitals() -> list[str]:
    """Fetch a list of current hospital names from a Neo4j database."""
    graph = Neo4jGraph(
        url=os.getenv("NEO4J_URI"),
        username=os.getenv("NEO4J_USERNAME"),
        password=os.getenv("NEO4J_PASSWORD"),
    )

    current_hospitals = graph.query(
        """
        MATCH (h:Hospital)
        RETURN h.name AS hospital_name
        """
    )

    return [hospital["hospital_name"].lower() for hospital in current_hospitals]

def _get_current_wait_time_minutes(hospital: str) -> int:
    """Get the current wait time at a hospital in minutes."""
    current_hospitals = _get_current_hospitals()

    if hospital.lower() not in current_hospitals:
        return -1

    return np.random.randint(low=0, high=600)


def get_current_wait_times(hospital: str) -> str:
    """Get the current wait time at a hospital formatted as a string."""
    wait_time_in_minutes = _get_current_wait_time_minutes(hospital)

    if wait_time_in_minutes == -1:
        return f"Hospital '{hospital}' does not exist."

    hours, minutes = divmod(wait_time_in_minutes, 60)

    if hours > 0:
        return f"{hours} hours {minutes} minutes"
    else:
        return f"{minutes} minutes"