from objectpack.actions import ObjectPack
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.auth.models import ContentType
from django.contrib.auth.models import Group

from objectpack.ui import ModelEditWindow
from .controller import observer
from . import ui


class PermissionPack(ObjectPack):
    model = Permission
    add_to_desktop = True
    add_window = edit_window = ModelEditWindow.fabricate(model, model_register=observer)
    #add_window = edit_window = ui.PermissionAddWindow

    columns = [
        {
            'data_index': 'codename',
            'header': u'Кодовое название',
            'width': 50,
        },
        {
            'data_index': 'name',
            'header': u'Имя',
        },
        {
            'data_index': 'content_type_id',
            'header': u'ID Контента',
        }
   ]


class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_menu = True
    add_to_desktop = True
    add_window = edit_window = ModelEditWindow.fabricate(model)


class UserPack(ObjectPack):
    model = User
    add_to_desktop = True
    add_window = edit_window = ui.UserAddWindow
    #edit_window = ModelEditWindow.fabricate(model)


class GroupPack(ObjectPack):
    model = Group
    add_to_desktop = True
    add_window = edit_window = ModelEditWindow.fabricate(model)




