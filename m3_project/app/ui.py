from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext


class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(UserAddWindow, self)._init_components()

        self.field__username = ext.ExtStringField(
            label=u'Имя польз-ля',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__password = ext.ExtStringField(
            label=u'Пароль',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__last_login = ext.ExtDateField(
            label=u'Последн. логин',
            name='last_login',
            allow_blank=True,
            anchor='100%')
        self.field__last_login.format = 'd.m.Y'

        self.field__is_superuser = ext.ExtCheckBox(
            label=u'Суперпольз.?',
            name='is_superuser',
            allow_blank=True,
            anchor='100%',
        )

        self.field__is_staff = ext.ExtCheckBox(
            label=u'Обсуж. перс.?',
            name='is_staff',
            allow_blank=True,
            anchor='100%',
        )

        self.field__first_name = ext.ExtStringField(
            label=u'Имя',
            name='first_name',
            allow_blank=True,
            anchor='100%')

        self.field__last_name = ext.ExtStringField(
            label=u'Фамилия',
            name='last_name',
            allow_blank=True,
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'email',
            name='e-mail',
            allow_blank=True,
            anchor='100%')

        self.field__is_active = ext.ExtCheckBox(
            label=u'Активен?',
            name='is_active',
            allow_blank=True,
            anchor='100%',
        )

        self.field__date_joined = ext.ExtDateField(
            label=u'Дата регистрации',
            name='date_joined',
            allow_blank=False,
            anchor='100%',
        )
        self.field__date_joined.format = 'd.m.Y'
    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((

            self.field__username,
            self.field__password,
            self.field__last_login,
            self.field__is_superuser,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__is_staff,
            self.field__is_active,
            self.field__date_joined,

        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'
