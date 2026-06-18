from rest_framework import throttling
from django.core.cache import cache
from rest_framework.throttling import ScopedRateThrottle

# class IPThrottling(throttling.BaseThrottle):
#     def allow_request(self, request, view):
#         # import pdb;pdb.set_trace()
#         ip_address=request.META.get('X-Forwarded-For', None)
#         if ip_address is None:
#             ip_address=request.META.get('REMOTE_ADDR')
            
#         if cache.get(ip_address):
#             total_calls = cache.get(ip_address)
#             if total_calls>=5:
#                 return False
#             else:
#                 cache.set(ip_address, total_calls+1)
            
#         else:
#             cache.set(ip_address, 1)
#         return True

class IPThrottling(ScopedRateThrottle):
    throttle_scope = 'list'