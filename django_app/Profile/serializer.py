#Importando librerías de Django
from rest_framework import routers,serializers,viewsets

#Importando el modelo del componente Login (desde el archivo models.py)
from Profile.models import ProfileModel, CiudadModel, GeneroModel, OcupacionModel, EstadoModel, EstadoCivilModel

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('__all__')
        
class ProfileGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('nombre','apPat','apMat','edad')

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CiudadModel
        fields = ('__all__')

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroModel
        fields = ('__all__')

class OcupacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OcupacionModel
        fields = ('__all__')

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoModel
        fields = ('__all__')

class EstadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivilModel
        fields = ('__all__')