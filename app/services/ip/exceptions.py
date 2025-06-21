class IpResolverError(Exception):
    """any error while resolve user IP"""


class IpResolverAPIError(IpResolverError):
    """any error related to API"""


class IpResolverParseError(IpResolverError):
    """any error in handling the response"""
