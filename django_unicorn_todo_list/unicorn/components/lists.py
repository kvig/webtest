from django_unicorn.components import UnicornView
from lists.models import List


class ListsView(UnicornView):
    title: str = ""
    lists = List.objects.none()

    def hydrate(self):
        self.lists = List.objects.filter(user=self.request.user)

    def add_list(self):
        new_list = List(title=self.title, user=self.request.user)
        new_list.save()
        self.title = ""

    def delete(self, id):
        List.objects.get(pk=id).delete()
        self.lists = self.lists.exclude(pk=id)
