import random
import string

def generate_short_code(instance, size=10, chars=string.ascii_lowercase + string.digits):
    
    new_code = "".join(random.choice(chars) for _ in range(size))
    
    if instance.__class__.objects.filter(short_code=new_code).exists():
        return generate_short_code(instance)
    
    return new_code
    