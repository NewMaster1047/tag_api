import re
from .models import Tag
from .serializer import TagSerializer


def tag_creater(description):
    data = re.findall(r"#.[^#|\s+]*", description)
    serialized_d = []
    for i in data:
        if '#' in i:
            serialized_d.append(i)

    for i in serialized_d:
        tag = Tag.objects.filter(name=i).first()
        if tag is None:
            serializer = TagSerializer(data={"name": i})
            serializer.is_valid(raise_exception=True)
            serializer.save()

    return serialized_d
