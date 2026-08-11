Middleware executes before and after every request and is used for cross-cutting concerns such as logging, CORS, authentication, request timing, and modifying requests or responses.
Request

↓

Middleware

↓

print("Before API")

↓

call_next()

↓

Your API

↓

Return Response

↓

print("After API")

↓

Browser