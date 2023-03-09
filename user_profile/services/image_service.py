from django.core.exceptions import ValidationError


def get_avatar_path(instance, file):

    return f'avatars/user_{instance.user.id}/{file}'


def get_cover_path(instance, file):

    return f'company_cover/user_{instance.user.id}/{file}'


def validate_image_size(file_obj):

    image_max_size = 3
    if file_obj.size > image_max_size * 1024 * 1024:
        raise ValidationError(f"Image size cant be bigger than {image_max_size}MB")
