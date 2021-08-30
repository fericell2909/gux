from gux.serializers import AuditSerializer
from .models import Testings

class TestingsSerializers(AuditSerializer):

    class Meta(AuditSerializer.Meta):
        model = Testings
        read_only_fields = ('active',)

