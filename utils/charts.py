"""
charts.py

Utility functions for generating charts used in the
Intelligent Resume Analyzer.
"""

import matplotlib.pyplot as plt

# ---------------------------------------------------
# Skill Match Pie Chart
# ---------------------------------------------------


def create_skill_pie(matched_skills, missing_skills):
    """
    Creates a pie chart showing matched vs missing skills.

    Returns
    -------
    matplotlib.figure.Figure
    """

    matched = len(matched_skills)
    missing = len(missing_skills)

    figure, ax = plt.subplots(figsize=(5, 5))

    ax.pie(
        [matched, missing],
        labels=["Matched", "Missing"],
        autopct="%1.1f%%",
        startangle=90,
    )

    ax.set_title("Skill Match Distribution")

    return figure


# ---------------------------------------------------
# Skill Coverage Bar Chart
# ---------------------------------------------------


def create_skill_bar(matched_skills, missing_skills):
    """
    Creates a horizontal bar chart showing
    matched and missing skills.
    """

    labels = ["Matched Skills", "Missing Skills"]

    values = [
        len(matched_skills),
        len(missing_skills),
    ]

    figure, ax = plt.subplots(figsize=(7, 3))

    ax.barh(
        labels,
        values,
    )

    ax.set_xlabel("Number of Skills")

    ax.set_title("Skill Coverage")

    return figure


# ---------------------------------------------------
# Candidate Ranking Chart
# ---------------------------------------------------


def create_candidate_ranking(results):
    """
    Parameters
    ----------
    results : list

    Expected:
        [
            {
                "candidate":"Rahul",
                "score":95
            },
            ...
        ]
    """

    names = []

    scores = []

    for result in results:

        names.append(result["candidate"])

        scores.append(result["score"])

    figure, ax = plt.subplots(figsize=(9, 5))

    ax.bar(
        names,
        scores,
    )

    ax.set_ylim(0, 100)

    ax.set_ylabel("Score")

    ax.set_title("Candidate Ranking")

    plt.xticks(rotation=20)

    return figure


# ---------------------------------------------------
# Batch Score Distribution
# ---------------------------------------------------


def create_score_distribution(results):
    """
    Creates score distribution chart.
    """

    scores = [result["score"] for result in results]

    figure, ax = plt.subplots(figsize=(7, 4))

    ax.hist(
        scores,
        bins=10,
    )

    ax.set_xlabel("Match Score")

    ax.set_ylabel("Candidates")

    ax.set_title("Score Distribution")

    return figure
