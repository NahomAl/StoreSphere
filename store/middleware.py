"""Middleware to rate limit requests"""
import time
from django.http import HttpResponseNotFound
from django.core.cache import cache
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication

class RateLimitMiddleware:
    """Middleware to rate limit requests"""
    def __init__(self, get_response):
        self.get_response = get_response
        self.rate_limits = {'/auth/jwt/create/': 3, 'default': 30}
        self.period = 60  # Time period for rate limit in seconds
        self.initial_block_duration = 180  # Initial block time in seconds
        self.additional_block_time = 120  # Additional block time in seconds
        self.max_block_duration = 14400  # Maximum block time in seconds (4 hours)
        self.block_count_expiry = 28800 # Block count expiry duration (8 hours)

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR', 'unknown')
        current_time = time.time()

        block_key = f"block:{ip}"
        rate_key = f"rate_limit:{ip}:{request.path}"
        limit = self.rate_limits.get(request.path, self.rate_limits['default'])

        block_info = cache.get(block_key, {"block_until": 0})
        block_until = block_info["block_until"]
        block_count_info = cache.get(f"block_count:{ip}", {"block_count": 0})
        block_count = block_count_info["block_count"]

        if block_until > current_time:
            wait_seconds = int(block_until - current_time)
            return JsonResponse({
                'error': f'Rate limit exceeded. Try again after {wait_seconds // 60} minutes and {wait_seconds % 60} seconds.'
            }, status=429)


        count = cache.get(rate_key, 0)
        if count >= limit:
            block_duration = min(
                self.initial_block_duration + block_count * self.additional_block_time,
                self.max_block_duration
            )
            block_until = current_time + block_duration


            cache.set(block_key, {"block_until": block_until},
                      timeout=block_duration)


            cache.set(f"block_count:{ip}", {
                      "block_count": block_count + 1}, timeout=self.block_count_expiry)

            wait_seconds = int(block_until - current_time)
            return JsonResponse({
                'error': f'Rate limit exceeded. Try again after {wait_seconds // 60} minutes and {wait_seconds % 60} seconds.'
            }, status=429)

        cache.set(rate_key, count + 1, timeout=self.period)
        return self.get_response(request)

class IgnoreFaviconMiddleware:
    """Middleware to ignore favicon requests"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/favicon.ico':
            return HttpResponseNotFound()
        return self.get_response(request)
