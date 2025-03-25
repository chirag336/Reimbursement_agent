#!/usr/bin/env python
import sys

from reimbursement.crew import (
    LatestAiDevelopmentCrew,
)


def run():
    """
    Run the crew.
    """
    inputs = {
        "query": """
            Classification of the receipt in and extracting the price.
    1) Fuel
    2) Travel
    3) Hotel
    4) Food
    5) others
        """,
    }
    LatestAiDevelopmentCrew().crew().kickoff(
        inputs=inputs
    )


if __name__ == "__main__":
    run()
