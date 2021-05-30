from treelib import Tree
from django.http import HttpResponse
from .models import Relation


def greet(request):
    tree = Tree()
    # uncomment when using database(relation table), make sure to use 0 as parent id instead of Null.
    # data = Relation.objects.all()
    # tree.create_node("Result", "Result")  # root node
    # for obj in data:
    #     if obj.parent_id == 0:  # all the independent node
    #         tree.create_node(obj.title, obj.title, parent="Result")
    #     else:
    #         tree.create_node(obj.title, obj.title, parent=data[int(obj.parent_id) - 1].title)


    # output using static data, shold be commented if database is used
    data = [
        {'sl': 1, 'title': 'Joke', 'p_id': None},
        {'sl': 2, 'title': 'Meme', 'p_id': None},
        {'sl': 3, 'title': 'Old', 'p_id': 2},
        {'sl': 4, 'title': '90s', 'p_id': 3},
        {'sl': 5, 'title': 'New', 'p_id': 2},
        {'sl': 6, 'title': 'Dank', 'p_id': None}
    ]

    tree.create_node("Result", "Result")  # root node
    for obj in data:
        if obj['p_id'] is None:  # all the independent node
            tree.create_node(obj['title'], obj['title'], parent="Result")
        else:
            tree.create_node(obj['title'], obj['title'], parent=data[obj['p_id'] - 1]['title'])
            
    # common portion, should not be commented
    tree.save2file('tree.txt')
    f = open('tree.txt', 'r+')
    file_content = f.readlines()[1:]  # ignore root
    f.truncate(0)  # clean tree.txt
    f.close()
    return HttpResponse(file_content, content_type="application/json", charset='utf-8')
