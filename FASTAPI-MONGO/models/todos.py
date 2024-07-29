from pydantic import BaseModel

class Todo(BaseModel):
    name:str
    description:str
    complete:bool







# class Config(BaseModel):
#     api_key: str
#     base_url: str
#     headers: dict
#     retries: int
#     retry_delay: int
#     retry_max_delay: int
#     backoff_factor: float
#     timeout: int
#     max_redirects: int
#     proxies: dict
#     ssl_context: dict
#     cert_reqs: str
#     ciphers: str
#     ssl_version: str
#     assert_hostname: bool
#     assert_fingerprint: bool