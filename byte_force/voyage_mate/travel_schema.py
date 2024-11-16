TRAVEL_ITINERARY_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "name": "travel_itinerary",
        "schema": {
            "type": "object",
            "properties": {
                "destination": {
                    "type": "string",
                    "description": "Name of the travel destination"
                },
                "number_of_days": {
                    "type": "integer",
                    "description": "Total number of days for the trip"
                },
                "itinerary": {
                    "type": "array",
                    "description": "List of daily activities for the trip",
                    "items": {
                        "type": "string",
                        "description": "Activities planned for a specific day"
                    }
                }
            },
            "required": ["destination", "number_of_days", "itinerary"],
            "additionalProperties": False
        }
    }
}
