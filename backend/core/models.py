from django.db import models

class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('Tecnico', 'Técnico'),
        ('Enfermagem', 'Enfermagem'),
        ('Administrativo', 'Administrativo'),
    ]

    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, unique=True)  # Validação pode ser feita com Regex ou libs.
    profissao = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)

    def __str__(self):
        return f"{self.nome} ({self.tipo_usuario})"

class Material(models.Model):
    nome = models.CharField(max_length=255, default="Outro")
    tipo_material = models.CharField(max_length=255)
    data_validade = models.DateField()
    serial = models.CharField(max_length=255, unique=True, editable=False)  # Serial gerado automaticamente.

    def save(self, *args, **kwargs):
        if not self.serial:  # Gera o serial automaticamente apenas na criação.
            self.serial = f"{self.nome[:3].upper()}-{self.pk or ''}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Processo(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    etapa = models.CharField(max_length=100) # Exemplo de campo etapa
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_fim = models.DateTimeField(null=True, blank=True)
    observacoes = models.TextField(blank=True)


    def __str__(self):
        return f"{self.etapa} - {self.material.nome}"

    @staticmethod
    def rastreabilidade(serial=None):
        if serial:
            return Processo.objects.filter(material__serial=serial).order_by("data_inicio")
        return Processo.objects.all().order_by("material", "data_inicio")