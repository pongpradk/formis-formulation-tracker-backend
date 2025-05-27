from django.apps import AppConfig


class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory'
    
    # This ensures signals.py is loaded when the app starts.
    # It guarantees the @receiver in signals.py get registered.
    def ready(self):
        import inventory.signals
