import re
from .models import Tag
from .serializer import TagSerializer


def tag_filter(description, tag):
    data = re.findall(r"#.[^#|\s+]*", description)
    l_data = []

    if len(data) == 0:
        return False

    for i in data:
        l_data.append(i.lower())

    if tag in l_data:
        return True

    return True


def tag_create(tag):
    tag = str(tag)
    tag_obj = Tag.objects.filter(name=tag).first()

    if tag_obj is None:
        serializer = TagSerializer(data={"name": tag})
        serializer.is_valid(raise_exception=True)
        serializer.save()

    return True
