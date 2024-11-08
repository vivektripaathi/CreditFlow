from django.apps import AppConfig



class CustomerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer'
    inject_container = None

    def ready(self):
        from customer.inject import CustomerContainer
        import customer

        self.inject_container = CustomerContainer()
        self.inject_container.wire(
            packages=[customer],
            modules=[],
        )
