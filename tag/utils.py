import re
from .models import Tag
from .serializer import TagSerializer


def tag_filter(description):
    data = re.findall(r"#.[^#|\s+]*", description)
    f_data = []
    for i in data:
        if '#' in i:
            f_data.append(i)

    return f_data


def tag_create(tag):
    tag = str(tag)
    tag_obj = Tag.objects.filter(name=tag).first()

    if tag_obj is None:
        serializer = TagSerializer(data={"name": tag})
        serializer.is_valid(raise_exception=True)
        serializer.save()

    return True
