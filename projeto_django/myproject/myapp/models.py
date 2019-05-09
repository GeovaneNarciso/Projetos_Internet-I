from django.db import models


class Post(models.Model):
    pass


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'short'),
        ('M', 'medium'),
        ('L', 'large')
    )

    first_name = models.CharField(max_length=30)
    midle_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=50, db_column='birth_city')
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, null=True)


# ---------------------------------------------------------
class Manufacter(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Car(models.Model):
    name = models.CharField(max_length=50)
    manufacter = models.ForeignKey(Manufacter, on_delete=models.CASCADE, related_name="cars")

    def __str__(self):
        return self.name

# ---------------------------------------------------------


class Categoria(models.Model):
    descricao = models.CharField(max_length=50, unique=True)


class Livro(models.Model):
    name = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="livros")

    def __str__(self):
        return self.name

# ---------------------------------------------------------


class Cobertura(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


class Pizza(models.Model):
    nome = models.CharField(max_length=50)
    coberturas = models.ManyToManyField(Cobertura)

    def __str__(self):
        return self.nome

# ---------------------------------------------------------


class CPF(models.Model):
    numero = models.CharField(max_length=9)

    @staticmethod
    def calcular_dv():
        return '00'

    def __str__(self):
        return self.numero + '-' + self.calcular_dv()


class PessoaFisica(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.OneToOneField(CPF, related_name='pessoa_fisica', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

# ---------------------------------------------------------


class Blog(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Entry(models.Model):
    headline = models.CharField(max_length=60)
    body_text = models.CharField(max_length=255)
    pub_date = models.DateField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline


# ---------------------------------------------------------


class Person2(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(Person2, through='Membership', through_fields=('group', 'person'))

    def __str__(self):
        return self.name


class Membership(models.Model):
    date_joined = models.DateField()
    inviter = models.ForeignKey(Person2, on_delete=models.CASCADE, related_name='membership_invites')
    invite_reason = models.CharField(max_length=30)
    person = models.ForeignKey(Person2, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.person.name

# ---------------------------------------------------------


class Perfil(models.Model):
    nome = models.CharField(max_length=50)
    amigos = models.ManyToManyField('self')

    def __str__(self):
        return self.nome
