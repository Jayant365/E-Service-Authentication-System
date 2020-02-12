import random
import string
from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


#print(random_string_generator())

#print(random_string_generator(size=50))

'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''
def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def unique_username_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    # if new_slug is not None:
    #     slug = new_slug
    # else:
    #     slug = slugify(instance.full_name)
    #
    # Klass = instance.__class__
    # qs_exists = Klass.objects.filter(username=slug).exists()
    # if qs_exists:
    #     new_slug = "{slug}-{randstr}".format(
    #                 slug=slug,
    #                 randstr=random_string_generator(size=4)
    #             )
    #     return unique_slug_generator(instance, new_slug=new_slug)
    slug=new_slug.full_name

    return slug