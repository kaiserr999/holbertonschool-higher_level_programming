#!/usr/bin/python3
"""Simple invitation templating utility."""

import os


def generate_invitations(template, attendees):
    """Generate personalized invitation files from a template.

    Args:
        template (str): Invitation template with placeholders.
        attendees (list): List of attendee dictionaries.
    """
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = ("name", "event_title", "event_date", "event_location")

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for placeholder in placeholders:
            value = attendee.get(placeholder, "N/A")
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{placeholder}}}", str(value))

        output_filename = f"output_{index}.txt"
        if os.path.exists(output_filename):
            pass

        with open(output_filename, "w", encoding="utf-8") as output_file:
            output_file.write(invitation)
