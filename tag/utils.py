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


def tag_create(tags):
    for i in tags:
        tag = Tag.objects.filter(name=i).first()
        if tag is None:
            serializer = TagSerializer(data={"name": i})
            serializer.is_valid(raise_exception=True)
            serializer.save()

    return tags
