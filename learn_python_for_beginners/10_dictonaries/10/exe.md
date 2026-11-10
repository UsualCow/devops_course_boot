Quest Status
Fantasy Quest stores each character's progress in a nested dictionary structure. Here's what it looks like:

{
    "character_name": "Kaladin",
    "quests": {
        "bridge_run": {
            "status": "In Progress",
        },
        "talk_to_syl": {
            "status": "Completed",
        },
    },
}

The values can change of course, but the structure will always be the same. For example, another character's progress might look like this:

{
    "character_name": "Shallan",
    "quests": {
        "bridge_run": {
            "status": "Completed",
        },
        "talk_to_syl": {
            "status": "In Progress",
        },
    },
}

Assignment
Complete the get_quest_status function. It accepts a progress dictionary (structure defined above) and should return the value of the "status" field for the "bridge_run" quest. You do not need to use any loops for this task.

Note, you can chain dictionary keys on the progress dictionary to access the nested quest information inside another dictionary:

outer_dictionary["outer_key"]["inner_key"]["inner_most_key"]
