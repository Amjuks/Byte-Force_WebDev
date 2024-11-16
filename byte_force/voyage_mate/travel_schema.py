TRAVEL_PROMPT = """You are a travel planner. I want you to generate a travel itinerary in JSON format. Follow these details carefully:  

- Include a mix of cultural experiences, nature exploration, and leisure activities.  
- Focus on iconic landmarks, peaceful experiences, and scenic views.  
- Activities should not be rushed; maintain a balanced pace.  

- Avoid repeating activities.  
- The plans should align with typical travel preferences for destination.  
- Ensure each day offers something unique.

This is the user's requirements:
{}

Please generate the itinerary based on this input."""

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
