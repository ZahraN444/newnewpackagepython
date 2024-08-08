# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class LocationAnalysis(object):

    """Implementation of the 'location_analysis' model.

    A nested object containing a breakdown of the analysis of a reverse
    geocoded location.

    Attributes:
        latitude (float): A positive or negative decimal indicating the
            geographic latitude of the address, specifying the north-to-south
            position of a location. This should be used with `longitude` to
            pinpoint locations on a map. Will not be returned for
            undeliverable addresses or military addresses (state is `AA`,
            `AE`, or `AP`).
        longitude (float): A positive or negative decimal indicating the
            geographic longitude of the address, specifying the north-to-south
            position of a location. This should be used with `latitude` to
            pinpoint locations on a map. Will not be returned for
            undeliverable addresses or military addresses (state is `AA`,
            `AE`, or `AP`).
        distance (float): The distance from the input location to this exact
            zip code in miles.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "latitude": 'latitude',
        "longitude": 'longitude',
        "distance": 'distance'
    }

    _nullables = [
        'latitude',
        'longitude',
    ]

    def __init__(self,
                 latitude=None,
                 longitude=None,
                 distance=None):
        """Constructor for the LocationAnalysis class"""

        # Initialize members of the class
        self.latitude = latitude 
        self.longitude = longitude 
        self.distance = distance 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        latitude = dictionary.get("latitude") if dictionary.get("latitude") else None
        longitude = dictionary.get("longitude") if dictionary.get("longitude") else None
        distance = dictionary.get("distance") if dictionary.get("distance") else None
        # Return an object of this model
        return cls(latitude,
                   longitude,
                   distance)
