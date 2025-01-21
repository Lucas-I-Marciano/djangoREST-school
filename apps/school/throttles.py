from rest_framework.throttling import UserRateThrottle

class MatriculaRateThrottle(UserRateThrottle):
    rate = '6/minute'